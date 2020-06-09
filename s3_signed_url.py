import os
import logging
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

s3_signature ={
    'v4':'s3v4',
    'v2':'s3'
}

access_keys = {
"AWS_ACCESS_KEY_ID" : "AKIAJMZYWXE3RWFHR3CQ",
"AWS_SECRET_ACCESS_KEY": "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",
"AWS_DEFAULT_REGION" : "us-east-2",
"BUCKET_NAME": "collegeproject"
}
def create_presigned_url(bucket_name, bucket_key="79716393_747121099119308_8457385614662036801_n.jpg ", expiration=3600, signature_version=s3_signature['v4']):

    AWS_ACCESS_KEY_ID = "AKIAJMZYWXE3RWFHR3CQ"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_DEFAULT_REGION = "us-east-2"

    s3_client = boto3.client('s3',
                             aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             config=Config(signature_version=signature_version),
                             region_name=AWS_DEFAULT_REGION
                             )
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': bucket_key},
                                                    ExpiresIn=expiration)
        # print(s3_client.list_buckets()['Owner'])
        # for key in s3_client.list_objects(Bucket=bucket_name, Prefix=bucket_key)['Contents']:
        #     print(key['Key'])
    except ClientError as e:
        logging.error(e)
        return None
    return response

if __name__ == '__main__':
    create_presigned_url(None,None)