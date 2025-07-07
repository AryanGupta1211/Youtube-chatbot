import requests

API_BASE_URL = "http://localhost:8000"

def send_transcript_request(youtube_url: str):
    response = requests.post(f"{API_BASE_URL}/transcript", json={"youtube_url": youtube_url})
    if response.status_code != 200:
        raise Exception(response.json().get("detail", "Unknown error"))
    return response.json()

def send_question(question: str):
    response = requests.post(f"{API_BASE_URL}/ask", json={"question": question})
    if response.status_code != 200:
        raise Exception(response.json().get("detail", "Unknown error"))
    return response.json().get("answer", "No answer received.")