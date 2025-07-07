from urllib.parse import urlparse, parse_qs

def extract_youtube_id(url: str) -> str:
    """
    Extract YouTube video ID from a URL.
    Example: https://www.youtube.com/watch?v=Mi0QycA81go
    """
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('v', [None])[0]