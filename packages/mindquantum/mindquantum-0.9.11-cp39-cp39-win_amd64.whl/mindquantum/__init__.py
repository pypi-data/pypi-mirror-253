# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
""".. MindQuantum package."""


# start delvewheel patch
def _delvewheel_init_patch_1_3_7():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'mindquantum.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-mindquantum-0.9.11')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-mindquantum-0.9.11')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not ctypes.windll.kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError()))


_delvewheel_init_patch_1_3_7()
del _delvewheel_init_patch_1_3_7
# end delvewheel patch



import os
import sys
import warnings

import numpy as np

from .mqbackend import logging

# isort: split


from . import (
    algorithm,
    config,
    core,
    device,
    dtype,
    engine,
    framework,
    io,
    simulator,
    utils,
)
from .algorithm import *
from .config import *
from .core import *
from .core import gates, operators
from .device import *
from .dtype import *
from .framework import *
from .io import *
from .simulator import *
from .utils import *

if sys.version_info < (3, 8):  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version
else:  # pragma: no cover
    from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("mindquantum")
    __version_info__ = tuple(__version__.split('.'))
    __all__ = ['__version__', '__version_info__']
except (PackageNotFoundError, AttributeError):
    __all__ = []

__all__.extend(core.__all__)
__all__.extend(algorithm.__all__)
__all__.extend(utils.__all__)
__all__.extend(simulator.__all__)
__all__.extend(framework.__all__)
__all__.extend(io.__all__)
__all__.extend(config.__all__)
__all__.extend(device.__all__)
__all__.extend(dtype.__all__)
__all__.sort()