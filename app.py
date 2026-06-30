import os

from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

# Paste Gemini API key here
load_dotenv()

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)


@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    task = data["task"]

    prompt = f"""
You are Deadline Guardian AI.

Analyse this task and return:

🚨 Priority
📅 Best time to start
⏳ Suggested work schedule
⚠️ Risk of missing deadline
💡 Productivity tips

Task:
{task}

Keep the answer short, neat and use emojis.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({
        "response": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)