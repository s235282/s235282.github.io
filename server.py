from flask import Flask, request, jsonify
import openai

# Set your OpenAI API key securely
openai.api_key = "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"

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Render!"


@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        # Make the OpenAI API call
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        response_content = chat_completion.choices[0].message.content
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
