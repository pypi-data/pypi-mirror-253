#
# Copyright (c) 2017-2021 NVIDIA CORPORATION. All rights reserved.
# This file is part of the WebDataset library.
# See the LICENSE file for licensing terms (BSD-style).
#

"""Mock implementations of paddle interfaces when paddle is not available."""


try:
    from paddle.io import DataLoader, IterableDataset
except ModuleNotFoundError:

    class IterableDataset:
        """Empty implementation of IterableDataset when paddle is not available."""

    class DataLoader:
        """Empty implementation of DataLoader when paddle is not available."""


try:
    from paddle import Tensor as PaddleTensor
except ModuleNotFoundError:

    class PaddleTensor:
        """Empty implementation of PaddleTensor when paddle is not available."""
