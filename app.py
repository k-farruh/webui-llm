from flask import Flask, render_template, request
import openai
import requests
import os
import datetime

app = Flask(__name__)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def retrieve(query):
    url = "http://127.0.0.1:8000/query"
    payload = {
        "queries": [
            {
                "query": query,
                "top_k": 2
            }
        ]
    }
    BEARER_TOKEN = "put you own BEARER_TOKEN"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(headers)
	
    if response.status_code == 200:
        res = response.json()
        contexts = [result["text"] for result in res["results"][0]["results"]]

        # build our prompt with the retrieved contexts included
        prompt_start = (
            "Pickup and delivery parcel. Answer the question based on the context below. don't try to make up an answern.\n\n" +
            "Context:\n"
        )
        prompt_end = (
            f"\n\nQuestion: {query}\nAnswer:"
        )

        limit = 2000

        # append contexts until hitting limit
        for i in range(1, len(contexts)):
            if len("\n\n---\n\n".join(contexts[:i])) >= limit:
                prompt = (
                    prompt_start +
                    "\n\n---\n\n".join(contexts[:i-1]) +
                    prompt_end
                )
                break
            elif i == len(contexts)-1:
                prompt = (
                    prompt_start +
                    "\n\n---\n\n".join(contexts) +
                    prompt_end
                )
        return prompt
    else:
        raise Exception(f"Error in retrieving data: {response.status_code}")


def complete(prompt):
    # query text-davinci-003
    res = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        temperature=0.8,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return res['choices'][0]['text'].strip()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["query"]
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        prompt = retrieve(query)
        print(prompt)
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        answer = complete(prompt)
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        
        return render_template("index.html", answer=answer)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

