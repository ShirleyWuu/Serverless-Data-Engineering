import boto3
import json

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Define the DynamoDB table
table_name = 'proj4-write-read'
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    
    if "phrase" in event:
        
        # ---- check if the item is in db ---
        # get the phrase entered by the user
        phrase = event['phrase']
        # query the DynamoDB table for the phrase
        response = table.get_item(
            Key={
                'phrase': phrase
            }
        )
        # check if the response contains any data
        if 'Item' in response:
            # return the record
            return response['Item']

        else:
            # do the sentiment analyze
            phrase = event["phrase"]
            comprehend = boto3.client("comprehend")
            result = comprehend.detect_sentiment(Text=phrase, LanguageCode='en')
            print(result)   #log this outcome to CloudWatch
            payload = {"phrase":phrase, "sentiment": result["Sentiment"]}
            
            # store into the database
            item_data = {
                'phrase': event['phrase'],
                'sentiment': result['Sentiment']
            }
        
            # Write the item to the table
            table.put_item(Item=item_data)
            
            print("Item written to DynamoDB table proj4-write-read")
        
            # Return a success message
            return {
                'statusCode': 200,
                'body': json.dumps('Response from AWS Lambda Function'),
                'Response': payload
            }

    return None
    
