import boto3, os
from botocore.client import Config
from s3_signed_url import access_keys
import pickle

def upload_to_s3():
    folder = "Unknown"
    image_path = os.listdir(folder)[-1]
    img_path = os.listdir(os.path.join(folder,image_path))
    image = open(os.path.join("Unknown/" + image_path,img_path[0]),"rb")

    s3 = boto3.resource("s3",
                        aws_access_key_id = access_keys["AWS_ACCESS_KEY_ID"],
                        aws_secret_access_key = access_keys["AWS_SECRET_ACCESS_KEY"],
                        config = Config(signature_version = "s3v4")
                        )

    unknown_person_number = pickle.load(open("UnknownPersonNumber.pickle","rb"))
    bucket_key = "Unknown_Person"+str(unknown_person_number)+".jpg"

    s3.Bucket(access_keys["BUCKET_NAME"]).put_object(Key=bucket_key,Body=image)
    return bucket_key

if __name__ == '__main__':
    upload_to_s3()
