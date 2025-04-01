import os
import json
from langchain_openai import OpenAIEmbeddings
from typing import List
from langchain_community.vectorstores.faiss import VectorStore, Document, Embeddings, FAISS
from dotenv import load_dotenv
# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "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"
load_dotenv()


class VectorStoreBuilder:
    """
    A class to build a vector store from a folder containing JSON documents.
    """

    def __init__(self, json_folder: str, embedding: Embeddings):
        """
        Initialize the VectorStoreBuilder.

        Parameters:
        - json_folder (str): The path to the folder containing JSON documents.
        - embedding (Embeddings): The embedding model to use for vectorization.
        """
        self.json_folder = json_folder
        self.embedding = embedding
        
    def load_documents_with_no_metadatas(self) -> List[Document]:
        """
        Load documents from JSON files in the specified folder.

        Returns:
        - List[Document]: A list of Document objects representing the loaded documents.
        """
        try:
            documents = []
            for filename in os.listdir(self.json_folder):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.json_folder, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        print(f"File content of {filename}: loaded")

                        # Assume that 'content' field exists for now
                        content = str(data).strip('{').strip('}')
                        
                        if not content:
                            print(f"Warning: Skipping document without content in file {filename}")
                            continue

                        # Use filename as title if title is not present in the JSON
                        title = data.get('title', filename).strip()
                        # Assume metadata exists or create an empty dictionary
                        # metadata = data.get('metadata', {})
                        metadata = {"filename" : filename}
                        # Create a document
                        document = Document(title=title, page_content=content, metadata=metadata)
                        documents.append(document)

                if not documents:
                    print("load_documents_with_no_metadatas - No documents loaded.")
                else:
                    print("load_documents_with_no_metadatas - Documents loaded.")

                return documents
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []
    
    def load_documents(self) -> List[Document]:
        """
        Load documents from JSON files in the specified folder.

        Returns:
        - List[Document]: A list of Document objects representing the loaded documents.
        """
        try:
            documents = []
            for filename in os.listdir(self.json_folder):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.json_folder, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        title = data.get('title', '')
                        content = data.get('content', '')
                        metadata = data.get('metadata', {})
                        # Add metadata to the content
                        content_with_metadata = f"Title: {title}\nMetadata: {metadata}\n Page Content: {content}"
                        documents.append(Document(title=title, page_content=content_with_metadata, metadata=metadata))
            
            # Print examples of loaded documents for verification
            # print("Loaded documents[0]:\n", documents[0], documents[8], documents[15])
            print("\nLoaded documents[15]:\n", documents[15])
            return documents
        
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []
    
    
    def load_any_documents(self) -> List[Document]:
        """
        Load documents from JSON files in the specified folder.

        Returns:
        - List[Document]: A list of Document objects representing the loaded documents.
        """
        try:
            documents = []
            for filename in os.listdir(self.json_folder):
                # if filename.endswith('.json'):
                    filepath = os.path.join(self.json_folder, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        title = filename
                        content = data #.get('content', '')
                        metadata = title #data.get('metadata', {})
                        # Add metadata to the content
                        content_with_metadata = f"Title: {title}\nMetadata: {metadata}\n Page Content: {content}"
                        documents.append(Document(title=title, page_content=content_with_metadata, metadata=metadata))
            
            # Print examples of loaded documents for verification
            # print("Loaded documents[0]:\n", documents[0], documents[8], documents[15])
            print("\nLoaded documents[15]:\n", documents[15])
            return documents
        
        except Exception as e:
            print(f"Error loading documents: {e}")
            return []
    
    def build_vector_store(self, documents) -> VectorStore:
        """
        Build a vector store from loaded documents using FAISS.

        Returns:
        - VectorStore: The built vector store.
        """
        try:
            # metadatas = [d.metadata for d in documents]
            vector_store = FAISS.from_documents(documents, self.embedding)
            # vector_store = FAISS.from_documents(documents, embedding=self.embedding, metadatas)
            return vector_store
        except Exception as e:
            print(f"Error building vector store: {e}")
            return None


def get_vector_store(
        json_folder='Tools/web_scraper_files',
        metadatas=True):
    """
    Main function to get the vector store.

    Parameters:
    - json_folder (str, optional): The folder containing JSON files to be used for building the vector store.
      Defaults to 'assistant/knowledge/data_store_files/web_scraper_files'.

    Returns:
    - vector_store: The constructed vector store object or None if an error occurred.
    """
    try:
        # Initialize the embedding model
        embedding = OpenAIEmbeddings()

        # Build the vector store
        builder = VectorStoreBuilder(json_folder, embedding)

        if metadatas == False:
            print("        if metadatas == False:")
            documents = builder.load_documents_with_no_metadatas()
        else:
            documents = builder.load_documents()
            
        vector_store = builder.build_vector_store(documents)

        # Check if the vector store was built successfully
        if vector_store is not None:
            print("Vector store built successfully!")
        else:
            print("Error building the vector store.")
    except Exception as e:
        print(f"Error during program execution: {e}")
    finally:
        print("Program completed.")
        return vector_store

def get_document_store(
        json_folder='Tools/web_scraper_files',
        metadatas=True):
    """
    Main function to get the document store.

    Parameters:
    - json_folder (str, optional): The folder containing JSON files to be used for building the document store.
      Defaults to 'assistant/knowledge/data_store_files/web_scraper_files'.

    Returns:
    - document_store: The constructed document store object or None if an error occurred.
    """
    try:
        # Initialize the embedding model
        embedding = OpenAIEmbeddings()

        # Build the document store
        builder = VectorStoreBuilder(json_folder, embedding)

        if metadatas == False:
            documents = builder.load_documents_with_no_metadatas()
        else:
            documents = builder.load_documents()

        document_store = builder.build_vector_store(documents)

        # Check if the document store was built successfully
        if document_store is not None:
            print("document store built successfully!")
        else:
            print("Error building the document store.")
    except Exception as e:
        print(f"Error during program execution: {e}")
    finally:
        print("Program completed.")
        return document_store

if __name__ == "__main__":
    get_vector_store()
