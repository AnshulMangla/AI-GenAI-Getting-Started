import requests
import os

api_key = os.getenv('OPENAI_API_KEY')
content = """
Give me a funny joke for software developers vs network engineers, only return the joke
"""

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
  }

json_data = {
   'model': 'gpt-4-turbo',
   'temperature': 0.9,
   'messages': [
        {
            'role': 'system',
            'content': 'Your name is Cisco Virtual Engineer',
        },
       {
            'role': 'user',
            'content': f'{content}',
       },
    ],
}

response = requests.post('https://cxai-playground.cisco.com/chat/completions', headers=headers, json=json_data)
response_json = response.json()
print (response_json.get("choices")[0].get("message").get("content"))
