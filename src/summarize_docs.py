from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.chains import RetrievalQA,RetrievalQAWithSourcesChain
from langchain.document_loaders import DirectoryLoader
from langchain.chains.summarize import load_summarize_chain

import magic
import os
import nltk

loader = DirectoryLoader('training_set/', glob='**/*.txt')
documents = loader.load()

#print(documents)

'''
Only for debugging
print(documents)
'''

llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
chain = load_summarize_chain(llm, chain_type = "map_reduce", verbose = False)
print(chain.run(documents))