import boto3
from argparse import ArgumentParser
import os

def parser():
    parser = ArgumentParser()
    parser.add_argument('-n', '--name', type=str, required=True) 
    parser.add_argument('-c', '--codepath', type=str, required=True)         
    parsed_arguments = parser.parse_args()
    return parsed_arguments

def main():
    parsed_arguments = parser()
    lambda_client = boto3.client('lambda')
    function_name = parsed_arguments.name
    codepath = parsed_arguments.codepath

    with open(codepath, 'rb') as zip_file:
        zip_bytes = zip_file.read()
        file_name = os.path.basename(codepath)
        file_name_without_extension = os.path.splitext(file_name)[0]
        handler_name = f'{file_name_without_extension}.lambda_handler'

        lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.9',
            Role='arn:aws:iam::672359518488:role/LabRole',
            Handler=handler_name,
            Code={
                'ZipFile': zip_bytes
            }
        )

if __name__ == '__main__':
    main()