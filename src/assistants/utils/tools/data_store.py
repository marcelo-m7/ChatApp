from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DocusaurusLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from utils.manager_tools import ManagerTools as mt
import pickle
import os


class DataStore:
    """	
    A class responsible for managing data storage and retrieval for the chat application.

    Attributes:
        WEB (str): Constant representing web-based data source.
        LOCAL (str): Constant representing local text-based data source.
        SITE_URL (str): URL of the website.
        site_datas_light (str): Path to light version of site data.
        site_datas (str): Path to full site data.
        LOCAL_PATH (str): Default local data path.
        docs_pickle_path (str): Path to pickle file for storing documents.
        origin (str): Data source origin.
    """
    WEB = "web"
    LOCAL = "text"
    PICKLE = "pickel"
    SITE_URL = "https://kobu.agency/"

    site_datas_light = 'assistant/knowledge/data_store_files/default/site_datas_light.txt'
    site_datas = 'assistant/knowledge/data_store_files/default/site_datas.txt'

    LOCAL_PATH = site_datas
    docs_pickle_path = "assistant/knowledge/data_store_files/default/docs.pickle"
    origin = LOCAL

    @classmethod
    def get_vector_store(cls, oringin_preference = PICKLE)  -> FAISS:
        """
        Retrieves documents from a pickle file and creates a vector store.

        Returns:
            FAISS: Vector store.
        """
        try:
            if oringin_preference == cls.PICKLE:
                vector_store = cls.get_doc_from_pickel()
                print("Vector Store sucessufly loaded")

            elif oringin_preference in [cls.WEB, cls.LOCAL]:
                    print("oringin_preference: ", oringin_preference)
                    vector_store = cls.create_db_critical(oringin_preference)
            else: 
                raise ValueError("Invalid origin")

        except Exception as e:
            print(f"DataStore - get_vector_store() Error: {e}")
            vector_store = cls.create_db_critical(cls.origin)

        finally:
            print("DataStore - Vector Store obtained:\n", vector_store)
            return vector_store

    @classmethod
    @mt.debugger_exception_decorator
    def get_doc_from_pickel(cls) -> FAISS:
        """
        Retrieves documents from a pickle file and creates a vector store.

        Returns:
            FAISS: Vector store.
        """
        print("Checking docs_pickle_path...")

        if os.path.exists(cls.docs_pickle_path):
            with open(cls.docs_pickle_path, 'rb') as f:
                docs = pickle.load(f)
            print("Doc pickel file load from: ", cls.docs_pickle_path)
        
        else: 
            docs = cls.prepare_doc_to_be_pickeled()
            docs = cls.pickle_handler(docs)

        print("Docs After Pickel: ", docs[2])
        embedding = OpenAIEmbeddings()
        vector_store = FAISS.from_documents(docs, embedding=embedding)

        return vector_store
   
    @classmethod
    @mt.debugger_exception_decorator
    def prepare_doc_to_be_pickeled(cls) -> list:
        """
        Prepares documents to be pickled.

        Returns:
            list: List of prepared documents.
        """
        if cls.origin == cls.WEB:
            loader = DocusaurusLoader(url=cls.SITE_URL)

        if cls.origin == cls.LOCAL:
            loader = TextLoader(file_path=cls.LOCAL_PATH, encoding='utf-8')

        docs = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=750, chunk_overlap=30)
        splitDocs = splitter.split_documents(docs)

        # print("prepare_doc_to_be_pickeled() - splitDocs:\n", splitDocs[2])
        print("prepare_doc_to_be_pickeled() - splitDocs SIZE: ", len(splitDocs))
        return splitDocs
        
    @classmethod
    @mt.debugger_exception_decorator
    def pickle_handler(cls, parameter: list) -> list:
        """
        Handles pickling of documents.

        Args:
            parameter (list): List of documents.

        Returns:
            list: List of documents.
        """

        # Check if the pickle file exists
        if not os.path.exists(cls.docs_pickle_path):
            # If the pickle file doesn't exist, create it with the parameter
            with open(cls.docs_pickle_path, 'wb') as f:
                pickle.dump(parameter, f)
                print(f"The pickle file '{cls.docs_pickle_path}' was successfully created.")
        else:
            print(f"The pickle file '{cls.docs_pickle_path}' already exists.")

        # Load the pickle file and return the variable
        with open(cls.docs_pickle_path, 'rb') as f:
            loaded_variable = pickle.load(f)
            print(f"Variable loaded from the pickle file: '{cls.docs_pickle_path}'")
            # print(f"Loaded variable: '{loaded_variable}'")
            # print(f"Loaded variable str: '{loaded_variable[2]}'")
        return loaded_variable
    
    @classmethod
    # @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
    def create_db_critical(cls, origin: str = WEB) -> FAISS:
        """
        Creates a vector store with extra context for critical mode.

        Args:
            origin (str): Data source origin. Defaults to LOCAL.

        Returns:
            FAISS: Vector store.
        """
        print("DataStore: create_db_critical() Starts: ", origin)
        
        def get_documents_from(origin=origin):
            if origin == cls.WEB:
                loader = DocusaurusLoader(
                    url=cls.SITE_URL,
                    # filter_urls=[
                    #     "https://kobu.agency/case-studies"
                    # ],
                # parsing_function=remove_nav_and_header_elements,
                )

            if origin == cls.LOCAL:
                file_path = cls.LOCAL_PATH # site_datas_light.txt or site_datas.txt (site inteiro)
                loader = TextLoader(file_path=file_path, encoding='utf-8')

            docs = loader.load()
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=550,
                chunk_overlap=30,            # separators = ['<p>', '<br>','</p>', '\n']
            )
            splitDocs = splitter.split_documents(docs)
            print("splitDocs", object)
            print("splitDocs", splitDocs[8])

            return splitDocs
        
        docs = get_documents_from(origin)
        embedding = OpenAIEmbeddings()
        print("openaiembeddings")
        vector_store = FAISS.from_documents(docs, embedding=embedding)
        # new = OpenAI
        return vector_store


