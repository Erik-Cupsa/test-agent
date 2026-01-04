import json
 import os
 from openai import OpenAI

 def main():
     # Read input from file (E2B writes this at /app/input.json)
     try:
         with open('input.json', 'r') as f:
             input_data = json.load(f)
     except FileNotFoundError:
         input_data = {'prompt': 'Hello! Tell me a fun fact.'}

     prompt = input_data.get('prompt', 'Hello!')
     print(f'Received prompt: {prompt}')

     # Initialize OpenAI client (API key injected by E2B)
     client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

     # Call OpenAI
     response = client.chat.completions.create(
         model='gpt-4o-mini',
         messages=[
             {'role': 'system', 'content': 'You are a helpful assistant. Be concise.'},
             {'role': 'user', 'content': prompt}
         ]
     )

     # Output result
     result = response.choices[0].message.content
     print(f'\n--- AI Response ---\n{result}')

 if __name__ == '__main__':
     main()
