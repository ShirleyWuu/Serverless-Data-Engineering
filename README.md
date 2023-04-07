# Serverless-Data-Engineering

### Introduction
To build a serverless data engineering project. Serverless means that I could just focus on the 'Function' and 'Data', without thinking about the server. This is a sample project that demonstrates how to use AWS services to build a simple web serverless application that can analyze phrase sentiment and store data in a database.

![graph](https://user-images.githubusercontent.com/123136573/230687402-9142d5aa-9304-4872-b06e-8f50616227ae.png)


#### TOOLS
- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- AWS Comprehend
- AWS CloudWatch

You will also need to install the following software on your machine:
- Python 3.8 or later
- AWS CLI


#### USAGE
To use the web application, follow these steps: <br>

- Open your web browser and navigate to the URL of the API Gateway. 
- Add a phrase in the following format behind the URL: https://txled833h4.execute-api.us-east-1.amazonaws.com/query-analyze-store?phrase="ENTER YOUR PHRASE"
- If the phrase exists in the DynamoDB database, the corresponding data will be returned.
- If it does not exist, the phrase will be sent to Comprehend for sentiment analysis and return back to you. 
- The results of the analysis will be stored in DynamoDB, along with the original phrase.
- Use CloudWatch to view the logs and debug any issues that arise.

### DEMO VIDEO

https://user-images.githubusercontent.com/123136573/230690486-8062c07f-79a5-47d9-9d93-ded82f1cc05c.mp4


