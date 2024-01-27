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

__all__ = (
    "getS3Client",
    "s3CheckFileExists",
    "bucketExists",
    "setAwsEnvCredentials",
    "unsetAwsEnvCredentials",
)

import functools
import os
from typing import Optional, Tuple, Union

try:
    import boto3
except ImportError:
    boto3 = None

try:
    import botocore
except ImportError:
    botocore = None

from ._resourcePath import ResourcePath
from .location import Location


def getS3Client() -> boto3.client:
    """Create a S3 client with AWS (default) or the specified endpoint.

    Returns
    -------
    s3client : `botocore.client.S3`
        A client of the S3 service.

    Notes
    -----
    The endpoint URL is from the environment variable S3_ENDPOINT_URL.
    If none is specified, the default AWS one is used.
    """
    if boto3 is None:
        raise ModuleNotFoundError("Could not find boto3. Are you sure it is installed?")
    if botocore is None:
        raise ModuleNotFoundError("Could not find botocore. Are you sure it is installed?")

    endpoint = os.environ.get("S3_ENDPOINT_URL", None)
    if not endpoint:
        endpoint = None  # Handle ""

    return _get_s3_client(endpoint)


@functools.lru_cache()
def _get_s3_client(endpoint: str) -> boto3.client:
    # Helper function to cache the client for this endpoint
    config = botocore.config.Config(read_timeout=180, retries={"mode": "adaptive", "max_attempts": 10})

    return boto3.client("s3", endpoint_url=endpoint, config=config)


def s3CheckFileExists(
    path: Union[Location, ResourcePath, str],
    bucket: Optional[str] = None,
    client: Optional[boto3.client] = None,
) -> Tuple[bool, int]:
    """Return if the file exists in the bucket or not.

    Parameters
    ----------
    path : `Location`, `ResourcePath` or `str`
        Location or ResourcePath containing the bucket name and filepath.
    bucket : `str`, optional
        Name of the bucket in which to look. If provided, path will be assumed
        to correspond to be relative to the given bucket.
    client : `boto3.client`, optional
        S3 Client object to query, if not supplied boto3 will try to resolve
        the credentials as in order described in its manual_.

    Returns
    -------
    exists : `bool`
        True if key exists, False otherwise.
    size : `int`
        Size of the key, if key exists, in bytes, otherwise -1.

    Notes
    -----
    S3 Paths are sensitive to leading and trailing path separators.

    .. _manual: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/\
    configuration.html#configuring-credentials
    """
    if boto3 is None:
        raise ModuleNotFoundError("Could not find boto3. Are you sure it is installed?")

    if client is None:
        client = getS3Client()

    if isinstance(path, str):
        if bucket is not None:
            filepath = path
        else:
            uri = ResourcePath(path)
            bucket = uri.netloc
            filepath = uri.relativeToPathRoot
    elif isinstance(path, (ResourcePath, Location)):
        bucket = path.netloc
        filepath = path.relativeToPathRoot
    else:
        raise TypeError(f"Unsupported path type: {path!r}.")

    try:
        obj = client.head_object(Bucket=bucket, Key=filepath)
        return (True, obj["ContentLength"])
    except client.exceptions.ClientError as err:
        # resource unreachable error means key does not exist
        if err.response["ResponseMetadata"]["HTTPStatusCode"] == 404:
            return (False, -1)
        # head_object returns 404 when object does not exist only when user has
        # s3:ListBucket permission. If list permission does not exist a 403 is
        # returned. In practical terms this generally means that the file does
        # not exist, but it could also mean user lacks s3:GetObject permission:
        # https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectHEAD.html
        # I don't think its possible to discern which case is it with certainty
        if err.response["ResponseMetadata"]["HTTPStatusCode"] == 403:
            raise PermissionError(
                "Forbidden HEAD operation error occured. "
                "Verify s3:ListBucket and s3:GetObject "
                "permissions are granted for your IAM user. "
            ) from err
        raise


def bucketExists(bucketName: str, client: Optional[boto3.client] = None) -> bool:
    """Check if the S3 bucket with the given name actually exists.

    Parameters
    ----------
    bucketName : `str`
        Name of the S3 Bucket
    client : `boto3.client`, optional
        S3 Client object to query, if not supplied boto3 will try to resolve
        the credentials as in order described in its manual_.

    Returns
    -------
    exists : `bool`
        True if it exists, False if no Bucket with specified parameters is
        found.

    .. _manual: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/\
    configuration.html#configuring-credentials
    """
    if boto3 is None:
        raise ModuleNotFoundError("Could not find boto3. Are you sure it is installed?")

    if client is None:
        client = getS3Client()
    try:
        client.get_bucket_location(Bucket=bucketName)
        return True
    except client.exceptions.NoSuchBucket:
        return False


def setAwsEnvCredentials(
    accessKeyId: str = "dummyAccessKeyId", secretAccessKey: str = "dummySecretAccessKey"
) -> bool:
    """Set AWS credentials environmental variables.

    Parameters
    ----------
    accessKeyId : `str`
        Value given to AWS_ACCESS_KEY_ID environmental variable. Defaults to
        `dummyAccessKeyId`.
    secretAccessKey : `str`
        Value given to AWS_SECRET_ACCESS_KEY environmental variable. Defaults
        to `dummySecretAccessKey`.

    Returns
    -------
    setEnvCredentials : `bool`
        True when environmental variables were set, False otherwise.

    Notes
    -----
    If either AWS_ACCESS_KEY_ID or AWS_SECRET_ACCESS_KEY are not set, both
    values are overwritten to ensure that the values are consistent.
    """
    if "AWS_ACCESS_KEY_ID" not in os.environ or "AWS_SECRET_ACCESS_KEY" not in os.environ:
        os.environ["AWS_ACCESS_KEY_ID"] = accessKeyId
        os.environ["AWS_SECRET_ACCESS_KEY"] = secretAccessKey
        return True
    return False


def unsetAwsEnvCredentials() -> None:
    """Unset AWS credential environment variables.

    Unsets the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environmental
    variables.
    """
    if "AWS_ACCESS_KEY_ID" in os.environ:
        del os.environ["AWS_ACCESS_KEY_ID"]
    if "AWS_SECRET_ACCESS_KEY" in os.environ:
        del os.environ["AWS_SECRET_ACCESS_KEY"]
