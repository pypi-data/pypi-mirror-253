from storages.backends.s3boto3 import S3Boto3Storage 
import boto3
from botocore.config import Config
from botocore.exceptions import ClientError

import random
import os


class MediaStorage(S3Boto3Storage):    
	location = 'media'
	file_overwrite = False


def create_presigned_post(bucket_name, object_name,
		fields=None, conditions=None, expiration=3600):
	"""Generate a presigned URL S3 POST request to upload a file

	:param bucket_name: string
	:param object_name: string
	:param fields: Dictionary of prefilled form fields
	:param conditions: List of conditions to include in the policy
	:param expiration: Time in seconds for the presigned URL to remain valid
	:return: Dictionary with the following keys:
		url: URL to post to
		fields: Dictionary of form fields and values to submit with the POST
	:return: None if error.
	"""
	filename, file_extension = os.path.splitext(object_name)
	object_name = '{}_{}{}'.format(filename, random.randint(10000, 100000), file_extension)

	s3_client = boto3.client('s3', config=Config(
		region_name = 'eu-west-3',
		signature_version = 's3v4',
		retries = {
			'max_attempts': 10,
			'mode': 'standard'
		}
	))
	try:
		response = s3_client.generate_presigned_post(
			bucket_name,
			'{}/{}'.format(MediaStorage.location, object_name),
			Fields=fields,
			Conditions=conditions,
			ExpiresIn=expiration)
		response['filename'] = object_name
	except ClientError as e:
		return None

	return response