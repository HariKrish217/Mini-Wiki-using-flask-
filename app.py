from flask import Flask, render_template, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
import wikipedia
import requests

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    keyword=request.form["search"].strip()
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{keyword}"

    headers = {
    "User-Agent": "MyMiniWikiApp/1.0 (contact: youremail@example.com)"
     }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
     data = response.json()
     Title=data.get("title")
     Summary=data.get("extract")
     Image= data.get("thumbnail", {}).get("source", None)

    else:
     print("Error:", response.status_code)

    return render_template("result.html",title=Title, summary=Summary, image=Image) 



    


if __name__=="__main__":
    app.run(debug=True)
