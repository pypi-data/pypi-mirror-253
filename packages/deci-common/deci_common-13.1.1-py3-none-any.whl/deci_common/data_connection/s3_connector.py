import os
import sys
from io import BytesIO, StringIO
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from botocore.exceptions import ClientError

from deci_common.abstractions.abstract_logger import ILogger
from deci_common.aws_connection import AWSConnector

if TYPE_CHECKING:
    from typing import Any, Dict, List, Optional, Tuple, Union

    from mypy_boto3_s3 import S3Client, S3ServiceResource
    from mypy_boto3_s3.type_defs import (
        BucketLifecycleConfigurationTypeDef,
        CopySourceTypeDef,
        CreateBucketOutputTypeDef,
        DeleteTypeDef,
        ErrorTypeDef,
        GetObjectOutputTypeDef,
        HeadObjectOutputTypeDef,
        LifecycleRuleTypeDef,
    )


class KeyNotExistInBucketError(Exception):
    pass


class DeleteKeyAfterRenamingItFailedError(Exception):
    pass


class InvalidS3UriError(Exception):
    pass


class S3Connector(ILogger):
    LIFECYCLE_RULES_LIMIT = 1000

    class LifecycleRulesLimitExceededError(Exception):
        def __init__(self) -> None:
            super().__init__(f"Number of lifecycle rules exceeds limit ({S3Connector.LIFECYCLE_RULES_LIMIT})")

    """
    S3Connector - S3 Connection Manager
    """

    def __init__(self, env: "Optional[str]" = None, *, bucket_name: str):
        """
        Initiate a connector to AWS S3 object storage
        :param env: profile name or environment for the s3 client and resource
        :param bucket_name: the name of the bucket to create the connection to
        """
        super().__init__()
        self.bucket_name = bucket_name

        self.s3_client = AWSConnector.get_aws_client_for_service_name(profile_name=env, service_name="s3")
        self.s3_resource = AWSConnector.get_aws_resource_for_service_name(profile_name=env, service_name="s3")

    def check_key_exists(self, s3_key_to_check: str) -> "Optional[bool]":
        """
        check_key_exists - Checks if an S3 key exists
        :param s3_key_to_check:
        :return:
        """
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=s3_key_to_check)
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "404":
                return False
            else:
                self._logger.error(
                    "Failed to check key: " + str(s3_key_to_check) + " existence in bucket" + str(self.bucket_name)
                )
                return None
        else:
            return True

    def get_object_by_etag(self, bucket_relative_file_name: str, etag: str) -> "Optional[GetObjectOutputTypeDef]":
        """
        get_object_by_etag - Gets S3 object by its ETag header if it. exists
        :param bucket_relative_file_name: The name of the file in the bucket (relative)
        :param etag: The ETag of the object in S3
        :return:
        """
        try:
            etag = etag.strip('"')
            s3_object = self.s3_client.get_object(Bucket=self.bucket_name, Key=bucket_relative_file_name, IfMatch=etag)
            return s3_object
        except ClientError as ex:
            if ex.response["Error"]["Code"] != "404":
                self._logger.error(
                    "Failed to check ETag: " + str(etag) + " existence in bucket " + str(self.bucket_name)
                )
        return None

    def create_bucket(self, s3_client: "Optional[S3Client]" = None) -> "CreateBucketOutputTypeDef":
        """
        Creates a bucket with the initialized bucket name.
        :return: The new bucket response
        :raises ClientError: If the creation failed for any reason.
        """
        client = s3_client or self.s3_client
        try:
            # TODO: Change bucket_owner_arn to the company's proper IAM Role
            self._logger.info("Creating Bucket: " + self.bucket_name)
            create_bucket_response = client.create_bucket(ACL="private", Bucket=self.bucket_name)
            self._logger.info(f"Successfully created bucket: {create_bucket_response}")

            # Changing the bucket public access block to be private (disable public access)
            self._logger.debug("Disabling public access to the bucket...")
            client.put_public_access_block(
                PublicAccessBlockConfiguration={
                    "BlockPublicAcls": True,
                    "IgnorePublicAcls": True,
                    "BlockPublicPolicy": True,
                    "RestrictPublicBuckets": True,
                },
                Bucket=self.bucket_name,
            )

            return create_bucket_response
        except ClientError as err:
            self._logger.fatal(f'Failed to create bucket "{self.bucket_name}": {err}')
            raise err

    def check_bucket_exists(
        self,
        bucket_name: "Optional[str]" = None,
        s3_resource: "Optional[S3ServiceResource]" = None,
    ) -> bool:
        resource = s3_resource or self.s3_resource
        bucket_name = bucket_name if bucket_name else self.bucket_name
        return resource.Bucket(bucket_name) in resource.buckets.all()  # type: ignore[union-attr]

    def delete_bucket(self, s3_resource: "Optional[S3ServiceResource]" = None) -> bool:
        """
        Deletes a bucket with the initialized bucket name.
        :return: True if succeeded.
        :raises ClientError: If the creation failed for any reason.
        """
        resource = s3_resource or self.s3_resource
        try:
            self._logger.info("Deleting Bucket: " + self.bucket_name + " from S3")
            bucket = resource.Bucket(self.bucket_name)  # type: ignore[union-attr]
            bucket.objects.all().delete()
            bucket.delete()
            self._logger.debug("Successfully Deleted Bucket: " + self.bucket_name + " from S3")
        except ClientError as ex:
            self._logger.fatal(f"Failed to delete bucket {self.bucket_name}: {ex}")
            raise ex
        return True

    def get_object_metadata(self, s3_key: str) -> "HeadObjectOutputTypeDef":
        try:
            return self.s3_client.head_object(Bucket=self.bucket_name, Key=s3_key)
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "404":
                msg = "[" + sys._getframe().f_code.co_name + "] - Key does not exist in bucket)"
                self._logger.error(msg)
                raise KeyNotExistInBucketError(msg)
            raise ex

    def delete_key(self, s3_key_to_delete: str) -> bool:
        """
        delete_key - Deletes a Key from an S3 Bucket
            :param s3_key_to_delete:
            :return: True/False if the operation succeeded/failed
        """
        try:
            self._logger.debug("Deleting Key: " + s3_key_to_delete + " from S3 bucket: " + self.bucket_name)
            obj_status = self.s3_client.head_object(Bucket=self.bucket_name, Key=s3_key_to_delete)
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "404":
                self._logger.error("[" + sys._getframe().f_code.co_name + "] - Key does not exist in bucket)")
            return False

        if obj_status["ContentLength"]:
            self._logger.debug(
                "[" + sys._getframe().f_code.co_name + "] - Deleting file s3://" + self.bucket_name + s3_key_to_delete
            )
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=s3_key_to_delete)

        return True

    def upload_file_from_stream(self, file: bytes, key: str) -> bool:
        """
        upload_file - Uploads a file to S3 via boto3 interface
                      *Please Notice* - This method is for working with files, not objects
            :param key: The key (filename) to create in the S3 bucket
            :param file: File to upload
            :return True/False if the operation succeeded/failed
        """
        try:
            self._logger.debug("Uploading Key: " + key + " to S3 bucket: " + self.bucket_name)
            _buffer = BytesIO(file)
            self.upload_buffer(key, _buffer)
            return True
        except Exception as ex:
            self._logger.critical(
                "["
                + sys._getframe().f_code.co_name
                + "] - Caught Exception while trying to upload file "
                + str(key)
                + "to S3"
                + str(ex)
            )
            return False

    def upload_file(self, filename_to_upload: str, key: str) -> bool:
        """
        upload_file - Uploads a file to S3 via boto3 interface
                      *Please Notice* - This method is for working with files, not objects
            :param key:                The key (filename) to create in the S3 bucket
            :param filename_to_upload: Filename of the file to upload
            :return True/False if the operation succeeded/failed
        """
        try:
            self._logger.info("Uploading Key: " + key + " to S3 bucket: " + self.bucket_name)

            self.s3_client.upload_file(Bucket=self.bucket_name, Filename=filename_to_upload, Key=key)
            return True

        except Exception as ex:
            self._logger.critical(
                "["
                + sys._getframe().f_code.co_name
                + "] - Caught Exception while trying to upload file "
                + str(filename_to_upload)
                + "to S3"
                + str(ex)
            )
            return False

    def create_folder(self, folder_name: str) -> bool:
        """
        :param folder_name: name of the folder to create.
        :return: bool - true if creation succeeded
        """
        try:
            self._logger.info(f'Creating S3 folder path {self.bucket_name + "/" + folder_name}')

            self.s3_client.put_object(Bucket=self.bucket_name, Key=folder_name + "/")
            return True

        except Exception as ex:
            self._logger.error(
                f"Failed to create folder {folder_name} in bucket {self.bucket_name}, returning False. ", exc_info=ex
            )
            return False

    def rename_key(self, source_key: str, destination_key: str) -> bool:
        self.copy_key(self.bucket_name, source_key=source_key, destination_key=destination_key)
        try:
            delete_success = self.delete_key(s3_key_to_delete=source_key)
            if not delete_success:
                raise
            return True
        except Exception as e:
            raise DeleteKeyAfterRenamingItFailedError(
                f"Failed to remove old key {source_key} after creating new copy with new name {destination_key}. "
            ) from e

    def download_key(self, target_path: str, key_to_download: str) -> bool:
        """
        download_file - Downloads a key from S3 using boto3 to the provided filename
                        Please Notice* - This method is for working with files, not objects
            :param key_to_download:    The key (filename) to download from the S3 bucket
            :param target_path:           Filename of the file to download the content of the key to
            :return:                   True/False if the operation succeeded/failed
        """
        try:
            self._logger.debug("Uploading Key: " + key_to_download + " from S3 bucket: " + self.bucket_name)
            self.s3_client.download_file(Bucket=self.bucket_name, Filename=target_path, Key=key_to_download)
        except ClientError as ex:
            if ex.response["Error"]["Code"] == "404":
                self._logger.error("[" + sys._getframe().f_code.co_name + "] - Key does exist in bucket)")
            else:
                self._logger.critical(
                    "["
                    + sys._getframe().f_code.co_name
                    + "] - Caught Exception while trying to download key "
                    + str(key_to_download)
                    + " from S3 "
                    + str(ex)
                )
            return False

        return True

    def download_keys_by_prefix(
        self,
        s3_bucket_path_prefix: str,
        local_download_dir: str,
        s3_file_path_prefix: str = "",
    ) -> None:
        """
        download_keys_by_prefix - Download all the keys who match the provided in-bucket path prefix and file prefix
            :param s3_bucket_path_prefix:   The S3 "folder" to download from
            :param local_download_dir:      The local directory to download the files to
            :param s3_file_path_prefix:     The specific prefix of the files we want to download
        :return:
        """
        if not os.path.isdir(local_download_dir):
            raise ValueError("[" + sys._getframe().f_code.co_name + "] - Provided directory does not exist")

        paginator = self.s3_client.get_paginator("list_objects")
        prefix = s3_bucket_path_prefix if not s3_file_path_prefix else s3_bucket_path_prefix + "/" + s3_file_path_prefix
        page_iterator = paginator.paginate(Bucket=self.bucket_name, Prefix=prefix)

        for item in page_iterator.search("Contents"):
            if item is None or item["Key"] == s3_bucket_path_prefix:
                continue
            key_to_download = item["Key"]
            local_filename = key_to_download.split("/")[-1]
            self.download_key(target_path=local_download_dir + "/" + local_filename, key_to_download=key_to_download)

    def download_file_by_path(self, s3_file_path: str, local_download_dir: str) -> str:
        """
        :param s3_file_path: str - path ot s3 file e.g./ "s3://x/y.zip"
        :param local_download_dir: path to download
        :return:
        """

        if not os.path.isdir(local_download_dir):
            raise ValueError("[" + sys._getframe().f_code.co_name + "] - Provided directory does not exist")

        local_filename = s3_file_path.split("/")[-1]
        self.download_key(target_path=local_download_dir + "/" + local_filename, key_to_download=s3_file_path)
        return local_filename

    def empty_folder_content_by_path_prefix(self, s3_bucket_path_prefix: str) -> "List[List[ErrorTypeDef]]":
        """
        empty_folder_content_by_path_prefix - Deletes all the files in the specified bucket path
            :param s3_bucket_path_prefix: The "folder" to empty
            :returns: Errors list
        """
        paginator = self.s3_client.get_paginator("list_objects")
        page_iterator = paginator.paginate(Bucket=self.bucket_name, Prefix=s3_bucket_path_prefix)

        files_dict_to_delete: "DeleteTypeDef" = dict(Objects=[])
        errors_list: "List[List[ErrorTypeDef]]" = []

        for item in page_iterator.search("Contents"):
            if item is not None:
                if item["Key"] == s3_bucket_path_prefix:
                    continue
                files_dict_to_delete["Objects"] = [*files_dict_to_delete["Objects"], dict(Key=item["Key"])]

                # IF OBJECTS LIMIT HAS BEEN REACHED, FLUSH
                if len(files_dict_to_delete["Objects"]) >= 1000:
                    self._delete_files_left_in_list(errors_list, files_dict_to_delete)
                    files_dict_to_delete = dict(Objects=[])

        # DELETE THE FILES LEFT IN THE LIST
        if len(files_dict_to_delete["Objects"]):
            self._delete_files_left_in_list(errors_list, files_dict_to_delete)

        return errors_list

    def _delete_files_left_in_list(
        self,
        errors_list: "List[List[ErrorTypeDef]]",
        files_dict_to_delete: "DeleteTypeDef",
    ) -> None:
        try:
            s3_response = self.s3_client.delete_objects(Bucket=self.bucket_name, Delete=files_dict_to_delete)
        except Exception as ex:
            self._logger.critical(
                "["
                + sys._getframe().f_code.co_name
                + "] - Caught Exception while trying to delete keys "
                + "from S3 "
                + str(ex)
            )
        if "Errors" in s3_response:
            errors_list.append(s3_response["Errors"])

    def upload_buffer(self, new_key_name: str, buffer_to_write: "Union[StringIO, BytesIO]") -> None:
        """
        Uploads a buffer into a file in S3 with the provided key name.
        :bucket: The name of the bucket
        :new_key_name: The name of the file to create in s3
        :buffer_to_write: A buffer that contains the file contents.
        """
        self.s3_resource.Object(self.bucket_name, new_key_name).put(Body=buffer_to_write.getvalue())  # type: ignore[union-attr]

    def upload_empty_file(self, key_name: str) -> None:
        """
        Uploads an empty buffer to S3 bucket in the provided key name
        :param key_name: the key to upload an empty file to
        :return: None
        """
        self.upload_buffer(new_key_name=key_name, buffer_to_write=StringIO())

    def list_bucket_objects(self, prefix: "Optional[str]" = None) -> "List[Dict[str, Any]]":
        """
        Gets a list of dictionaries, representing files in the S3 bucket that is passed in the constructor (self.bucket).
        :param prefix: A prefix filter for the files names.
        :return: the objects, dict as received from botocore.
        """
        paginator = self.s3_client.get_paginator("list_objects")
        if prefix:
            page_iterator = paginator.paginate(Bucket=self.bucket_name, Prefix=prefix)
        else:
            page_iterator = paginator.paginate(Bucket=self.bucket_name)

        bucket_objects = []
        for item in page_iterator.search("Contents"):
            if not item or item["Key"] == self.bucket_name:
                continue
            bucket_objects.append(item)
        return bucket_objects

    def create_presigned_upload_url(
        self,
        object_name: str,
        fields: "Any" = None,
        conditions: "Any" = None,
        expiration: int = 3600,
        override: bool = False,
    ) -> "Dict[str, Any]":
        """Generate a presigned URL S3 POST request to upload a file
        :param object_name: string
        :param fields: Dictionary of prefilled form fields
        :param conditions: List of conditions to include in the policy
        :param expiration: Time in seconds for the presigned URL to remain valid
        :param override: Allows disregarding the existence of an object in S3
        :return: Dictionary with the following keys:
            url: URL to post to
            fields: Dictionary of form fields and values to submit with the POST request
        """
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html#generating-a-presigned-url-to-upload-a-file
        if not override:
            file_already_exist = self.check_key_exists(object_name)
            if file_already_exist:
                raise FileExistsError(f"The key {object_name} already exists in bucket {self.bucket_name}")

        response = self.s3_client.generate_presigned_post(
            self.bucket_name, object_name, Fields=fields, Conditions=conditions, ExpiresIn=expiration
        )
        return response

    def create_presigned_download_url(
        self,
        object_name: str,
        expiration: int = 3600,
        download_name: "Optional[str]" = None,
    ) -> str:
        """Generate a presigned URL S3 Get request to download a file
        :param object_name: string
        :param expiration: Time in seconds for the presigned URL to remain valid
        :param download_name: If given the downloaded file will be renamed to this name
        :return: URL encoded with the credentials in the query, to be fetched using any HTTP client.
        """
        # https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html
        if download_name is None:
            # overriding the file name if specified
            download_name = object_name
        response = self.s3_client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": self.bucket_name,
                "Key": object_name,
                "ResponseContentDisposition": f'attachment; filename="{download_name}"',
            },
            ExpiresIn=expiration,
        )
        return response

    @staticmethod
    def convert_content_length_to_mb(content_length: int) -> float:
        return round(float(f"{content_length / (1e+6):2f}"), 2)

    def copy_key(self, destination_bucket_name: str, source_key: str, destination_key: str) -> bool:
        self._logger.info(
            f"Copying the bucket object {self.bucket_name}/{source_key} to {destination_bucket_name}/{destination_key}"
        )
        copy_source: "CopySourceTypeDef" = {"Bucket": self.bucket_name, "Key": source_key}

        # Copying the key
        bucket = self.s3_resource.Bucket(destination_bucket_name)  # type: ignore[union-attr]
        bucket.copy(copy_source, destination_key)
        return True

    def change_lifecycle_configuration(self, lifecycle_configuration: "BucketLifecycleConfigurationTypeDef") -> None:
        self.s3_client.put_bucket_lifecycle_configuration(
            Bucket=self.bucket_name, LifecycleConfiguration=lifecycle_configuration
        )

    def add_lifecycle_configuration_rule(self, rule: "LifecycleRuleTypeDef") -> None:
        lifecycle_config_rules: "List[LifecycleRuleTypeDef]" = []
        try:
            lifecycle_config = self.s3_client.get_bucket_lifecycle_configuration(Bucket=self.bucket_name)
            lifecycle_config_rules = lifecycle_config["Rules"] if "Rules" in lifecycle_config else []
        except ClientError as ex:
            self._logger.warning(f"Could not get lifecycle configuration for bucket {self.bucket_name} due to {ex}")
        lifecycle_config_rules.append(rule)
        if len(lifecycle_config_rules) >= int(0.8 * self.LIFECYCLE_RULES_LIMIT):
            self._logger.warning(f"Reached 80% of the lifecycle rules limit for bucket {self.bucket_name}")
        if len(lifecycle_config_rules) > self.LIFECYCLE_RULES_LIMIT:
            raise S3Connector.LifecycleRulesLimitExceededError
        self.change_lifecycle_configuration(lifecycle_configuration={"Rules": lifecycle_config_rules})

    def set_expiration_for_prefix(self, prefix: str, days_to_expiration: int) -> None:
        expiration_rule: "LifecycleRuleTypeDef" = {
            "Expiration": {"Days": days_to_expiration},
            "Filter": {"Prefix": prefix},
            "ID": f"Expiration for {self.bucket_name}/{prefix}",
            "Status": "Enabled",
        }
        self.add_lifecycle_configuration_rule(rule=expiration_rule)

    @staticmethod
    def parse_s3_uri(uri: str) -> "Tuple[str, str]":
        """
        Parses S3 object URI and returns bucket name and object key.
        :param uri: S3 URI string
        :return: bucket name and object key tuple
        :raises InvalidS3UriError: If S3 object URI is not valid.
        """
        parsed = urlparse(uri, allow_fragments=False)
        if parsed.scheme != "s3" or not parsed.netloc or not parsed.path:
            raise InvalidS3UriError
        return parsed.netloc, parsed.path.lstrip("/")
