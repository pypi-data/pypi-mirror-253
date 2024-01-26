# This file is part of lsst-resources.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

__all__ = ("os2posix", "posix2os", "NoTransaction", "TransactionProtocol")

import contextlib
import logging
import os
import posixpath
import shutil
import tempfile
from collections.abc import Callable, Iterator
from pathlib import Path, PurePath, PurePosixPath
from typing import Any, Protocol

# Determine if the path separator for the OS looks like POSIX
IS_POSIX = os.sep == posixpath.sep

# Root path for this operating system. This can use getcwd which
# can fail in some situations so in the default case assume that
# posix means posix and only determine explicitly in the non-posix case.
OS_ROOT_PATH = posixpath.sep if IS_POSIX else Path().resolve().root

log = logging.getLogger(__name__)


def os2posix(ospath: str) -> str:
    """Convert a local path description to a POSIX path description.

    Parameters
    ----------
    ospath : `str`
        Path using the local path separator.

    Returns
    -------
    posix : `str`
        Path using POSIX path separator
    """
    if IS_POSIX:
        return ospath

    posix = PurePath(ospath).as_posix()

    # PurePath strips trailing "/" from paths such that you can no
    # longer tell if a path is meant to be referring to a directory
    # Try to fix this.
    if ospath.endswith(os.sep) and not posix.endswith(posixpath.sep):
        posix += posixpath.sep

    return posix


def posix2os(posix: PurePath | str) -> str:
    """Convert a POSIX path description to a local path description.

    Parameters
    ----------
    posix : `str`, `~pathlib.PurePath`
        Path using the POSIX path separator.

    Returns
    -------
    ospath : `str`
        Path using OS path separator
    """
    if IS_POSIX:
        return str(posix)

    posixPath = PurePosixPath(posix)
    paths = list(posixPath.parts)

    # Have to convert the root directory after splitting
    if paths[0] == posixPath.root:
        paths[0] = OS_ROOT_PATH

    # Trailing "/" is stripped so we need to add back an empty path
    # for consistency
    if str(posix).endswith(posixpath.sep):
        paths.append("")

    return os.path.join(*paths)


class NoTransaction:
    """A simple emulation of the
    `~lsst.daf.butler.core.datastore.DatastoreTransaction` class.

    Notes
    -----
    Does nothing. Used as a fallback in the absence of an explicit transaction
    class.
    """

    def __init__(self) -> None:
        return

    @contextlib.contextmanager
    def undoWith(self, name: str, undoFunc: Callable, *args: Any, **kwargs: Any) -> Iterator[None]:
        """No-op context manager to replace
        `~lsst.daf.butler.core.datastore.DatastoreTransaction`.
        """
        yield None


class TransactionProtocol(Protocol):
    """Protocol for type checking transaction interface."""

    @contextlib.contextmanager
    def undoWith(self, name: str, undoFunc: Callable, *args: Any, **kwargs: Any) -> Iterator[None]:
        ...


def makeTestTempDir(default_base: str | None = None) -> str:
    """Create a temporary directory for test usage.

    The directory will be created within ``LSST_RESOURCES_TEST_TMP`` if that
    environment variable is set, falling back to ``LSST_RESOURCES_TMPDIR``
    amd then ``default_base`` if none are set.

    Parameters
    ----------
    default_base : `str`, optional
        Default parent directory. Will use system default if no environment
        variables are set and base is set to `None`.

    Returns
    -------
    dir : `str`
        Name of the new temporary directory.
    """
    base = default_base
    for envvar in ("LSST_RESOURCES_TEST_TMP", "LSST_RESOURCES_TMPDIR"):
        if envvar in os.environ and os.environ[envvar]:
            base = os.environ[envvar]
            break
    return tempfile.mkdtemp(dir=base)


def removeTestTempDir(root: str | None) -> None:
    """Attempt to remove a temporary test directory, but do not raise if
    unable to.

    Unlike `tempfile.TemporaryDirectory`, this passes ``ignore_errors=True``
    to ``shutil.rmtree`` at close, making it safe to use on NFS.

    Parameters
    ----------
    root : `str`, optional
        Name of the directory to be removed.  If `None`, nothing will be done.
    """
    if root is not None and os.path.exists(root):
        shutil.rmtree(root, ignore_errors=True)
