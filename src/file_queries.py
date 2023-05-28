
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.chains import RetrievalQA,RetrievalQAWithSourcesChain
from langchain.document_loaders import DirectoryLoader

import magic
import os
import nltk

loader = DirectoryLoader('training_set/', glob='*.txt')
documents = loader.load()

'''
Only for debugging
print(documents)
'''

# Split the text into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])

# Local in memory db
docsearch = Chroma.from_documents(texts, embeddings)

#qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch, top_k_docs_for_context=1)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever(search_kwargs={"k": 1}))

# This one works:
#query = "can you tell the summary of these docs?"

query = "how can someone generate new ideas?"
print(qa.run(query))
