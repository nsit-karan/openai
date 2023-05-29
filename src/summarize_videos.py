from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=Fquj2u7ay40", add_video_info=True)
result = loader.load()

# initialize llm
print (f"Found video from {result[0].metadata['author']}")
llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

texts = text_splitter.split_documents(result)

'''
if used with chain_type as stuff without splitting,
it will hit the token limit and wont go through
'''
chain = load_summarize_chain(llm, chain_type="map_reduce", verbose = False)
print(chain.run(texts))