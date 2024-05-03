import datetime
import locale
from flask import Flask, render_template, request
from pymongo import MongoClient

locale.setlocale(locale.LC_TIME, 'fr_FR')

app = Flask(__name__)
# Usage de la configuration de développement
app.config.from_object('config.DevConfig')

client = MongoClient(app.config.get("MONGODB_URI"))
app.db = client.microblog

def create_app(db_url=None):
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [
            {
                "content" : entry["content"],
                "date": entry["date"],
                "month_year": datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %y").capitalize(),
            }
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entries_with_date)
    
    return app

create_app()