from llama_index.llama_pack import download_llama_pack
import os
import pickle
from llama_index import download_loader
 
# Download VoyageQueryEnginePack
voyage_pack = download_llama_pack("VoyageQueryEnginePack", "./voyage_pack")
 
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
# GITHUB_TOKEN = "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"
if not GITHUB_TOKEN:
    raise EnvironmentError("GITHUB_TOKEN environment variable not set.")
 
# Download Github Repository Loader
download_loader("GithubRepositoryReader")
 
from llama_hub.github_repo import GithubClient, GithubRepositoryReader
 
# Setup Github Client with your token
github_client = GithubClient(GITHUB_TOKEN)
 
# Initialize GithubRepositoryReader with desired parameters
loader = GithubRepositoryReader(
    github_client,
    owner="jsocarras",
    repo="nextjstemplate",
    filter_directories=(["api", "ui"], GithubRepositoryReader.FilterType.INCLUDE),
    filter_file_extensions=([".ts", ".tsx", ".cs", ".mdx", ".js", ".html", ".css", ".vb", ".aspx", ".dll"], GithubRepositoryReader.FilterType.INCLUDE),
    verbose=True,
    concurrent_requests=10,
)
 
# Load documents from the main branch or a specific commit
docs = loader.load_data(branch="main")
# Alternatively, to load from a specific commit, use:
# docs = loader.load_data(commit_sha="a6c89159bf8e7086bea2f4305cff3f0a4102e370")
 
# Example usage with Llama Index
# Make sure to set OPENAI_API_KEY for using with Llama Index
OPENAI_API_KEY="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"
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY environment variable not set.")
 
# Save or load the documents for efficient reuse
docs_file_path = "docs.pkl"
if not os.path.exists(docs_file_path):
    with open(docs_file_path, "wb") as f:
        pickle.dump(docs, f)
else:
    with open(docs_file_path, "rb") as f:
        docs = pickle.load(f)
 
# Use the documents as needed, e.g., create an index, query, etc.
# This part is placeholder for integrating with Llama Index or other components
# index = VectorStoreIndex.from_documents(docs)
# query_engine = index.as_query_engine()
# response = query_engine.query("Explain each LlamaIndex class?")
# print(response)