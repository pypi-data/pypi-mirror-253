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

from . import decoders as decoders
from . import readers as readers
from . import inputs as inputs

class AudioResample:
    """
    .. warning::

       This operator is now deprecated. Use :meth:`AudioResample` instead.

       This operator was moved out from the experimental phase, and is now a regular DALI operator. This is just an deprecated alias kept for backward compatibility.

    Legacy alias for :meth:`audio_resample`.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        in_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        out_length: Union[DataNode, TensorLikeArg, int, None] = None,
        out_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        preserve: Union[bool, None] = False,
        quality: Union[float, None] = 50.0,
        scale: Union[DataNode, TensorLikeArg, float, None] = None,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        in_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        out_length: Union[DataNode, TensorLikeArg, int, None] = None,
        out_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        preserve: Union[bool, None] = False,
        quality: Union[float, None] = 50.0,
        scale: Union[DataNode, TensorLikeArg, float, None] = None,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """ """
        ...
    @overload
    def __call__(
        self,
        __input: List[DataNode],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        in_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        out_length: Union[DataNode, TensorLikeArg, int, None] = None,
        out_rate: Union[DataNode, TensorLikeArg, float, None] = None,
        preserve: Union[bool, None] = False,
        quality: Union[float, None] = 50.0,
        scale: Union[DataNode, TensorLikeArg, float, None] = None,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """ """
        ...

class Debayer:
    """
    Performs image demosaicing/debayering.

    Converts single-channel image to RGB using specified color filter array.

    The supported input types are ``uint8_t`` and ``uint16_t``.
    The input images must be 2D tensors (``HW``) or 3D tensors (``HWC``) where the number of channels is 1.
    The operator supports sequence of images/video-like inputs (layout ``FHW``).

    For example, the following snippet presents debayering of batch of image sequences::

      def bayered_sequence(sample_info):
        # some actual source of video inputs with corresponding pattern
        # as opencv-style string
        video, bayer_pattern = get_sequence(sample_info)
        if bayer_pattern == "bggr":
            blue_position = [0, 0]
        elif bayer_pattern == "gbrg":
            blue_position = [0, 1]
        elif bayer_pattern == "grbg":
            blue_position = [1, 0]
        else:
            assert bayer_pattern == "rggb"
            blue_position = [1, 1]
        return video, np.array(blue_position, dtype=np.int32)

      @pipeline_def
      def debayer_pipeline():
        bayered_sequences, blue_positions = fn.external_source(
          source=bayered_sequence, batch=False, num_outputs=2,
          layout=["FHW", None])  # note the "FHW" layout, for plain images it would be "HW"
        debayered_sequences = fn.experimental.debayer(
          bayered_sequences.gpu(), blue_position=blue_positions)
        return debayered_sequences



    This operator allows sequence inputs.

    Supported backends
     * 'gpu'


    Keyword args
    ------------
    `blue_position` : int or list of int or TensorList of int
        The layout of color filter array/bayer tile.

        A position of the blue value in the 2x2 bayer tile.
        The supported values correspond to the following OpenCV bayer layouts:

        * ``(0, 0)`` - ``BG``/``BGGR``
        * ``(0, 1)`` - ``GB``/``GBRG``
        * ``(1, 0)`` - ``GR``/``GRBG``
        * ``(1, 1)`` - ``RG``/``RGGB``

        The argument follows OpenCV's convention of referring to a 2x2 tile that starts
        in the second row and column of the sensors' matrix.

        For example, the ``(0, 0)``/``BG``/``BGGR`` corresponds to the following matrix of sensors:

        .. list-table::
           :header-rows: 0

           * - R
             - G
             - R
             - G
             - R
           * - G
             - **B**
             - **G**
             - B
             - G
           * - R
             - **G**
             - **R**
             - G
             - R
           * - G
             - B
             - G
             - B
             - G

        Supports :func:`per-frame<nvidia.dali.fn.per_frame>` inputs.
    `algorithm` : str, optional, default = `'bilinear_npp'`
        The algorithm to be used when inferring missing colours for any given pixel.
        Currently only ``bilinear_npp`` is supported.

        * The ``bilinear_npp`` algorithm uses bilinear interpolation to infer red and blue values.
          For green values a bilinear interpolation with chroma correlation is used as explained in
          `NPP documentation <https://docs.nvidia.com/cuda/npp/group__image__color__debayer.html>`_.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        blue_position: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        algorithm: Union[str, None] = "bilinear_npp",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        blue_position: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        algorithm: Union[str, None] = "bilinear_npp",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HW', 'HWC', 'FHW', 'FHWC')
            Input to the operator.

        """
        ...
    @overload
    def __call__(
        self,
        __input: List[DataNode],
        /,
        *,
        blue_position: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = None,
        algorithm: Union[str, None] = "bilinear_npp",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HW', 'HWC', 'FHW', 'FHWC')
            Input to the operator.

        """
        ...

