from fastapi import APIRouter, HTTPException
from app.schemas.request_response import TranscriptRequest, AskQuestionRequest, AnswerResponse
from app.utils.youtube_utils import extract_youtube_id
from app.services.transcript_service import fetch_transcript
from app.services.text_splitter import split_text
from app.core.vectorstore import build_vector_store
from app.core.qa_chain import create_qa_chain

router = APIRouter()

# Keep retriever and chain global (simulate persistence for demo)
vector_store = None
qa_chain = None

@router.post("/transcript")
def process_transcript(request: TranscriptRequest):
    global vector_store, qa_chain

    try:
        # video_id = extract_youtube_id(request.youtube_url)
        # transcript = fetch_transcript(video_id)
        
        transcript = fetch_transcript(request.youtube_url)
        
        documents = split_text(transcript)

        vector_store = build_vector_store(documents)
        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        qa_chain = create_qa_chain(retriever)

        return {"message": "Transcript processed and vector store created."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: AskQuestionRequest):
    global qa_chain

    if qa_chain is None:
        raise HTTPException(status_code=400, detail="Please process transcript first using /transcript.")

    try:
        answer = qa_chain.invoke(request.question)
        return AnswerResponse(answer=answer)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))