import os
from langchain_openai import OpenAIEmbeddings
from typing import List
from langchain_community.vectorstores.faiss import FAISS
from langchain.schema import Document
from dotenv import load_dotenv

load_dotenv("env")


class VectorStoreBuilder:
    """
    Classe para construir um vector store a partir de arquivos .py.
    """

    def __init__(self, code_folder: str, embedding_model: OpenAIEmbeddings):
        """
        Inicializa a classe.

        Parameters:
        - code_folder (str): Caminho para a pasta contendo arquivos .py.
        - embedding_model (OpenAIEmbeddings): Modelo de embeddings usado para vetorização.
        """
        self.code_folder = code_folder
        self.embedding_model = embedding_model

    def load_python_files(self) -> List[Document]:
        """
        Carrega e processa os arquivos Python.

        Returns:
        - List[Document]: Lista de objetos Document com código e metadados.
        """
        documents = []

        try:
            for filename in os.listdir(self.code_folder):
                if filename.endswith(".py"):
                    filepath = os.path.join(self.code_folder, filename)
                    
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Criar documento com metadados
                    doc = Document(
                        page_content=content,
                        metadata={"filename": filename, "filepath": filepath},
                    )
                    documents.append(doc)

            print(f"Carregados {len(documents)} arquivos Python.")
        except Exception as e:
            print(f"Erro ao carregar arquivos Python: {e}")

        return documents

    def build_vector_store(self) -> FAISS:
        """
        Constrói o vector store usando FAISS.

        Returns:
        - FAISS: O vetor de pesquisa construído.
        """
        try:
            documents = self.load_python_files()
            vector_store = FAISS.from_documents(documents, self.embedding_model)
            print("Vector store criado com sucesso!")
            return vector_store
        except Exception as e:
            print(f"Erro ao construir o vector store: {e}")
            return None


def get_vector_store(code_folder: str = "codigo_extraido") -> FAISS:
    """
    Função principal para criar o vector store.

    Parameters:
    - code_folder (str): Pasta contendo os arquivos Python.

    Returns:
    - FAISS: O vector store construído ou None se ocorrer um erro.
    """
    try:
        embedding = OpenAIEmbeddings()
        builder = VectorStoreBuilder(code_folder, embedding)
        vector_store = builder.build_vector_store()
        return vector_store
    except Exception as e:
        print(f"Erro na execução: {e}")
        return None


if __name__ == "__main__":
    path = '''src/assistants/data/knowledge/flet/__generated_python'''
    get_vector_store(path)
    print("Vector store criado com sucesso!")