import json
import asyncio
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from .manager_tools import *
from ..knowledge import Prompts


class Utils(Prompts):
    """
    Utility functions for handling chat history, saving lead data, and invoking chat chains.
    """
    buffer_saver_file_path = 'assistant/buffer/buffer.json'
    exported_lead_datas = 'assistant/buffer/lead_datas.json'

    def set_user_attributes(self, response: dict) -> None:
        """
        Set user attributes based on response.
        
        Args:
            response (dict): Response containing attribute-value pairs.
        """
        for key, valor in response.items():
            if hasattr(self, key) and valor not in (None, '', []):
                setattr(self, key, valor)

    async def chat_buffer(self, user_input: str = None, response: str = None, system_message: str = None) -> None:
        """
        Store site history in a list self.chat_history.
        
        Args:
            user_input (str): User input message.
            response (str): Assistant response message.
            system_message (str): System message.
        """

        try: 
            
            if user_input != None and response == None:
                self.chat_history.append(HumanMessage(content=user_input))

            if response != None:
                self.chat_history.append(AIMessage(content=response))
                self.chat_history.append(SystemMessage(content=f"Awnswered at: {datetime.now()}"))

            if system_message != None:
                # self.chat_history.append(HumanMessage(content='user_input'))
                self.chat_history.append(SystemMessage(content=f"{system_message}\nSystem Message set at: {datetime.now()}"))
                
            # print("actual chathistory", self.chat_history)

            print("chat_buffer Buffer saved in self.chat_history list")

        except Exception as e:
            print(f"chat_buffer Error {e}")
    
    async def chat_buffer_saver(self, user_input: str, response: str) -> None:
        """
        Save the chat history in a JSON file.
        
        Args:
            user_input (str): User input message.
            response (str): Assistant response message.
        """

        messages_history = []

        messages_history.append({'role': 'user', 'content': user_input})
        messages_history.append({'role': 'assistant', 'content': response})
        messages_history.append({'role': 'system', 'content': datetime.now()})


        try:
            try:
                with open(self.buffer_saver_file_path, 'r', encoding='utf-8') as existing_json_file:
                    existing_data = json.load(existing_json_file)
            except FileNotFoundError:
                existing_data = []

            existing_data.extend(messages_history)

            with open(self.buffer_saver_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(existing_data, json_file, ensure_ascii=False, indent=2)

            print(f'chat_history saved in {self.buffer_saver_file_path}')

        except Exception as e:
            print(f"chat_buffer_saver Error {e}")

    @retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
    def chain_invoker(self, chain, user_input: str = '', extra_context = '') -> str:
        """
        Invoke the main chain and return the assistant response.
        
        Args:
            chain: Main chat chain.
            user_input (str): User input message.
        
        Returns:
            str: Assistant response.
        """
        try:
            if self.extra_context:
                print("Extra context added to the chain to be invoked: ", self.extra_context, self.vector_store)
            response = chain.invoke({
                "input": user_input, 
                "chat_history": self.chat_history, 
                "subject_instructions": self.subject_instructions,
                "basic_instructions": self.basic_instructions, 
                "lead_string": str(self.lead).strip('{').strip('}').strip(']').strip(']'),
                "data_required": self.data_required})
                # "context": self.vector_store if self.extra_context else extra_context})
            
            print("chain_invoker(): The chain has been invoked.")
            # print("Response:\n", response)

            if type(response) == dict:
                message = response['answer']
            else:
                message = response.content

        except AttributeError as e:
            if "'list' object has no attribute 'content'" in str(e):
                print(f"chain_invoker Error: {e}")
                message = response

            else:
                raise

        except Exception as e:
            if user_input == '':
                print(f"chain_invoker Error {e}")
                message = "I'm not feeling ok... Would you mind if we talk another time?"
            
            else:    
                print(f"chain_invoker Error {e}")
                print(f"It will responde with basic parameterse. User input to be answered: {user_input}, ")
                # To future integration of error actions
                message = {'orientation': self.CRITICAL, 'user_input': user_input}
                
        finally:
            return message

    async def chain_builder(self, stage: str = '') -> object:
        """
        Build the main chain that will answer the user_input.
        
        Args:
            stage (str): Stage of the conversation.
        
        Returns:
            object: Main chat chain.
        """
        print("chain_builder starts")

        try:
            # prompt = await asyncio.create_task(self.prompt_chooser(stage=stage))
            prompt = await asyncio.create_task(self.prompt_chooser(stage=stage))

            if self.extra_context == False:
                chain = prompt | self.llm_conversation
                return chain
        
            elif self.extra_context == True:          # Add a retriever to the chain with the extra context obtained
                print("self.extra_context == True")
                
                chain = create_stuff_documents_chain(
                    llm=self.llm_retriver,
                    prompt=prompt
                )

                retriever = self.vector_store.as_retriever(search_kwargs={"k": self.search_kwargs})
                    
                retriever_prompt = ChatPromptTemplate.from_messages([
                    # MessagesPlaceholder(variable_name="chat_history"),
                    ("human", """Given the above conversation, generate a search query to look up 
                     in order to get information relevant to the conversation"""),
                    ("system", "Messages History: {chat_history}"),
                    ("human", "{input}")
                ])

                history_aware_retriever = create_history_aware_retriever(
                    llm=self.llm_retriver,
                    retriever=retriever,
                    prompt=retriever_prompt
                )

                # history_aware_retriever_response = self.chain_invoker(history_aware_retriever) # Verify context added
                # print("History_aware_retriever:\n", history_aware_retriever_response)

                retrieval_chain = create_retrieval_chain(
                    # retriever,
                    history_aware_retriever,
                    chain
                )

                return retrieval_chain

        except Exception as e:
            print(f"chain_builder Error {e}")
            return False
   
    @ManagerTools.debugger_exception_decorator
    def debugger_print(*args):
        """
        Print debugging information.
        
        Args:
            *args: Variable number of arguments to print.
        """
        message = ' '.join(map(str, args))
        print(message)

