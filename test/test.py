from openai import OpenAI
import os
client = OpenAI(
	base_url="https://router.huggingface.co/novita",
	api_key=os.getenv("API_KEY")
)

messages = [
	{
		"role": "user",
		"content": "What is the capital of France?"
	}
]

completion = client.chat.completions.create(
	model="deepseek/deepseek-r1", 
	messages=messages, 
	max_tokens=500,
)

print(completion.choices[0].message)