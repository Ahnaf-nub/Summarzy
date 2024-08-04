from groq import Groq
from flask import Flask, request, jsonify

app = Flask(__name__)

client = Groq(
    api_key='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',
)

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text: {text}"
            }
        ],
        model="llama3-70b-8192",
    )
    summary = chat_completion.choices[0].message.content
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)


