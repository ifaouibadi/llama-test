from dotenv import load_dotenv
from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
import streamlit as st

load_dotenv()

hub_llm = HuggingFaceHub(
    # repo_id="gpt2",
    model_kwargs={"max_length": 4000, "temperature": 0.6},
    repo_id="meta-llama/Llama-2-7b-chat-hf",
    # repo_id="mrm8488/t5-base-finetuned-wikiSQL",
)

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
    You're a help full assistance agent for GuardMe,
    GuardMe is a solutions-focused health and wellness insurance provider for international students, staff, and schools. Our dedicated team understands the exciting journey international students are on, and how an unexpected medical bill or mental health concern can stop it. No matter the situation, we care to look for solutions.
We empower students, schools, and support staff, to safely travel the world to enrich their lives through international study. We believe everyone should feel safe, supported, and cared for during their time abroad. What sets  apart is that we genuinely care, that’s why we’ve created multiple solutions to ensure you’re taken care of in any situation.



    answer the customers question: {question}
    """,
)


hub_chain = LLMChain(
    prompt=prompt,
    llm=hub_llm,
    verbose=True,
)


text = st.text_area("enter some text")

if text:
    out = hub_chain.run(text)
    st.json({
        "input": text,
        "output": out
    })