class Equalize:
    """
    Performs grayscale/per-channel histogram equalization.

    The supported inputs are images and videos of uint8_t type.

    This operator allows sequence inputs.

    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HW', 'HWC', 'CHW', 'FHW', 'FHWC', 'FCHW')
            Input to the operator.

        """
        ...
    @overload
    def __call__(
        self,
        __input: List[DataNode],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(__input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HW', 'HWC', 'CHW', 'FHW', 'FHWC', 'FCHW')
            Input to the operator.

        """
        ...

class Filter:
    """
    Convolves the image with the provided filter.

    .. note::
      In fact, the operator computes a correlation, not a convolution,
      i.e. the order of filter elements is not flipped when computing the product of
      the filter and the image.



    This operator allows sequence inputs.

    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `anchor` : int or list of int or TensorList of int, optional, default = `[-1]`
        Specifies the position of the filter over the input.

        If the filter size is ``(r, s)`` and the anchor is ``(a, b)``, the output
        at position ``(x, y)`` is a product of the filter and the input rectangle spanned between the
        corners: top-left ``(x - a, y - b)`` and bottom-right ``(x - a + r - 1, x - b + s - 1)``.

        If the -1 (the default) is specifed, the middle (rounded down to integer)
        of the filter extents is used, which, for odd sized filters, results in the filter
        centered over the input.

        The anchor must be, depending on the input dimensionality, a 2D or 3D point whose each extent lies
        within filter boundaries (``[0, ..., filter_extent - 1]``). The ordering of anchor's extents
        corresponds to the order of filter's extents.

        The parameter is ignored in ``"valid"`` mode.
        .

        Supports :func:`per-frame<nvidia.dali.fn.per_frame>` inputs.
    `border` : str, optional, default = `'reflect_101'`
        Controls how to handle out-of-bound filter positions over the sample.

        Supported values are: ``"reflect_101"``, ``"reflect_1001"``, ``"wrap"``,
        ``"clamp"``, ``"constant"``.

        - ``"reflect_101"`` (default), reflects the input but does not repeat the outermost
          values (``dcb|abcdefghi|hgf``).
        - ``"reflect_1001"``: reflects the input including outermost values (``cba|abcdefghi|ihg``)
        - ``"wrap"``: wraps the input (``ghi|abcdefghi|abc``).
        - ``"clamp"``: the input is padded with outermost values (``aaa|abcdefghi|iii``).
        - ``"constant"``: the input is padded with the user-provided scalar (zeros by default).
          within the sample.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type.
        The output type can either be float or must be same as input type.
        If not set, the input type is used.

        .. note::
          The intermediate type used for actual computation is float32. If the output is of integral type,
          the values will be clamped to the output type range.
    `mode` : str, optional, default = `'same'`
        Supported values are: ``"same"`` and ``"valid"``.

        - ``"same"`` (default): The input and output sizes are the same and ``border`` is used
          to handle out-of-bound filter positions.
        - ``"valid"``: the output sample is cropped (by ``filter_extent - 1``) so that all
          filter positions lie fully within the input sample.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        anchor: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [-1],
        border: Union[str, None] = "reflect_101",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mode: Union[str, None] = "same",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __data: Union[DataNode, TensorLikeIn],
        __filter: Union[DataNode, TensorLikeIn],
        __fill_value: Union[DataNode, TensorLikeIn, None] = None,
        /,
        *,
        anchor: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [-1],
        border: Union[str, None] = "reflect_101",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mode: Union[str, None] = "same",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(data, filter, fill_value = None, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__data` : TensorList
            Batch of input samples.

            Sample can be an image, a video or volumetric (3D) data.
            Samples can contain channels: channel-first and channel-last layouts are supported.
            In case of video/sequences, the frame extent must preced the channels extent, i.e.,
            for example, a video with ``"FCHW"`` layout is supported, but ``"CFHW"`` samples are not.

            Samples with the following types are supported:
            int8, int16, uint8, uint16, float16, float32.

            Please note that the intermediate type used for the computation is always float32.

            .. note::
              The CPU variant does not support volumetric (3D) data, nor inputs of types: int8 and float16.

        `__filter` : TensorList
            Batch of filters.

            For inputs with two spatial dimensions (images or video), each filter must be a 2D array
            (or a sequence of 2D arrays to be applied
            :func:`per-frame<nvidia.dali.fn.per_frame>` to a video input).
            For volumetric inputs, the filter must be a 3D array.
            The filter values must have float32 type.
        `__fill_value` : TensorList, optional
            Batch of scalars used for padding.

            If ``"border"`` is set to ``"constant"``, the input samples will be padded with
            the corresponding scalars when convolved with the filter.
            The scalars must be of the same type as the input samples.
            For video/sequence input, an array of scalars can be specified to be applied
            :func:`per-frame<nvidia.dali.fn.per_frame>`.


        """
        ...
    @overload
    def __call__(
        self,
        __data: Union[List[DataNode], DataNode, TensorLikeIn],
        __filter: Union[List[DataNode], DataNode, TensorLikeIn],
        __fill_value: Union[List[DataNode], DataNode, TensorLikeIn, None] = None,
        /,
        *,
        anchor: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [-1],
        border: Union[str, None] = "reflect_101",
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        mode: Union[str, None] = "same",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(data, filter, fill_value = None, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__data` : TensorList
            Batch of input samples.

            Sample can be an image, a video or volumetric (3D) data.
            Samples can contain channels: channel-first and channel-last layouts are supported.
            In case of video/sequences, the frame extent must preced the channels extent, i.e.,
            for example, a video with ``"FCHW"`` layout is supported, but ``"CFHW"`` samples are not.

            Samples with the following types are supported:
            int8, int16, uint8, uint16, float16, float32.

            Please note that the intermediate type used for the computation is always float32.

            .. note::
              The CPU variant does not support volumetric (3D) data, nor inputs of types: int8 and float16.

        `__filter` : TensorList
            Batch of filters.

            For inputs with two spatial dimensions (images or video), each filter must be a 2D array
            (or a sequence of 2D arrays to be applied
            :func:`per-frame<nvidia.dali.fn.per_frame>` to a video input).
            For volumetric inputs, the filter must be a 3D array.
            The filter values must have float32 type.
        `__fill_value` : TensorList, optional
            Batch of scalars used for padding.

            If ``"border"`` is set to ``"constant"``, the input samples will be padded with
            the corresponding scalars when convolved with the filter.
            The scalars must be of the same type as the input samples.
            For video/sequence input, an array of scalars can be specified to be applied
            :func:`per-frame<nvidia.dali.fn.per_frame>`.


        """
        ...

class MedianBlur:
    """

    Median blur performs smoothing of an image or sequence of images by replacing each pixel
    with the median color of a surrounding rectangular region.


    Supported backends
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `window_size` : int or list of int or TensorList of int, optional, default = `[3, 3]`
        The size of the window over which the smoothing is performed

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        window_size: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [3, 3],
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        window_size: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [3, 3],
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HWC', 'FHWC', 'CHW', 'FCHW')
            Input data. Must be images in HWC or CHW layout, or a sequence of those.


        """
        ...
    @overload
    def __call__(
        self,
        __input: List[DataNode],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        window_size: Union[DataNode, TensorLikeArg, Sequence[int], int, None] = [3, 3],
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(input, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HWC', 'FHWC', 'CHW', 'FCHW')
            Input data. Must be images in HWC or CHW layout, or a sequence of those.


        """
        ...

class PeekImageShape:
    """
    Obtains the shape of the encoded image.

    Supported backends
     * 'cpu'


    Keyword args
    ------------
    `adjust_orientation` : bool, optional, default = `True`
        Use the EXIF orientation metadata when calculating the shape.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional, default = `DALIDataType.INT64`
        Data type, to which the sizes are converted.
    `image_type` : :class:`nvidia.dali.types.DALIImageType`, optional, default = `DALIImageType.RGB`
        Color format of the image.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        adjust_orientation: Union[bool, None] = True,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = DALIDataType.INT64,
        image_type: Union[DALIImageType, None] = DALIImageType.RGB,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        adjust_orientation: Union[bool, None] = True,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = DALIDataType.INT64,
        image_type: Union[DALIImageType, None] = DALIImageType.RGB,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
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
        __input: List[DataNode],
        /,
        *,
        adjust_orientation: Union[bool, None] = True,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = DALIDataType.INT64,
        image_type: Union[DALIImageType, None] = DALIImageType.RGB,
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
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

class Remap:
    """

    The remap operation applies a generic geometrical transformation to an image. In other words,
    it takes pixels from one place in the input image and puts them in another place in
    the output image. The transformation is described by ``mapx`` and ``mapy`` parameters, where:

        output(x,y) = input(mapx(x,y),mapy(x,y))

    The type of the output tensor will match the type of the input tensor.

    Handles only HWC layout.

    Currently picking border policy is not supported.
    The ``DALIBorderType`` will always be ``CONSTANT`` with the value ``0``.


    This operator allows sequence inputs.

    Supported backends
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `interp` : :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Interpolation type.
    `pixel_origin` : str, optional, default = `'corner'`

        Pixel origin. Possible values: ``"corner"``, ``"center"``.

        Defines which part of the pixel (upper-left corner or center) is interpreted as its origin.
        This value impacts the interpolation result. To match OpenCV, please pick ``"center"``.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.

    """

    def __init__(
        self,
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        interp: Union[DALIInterpType, None] = DALIInterpType.INTERP_LINEAR,
        pixel_origin: Union[str, None] = "corner",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        __mapx: Union[DataNode, TensorLikeIn],
        __mapy: Union[DataNode, TensorLikeIn],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        interp: Union[DALIInterpType, None] = DALIInterpType.INTERP_LINEAR,
        pixel_origin: Union[str, None] = "corner",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> DataNode:
        """__call__(input, mapx, mapy, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HWC', 'FHWC')
            Input data. Must be a 1- or 3-channel HWC image.
        `__mapx` : TensorList of float ('HWC', 'HW', 'FHWC', 'FHW', 'F***', 'F**')
            Defines the remap transformation for x coordinates.
        `__mapy` : TensorList of float ('HWC', 'HW', 'FHWC', 'FHW', 'F***', 'F**')
            Defines the remap transformation for y coordinates.


        """
        ...
    @overload
    def __call__(
        self,
        __input: Union[List[DataNode], DataNode, TensorLikeIn],
        __mapx: Union[List[DataNode], DataNode, TensorLikeIn],
        __mapy: Union[List[DataNode], DataNode, TensorLikeIn],
        /,
        *,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        interp: Union[DALIInterpType, None] = DALIInterpType.INTERP_LINEAR,
        pixel_origin: Union[str, None] = "corner",
        preserve: Union[bool, None] = False,
        seed: Union[int, None] = -1,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> Union[DataNode, List[DataNode]]:
        """__call__(input, mapx, mapy, **kwargs)

        Operator call to be used in graph definition.

        Args
        ----
        `__input` : TensorList ('HWC', 'FHWC')
            Input data. Must be a 1- or 3-channel HWC image.
        `__mapx` : TensorList of float ('HWC', 'HW', 'FHWC', 'FHW', 'F***', 'F**')
            Defines the remap transformation for x coordinates.
        `__mapy` : TensorList of float ('HWC', 'HW', 'FHWC', 'FHW', 'F***', 'F**')
            Defines the remap transformation for y coordinates.


        """
        ...

class TensorResize:
    """
    Resize tensors.

    This operator allows sequence inputs and supports volumetric data.

    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `alignment` : float or list of float or TensorList of float, optional, default = `[0.5]`
        Determines the position of the ROI
        when using scales (provided or calculated).

        The real output size must be integral and may differ from "ideal" output size calculated as input
        (or ROI) size multiplied by the scale factor. In that case, the output size is rounded (according
        to `size_rounding` policy) and the input ROI needs to be adjusted to maintain the scale factor.
        This parameter defines which relative point of the ROI should retain its position in the output.

        This point is calculated as ``center = (1 - alignment) * roi_start + alignment * roi_end``.
        Alignment 0.0 denotes alignment with the start of the ROI, 0.5 with the center of the region, and 1.0 with the end.
        Note that when ROI is not specified, roi_start=0 and roi_end=input_size is assumed.

        When using 0.5 (default), the resize operation has flip invariant properties (flipping after resizing is
        mathematically equivalent to resizing after flipping).

        The value of this argument contains as many elements as dimensions provided for
        sizes/scales. If only one value is provided, it is applied to all dimensions.
    `antialias` : bool, optional, default = `True`
        If enabled, it applies an antialiasing filter when scaling down.

        .. note::
          Nearest neighbor interpolation does not support antialiasing.
    `axes` : int or list of int, optional
        Indices of dimensions that `sizes`, `scales`, `max_size`, `roi_start`, `roi_end` refer to.

        Accepted range is [-ndim, ndim-1]. Negative indices are counted from the back.

        By default, all dimensions are assumed. The ``axis_names`` and ``axes`` arguments are mutually exclusive.
    `axis_names` : :ref:`layout str<layout_str_doc>`, optional
        Names of the axes that `sizes`, `scales`, `max_size`, `roi_start`, `roi_end` refer to.

        By default, all dimensions are assumed. The ``axis_names`` and ``axes`` arguments are mutually exclusive.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dtype` : :class:`nvidia.dali.types.DALIDataType`, optional
        Output data type.

        Must be same as input type or ``float``. If not set, input type is used.
    `interp_type` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Type of interpolation to be used.

        Use ``min_filter`` and ``mag_filter`` to specify different filtering for downscaling and upscaling.

        .. note::
          Usage of INTERP_TRIANGULAR is now deprecated and it should be replaced by a combination of
        INTERP_LINEAR with ``antialias`` enabled.
    `mag_filter` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Filter used when scaling up.
    `max_size` : float or list of float, optional
        Limit of the output size.

        When the operator is configured to keep aspect ratio and only the smaller dimension is specified,
        the other(s) can grow very large. This can happen when using ``resize_shorter`` argument
        or "not_smaller" mode or when some extents are left unspecified.

        This parameter puts a limit to how big the output can become. This value can be specified per-axis
        or uniformly for all axes.

        .. note::
          When used with "not_smaller" mode or ``resize_shorter`` argument, ``max_size`` takes
          precedence and the aspect ratio is kept - for example, resizing with
          ``mode="not_smaller", size=800, max_size=1400`` an image of size 1200x600 would be resized to
          1400x700.
    `min_filter` : :class:`nvidia.dali.types.DALIInterpType` or TensorList of :class:`nvidia.dali.types.DALIInterpType`, optional, default = `DALIInterpType.INTERP_LINEAR`
        Filter used when scaling down.
    `minibatch_size` : int, optional, default = `32`
        Maximum number of images that are processed in
        a kernel call.
    `mode` : str, optional, default = `'default'`
        Resize mode.

          Here is a list of supported modes:

          * | ``"default"`` - image is resized to the specified size.
            | Missing extents are scaled with the average scale of the provided ones.
          * | ``"stretch"`` - image is resized to the specified size.
            | Missing extents are not scaled at all.
          * | ``"not_larger"`` - image is resized, keeping the aspect ratio, so that no extent of the
              output image exceeds the specified size.
            | For example, a 1280x720, with a desired output size of 640x480, actually produces
              a 640x360 output.
          * | ``"not_smaller"`` - image is resized, keeping the aspect ratio, so that no extent of the
              output image is smaller than specified.
            | For example, a 640x480 image with a desired output size of 1920x1080, actually produces
              a 1920x1440 output.

            This argument is mutually exclusive with ``resize_longer`` and ``resize_shorter``
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `roi_end` : float or list of float or TensorList of float, optional
        End of the input region of interest (ROI).

        Must be specified together with ``roi_start``. The coordinates follow the tensor shape order, which is
        the same as ``size``. The coordinates can be either absolute (in pixels, which is the default) or
        relative (0..1), depending on the value of ``relative_roi`` argument. If the ROI origin is greater
        than the ROI end in any dimension, the region is flipped in that dimension.
    `roi_relative` : bool, optional, default = `False`
        If true, ROI coordinates are relative to the input size,
        where 0 denotes top/left and 1 denotes bottom/right
    `roi_start` : float or list of float or TensorList of float, optional
        Origin of the input region of interest (ROI).

        Must be specified together with ``roi_end``. The coordinates follow the tensor shape order, which is
        the same as ``size``. The coordinates can be either absolute (in pixels, which is the default) or
        relative (0..1), depending on the value of ``relative_roi`` argument. If the ROI origin is greater
        than the ROI end in any dimension, the region is flipped in that dimension.
    `scales` : float or list of float or TensorList of float, optional
        Scale factors.

        The resulting output size is calculated as
        ``out_size = size_rounding(scale_factor * original_size)``.
        See ``size_rounding`` for a list of supported rounding policies.

        When ``axes`` is provided, the scale factor values refer to the axes specified.
        Note: Arguments ``sizes`` and ``scales`` are mutually exclusive.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `size_rounding` : str, optional, default = `'round'`
        Determines the rounding policy when using scales.

        Possible values are:
        * | ``"round"`` - Rounds the resulting size to the nearest integer value, with halfway cases rounded away from zero.
        * | ``"truncate"`` - Discards the fractional part of the resulting size.
        * | ``"ceil"`` - Rounds up the resulting size to the next integer value.
    `sizes` : float or list of float or TensorList of float, optional
        Output sizes.

        When ``axes`` is provided, the size values refer to the axes specified.
        Note: Arguments ``sizes`` and ``scales`` are mutually exclusive.
    `subpixel_scale` : bool, optional, default = `True`
        If True, fractional sizes, directly specified or
        calculated, will cause the input ROI to be adjusted to keep the scale factor.

        Otherwise, the scale factor will be adjusted so that the source image maps to
        the rounded output size.
    `temp_buffer_hint` : int, optional, default = `0`
        Initial size in bytes, of a temporary buffer for resampling.

        .. note::
          This argument is ignored for the CPU variant.

    """

    def __init__(
        self,
        /,
        *,
        alignment: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [0.5],
        antialias: Union[bool, None] = True,
        axes: Union[Sequence[int], int, None] = None,
        axis_names: Union[str, None] = None,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        interp_type: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        mag_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        max_size: Union[Sequence[float], float, None] = None,
        min_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        minibatch_size: Union[int, None] = 32,
        mode: Union[str, None] = "default",
        preserve: Union[bool, None] = False,
        roi_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        roi_relative: Union[bool, None] = False,
        roi_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        scales: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        seed: Union[int, None] = -1,
        size_rounding: Union[str, None] = "round",
        sizes: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        subpixel_scale: Union[bool, None] = True,
        temp_buffer_hint: Union[int, None] = 0,
        device: Union[str, None] = None,
        name: Union[str, None] = None,
    ) -> None: ...
    @overload
    def __call__(
        self,
        __input: Union[DataNode, TensorLikeIn],
        /,
        *,
        alignment: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [0.5],
        antialias: Union[bool, None] = True,
        axes: Union[Sequence[int], int, None] = None,
        axis_names: Union[str, None] = None,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        interp_type: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        mag_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        max_size: Union[Sequence[float], float, None] = None,
        min_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        minibatch_size: Union[int, None] = 32,
        mode: Union[str, None] = "default",
        preserve: Union[bool, None] = False,
        roi_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        roi_relative: Union[bool, None] = False,
        roi_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        scales: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        seed: Union[int, None] = -1,
        size_rounding: Union[str, None] = "round",
        sizes: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        subpixel_scale: Union[bool, None] = True,
        temp_buffer_hint: Union[int, None] = 0,
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
        __input: List[DataNode],
        /,
        *,
        alignment: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = [0.5],
        antialias: Union[bool, None] = True,
        axes: Union[Sequence[int], int, None] = None,
        axis_names: Union[str, None] = None,
        bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
        dtype: Union[DALIDataType, None] = None,
        interp_type: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        mag_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        max_size: Union[Sequence[float], float, None] = None,
        min_filter: Union[
            DataNode, TensorLikeArg, DALIInterpType, None
        ] = DALIInterpType.INTERP_LINEAR,
        minibatch_size: Union[int, None] = 32,
        mode: Union[str, None] = "default",
        preserve: Union[bool, None] = False,
        roi_end: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        roi_relative: Union[bool, None] = False,
        roi_start: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        scales: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        seed: Union[int, None] = -1,
        size_rounding: Union[str, None] = "round",
        sizes: Union[DataNode, TensorLikeArg, Sequence[float], float, None] = None,
        subpixel_scale: Union[bool, None] = True,
        temp_buffer_hint: Union[int, None] = 0,
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
