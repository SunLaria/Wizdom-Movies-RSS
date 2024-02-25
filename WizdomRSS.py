from requests_html import HTMLSession,HTML
from bs4 import BeautifulSoup
from rfeed import *

session = HTMLSession()
r = session.get("https://wizdom.xyz/")
r.html.render()

movies = []

soup = BeautifulSoup(r.html.html,"html.parser")


for movie_card in soup.findAll("div",attrs={"class": "poster col-md-3 col-lg-2 col-xl-1 col-6"}):
    imdb = movie_card.find('a').attrs["href"].split("/movie/")[1]
    name = movie_card.find("div",attrs={"class": "v-card__title poster-title"}).text
    movies.append(Item(
        title=name,
        description=imdb
    ))

feed = rfeed.Feed(title="Wizdom Rss",
                  description = "Hebrew Subtitles Rss Feed,",
                  language="en-US",
                  items=movies,
                  link="https://example.com/rss"
                  )

print(feed.rss())