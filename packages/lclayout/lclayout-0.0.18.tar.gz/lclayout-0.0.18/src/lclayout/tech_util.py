# Copyright 2019-2020 Thomas Kramer.
# SPDX-FileCopyrightText: 2022 Thomas Kramer
#
# SPDX-License-Identifier: CERN-OHL-S-2.0

import networkx as nx
from typing import Any, Dict, Tuple
import logging
import importlib.machinery
import types

logger = logging.getLogger(__name__)


def spacing_graph(min_spacing: Dict[Tuple[Any, Any], int]) -> nx.Graph:
    """
    Build a spacing rule graph by mapping the minimal spacing between layer a and layer b to an edge
    a-b in the graph with weight=min_spacing.
    """
    g = nx.Graph()
    for (l1, l2), spacing in min_spacing.items():
        g.add_edge(l1, l2, min_spacing=spacing)
    return g


def load_tech_file(path, module_name='tech'):
    """
    Load a python module containing technology information.
    :param path:
    :param module_name:
    :return: Handle to the module.
    """
    logger.info('Loading tech file: %s', path)
    loader = importlib.machinery.SourceFileLoader('module_name', path)
    tech = types.ModuleType(loader.name)
    loader.exec_module(tech)
    return tech
