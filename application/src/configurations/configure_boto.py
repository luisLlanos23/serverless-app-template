import mypy_boto3_s3
import mypy_boto3_lambda
from boto3 import client
from botocore.config import Config
from src.constants.environments import Environments

__s3: mypy_boto3_s3.S3Client
__lambda: mypy_boto3_lambda.LambdaClient


def configure_boto() -> None:
  global __s3, __lambda
  config = Config(region_name=Environments.cloud_config['AWS_REGION'])
  if not Environments.cloud_config or 'AWS_ACCESS_KEY_ID' not in Environments.cloud_config or 'AWS_SECRET_KEY_ID' not in Environments.cloud_config:
    __s3 = client('s3', config=config)
    __lambda = client('lambda', config=config)
  else:
    __s3 = client(
        's3',
        aws_access_key_id=Environments.cloud_config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=Environments.cloud_config['AWS_SECRET_KEY_ID'],
        config=config)
    __lambda = client(
        'lambda',
        aws_access_key_id=Environments.cloud_config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=Environments.cloud_config['AWS_SECRET_KEY_ID'],
        config=config)

def get_s3() -> mypy_boto3_s3.S3Client:
  return  globals()['__s3']

def get_lambda() -> mypy_boto3_lambda.LambdaClient:
    return globals()['__lambda']
