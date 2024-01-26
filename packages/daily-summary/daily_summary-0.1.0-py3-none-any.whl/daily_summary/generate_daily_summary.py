from openai import OpenAI
import json
import os
from datetime import datetime

# Get the API key from the environment variable
client = OpenAI()
client.api_key = os.environ["OPENAI_API_KEY"]


date = datetime.now().date()


def daily_summary(summaries):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": f"Create a daily development report for Jack Driscoll's commits on {date}. The recipient of this report is Jack Driscoll. The report should start \"Your day in review\" followed by the top development updates of the day. Don't list by commit, but just give a holistic report of the day.  Here are the key changes made in each commit: ",
            },
            {
                "role": "user",
                "content": summaries,
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content


def generate():
    # Read the diffs from the JSON file
    with open("summaries.txt", "r") as file:
        summaries = file.read()

    # Summarize the diffs
    report = daily_summary(summaries)

    # make a direcrory for the daily summary if it doesn't exist
    if not os.path.exists("daily-summaries"):
        os.makedirs("daily-summary")

    # Writing daily summary to a file named after the date
    with open(f"daily-summary/{date}.md", "w") as file:
        file.write(report)
