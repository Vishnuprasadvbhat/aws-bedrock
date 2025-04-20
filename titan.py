import boto3
import json


prompt_data = """
  I am Groot.
"""

bedrock = boto3.client(service_name= "bedrock-runtime")

payload = {
  "inputText" : prompt_data,
  "dimensions" : 256,
  "normalize" : True
}

body = json.dumps(payload)

model_id =  "amazon.titan-embed-text-v2:0"

response = bedrock.invoke_model(
  modelId=model_id,
  accept = "application/json",
  contentType = "application/json",
  body = body

)


response_body = json.loads(response['body'].read().decode('utf-8'))

with open('response.json', 'w') as file:
  json.dump(response_body, file, indent= 4)

response_text = response_body

print(response_text)

# This is a text to embedding model from Amazon 

''' 
Text as input: I am Groot.

Embedding as output: [-0.23950695991516113, 0.03579961508512497, 0.0456492081284523, 0.021612146869301796, ..... ]

'''

