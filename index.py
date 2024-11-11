from openai import OpenAI
client = OpenAI()

prompt = input("Hola, soy ChatGPT, ¿En que te puedo ayudar? :) - ")

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("CHAT GPT: ", completion.choices[0].message.content)
