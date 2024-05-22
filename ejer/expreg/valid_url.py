import re


def is_valid_url(url: str) -> bool:
    url_is_valid = r'http(s)?://.+\..+'
    return re.fullmatch(url_is_valid, url) is not None
