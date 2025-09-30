from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
import os

# set up Ollama embedding and llm
Settings.embed_model = OllamaEmbedding(
     model_name="mxbai-embed-large:latest", base_url="http://localhost:11434"
)

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")  # replace with new key!
Settings.llm = Gemini(model="models/gemini-2.0-flash-exp")

try: # try to load existing index, create new one if it doesn't exist
#   storage_context = StorageContext.from_defaults(persist_dir="./storage")
    storage_context = StorageContext.from_defaults(persist_dir="./saved")
    index = load_index_from_storage(storage_context)
    print("loaded existing index")
except:
    print("creating new index...")
    documents = SimpleDirectoryReader("./data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./saved")
    print("index created and saved")

# query the index
query_engine = index.as_query_engine()
response = query_engine.query("can you explain ollama in one sentence?")
print(response)
# print("\n".join([node.node.text for node in response.source_nodes])) # to print context passed
