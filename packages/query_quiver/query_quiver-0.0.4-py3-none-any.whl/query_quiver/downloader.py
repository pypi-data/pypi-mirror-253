import threading
import time

import requests
from bs4 import BeautifulSoup
from urllib3.util import parse_url

from query_quiver.logger import create_logger
from query_quiver.types import WebPageInfo


class Downloader(object):
    def __init__(self, client=requests) -> None:
        self.logger = create_logger(__name__)
        self.client = client
        self.origin_locks: dict = {}
        self.results: list[str] = []

    def extract_information_from_webpages(self, urls: list[str]) -> list[WebPageInfo]:
        """Extract information from webpage"""
        html_list = self.download_webpages(urls)
        return [self.parse_webpage_info(html) for html in html_list]

    def _download(self, url: str):
        """Download webpage from URL"""
        origin = parse_url(url).host
        with self.origin_locks.setdefault(origin, threading.Lock()):
            try:
                self.logger.debug(f"Downloading {url}")
                response = self.client.get(url)
                time.sleep(1)
                self.results.append(response.text)
            except Exception as e:
                self.logger.warning(f"Failed to download {url}: {e}")

    def download_webpages(self, urls: list[str]) -> list[str]:
        """Download webpages from URLs"""
        # reset results
        self.results = []
        threads = []
        self.logger.debug(f"Downloading {len(urls)} webpages")
        for url in urls:
            thread = threading.Thread(target=self._download, args=(url,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        self.logger.debug(f"Downloaded {len(self.results)} webpages")
        return self.results

    def parse_webpage_info(self, html: str) -> WebPageInfo:
        """Parse webpage info from HTML

        NOTE: bs4 type hints are not correct so we ignore many type errors
        """
        self.logger.debug("Parsing webpage info")
        soup = BeautifulSoup(html, "html.parser")
        title: str = soup.title.string if soup.title else ""  # type: ignore
        description = soup.find("meta", attrs={"name": "description"})
        description_content = description["content"] if description else ""  # type: ignore
        keywords = soup.find("meta", attrs={"name": "keywords"})
        keyword_contents = keywords["content"].split(",") if keywords else []  # type: ignore
        return WebPageInfo(
            title=title,
            description=description_content
            if isinstance(description_content, str)
            else ",".join([str(d) for d in description_content]),
            keywords=keyword_contents,
        )
