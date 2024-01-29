# Copyright 2019-2020 Thomas Kramer.
# SPDX-FileCopyrightText: 2022 Thomas Kramer
#
# SPDX-License-Identifier: CERN-OHL-S-2.0

from z3 import *
from .place import TransistorPlacer
from typing import Iterable
from ..data_types import Transistor, Cell, ChannelType
from itertools import combinations, chain
import logging
import math
from typing import *

logger = logging.getLogger(__name__)


class SMTPlacer(TransistorPlacer):

    def __init__(self):
        self.facing_gates_must_have_same_net: bool = True
        self.minimize_net_bounding_boxes: bool = True
    
    def _place(self,
        nmos: List[Transistor],
        pmos: List[Transistor], 
        cell_width: int, 
        cell_height: int = 1
    ) -> Iterable[Cell]:

        assert len(nmos) <= cell_width * cell_height
        assert len(pmos) <= cell_width * cell_height
        
        transistors = []
        transistors.extend(nmos)
        transistors.extend(pmos)

        solver = Optimize()

        # Wrapper arount solver.add
        def add_assertion(assertion, **kw):
            solver.add(assertion)

        # Create symbols for transistor positions.
        transistor_positions = {t: (Int("transistor_{}_x".format(i)), Int("transistor_{}_y".format(i)))
                                for i, t in enumerate(transistors)}

        # Create boolean symbols for transistor flips.
        # Each transistor can be flipped (source/drain swapped).
        transistor_flipped = {t: Bool("transistor_{}_flipped".format(i))
                              for i, t in enumerate(transistors)}

        # Constraint: Positions are bounded.
        # Add bounds on positions.
        for x, y in transistor_positions.values():
            add_assertion(x >= 0)
            add_assertion(y >= 0)

            # Add upper bounds on transistor positions.
            add_assertion(x < cell_width)
            add_assertion(y < cell_height * 2)

        # Constraint: Separate rows for NMOS and PMOS
        # Assign rows to NMOS and PMOS
        for t, (x, y) in transistor_positions.items():

            or_constraints = []

            for r in range(cell_height * 2):
                # Place transistor in upper or lower stack?
                # Ordering alternates from row to row such that power stripe can be shared.
                stack = r % 2 if t.channel_type == ChannelType.NMOS else 1 - r % 2

                allowed_y = r * 2 + stack
                or_constraints.append(y == allowed_y)

            on_allowed_row = Or(*or_constraints)
            add_assertion(on_allowed_row)

        # Constraint: Non-overlapping positions
        # No two transistors should have the same position.
        # Assumes that NMOS and PMOS transistors are on different rows already.
        #for ts in [nmos, pmos]:
        #    # Loop through all potential (left, right) pairs.
        #    for a, b in combinations(ts, 2):
        #        xa, ya = transistor_positions[a]
        #        xb, yb = transistor_positions[b]
        #        
        #        if cell_width > 1:
        #            same_position = And(
        #                xa == xb,
        #                ya == yb
        #            )
        #            different_positions = Not(same_position)
        #            add_assertion(different_positions)
        #        else:
        #            add_assertion(xa != xb)

        for (x1, y1), (x2, y2) in combinations(transistor_positions.values(), 2):
            same_position = And(
                x1 == x2,
                y1 == y2
            )
            different_positions = Not(same_position)
            add_assertion(different_positions)

        # Constraint: Diffusion sharing
        # If two transistors are placed side-by-side then the abutted sources/drain nets must match.
        for ts in [nmos, pmos]:
            # Loop through all potential (left, right) pairs.
            for a, b in combinations(ts, 2):
                for t_left, t_right in [(a, b), (b, a)]:
                    xl, yl = transistor_positions[t_left]
                    xr, yr = transistor_positions[t_right]

                    # Checks if t_left is left neighbor of t_right.
                    are_neighbors = And(
                        yl == yr,
                        xl + 1 == xr
                    )

                    # Go through all combinations of flipped transistors
                    # and check if they are allowed to be directly abutted if flipped
                    # in a specific way.
                    flip_combinations = [[False, False], [False, True], [True, False], [True, True]]
                    for flip_l, flip_r in flip_combinations:
                        l = t_left.flipped() if flip_l else t_left
                        r = t_right.flipped() if flip_r else t_right

                        if l.drain_net != r.source_net:
                            # Drain/Source net mismatch.
                            # In case the transistors are flipped that way,
                            # they are not allowed to be direct neighbors.
                            add_assertion(
                                Implies(
                                    And(transistor_flipped[t_left] == flip_l,
                                        transistor_flipped[t_right] == flip_r),
                                    Not(are_neighbors)
                                )
                            )

        # Constraint: NMOS and PMOS transistors which face eachother have the same gate net.
        if self.facing_gates_must_have_same_net:
            for tn in nmos:
                for tp in pmos:
                    if tn.gate_net != tp.gate_net:
                        (xn, yn) = transistor_positions[tn]
                        (xp, yp) = transistor_positions[tp]
                        same_x = xn == xp
                        neighbour_rows = yn + 1 == yp
                        
                        if cell_height > 1:
                            add_assertion(
                                Implies(
                                    neighbour_rows,
                                    Not(same_x)
                                )
                            )
                        else:
                            add_assertion(Not(same_x))
        
        # Extract all net names.
        nets = set(chain(*(t.terminals() for t in transistors)))

        # Create net bounds. This will be used to optimize
        # the bounding box perimeter of the nets (for wiring length optimization).
        net_max_x = {net: Int("net_max_x_{}".format(net))
                     for net in nets}

        net_min_x = {net: Int("net_min_x_{}".format(net))
                     for net in nets}

        net_max_y = {net: Int("net_max_y_{}".format(net))
                     for net in nets}

        net_min_y = {net: Int("net_min_y_{}".format(net))
                     for net in nets}

        for t in transistors:
            x, y = transistor_positions[t]

            # TODO: Net positions dependent on transistor terminal.
            #       Now, the net position equals the transistor position.
            #       Make it dependent on the actual terminal (drain, gate, source).
            #       Also depends on transistor flips.
            for net in t.terminals():
                add_assertion(x <= net_max_x[net])
                add_assertion(x >= net_min_x[net])
                add_assertion(y <= net_max_y[net])
                add_assertion(y >= net_min_y[net])

        # Optiimization goals
        # Note: z3 uses lexicographic priorities of objectives by default.
        # Here, the cell width is optimized first.
        # Could be interesting: z3 could also find pareto fronts.

        # # Optimization objective 1
        # # Minimize cell width.
        # solver.minimize(max_x)

        # Optimization objective 2
        # Minimize wiring length (net bounding boxes)
        # TODO: sort criteria by what? Number of terminals?
        if self.minimize_net_bounding_boxes:
            for net in nets:
                # TODO: skip VDD/GND nets
                solver.minimize(net_max_x[net] - net_min_x[net])
                solver.minimize(net_max_y[net] - net_min_y[net])

        # TODO: optimization objective for pin nets.

        logger.info("Run SMT optimizer (Z3)")
        is_sat = solver.check() == z3.sat

        logger.info("Is satisfiable: %s", is_sat)
        if not is_sat:
            return [] # No solution found

        logger.debug("model = %s", solver.model())

        model = solver.model()
        assert len(model) > 0, "model is empty"
        
        cell = Cell(cell_width)
        rows = [cell.lower, cell.upper]
        for t in transistors:
            x, y = transistor_positions[t]
            x = model[x].as_long()
            y = model[y].as_long()
            flip = is_true(model[transistor_flipped[t]])

            flipped = t.flipped() if flip else t

            rows[y][x] = flipped

        return [cell]

    def place(self, transistors: Iterable[Transistor]) -> Iterable[Cell]:
        """
        Place transistors using an SMT solver (Z3).
        :param transistors:
        :return: Placed cell.
        """
        transistors = list(transistors)
        nmos = [t for t in transistors if t.channel_type == ChannelType.NMOS]
        pmos = [t for t in transistors if t.channel_type == ChannelType.PMOS]

        cell_height = 1
        minimal_cell_width = math.ceil(max(len(nmos), len(pmos)) / cell_height)
        maximal_cell_width = max(len(nmos), len(pmos)) * 2
        
        for cell_width in range(minimal_cell_width, maximal_cell_width+1):
            logger.info(f"Try cell width {cell_width}")
            cells = self._place(nmos, pmos, cell_width, cell_height)
            if len(cells) > 0:
                for cell in cells:
                    # Return cells with current `cell_width`
                    yield cell
            else:
                logger.info(f"Placement of width {cell_width} is impossible")

        

def test():
    placer = SMTPlacer()
    from itertools import count
    c = count()
    transistors = [Transistor(ChannelType.PMOS, 1, 1, 3, name=next(c)),
                   Transistor(ChannelType.NMOS, 1, 2, 3, name=next(c)),
                   Transistor(ChannelType.PMOS, 1, 1, 3, name=next(c)),
                   Transistor(ChannelType.NMOS, 1, 2, 3, name=next(c)),
                   Transistor(ChannelType.PMOS, 1, 1, 3, name=next(c)),
                   Transistor(ChannelType.NMOS, 1, 2, 3, name=next(c))]
    placmements = placer.place(transistors)
    placement = next(placements)
    assert placement is not None
