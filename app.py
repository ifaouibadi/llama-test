import streamlit as st
from dotenv import load_dotenv
from langchain import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Chroma

from constants import PERSIST_DIRECTORY

load_dotenv()

hub_llm = HuggingFaceHub(
    # model_kwargs={"max_length": 4000, "temperature": 0.6},
    repo_id="meta-llama/Llama-2-7b-chat-hf",
)

system_prompt = """You are a helpful assistant, you will use the provided context to answer user questions.
Read the given context before answering questions and think step by step. If you can not answer a user question based on 
the provided context, inform the user. Do not use any other information for answering user. Provide a detailed answer to the question."""

instruction = """
            Context: {context}
            User: {question}"""

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
SYSTEM_PROMPT = B_SYS + system_prompt + E_SYS
prompt_template = B_INST + SYSTEM_PROMPT + instruction + E_INST


prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template,
)


embeddings = HuggingFaceEmbeddings()
db = Chroma(
    embedding_function=embeddings,
    persist_directory=PERSIST_DIRECTORY,
)

retriever = db.as_retriever()


qa = RetrievalQA.from_chain_type(
    llm=hub_llm,
    chain_type="stuff",
    verbose=True,
    retriever=retriever,
    chain_type_kwargs={"prompt": prompt},
    # chain_type_kwargs={"prompt": prompt, "memory": memory},
)


text = st.text_area("enter some text")

if text:
    out = qa.run(text)
    st.json({"input": text, "output": out})
