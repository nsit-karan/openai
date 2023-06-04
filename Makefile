python-config:
	pip install langchain
	pip install openai
	pip install wolframalpha
	pip install unstructured
	pip install python-magic-bin
	pip install chromadb
	pip install tabulate
	pip install pdf2image
	pip install pinecone-client

run-basics:
	python src/basic_langchain.py

run-file-queries:
	python src/file_queries.py

run-pdf-queries:
	python src/pdf_reader.py
