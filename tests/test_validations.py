from validator import is_valid_url
from .fixtures import ONLY_VALID_URLS, WITH_INVALID_URLS


def test_invalid_urls_return_false():
    for url in WITH_INVALID_URLS:
        assert is_valid_url(url=url) is False


def test_valid_urls_return_true():
    for url in ONLY_VALID_URLS:
        assert is_valid_url(url=url) is True
