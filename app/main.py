from fastapi import FastAPI
from fastapi.responses import Response
from requests_html import AsyncHTMLSession,HTML
from bs4 import BeautifulSoup
from rfeed import *

app = FastAPI()


@app.get("/")
async def main():
    asession = AsyncHTMLSession()
    r = await asession.get("https://wizdom.xyz/")
    await r.html.arender(wait = 1.5)
    text = r.html.html
    print(text)
    print("render achieved")
    print("now soup....")
    soup = BeautifulSoup(text,"html.parser")
    movies = []
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
                    link="https://wizdom.xyz/"
                    )

    return Response(content=feed.rss(), media_type="application/xml")

