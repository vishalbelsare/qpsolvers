#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2021 Stéphane Caron <stephane.caron@normalesup.org>
#
# This file is part of qpsolvers.
#
# qpsolvers is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# qpsolvers is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with qpsolvers. If not, see <http://www.gnu.org/licenses/>.

"""Types for solve_qp function arguments."""

from typing import Union

from numpy import ndarray
from scipy.sparse import csc_matrix

try:
    from cvxopt import spmatrix

    Matrix = Union[ndarray, csc_matrix, spmatrix]
    Vector = Union[ndarray, csc_matrix, spmatrix]
except ImportError:
    Matrix = Union[ndarray, csc_matrix]  # type: ignore
    Vector = Union[ndarray, csc_matrix]  # type: ignore

__all__ = [
    "Matrix",
    "Vector",
]
