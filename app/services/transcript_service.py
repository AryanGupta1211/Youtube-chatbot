import subprocess
import os
from urllib.parse import urlparse, parse_qs

def fetch_transcript(video_url: str) -> str:
    """
    Downloads auto-generated subtitles using yt-dlp and reads them.
    """
    video_id = extract_youtube_id(video_url)
    output_file = f"{video_id}.en.vtt"

    try:
        subprocess.run([
            "yt-dlp",
            "--skip-download",
            "--write-auto-sub",
            "--sub-lang", "en",
            "--output", f"{video_id}.%(ext)s",
            video_url
        ], check=True)

        # Read the generated .vtt subtitle file
        with open(output_file, "r", encoding="utf-8") as f:
            vtt_content = f.read()

        # Clean up the file
        os.remove(output_file)

        # Parse .vtt to plain text
        return parse_vtt(vtt_content)

    except subprocess.CalledProcessError:
        raise RuntimeError("yt-dlp failed to download subtitles.")
    except FileNotFoundError:
        raise RuntimeError("Subtitle file not found after yt-dlp run.")

def extract_youtube_id(url: str) -> str:
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('v', [None])[0]

def parse_vtt(vtt_content: str) -> str:
    """
    Parses .vtt content and extracts only the subtitle text.
    """
    lines = vtt_content.splitlines()
    transcript_lines = []
    for line in lines:
        # Skip timestamps and metadata
        if "-->" in line or line.strip() == "" or line.startswith("WEBVTT"):
            continue
        transcript_lines.append(line.strip())
    return " ".join(transcript_lines)


# from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

# def fetch_transcript(video_id: str, languages=['en', 'hi']) -> str:
#     """
#     Fetch transcript for the given YouTube video ID.
#     """
#     try:
#         ytt_api = YouTubeTranscriptApi() 

#         # Fetch the transcript
#         fetched_transcript = ytt_api.fetch(video_id, languages=languages)

#         # Join all snippet texts
#         transcript = " ".join(snippet.text for snippet in fetched_transcript)
#         return transcript

#     except Exception as e:
#         raise RuntimeError(f"Failed to fetch transcript: {str(e)}")


#     except TranscriptsDisabled:
#         raise ValueError("Transcripts are disabled for this video.")
    
#     except NoTranscriptFound:
#         raise ValueError("No transcript found for this video in the requested languages.")
    
#     except VideoUnavailable:
#         raise ValueError("The video is unavailable.")
    
#     except Exception as e:
#         raise RuntimeError(f"Failed to fetch transcript: {str(e)}")
