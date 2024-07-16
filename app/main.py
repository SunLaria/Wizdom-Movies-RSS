from fastapi import FastAPI, status
from fastapi.responses import Response, JSONResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from rfeed import Item, Feed
import time
import uvicorn

app = FastAPI()


@app.get("/")
async def main():
    print("Settings Up WebDriver...")
    max_attempts = 10
    max_result = 60
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)

    driver.get("https://wizdom.xyz/")
    time.sleep(5)

    movies = []
    print("Scraping Movies....")
    try:
        attempts = 0
        while attempts < max_attempts and len(movies) < max_result:
            rendered_html = driver.page_source
            soup = BeautifulSoup(rendered_html, "html.parser")
            movie_cards_search = soup.findAll(
                "div", class_="v-card-title poster-title")
            if movie_cards_search:
                for movie_card in movie_cards_search:
                    movies.append(Item(
                        title=movie_card.text,
                        description=movie_card.find_parent("a").attrs["href"].split(
                            "/movie/")[1]
                    ))
                    if len(movies) >= max_result:
                        break
            else:
                attempts += 1

        driver.quit()
        print("Movies Scrap Done!")
        print("Generating RSS Feed...")
        if len(movies) >= max_result:
            feed = Feed(
                title="Wizdom RSS",
                description="Hebrew Subtitles Rss Feed",
                language="en-US",
                items=movies,
                link="https://wizdom.xyz/"
            )
            return Response(content=feed.rss(), media_type="application/xml", status_code=status.HTTP_200_OK)

    except Exception as e:
        driver.quit()
        return JSONResponse(content={"Error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8020)
