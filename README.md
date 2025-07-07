# 📺 YouTube Transcript Q\&A System 🎙️

**A Production-ready AI system to extract YouTube video transcripts, build embeddings, and enable contextual Q\&A—powered by FastAPI, Streamlit, LangChain, Ollama, and FAISS.** <br>

---

## 🎀 Project Overview

This project demonstrates an **end-to-end AI-powered microservice architecture** that:

* Extracts transcripts from **YouTube videos** using `yt-dlp`
* Splits and embeds the transcript with **LangChain + Ollama (Mistral model)**
* Stores vector embeddings in a **FAISS** database for fast similarity search
* Answers user questions based **only on the YouTube transcript**, not hallucinated data
* Provides a clean **FastAPI backend API** and a **Streamlit frontend** for easy interaction

---

## 🌟 Key Features

* ✅ Extract auto-generated captions from YouTube using reliable open-source tooling
* ✅ Local LLM inference using **Ollama** (Mistral 7B)
* ✅ Efficient semantic search using FAISS
* ✅ Modular LangChain pipelines for easy model/embedding swap
* ✅ Clean RESTful APIs with FastAPI
* ✅ Interactive user interface built with Streamlit
* ✅ Easily extensible to other data sources like PDFs, web pages, or databases

---

## 🛠️ Tech Stack

| Layer              | Tools/Tech                                          |
| ------------------ | --------------------------------------------------- |
| 🧐 LLM Inference   | Ollama (Mistral 7B), LangChain                      |
| 🔎 Embedding Store | FAISS                                               |
| 📄 Transcript      | yt-dlp, WebVTT parsing                              |
| 🔌 Backend API     | FastAPI, Pydantic                                   |
| 🖖️ Frontend       | Streamlit                                           |
| 🔧 Utilities       | Python (subprocess, urllib), Modular Service Layers |
| 🔬 DevOps Ready    | Docker-ready structure (future extension)           |

---

## 🛡️ Why Recruiters & Engineers Should Care

🔁 Demonstrates **real-world AI system design, not just scripts**
🔁 Shows hands-on experience with **LLMs, Vector Databases, and Retrieval-Augmented Generation (RAG)**
🔁 Builds a complete microservice + frontend, showcasing **full-stack AI engineering skills**
🔁 Practical example of **cloud-ready, modular, production-compliant code**

---

### Workflow:

* Enter YouTube video URL → Process transcript
* Ask questions → Get context-aware answers

---

## 🔮 Example Use Case

* Analyze a coding tutorial: "How to build a Chrome Extension"
* Ask: "Is the Chrome Extension built locally or published?"
* The app will search the transcript and give you the correct context-based answer.

---

## 🔮 Future Improvements

* Add persistent vector storage (e.g., ChromaDB, Pinecone)
* Dockerize the backend + frontend for easier deployment
* Extend data sources: PDFs, websites, Google Docs, etc.
* Add user authentication and session management
* Deploy to cloud: AWS/GCP/Azure or Hugging Face Spaces

---
