
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_openai import ChatOpenAI
from VectorStoreBuilder import get_vector_store
import json
from dotenv import load_dotenv
load_dotenv()


class VectorStoreQueryResearcher:

    def __init__(self, vector_store, llm_retriever, search_kwargs=3) -> None:
        self.vector_store = vector_store # or get_vector_store()
        self.llm_retriever = llm_retriever or ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")
        self.output_path = 'Buffer/VectorStoreQueryResearcherBuffer.json'
        self.conversation_history = []
        self.search_kwargs = search_kwargs

    def main(self, input):
        """
        Manages traffic responses to messages sent and received. 
        It also executes the buffer save methods.
        """

        # self.save_dossier_chapter(response, key)
        print(input)
        print("VectorStoreQueryResearcher - main() Starts")

        try:
            self.conversation_buffer(user_input=input)
            response = self.get_responde_by_researcher(input)

            if type(response) == dict:
                message = response['answer']
                # context = response['context']
            else:
                message = response.content

            self.conversation_buffer(response=message)

        except Exception as e:
            response = {"message": "I'm not feeling ok... Would you mind if we talk another time?",
                        'orientation': '', 'current_stage': 'error'}
            print(f"Chat: main() Error {e}")

        # return response # {"answer": message}, "filename": response['filename'], "metadata": response['metadata']}
        return {"message": message, "context": self.extract_metadata_and_filename(response)}
  
    def extract_metadata_and_filename(self, input_dict):
        """Needs correction, still doesn't search all filenames from all docs."""
        output_dict = {}

        if 'context' in input_dict and input_dict['context']:
            document = input_dict['context'][0]

            filename = document.metadata.get('filename', 'Unknown')
            metadatas = document.metadata

            output_dict['filename'] = filename
            output_dict['metadatas'] = metadatas

        return output_dict
    
    def get_responde_by_researcher(self, input) -> dict:
        """Writes a chapter based on the chapter outines, using as resource the class Vector Store."""
        print("get_responde_by_researcher starts")

        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", "Conversation history: \n {conversation_history}"),
                ("system", """Based on the resources received answer the user input."""),
                ("system", "Resources:\n {context}"),
                ("human", "User input: {input}"),
            ])

            chain = create_stuff_documents_chain(
                llm=self.llm_retriever,
                prompt=prompt
            )

            retriever = self.vector_store.as_retriever(search_kwargs={"k": self.search_kwargs})

            retriever_prompt = ChatPromptTemplate.from_messages([
                ("system", "Conversation history: \n {conversation_history}"),
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

            response = retrieval_chain.invoke({"input": input,
                                               "conversation_history": self.conversation_history,
                                              })
            return response
        except Exception as e:
            print(f"get_responde_by_researcher Error {e}")
            return False

    def conversation_buffer(self, user_input: str = None, response: str = None, system_message: str = None) -> None:
        """
        Store site history in a list self.conversation_history.
        
        Args:
            user_input (str): User input message.
            response (str): Assistant response message.
            system_message (str): System message.
        """

        try: 
            
            if user_input != None and response == None:
                self.conversation_history.append(HumanMessage(content=user_input))

            if response != None:
                self.conversation_history.append(AIMessage(content=response))
                self.conversation_history.append(SystemMessage(content=f"Awnswered at: {datetime.now()}"))

            if system_message != None:
                # self.conversation_history.append(HumanMessage(content='user_input'))
                self.conversation_history.append(SystemMessage(content=f"{system_message}\nSystem Message set at: {datetime.now()}"))
                
            print("conversation_buffer Buffer saved in self.conversation_history list")

        except Exception as e:
            print(f"conversation_buffer Error {e}")

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


def start_conversation():
    vector_store = get_vector_store(
         json_folder='Tools/dossier_chapters_files',
         metadatas=False)
    llm_retriever = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")
    assistant = VectorStoreQueryResearcher(llm_retriever=llm_retriever, vector_store=vector_store)

    while True:
        user_input = input("User: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        else:
            response = assistant.main(user_input)
            print("Assistant:", response)


if __name__ == "__main__":
    start_conversation()