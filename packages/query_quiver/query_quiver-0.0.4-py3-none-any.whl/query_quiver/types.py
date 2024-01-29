from dataclasses import dataclass


@dataclass
class WebPageInfo(object):
    title: str
    description: str
    keywords: list[str]

    def __str__(self) -> str:
        return f"title: {self.title}\ndescription: {self.description}\nkeywords: {self.keywords}"


@dataclass
class ChromeKeyword(object):
    keywords: list[str]

    def __str__(self) -> str:
        return f"keywords: {', '.join(self.keywords)}"
