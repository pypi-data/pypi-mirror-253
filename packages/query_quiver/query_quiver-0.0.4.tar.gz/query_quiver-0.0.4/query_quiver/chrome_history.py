import os
import sqlite3
from contextlib import closing
from typing import Any
from urllib.parse import unquote

from query_quiver.logger import create_logger
from query_quiver.types import ChromeKeyword

DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH = f"/Users/{os.environ.get('USER')}/Library/Application Support/Google/Chrome/Default/History"  # noqa: E501


class ChromeHistory(object):
    def __init__(self, chrome_history_path: str | None = None) -> None:
        """Initialize

        Args:
            chrome_history_path (str | None, optional): Path of chrome history SQLite file.

            Default is `~/Library/Application Support/Google/Chrome/Default/History`.
        """
        self.sqlite_path = (
            chrome_history_path or DEFAULT_GOOGLE_CHROME_HISTORY_SQLITE_PATH
        )
        self.logger = create_logger(__name__)

    def get_history(self, limit: int = 100) -> list[list[str]]:
        """Get past visited sites from Google Chrome history

        Args:
            limit (int, optional): Number of histories to fetch. Defaults to 100.

        Returns:
            list[list[str]]: List of past visited site urls
        """
        self.logger.debug("Fetching history")
        histories = self.fetch_data_from_chrome_history_db(
            """
            SELECT
              DISTINCT
              CASE
                WHEN INSTR(urls.url, "?") > 0 THEN SUBSTR(urls.url, 0, INSTR(urls.url, "?"))
                ELSE urls.url
              END,
              urls.title
            FROM
              visits
            LEFT OUTER JOIN
              urls
              ON
                visits.url = urls.id
            WHERE urls.url NOT LIKE 'https://www.google.com/search%'
            ORDER BY
              visits.visit_time DESC
            LIMIT ?
            """,
            (limit,),
        )
        self.logger.debug(f"Found {len(histories)} histories")
        return histories

    def get_google_search_words_history(self, limit: int = 100) -> list[ChromeKeyword]:
        """Extract past Google search words from Google Chrome history

        Args:
            limit (int, optional): Number of histories to fetch. Defaults to 100.

        Returns:
            list[ChromeKeyword]: List of past Google search words
        """
        histories = self.fetch_data_from_chrome_history_db(
            """
            SELECT
              DISTINCT
              urls.url
            FROM
              visits
            LEFT OUTER JOIN
              urls
              ON
                visits.url = urls.id
            WHERE urls.url LIKE 'https://www.google.com/search?%'
            ORDER BY
              visits.visit_time DESC
            LIMIT ?
            """,
            (limit,),
        )
        return [
            ChromeKeyword(
                keywords=self.extract_chrome_query_from_url(url[0]),
            )
            for url in histories
        ]

    def extract_chrome_query_from_url(self, url: str) -> list[str]:
        """Extract query from url"""
        keywords_encoded = url.split("q=")[1].split("&")[0].replace("+", " ").split(" ")
        return [unquote(keyword) for keyword in keywords_encoded]

    def fetch_data_from_chrome_history_db(
        self, query: str, params: tuple[Any, ...]
    ) -> list:
        """Execute SQL query"""
        with closing(sqlite3.connect(self.sqlite_path, timeout=5)) as conn:
            c = conn.cursor()
            c.execute(query, params)
            return c.fetchall()
