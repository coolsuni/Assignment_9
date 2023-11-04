#1) Build a Flask app that scrapes data from multiple websites and displays it on your site.
#You can try to scrap websites like youtube , amazon and show data on output pages and deploy it on cloud
#platform

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
 return render_template("index.html")
if __name__ == "__main__":
 app.run(debug=True)

import requests 
from bs4 import BeautifulSoup
def scrape_news():
    url = "https://www.example-news.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []
    for headline in soup.find_all("h3", class_="headline"):
      headlines.append(headline.text)
    return headlines

    @app.route("/")
    def home():
        headlines = scrape_news()
    return render_template("index.html", headlines=headlines)