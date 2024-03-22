import boto3
aws_mag_con = boto3.session.Session(profile_name="terraform",region_name="us-east-1")
sqs_con = aws_mag_con.client('sqs')
response = sqs_con.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/431995393781/test',)
print(response)
