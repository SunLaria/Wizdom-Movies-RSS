from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from requests_html import AsyncHTMLSession,HTML
from bs4 import BeautifulSoup
from rfeed import *
# from playwright.async_api import async_playwright

app = FastAPI()


# async def get_rendered_html(url):
#     async with async_playwright() as p:
#         browser = await p.chromium.launch()
#         page = await browser.new_page()
#         await page.goto(url)
#         # Wait for the page to render completely
#         await page.wait_for_load_state("networkidle")
#         # Retrieve the HTML content
#         html_content = await page.content()
#         await browser.close()
#         return html_content



@app.get("/")
async def main():
    session = AsyncHTMLSession()
    r = await session.get("https://wizdom.xyz/")
    await r.html.arender()
    text = r.html.html
    # text = await get_rendered_html("https://wizdom.xyz/")
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
                    link="https://example.com/rss"
                    )

    return PlainTextResponse(feed.rss())

