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

def fits(
    *,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    dtypes: Union[Sequence[DALIDataType], DALIDataType, None] = None,
    file_filter: Union[str, None] = "*.fits",
    file_list: Union[str, None] = None,
    file_root: Union[str, None] = None,
    files: Union[Sequence[str], str, None] = None,
    hdu_indices: Union[Sequence[int], int, None] = [2],
    initial_fill: Union[int, None] = 1024,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    shuffle_after_epoch: Union[bool, None] = False,
    skip_cached_images: Union[bool, None] = False,
    stick_to_shard: Union[bool, None] = False,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Reads Fits image HDUs from a directory.

    This operator can be used in the following modes:

    1. Read all files from a directory indicated by ``file_root`` that match given ``file_filter``.
    2. Read file names from a text file indicated in ``file_list`` argument.
    3. Read files listed in ``files`` argument.
    4. Number of outputs per sample corresponds to the length of ``hdu_indices`` argument. By default,
    first HDU with data is read from each file, so the number of outputs defaults to 1.


    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `dtypes` : nvidia.dali.types.DALIDataType or list of nvidia.dali.types.DALIDataType, optional
        Data types of the respective outputs.

        If specified, it must be a list of types of respective outputs. By default, all outputs are assumed to be UINT8."
    `file_filter` : str, optional, default = `'*.fits'`
        If a value is specified, the string is interpreted as glob string to filter the
        list of files in the sub-directories of the ``file_root``.

        This argument is ignored when file paths are taken from ``file_list`` or ``files``.
    `file_list` : str, optional
        Path to a text file that contains filenames (one per line).
        The filenames are relative to the location of the text file or to ``file_root``, if specified.

        This argument is mutually exclusive with ``files``.
    `file_root` : str, optional
        Path to a directory that contains the data files.

        If not using ``file_list`` or ``files``, this directory is traversed to discover the files.
        ``file_root`` is required in this mode of operation.
    `files` : str or list of str, optional
        A list of file paths to read the data from.

        If ``file_root`` is provided, the paths are treated as being relative to it.

        This argument is mutually exclusive with ``file_list``.
    `hdu_indices` : int or list of int, optional, default = `[2]`
        HDU indices to read. If not provided, the first HDU after the primary
        will be yielded. Since HDUs are indexed starting from 1, the default value is as follows: hdu_indices = [2].
        Size of the provided list hdu_indices defines number of outputs per sample.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `shuffle_after_epoch` : bool, optional, default = `False`
        If set to True, the reader shuffles the entire dataset after each epoch.

        ``stick_to_shard`` and ``random_shuffle`` cannot be used when this argument is set to True.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...

def video(
    *,
    sequence_length: int,
    bytes_per_sample_hint: Union[Sequence[int], int, None] = [0],
    dont_use_mmap: Union[bool, None] = False,
    filenames: Union[Sequence[str], str, None] = [],
    initial_fill: Union[int, None] = 1024,
    labels: Union[Sequence[int], int, None] = None,
    lazy_init: Union[bool, None] = False,
    num_shards: Union[int, None] = 1,
    pad_last_batch: Union[bool, None] = False,
    prefetch_queue_depth: Union[int, None] = 1,
    preserve: Union[bool, None] = False,
    random_shuffle: Union[bool, None] = False,
    read_ahead: Union[bool, None] = False,
    seed: Union[int, None] = -1,
    shard_id: Union[int, None] = 0,
    skip_cached_images: Union[bool, None] = False,
    step: Union[int, None] = -1,
    stick_to_shard: Union[bool, None] = False,
    stride: Union[int, None] = 1,
    tensor_init_bytes: Union[int, None] = 1048576,
    device: Union[str, None] = None,
    name: Union[str, None] = None,
) -> Union[DataNode, Sequence[DataNode], None]:
    """
    Loads and decodes video files using FFmpeg.

    The video streams can be in most of the container file formats. FFmpeg is used to parse video
    containers and returns a batch of sequences of ``sequence_length`` frames with shape
    ``(N, F, H, W, C)``, where ``N`` is the batch size, and ``F`` is the number of frames).

    .. note::
      Containers which do not support indexing, like MPEG, require DALI to build the index.
    DALI will go through the video and mark keyframes to be able to seek effectively,
    even in the variable frame rate scenario.

    Supported backends
     * 'cpu'
     * 'gpu'


    Keyword args
    ------------
    `sequence_length` : int
        Frames to load per sequence.
    `bytes_per_sample_hint` : int or list of int, optional, default = `[0]`
        Output size hint, in bytes per sample.

        If specified, the operator's outputs residing in GPU or page-locked host memory will be preallocated
        to accommodate a batch of samples of this size.
    `dont_use_mmap` : bool, optional, default = `False`
        If set to True, the Loader will use plain file I/O instead of trying to map
        the file in memory.

        Mapping provides a small performance benefit when accessing a local file system, but most network file
        systems, do not provide optimum performance.
    `filenames` : str or list of str, optional, default = `[]`
        Absolute paths to the video files to load.
    `initial_fill` : int, optional, default = `1024`
        Size of the buffer that is used for shuffling.

        If ``random_shuffle`` is False, this parameter is ignored.
    `labels` : int or list of int, optional
        Labels associated with the files listed in
        ``filenames`` argument. If not provided, no labels will be yielded.
    `lazy_init` : bool, optional, default = `False`
        Parse and prepare the dataset metadata only during the first run instead of
        in the constructor.
    `num_shards` : int, optional, default = `1`
        Partitions the data into the specified number of parts (shards).

        This is typically used for multi-GPU or multi-node training.
    `pad_last_batch` : bool, optional, default = `False`
        If set to True, pads the shard by repeating the last sample.

        .. note::
          If the number of batches differs across shards, this option can cause an entire batch of repeated
          samples to be added to the dataset.
    `prefetch_queue_depth` : int, optional, default = `1`
        Specifies the number of batches to be prefetched by the internal Loader.

        This value should be increased when the pipeline is CPU-stage bound, trading memory
        consumption for better interleaving with the Loader thread.
    `preserve` : bool, optional, default = `False`
        Prevents the operator from being removed from the
        graph even if its outputs are not used.
    `random_shuffle` : bool, optional, default = `False`
        Determines whether to randomly shuffle data.

        A prefetch buffer with a size equal to ``initial_fill`` is used to read data sequentially,
        and then samples are selected randomly to form a batch.
    `read_ahead` : bool, optional, default = `False`
        Determines whether the accessed data should be read ahead.

        For large files such as LMDB, RecordIO, or TFRecord, this argument slows down the first access but
        decreases the time of all of the following accesses.
    `seed` : int, optional, default = `-1`
        Random seed.

        If not provided, it will be populated based on the global seed of the pipeline.
    `shard_id` : int, optional, default = `0`
        Index of the shard to read.
    `skip_cached_images` : bool, optional, default = `False`
        If set to True, the loading data will be skipped when the sample is
        in the decoder cache.

        In this case, the output of the loader will be empty.
    `step` : int, optional, default = `-1`
        Frame interval between each sequence.

        When the value is less than 0, ``step`` is set to ``sequence_length``.
    `stick_to_shard` : bool, optional, default = `False`
        Determines whether the reader should stick to a data shard instead of going through
        the entire dataset.

        If decoder caching is used, it significantly reduces the amount of data to be cached, but
        might affect accuracy of the training.
    `stride` : int, optional, default = `1`
        Distance between consecutive frames in the sequence.
    `tensor_init_bytes` : int, optional, default = `1048576`
        Hint for how much memory to allocate per image.

    """
    ...
