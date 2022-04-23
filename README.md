# BTU-Python-Lambda

## 1 - From the configure_notifications.py file, we give permission to the bucket to receive/send notifications/events.
## 2 - configure_notifications.py takes two parameters, bucket and arn of the lambda function. the lambda function has to be added in aws and we should enter arn of the lambda function
## 3 - lambda_creator.py takes two parameters, that are name of the function that will be created in AWS and path, where the zipped code is placed in computer. After entering those two parameters, lambda function will be created.
## 4 - lambdafunc.py contains the code, that handles the event and data, that is received from the notification. sends the .jpeg data to huggingface and receives and uploads .json format of the same file in the bucket
