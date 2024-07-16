# Wizdom Movies RSS

Generate Wizdom.xyz RSS feed using this docker container.

Can be Added To Radarr Movie Manager as a list.

## How Its Achieved

- JS Rendered HTML Content retrived using Selenium Chrome WebDriver.
- Data is Scraped using BeautifulSoup4.
- RSS is generated using Rfeed.

## Setup

Docker:
```
docker run -p 8020:8000 docker.io/randomg1/wizdom-movies-rss
```

Docker-compose:
```
version: '4'
services:
  wizdom-movies-rss:
    container_name: wizdom-rss
    image: docker.io/randomg1/wizdom-movies-rss:latest
    ports:
      - "8020:8000"
    restart: unless-stopped
```

Manually :
```
git clone https://github.com/SunLaria/Wizdom-Movies-RSS.git
cd Wizdom-Movies-RSS
python app/main.py
```

## Usage
- Go To "http://localhost:8020" Or "http://127.0.0.1:8020"
- See docker interactive shell for notifications.

## How to add to Radarr

- Settings -> Import Lists -> + -> "RSS List"
- Add "http://your-ip:8020" as RSS Link
