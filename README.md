***Mini Wiki – Flask Project***

A simple Wikipedia-like web app built with Flask, where users can search for topics, view summaries, and explore quick facts using the Wikipedia API.
This project demonstrates how to integrate APIs, manage Flask routes, and render dynamic content with templates.

🚀 **Features**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔎 **Search Bar**: Search for any topic or keyword

📄 **Summary View**: Fetch and display short summaries from Wikipedia

🖼️ **Image Support**: Show the main image of the searched article (if available)

🧩 **Dynamic Rendering**: Flask templates render live data from the API

⚠️ **Error Handling**: Graceful response for invalid or missing pages

🧰 **Tech Stack**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Backend: Flask (Python)

Frontend: HTML, CSS, Bootstrap / Sass

API: Wikipedia REST API (https://en.wikipedia.org/api/rest_v1/page/summary/{topic})

Language: Python 3


📦 **Installation**
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Clone the repository***

git clone https://github.com/yourusername/mini-wiki-flask.git
cd mini-wiki-flask


***Create and activate a virtual environment***

python -m venv env
source env/bin/activate  # on Windows: env\Scripts\activate


***Install dependencies***

pip install -r [requirements.txt](requirements.txt)


***Run the Flask server***

python app.py


The app will start on:
👉 http://127.0.0.1:5000/

⚙️ Project Structure
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
mini-wiki-flask/
│
├── app.py                   # Main Flask app file

├── templates/

│   ├── index.html           # Home + search page

│   ├── result.html          # Displays search result

│   └── error.html           # Error page for missing topics

│

├── static/

│   ├── css/

│   │   └── style.css        # Custom styles or compiled Sass

│   └── scss/                # Optional Sass source files

│

├── requirements.txt         # Dependencies

└── [README.md](README.md)                # Project documentation

🧑‍💻 Usage
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Open the homepage.

Enter any topic name in the search bar.

The app will fetch the summary and display:

Title

Description

Extract (short summary)

Image (if available)

If no results are found, it will show an error page.

🪄 Example
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Search: India

Result: Displays a short summary about India along with an image and a link to the full Wikipedia page.

🧩 Future Enhancements
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔎 Auto-suggest search results

🕹️ Add related article links

💾 Save recent searches

🌙 Dark mode support

🤝 Contributing
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Feel free to fork the repo, open issues, or submit pull requests.
Contributions, ideas, and improvements are always welcome!

🧑‍🎓 Credits

Developed by Arch 💙

Data powered by Wikipedia REST API
