# Copyright 2019-2020 Thomas Kramer.
# SPDX-FileCopyrightText: 2022 Thomas Kramer
#
# SPDX-License-Identifier: CERN-OHL-S-2.0

from ..data_types import *

from typing import Iterable


class TransistorPlacer:
    """
    Interface definition of a transistor placement algorithm.
    """

    def place(self, transistors: Iterable[Transistor]) -> Iterable[Cell]:
        pass
