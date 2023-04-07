import boto3

# def lambda_handler(event, context):
    
#     if "phrase" in event:
#         phrase = event["phrase"]
#         comprehend = boto3.client("comprehend")
#         result = comprehend.detect_sentiment(Text=phrase, LanguageCode='en')
#         print(result)   #log this outcome to CloudWatch
#         payload = {"phrase":phrase, "sentiment": result["Sentiment"]}
#         return payload
#     return None #if the wrong payload is passed in, return None
    
   def lambda_handler(event, context):
    
    phrase = event["phrase"]
    comprehend = boto3.client("comprehend")
    result = comprehend.detect_sentiment(Text=phrase, LanguageCode='en')
    print(result)   #log this outcome to CloudWatch
    payload = {"phrase":phrase, "sentiment": result["Sentiment"]}
    

    return {
        'statusCode': 200,
        'body': json.dumps('Response from AWS Lambda Function 1'),
        'Response': payload
    }

