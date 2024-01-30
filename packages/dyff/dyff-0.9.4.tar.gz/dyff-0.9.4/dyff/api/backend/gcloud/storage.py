# Copyright UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

# mypy: disable-error-code="import-untyped"
import base64
import datetime
from pathlib import Path
from typing import Optional, Tuple

import google.auth.compute_engine
import google.auth.transport.requests
import google.cloud.storage as gcs

from dyff.api.backend.base.storage import StorageBackend
from dyff.api.storage import paths
from dyff.schema.dataset import max_artifact_size_bytes
from dyff.schema.platform import Artifact, StorageSignedURL


def _bucket_name_from_path(path: str) -> str:
    return _split_bucket_path(path)[0]


def _drop_protocol(path: str) -> str:
    protocol = "gs://"
    if path.startswith(protocol):
        path = path[len(protocol) :]
    return path


def _split_bucket_path(path: str) -> Tuple[str, str]:
    path = _drop_protocol(path)
    parts = path.split("/")
    return parts[0], "/".join(parts[1:])


class GCloudStorageBackend(StorageBackend):
    def storage_size(self, path: str) -> int:
        bucket, prefix = _split_bucket_path(path)
        client = gcs.Client()
        bucket_obj = client.get_bucket(bucket)
        blobs = bucket_obj.list_blobs(prefix=prefix)
        return sum(b.size for b in blobs)

    def list_dir(self, path: str) -> list[str]:
        if not path.startswith("gs://"):
            raise ValueError("path must be a GCS object")
        if not path.endswith("/"):
            path += "/"
        client = gcs.Client()
        remote_path = path[len("gs://") :]
        bucket_name, *rest = remote_path.split("/")
        prefix = "/".join(rest)
        bucket = client.get_bucket(bucket_name)
        # Get the objects under the 'source' path
        blobs = bucket.list_blobs(prefix=prefix)
        return [f"gs://{blob.bucket.name}/{blob.name}" for blob in blobs]

    def download_recursive(self, source: str, destination: str) -> None:
        if not source.startswith("gs://"):
            raise ValueError("source must be a GCS object")
        if not source.endswith("/"):
            source += "/"
        client = gcs.Client()
        remote_path = source[len("gs://") :]
        parts = remote_path.split("/")
        bucket_name = parts[0]
        bucket = client.bucket(bucket_name)
        blob_name = "/".join(parts[1:])
        bucket = client.get_bucket(bucket_name)
        # Get the objects under the 'source' path
        blobs = bucket.list_blobs(prefix=blob_name)
        for blob in blobs:
            if blob.name.endswith("/"):
                # Not a file
                continue
            remote_directory = Path(blob.name).parent
            local_path = Path(destination) / remote_directory
            local_path.mkdir(parents=True, exist_ok=True)
            blob.download_to_filename(Path(destination) / blob.name)

    def signed_url_for_dataset_upload(
        self,
        dataset_id: str,
        artifact: Artifact,
        *,
        size_limit_bytes: Optional[int] = None,
        storage_path: Optional[str] = None,
    ) -> StorageSignedURL:
        if size_limit_bytes is None:
            size_limit_bytes = max_artifact_size_bytes()
        if artifact.digest.md5 is None:
            raise ValueError("requires artifact.digest.md5")
        storage_path = storage_path or paths.dataset_root(dataset_id)
        bucket_name = _bucket_name_from_path(storage_path)
        client = gcs.Client()
        blob = client.bucket(bucket_name).blob(f"{dataset_id}/{artifact.path}")

        auth_request = google.auth.transport.requests.Request()
        signing_credentials = google.auth.compute_engine.IDTokenCredentials(
            auth_request,
            "api-server.dyff.io",
            service_account_email="api-server@dyff-354017.iam.gserviceaccount.com",
        )

        # Google custom header limiting the size of the artifact
        headers = {
            "x-goog-content-length-range": f"0,{size_limit_bytes}",
        }
        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(hours=1),
            method="PUT",
            content_md5=artifact.digest.md5,
            headers=headers.copy(),  # The function mutates this argument
            credentials=signing_credentials,
        )
        return StorageSignedURL(url=url, method="PUT", headers=headers)

    def dataset_artifact_md5hash(
        self, dataset_id: str, artifact_path: str, *, storage_path: Optional[str] = None
    ) -> bytes:
        storage_path = storage_path or paths.dataset_root(dataset_id)
        bucket_name = _bucket_name_from_path(storage_path)
        client = gcs.Client()
        blob = client.bucket(bucket_name).get_blob(f"{dataset_id}/{artifact_path}")
        if blob is None:
            raise ValueError(
                f"no artifact {artifact_path} stored for dataset {dataset_id}"
            )
        return base64.b64decode(blob.md5_hash)


__all__ = ["GCloudStorageBackend"]
