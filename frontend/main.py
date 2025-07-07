import streamlit as st
from api_client import send_transcript_request, send_question

st.set_page_config(page_title="YouTube Q&A Bot", page_icon="🤖")

st.title("🎥 YouTube Transcript Q&A Bot")
st.write("Enter a YouTube video link and ask questions from its transcript.")

# ------------------------- Transcript Section -------------------------

with st.form("transcript_form"):
    youtube_url = st.text_input("YouTube Video URL", placeholder="https://www.youtube.com/watch?v=Mi0QycA81go")
    process_btn = st.form_submit_button("Fetch Transcript & Create Vector Store")

    if process_btn and youtube_url:
        with st.spinner("Processing transcript..."):
            try:
                result = send_transcript_request(youtube_url)
                st.success(result.get("message", "Transcript processed successfully!"))
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------------- Ask Questions Section -------------------------

st.markdown("---")
st.subheader("❓ Ask Questions")

question = st.text_input("Your Question", placeholder="Ask anything about the video...")

if st.button("Ask"):
    if not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                answer = send_question(question)
                st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")
