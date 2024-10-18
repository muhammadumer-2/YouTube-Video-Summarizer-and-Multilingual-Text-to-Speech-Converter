import os
import openai
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser
from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from gtts import gTTS
from langchain_openai import OpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from deep_translator import GoogleTranslator


os.environ["OPENAI_API_KEY"] = "USE YOUR OWN API KEY"

url="https://www.youtube.com/watch?v=5lNQdVJs3pg"

save_dir = "./docs/youtube/"

loader = GenericLoader(
    YoutubeAudioLoader([url],save_dir),
    OpenAIWhisperParser()
)

docs = loader.load()

doc = docs[0].page_content

combine_prompt_template = """You will be given points and any important details of a text in bullet points.
                            Your goal is to give a final summary of the main topics and findings
                            which will be useful and related to Data engineer
                            to grasp what was done during the work.
                            ```{text}```
                            FINAL SUMMARY:
                            """

combine_prompt = PromptTemplate(input_variables=["text"],template=combine_prompt_template)

def summarize_pdf(text,chunk_size,chunk_overlap,combine_prompt):

    #instantiate LM model gpt-3.5-turbo-16k
    llm = ChatOpenAI(model="gpt-3.5-turbo-16k",temperature=0,openai_api_key = os.environ["OPENAI_API_KEY"])

    #load pdf file
    

    #create multiple documents
    docs_raw_text = [doc.page_content for doc in docs]

    #Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size,chunk_overlap=chunk_overlap)
    docs_chunks = text_splitter.create_documents(docs_raw_text)

    #Summarize the Chunks
    #chain = load_summarize_chain(llm,chain_type="stuff")
    chain = load_summarize_chain(llm,chain_type="map_reduce", combine_prompt=combine_prompt)
    
    #Return the summary
    summary = chain.invoke(docs_chunks,return_only_outputs=True)
    return summary['output_text']

summarized_text = summarize_pdf(docs,1000,20,combine_prompt)
#print(summarized_text)

translated_text = GoogleTranslator(source='en', target='ur').translate(summarized_text)
#print(f"Translated Text: {translated_text}")

# Text to voice changing

tts = gTTS(text=translated_text, lang='ur')
tts.save("output1.mp3")
os.system("start output1.mp3")  # For Windows, adjust for other OS