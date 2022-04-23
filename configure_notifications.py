import boto3
from argparse import ArgumentParser

def parser():
    parser = ArgumentParser()
    parser.add_argument('-b', '--bucket', type=str, required=True) 
    parser.add_argument('-l', '--lambdafunc', type=str, required=True)         
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    parsed_arguments = parser()
    bucket = parsed_arguments.bucket
    lambdafunc = parsed_arguments.lambdafunc
    notification_configuration = {
            'LambdaFunctionConfigurations': [
                {
                'LambdaFunctionArn': lambdafunc,
                    'Events': ['s3:ObjectCreated:*'],
                    'Filter': {
                        'Key': {
                            'FilterRules': [
                                {
                                    'Name': 'suffix',
                                    'Value': '.jpeg'
                                }
                            ]
                        }
                    }
                }
            ]
        }

    s3 = boto3.client('s3')
    lambda_client = boto3.client('lambda')
    lambda_client.add_permission(
        FunctionName=lambdafunc,
        StatementId=f'{bucket}',
        Action='lambda:InvokeFunction',
        Principal='s3.amazonaws.com',
        SourceArn=f'arn:aws:s3:::{bucket}'
    )
    s3.put_bucket_notification_configuration(
        Bucket=bucket,
        NotificationConfiguration=notification_configuration
    )

if __name__ == '__main__':
    main()