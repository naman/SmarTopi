from boto.s3.connection import S3Connection
from s3FMA import S3FileManager

AWS_KEY = ''
AWS_SECRET = ''
s3FileManager = S3FileManager(AWS_KEY, AWS_SECRET, use_ssl = True)

def s3_get_file(filename, bucket):
	s3FileManager.downloadFileFromBucket(aws_bucketname=bucket, filename=filename, local_download_directory="./ImageData")
