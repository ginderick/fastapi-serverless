import boto3
from boto3.resources.base import ServiceResource

def initialize_db() -> ServiceResource:
    ddb = boto3.resource('dynamodb',
        endpoint_url='http://localhost:8000',
        region_name='ap-southeast-1',
        aws_access_key="AWS_ACCESS_KEY",
        aws_secret_access_key="AWS_SECRET_ACCESS_KEY")
