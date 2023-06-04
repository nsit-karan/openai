from langchain.document_loaders import UnstructuredPDFLoader, OnlinePDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma, Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import pinecone
import os

def index_pdf():
    loader = UnstructuredPDFLoader("../2015-field-guide-to-data-science.pdf")
    data = loader.load()
    
    print (f'You have {len(data)} documents in your data')
    print (f'There are {len(data[0].page_content)}  characters in your data')
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(data)
    
    print (f'Now you have {len(texts)} documents')

    return texts

def create_embeddings():
    texts = index_pdf()

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])

    pinecone.init(
        api_key=os.environ['PINECONE_API_KEY'],
        environment=os.environ['PINECONE_API_ENV']
    )
    index_name = "langchainpdf1"

    docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name=index_name)
    
def query_text():

    llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
    pinecone.init(
        api_key=os.environ['PINECONE_API_KEY'],
        environment=os.environ['PINECONE_API_ENV']
    )
    chain = load_qa_chain(llm, )

    index_name = "langchainpdf1"
    index = pinecone.Index(index_name)
    print(index.describe_index_stats())

    # Find the documents which match the query
    # Note : this returns the document chunks which were used to create the
    # embeddings
    docsearch = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    query = "What are examples of good data science teams?"
    docs = docsearch.similarity_search(query)

    print (f'Documents returned which matches were {len(docs)}')

    # Now return the ans that we are seeking
    # Use the docs from the previous steps (we zoomed in on the possible documents)
    # which should have the ans we are seeking
    query_result = chain.run(input_documents=docs, question=query)
    print(query_result)


'''
Run this only once to create indexes and embeddings for your document
This will also store the embeddings, indexes in pinecone which will be
used for querying data

create_embeddings()
'''

'''
This will leverage the embeddings to answer questons. We need to do the following:
- load the index from pinecone using the indexname and pinecone client
- find the documents which match the query by using the index instance from the previous step
- use the documents , the query and now feed this to OpenAI to get the needed ans
'''
query_text()