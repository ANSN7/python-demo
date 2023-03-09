import boto3

s3 = boto3.client('s3', aws_access_key_id='ASIATZQTYOSCOTO3J6IH', aws_secret_access_key='J5XpwUOLQ2ZMgi4JlSsxPwGzGfZHDC5G7fewznvE')
                  
local_file_path = 'C:/Users/User'
bucket_name = 'webapp1buckett'
s3_key = 'mybucket'

s3.upload_file(local_file_path, bucket_name, s3_key)
