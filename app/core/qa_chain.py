from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def build_prompt():
    return PromptTemplate(
        template="""
        You are a helpful assistant.
        Answer only from the provided transcript context.
        If the context is insufficient, just say you don't know.

        {context}
        question: {question}
        """,
        input_variables=['context', 'question']
    )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def create_qa_chain(retriever):
    prompt = build_prompt()
    llm = ChatOllama(model="mistral", temperature=0.2)

    # Step 1: Run retriever and prepare prompt inputs
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    # Step 2: Full chain → run retriever → build prompt → LLM → parse output
    main_chain = parallel_chain | prompt | llm | StrOutputParser()

    return main_chain