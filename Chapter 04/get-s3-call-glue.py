import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
glue = boto3.client('glue')

# Variables for the job: 
glue_job_name = "tabular-features-glue-etl"


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print('received trigger from S3 bucket {} and key {}'.format(bucket, key))
    try:
        runresponse = glue.start_job_run(JobName = glue_job_name, Arguments={'--JOB_NAME':glue_job_name, '--s3_input_dataset':'s3://'+bucket+'/'+key})
        print("Glue job triggered: " + runresponse['JobRunId'])
    except Exception as e:
        print(e)
        print('Error calling glue job name {}.'.format(glue_job_name))
        raise e