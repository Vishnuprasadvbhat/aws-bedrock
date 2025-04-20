import boto3
import json


prompt_data = """
  Act as Shakespeare and write a poem on Machine Learning
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
Text as input:  Act as Shakespeare and write a poem on Machine Learning

Embedding as output: [-0.12780310213565826, 0.08587569743394852, 0.06469380110502243, ..... ]

'''

