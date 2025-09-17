from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-3.5-turbo",
  input="write a haiku about ai",
)

print(response.output_text);