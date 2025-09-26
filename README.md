# document-qa
document question answering using mxbai-embed-large and llm

## setup:
- `pip install -r requirements.txt`
- add enviroment variable `GOOGLE_API_KEY=<api_key>`
- paste your documents (any type) into the `./data` folder
- run `ollama pull mxbai-embed-large`
- run `python document_qa.py`
