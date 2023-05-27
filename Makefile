python-config:
	pip3 install langchain
	pip3 install openai
	pip3 install wolframalpha
	pip3 install unstructured
	pip3 install python-magic-bin
	pip3 install chromadb
	pip3 install tabulate
	pip3 install pdf2image

run-basics:
	python3 src/basic_langchain.py

run-file-queries:
	python3 src/file_queries.py
