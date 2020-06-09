# # from twilio.rest import  Client
# # import boto3, boto
# # from botocore.client import Config
# # from boto.s3.connection import S3Connection
# # from boto.s3.key import Key
# #
# # # access_keys = {
# # # "AWS_ACCESS_KEY_ID" : "AKIAJMZYWXE3RWFHR3CQ",
# # # "AWS_SECRET_ACCESS_KEY": "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",
# # # "AWS_DEFAULT_REGION" : "us-east-2",
# # # "BUCKET_NAME": "new-bucket-1999"
# # # }
# # #
# # # access_key = " AKIATNS4G2WKQOS3D37B"
# # #
# # # account_sid = "ACa84eb22d69d17caa72b0b4a6057b4c23"
# # # auth_token = "c53f5c61021a8b14ae5e75a33471a7ac"
# # #
# # # from_whatsapp_number = "whatsapp:+14155238886"
# # # to_whatsapp_number = "whatsapp:+918826332442"
# # #
# # # s3 = boto3.resource("s3",
# # #                         aws_access_key_id = access_keys["AWS_ACCESS_KEY_ID"],
# # #                         aws_secret_access_key = access_keys["AWS_SECRET_ACCESS_KEY"],
# # #                         config = Config(signature_version = "s3v4")
# # #                     )
# # # s3.Bucket("new-bucket-1999").upload_file("/home/aditya/Pictures/67834857_141978077040402_6028266456925167025_n.jpg","image.jpg")
# #
# #
# # from twilio.rest import Client
# # from PIL import Image
# # import requests as req
# # import urllib.request
# # url = "https://new-bucket-1999.s3.ap-south-1.amazonaws.com/image.jpg"
# #
# # # url="https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__340.jpg"
# #
# # account_sid = "ACa84eb22d69d17caa72b0b4a6057b4c23"
# # auth_token = "c53f5c61021a8b14ae5e75a33471a7ac"
# #
# # from_whatsapp_number = "whatsapp:+14155238886"
# # to_whatsapp_number = "whatsapp:+918826332442"
# #
# # client = Client(account_sid, auth_token)
# # client.messages.create(to=to_whatsapp_number, from_=from_whatsapp_number,
# #                        media_url=url,
# #                        body="message")
# #
# #
# # print("Done")
#
from twilio.rest import Client
# # import  boto3
# #
# # # Access keys and Access secret keys for AWS [REMEMBER]
# # s3 = boto3.client("s3",
# #                   aws_access_key_id="AKIATNS4G2WKY36VF6NJ",
# #                   aws_secret_access_key="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")
# #
# # result = s3.get_bucket_acl(Bucket="aws-bucket-project")
# # image = "/home/aditya/Pictures/76879332_104136811009990_5862828344340212320_n.jpg"
#
# # result(image,"aws-bucket-project","image.jpg",ExtraArgs={"ACL": "public-read"})
# # print(result)
# # help(result)
# # image = "/home/aditya/Pictures/76879332_104136811009990_5862828344340212320_n.jpg"
# # s3.upload_file(image,"aws-bucket-project","image.jpg",ExtraArgs={"ACL": "public-read"})
# #
# # location = s3.get_bucket_location(
# #     Bucket = "aws-bucket-project")["LocationConstraint"]
# #
# # url = "https://s3-{}.amazonaws.com/{}/{}".format(location,"aws-bucket-project", "image.jpg")
# #
#


account_sid = "ACa84eb22d69d17caa72b0b4a6057b4c23"
auth_token = "c53f5c61021a8b14ae5e75a33471a7ac"

from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:+918826332442"

client = Client(account_sid,
                auth_token)
client.messages.create(to=to_whatsapp_number,
                       from_=from_whatsapp_number,
                       body="Intruder Alert")


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from flask import Flask, request
# from twilio.twiml.messaging_response import MessagingResponse
#
#
# app = Flask(__name__)
#
#
# GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
#
#
# @app.route("/whatsapp", methods=["GET", "POST"])
# def reply_whatsapp():
#
#     response = MessagingResponse()
#     num_media = int(request.values.get("NumMedia"))
#     if not num_media:
#         msg = response.message("Send us an image!")
#     else:
#         msg = response.message("Thanks for the image. Here's one for you!")
#         msg.media(GOOD_BOY_URL)
#     return str(response)
#
#
# if __name__ == "__main__":
#     app.run()
