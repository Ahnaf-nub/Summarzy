from groq import Groq

client = Groq(
    api_key= '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',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)