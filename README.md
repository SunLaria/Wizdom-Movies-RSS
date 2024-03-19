# Wizdom Movies RSS

Get Wizdom RSS feed using this server.

Can be Added To Radarr as a list.

##  Why i made it

I was trying to find a wizdom.xyz RSS Feed for my Radarr setup but couldn't find anything related on the internet.
I contacted the site staff through email but received negative feedback in response.
So, I decided to create it myself.
I noticed that the site's HTML renders its movie cards with JavaScript, which presented some challenges for me, However, thankfully, I found the solution.

## How Its Achieved
- JS Rendered HTML Content retrived using request-html.
- Multiple Attempts To Achieve JS Rednered HTML.
- Data is Scraped using beautifulsoup4.
- RSS is generated using rfeed.

## Setup

docker:
```
docker run -p 8020:8000 docker.io/randomg1/wizdom-movies-rss:2
```

docker-compose:
```
version: '4'
services:
  wizdom-movies-rss:
    container_name: wizdom-rss
    image: docker.io/randomg1/wizdom-movies-rss:2
    ports:
      - "8020:8000"
```


## Usage
- First Link Entry, Downloads Chromium - Takes More Time
- Go To "http://localhost:8020" Or "http://127.0.0.1:8020"

## How to add to Radarr

- Settings -> Import Lists -> + -> "RSS List"
- Add "http://your-ip:8020" as RSS Link
