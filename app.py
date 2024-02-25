from fastapi import FastAPI
import uvicorn
from fastapi.responses import PlainTextResponse
from requests_html import AsyncHTMLSession,HTML
from bs4 import BeautifulSoup
from rfeed import *


if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)



app = FastAPI()




@app.get("/")
async def root():
    session = AsyncHTMLSession()
    r = await session.get("https://wizdom.xyz/")
    await r.html.arender()
    soup = BeautifulSoup(r.html.html,"html.parser")
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
                    link="https://example.com/rss"
                    )

    return PlainTextResponse(feed.rss())