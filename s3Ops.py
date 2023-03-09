import boto3

s3 = boto3.client('s3', aws_access_key_id='ASIATZQTYOSCOTO3J6IH', aws_secret_access_key='J5XpwUOLQ2ZMgi4JlSsxPwGzGfZHDC5G7fewznvE')
                  
bucket_name = 'webapp1buckett'
s3_key = 'mem.sh'

s3.upload_file(r"C:\Users\User\mem.sh", bucket_name, s3_key)
