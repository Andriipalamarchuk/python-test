import hashlib
from urllib.parse import urlparse


def shorten_url(original_url):
        parsed_url = urlparse(original_url)
        print(parsed_url.hostname)
        hash_value = hashlib.md5(parsed_url.path.encode()).hexdigest()[:10]

        return f"{parsed_url.scheme}://{parsed_url.hostname}/{hash_value}" 