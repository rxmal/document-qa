# document-qa
document question answering using mxbai-embed-large and llm (Retrieval-Augmented Generation)

## setup:
```bash
pip install -r requirements.txt
```
```bash
export GOOGLE_API_KEY=<api_key> #set env variable
```
```bash 
ollama pull mxbai-embed-large #pull embedding model
```
```bash
python document_qa.py
```

## usage:

> ***question:*** can you explain ollama in one sentence?

> ***answer:*** Ollama enables you to locally operate open-source large language models on your hardware, ensuring a secure and customizable environment for various AI tasks, and simplifying the setup and interaction with these models.

> ***context:*** *ollama is used to run open-source large language models (llms) locally on your own hardware, providing a secure, private, and customizable environment for AI-powered tasks like coding assistance, content generation, research, and building local chatbots. It simplifies the complex process of setting up and interacting with these powerful models, making them accessible to developers, researchers, and businesses without relying on cloud-based services.*
