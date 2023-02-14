import boto3
import os
import argparse

parser = argparse.ArgumentParser(description='Creating an AWS Kinesis Data Stream')
parser.add_argument('--region', type=str, required=True, help='The AWS Region the stream will be created in')
parser.add_argument('--stream_name', type=str, required=True, help='The name of the stream')
parser.add_argument('--shards', type=str, required=False, help='The number of shards for the stream (only needed for Provisioned mode)')
parser.add_argument('--stream_mode', type=str, required=True, help='Stream Mode: "Provisioned" or "On-Demand"')
args = parser.parse_args()

def create_stream(**kwargs):
    try:
        kinesis = boto3.client("kinesis", region_name=region)
        kinesis.create_stream(
            stream_name,
            shards,
            StreamModeDetails={
                'StreamMode': stream_mode
            }
        )
        print('stream {} created in region {}'.format(stream_name, region))
    except ResourceInUseException:
        print('stream {} already exists in region {}'.format(stream_name, region))
