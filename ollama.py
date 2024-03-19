from flask import Flask, request
import ollama
from datetime import date

app = Flask(__name__)


@app.route('/process_resume', methods=['POST'])
def process_resume():
    resume_text = request.json['resume_text']

    # Get today's date
    today = date.today()
    today = today.strftime("%Y-%m-%d")

    # Define your prompt
    prompt = resume_text+"""
    I need answers in key-value pairs. What are the name, phone number, email, skills, companies worked at, designation at those companies,duration in each company from the above resume text? Today is """+today+""", also caluculate total experience as years and months ,till present data. Give the data in the format
    {
        "Name": "",
        "Phone Number": "",
        "Email": "",
        "Skills" : "",
        "Companies Worked At": [""]
        "Designation at Companies": [""]
        "Duration at Each Company": [""]
        "Total Work Experience" : ""
    }
    . i dont need extra data."""

    # Prepare the message to send to the Mistral model
    message = {
        'role': 'system',
        'content': prompt
    }

    # Send the message and get the response
    response = ollama.chat(model='mistral:instruct', messages=[message])

    return response['message']['content']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
