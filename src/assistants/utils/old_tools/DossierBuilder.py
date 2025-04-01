import json
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_openai import ChatOpenAI
from VectorStoreBuilder import get_vector_store


class DossierBuilder:
    def __init__(self, dossier_structure_path, vector_store, llm_retriever, output_path) -> None:
        self.vector_store = vector_store
        self.llm_retriever = llm_retriever
        self.dossier_structure_path = dossier_structure_path
        self.output_path = output_path

    def main(self):
        for key, value in self.iterate_json_file(self.dossier_structure_path):
            print(key, value)
            chapter_outline = {key: value}
            response = self.chapter_writer(chapter_outline)
            self.save_dossier_chapter(response, key)
            print(response)

    def iterate_json_file(self, json_file):
        """
        Iterates over the key-value pairs of each element in a JSON file.

        Args:
            json_file (str): The path to the JSON file.

        Yields:
            tuple: A tuple containing the key-value pairs of each element.
        """
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for element in data:
                yield element, data[element]

    def chapter_writer(self, chapter_outline: dict) -> dict:
        """Writes a chapter based on the chapter outines, using as resource the class Vector Store."""
        print("chapter_writer starts")

        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a professional writer."),
                ("system", """Based on the resources received bellow, write a entire chapter for a company dossier.
                  Try to organize chapter titles following this structure: {input}"""),
                ("human", "Resources: {context}"),
            ])

            chain = create_stuff_documents_chain(
                llm=self.llm_retriever,
                prompt=prompt
            )

            retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})

            retriever_prompt = ChatPromptTemplate.from_messages([
                ("system",
                 "Given the above information required, generate a search query to look up in order to get information relevant to the conversation"),
                ("system", "Information required: {input}"),
            ])

            history_aware_retriever = create_history_aware_retriever(
                llm=self.llm_retriever,
                retriever=retriever,
                prompt=retriever_prompt
            )
            # print("History_aware_retriever:\n", history_aware_retriever.invoke({"input": str(chapter).strip('{').strip('}')}))
            retrieval_chain = create_retrieval_chain(
                # retriever,
                history_aware_retriever,
                chain
            )

            response = retrieval_chain.invoke({"input": str(chapter_outline).strip('{').strip('}')})
            return response

        except Exception as e:
            print(f"chapter_writer Error {e}")
            return False

    def save_dossier_chapter(self, response: dict, file_name) -> None:
        """
        Extracts the 'answer' and metadata from the response and saves them to a JSON file.
        Args:
            response (dict): The response dictionary containing the 'answer' and 'context'.
        """
        answer = response.get('answer', 'Answer not found')
        metadatas = [doc.metadata for doc in response.get('context', [])]
        data = {
            'answer': answer,
            'metadatas': metadatas
        }

        with open(f'{self.output_path}/{file_name}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


def start_dossier_builder(dossier_structure_path=None, 
                          vector_store=None, 
                          llm_retriever=None,
                          output_path='Tools/dossier_chapters_files') -> None:
    """
    Initialize and run the dossier builder with optional parameters.

    Parameters:
    - dossier_structure_path (str): The path to the dossier structure JSON file.
    - vector_store (object): The vector store object.
    - llm_retriever (object): The language model retriever object.
    - output_path (str): The folder path to save the dossier chapters.
    """
    dossier_structure_path = dossier_structure_path or 'Tools/dossier_structure.json'
    vector_store = vector_store or get_vector_store()
    llm_retriever = llm_retriever or ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")

    try:
        dossier = DossierBuilder(
            dossier_structure_path=dossier_structure_path,
            vector_store=vector_store,
            llm_retriever=llm_retriever,
            output_path=output_path
        )
        dossier.main()
        print("Dossier building completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"The path '{output_path}' has not been changed.")


if __name__ == "__main__":
    # start_dossier_builder()
    vector_store = get_vector_store(json_folder="C:/Users/marce/OneDrive - Universidade do Algarve/Vida Pessoal e Estágio/Estágio Kobu Agency/GitHub/kobu-ai-assistant-v3.0/backend")
    start_dossier_builder(dossier_structure_path='Relatório/dossier_structure.json', output_path='Relatório')
    