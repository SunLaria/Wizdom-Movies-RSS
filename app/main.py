from fastapi import FastAPI
from fastapi.responses import Response
from requests_html import AsyncHTMLSession,HTML
from bs4 import BeautifulSoup
from rfeed import *

app = FastAPI()


@app.get("/")
async def main():
    asession = AsyncHTMLSession()
    max_attempts = 4
    attempt = 0
    print("Trying to Render Site JavaScript... ")
    while attempt <= max_attempts:
        r = await asession.get("https://wizdom.xyz/")
        try:
            await r.html.arender()
            search_check=r.html.find(".v-card__title")
            if len(search_check) >1:
                text = r.html.html
                r.close()
                break
            else:
                print(f"Site JavaScript Render Failed on attempt {attempt}.")
                attempt += 1
            
        except:
            print(f"Site JavaScript Render Failed on attempt {attempt}.")
            attempt += 1
    else:
        print(f"Failed To Render Site After {max_attempts} attempts")
        raise ValueError(f'Failed To Render Site After {max_attempts} attempts')
    print("Site Render Achieved")
    print("Scraping Site Data")
    soup = BeautifulSoup(text,"html.parser")
    movies = []
    for movie_card in soup.findAll("div",attrs={"class": "poster col-md-3 col-lg-2 col-xl-1 col-6"}):
        movies.append(Item(
            title=movie_card.find("div",attrs={"class": "v-card__title poster-title"}).text,
            description=movie_card.find('a').attrs["href"].split("/movie/")[1]
        ))

    feed = rfeed.Feed(title="Wizdom Rss",
                    description = "Hebrew Subtitles Rss Feed,",
                    language="en-US",
                    items=movies,
                    link="https://wizdom.xyz/"
                    )
    print("Movies RSS Feed Generated")
    print("Returning Passing RSS Feed")
    return Response(content=feed.rss(), media_type="application/xml")

