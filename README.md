# Wizdom RSS

Get Wizdom RSS feed using this server.

Can be Added To Radarr as a list.

- HTML Content retrived using request-html.
- Data is Scraped using beautifulsoup4.
- RSS is generated using rfeed.

## Setup

docker:
'''
docker run -p 8020:8000 docker.io/randomg1/wizdom-rss:1
'''

docker-compose:
'''
version: '4'
services:
  wizdom-rss:
    image: docker.io/randomg1/wizdom-rss:1
    ports:
      - "8020:8000"
'''


## Usage

- Go To "http://localhost:8020" Or "http://127.0.0.1:8020"

## How to add to Radarr

- Settings -> Import Lists -> + -> "RSS List"
- Add "http://wizdom-rss:8020" as RSS Link
