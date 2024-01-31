# Copyright (c) 2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Union, Optional, overload
from typing import Any, List, Sequence

from nvidia.dali._typing import TensorLikeIn, TensorLikeArg

from nvidia.dali.data_node import DataNode

from nvidia.dali.types import DALIDataType, DALIImageType, DALIInterpType

class CoinFlip:
    """
    Generates random boolean values following a bernoulli distribution.

    The probability of generating a value 1 (true) is determined by the ``probability`` argument.

    The shape of the generated data can be either specified explicitly with a ``shape`` argument,
    or chosen to match the shape of the input, if provided. If none are present, a single value per
    sample is generated.


    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type.

        .. note::
          The generated numbers are converted to the output data type, rounding and clamping if necessary.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `probability` : float or TensorList of float, optional, default = `0.5`
        Probability of value 1.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shape` : int or list of int or TensorList of int, optional
        Shape of the output data.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        probability: Union[DataNode, TensorLikeArg, float, None] = 0.5,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        probability: Union[DataNode, TensorLikeArg, float, None] = 0.5,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...
    @overload
    def __call__(
        self,
        __input: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        probability: Union[DataNode, TensorLikeArg, float, None] = 0.5,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...

class Normal:
    """
    Generates random numbers following a normal distribution.

    The shape of the generated data can be either specified explicitly with a ``shape`` argument,
    or chosen to match the shape of the input, if provided. If none are present, a single value per
    sample is generated.


    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type.

        .. note::
          The generated numbers are converted to the output data type, rounding and clamping if necessary.
    `mean` : float or TensorList of float, optional, default = `0.0`
        Mean of the distribution.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shape` : int or list of int or TensorList of int, optional
        Shape of the output data.
    `stddev` : float or TensorList of float, optional, default = `1.0`
        Standard deviation of the distribution.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mean: Union[DataNode, TensorLikeArg, float, None] = 0.0,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        stddev: Union[DataNode, TensorLikeArg, float, None] = 1.0,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mean: Union[DataNode, TensorLikeArg, float, None] = 0.0,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        stddev: Union[DataNode, TensorLikeArg, float, None] = 1.0,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...
    @overload
    def __call__(
        self,
        __input: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mean: Union[DataNode, TensorLikeArg, float, None] = 0.0,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        stddev: Union[DataNode, TensorLikeArg, float, None] = 1.0,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...

class Uniform:
    """
    Generates random numbers following a uniform distribution.

    It can be configured to produce a continuous uniform distribution in the ``range`` [min, max),
    or a discrete uniform distribution where any of the specified ``values`` [v0, v1, ..., vn] occur
    with equal probability.

    The shape of the generated data can be either specified explicitly with a ``shape`` argument,
    or chosen to match the shape of the input, if provided. If none are present, a scalar is
    generated.


    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type.

        .. note::
          The generated numbers are converted to the output data type, rounding and clamping if necessary.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `range` : float or list of float or TensorList of float, optional, default = `[-1.0, 1.0]`
        Range ``[min, max)`` of a continuous uniform distribution.

        This argument is mutually exclusive with ``values``.

        .. warning::
          When specifying an integer type as ``dtype``, the generated numbers can go outside
          the specified range, due to rounding.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shape` : int or list of int or TensorList of int, optional
        Shape of the output data.
    `values` : float or list of float or TensorList of float, optional
        The discrete values [v0, v1, ..., vn] produced by a discrete uniform distribution.

        This argument is mutually exclusive with ``range``.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        range: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [-1.0, 1.0],
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        values: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        range: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [-1.0, 1.0],
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        values: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...
    @overload
    def __call__(
        self,
        __input: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        preserve: Union[bool, None] = False,
        range: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [-1.0, 1.0],
        seed: Union[int, None] = -1,
        shape: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        values: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList
            Input to the operator.

        """
        ...
