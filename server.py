from flask import Flask, request, jsonify
import openai

# Set your OpenAI API key securely
openai.api_key = "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"

app = Flask(__name__)

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