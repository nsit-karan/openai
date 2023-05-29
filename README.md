# openai

**Description** : `openai, langchain, learnings and integrations`

## Good reference materials to follow

### Generic backgroud on ai/ml

* start with <https://developers.google.com/machine-learning/crash-course> as
  the first step (not yet gone through this). if this is done as the first step,
  all the diff terms (embeddings, vectors, vectordb, aimodel, etc) will go easier
  into the brain

### langchain

* langchain by harrison (founder) - look for recordings, videos by him
* go for <https://www.youtube.com/watch?v=EnT-ZTrcPrg> and other videos in this
  channel and try along

### summaries
* chain_type = stuff (consolidate stuff)
* chain_type = map_reduce (multiple smaller docs -> summarized into a single simple summary)

### embeddings

* start with <https://www.youtube.com/watch?v=5MaWmXwxFNQ> - best explanation
  of what embeddings is and the overall feel of what openai and langchain
  integration intuitively is trying to do

### vector databases

* vectordatabases - <https://www.youtube.com/watch?v=dN0lsF2cvm4> - concept explanation

## pre-requisites

Have the following modules in place

```bash
pip3 install langchain
pip3 install openai
pip3 install wolframalpha
pip3 install unstructured
pip3 install python-magic-bin
pip3 install chromadb
pip3 install tabulate
pip3 install pdf2image
```

## Env variables to be set:

```bash
export OPENAI_API_KEY="api-key"
export WOLFRAMA_ALPHA_APPID="app-api-key"
```
