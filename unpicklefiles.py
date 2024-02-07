import os
import pickle
 
# Path to the pickle file
pickle_file_path = "/Users/joseph.socarras/nextjs/docs.pkl"
 
# Directory to save the documents
docs_dir = "./unpacked_docs"
if not os.path.exists(docs_dir):
    os.makedirs(docs_dir)
 
# Function to save a document to a file
def save_document(doc, index):
    # Derive the filename for each document
    file_path = os.path.join(docs_dir, f"doc_{index}.txt")
 
    # Assuming each document is a string; if not, convert or handle differently
    doc_content = doc if isinstance(doc, str) else str(doc)  # Adjust as needed based on the structure of 'doc'
 
    # Write the document content to a file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(doc_content)
 
# Load the documents from the pickle file
if os.path.exists(pickle_file_path):
    with open(pickle_file_path, "rb") as f:
        docs = pickle.load(f)
 
    # Iterate over the documents and save each one
    for i, doc in enumerate(docs):
        save_document(doc, i)
 
    print(f"Documents successfully unpacked to {docs_dir}")
else:
    print(f"File not found: {pickle_file_path}")