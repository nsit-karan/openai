python-config:
	pip3 install langchain
	pip3 install openai

run-basics: python-config
	python3 src/basic_langchain.py
