# Wizdom Movies RSS

Generate Wizdom.xyz RSS feed using this Docker container..

Can be added to your RSS reader or any compatible service.

## How Its Achieved

- Uses Selenium Chrome WebDriver to fetch JavaScript-rendered HTML content.
- Scrapes data using BeautifulSoup4.
- Generates RSS feed using Rfeed.

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
python -m pip install -r requirements.txt
python app/main.py
```

## Usage
- Navigate to "http://localhost:8020" or "http://127.0.0.1:8020" to access the RSS feed.
- Monitor Docker logs for notifications and error messages Using Loguru Module.

## How to Add to RSS Reader

- Add the RSS feed link to your RSS reader using "http://your-ip:8020".
