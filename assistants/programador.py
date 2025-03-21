from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(".env")

class Programador:
    CLIENT = OpenAI()
    TEMPERATURE = 0.7
    MODEL = "gpt-3.5-turbo"
    # VECTOR_STORE = None
    def get_response(self, input, conversation_history) -> str:
        print("Programador: get_response()")

        try:
            completion = self.CLIENT.chat.completions.create(
                model=self.MODEL, # This model is better for extractions
                # response_format={"type": "json_object"},
                temperature=self.TEMPERATURE,
                messages=[
                    {'role': 'system', 'content': 'Você é um programador sênior especialista em Flet, OpenAI integrations, Python e LangChain'},
                    {'role': 'system', 'content': 'Você é bem descontraído em suas e piadista. Também sarcástico com suas respostas.'},
                    {'role': 'system', 'content': 'Responda às questões do usuário com um especilista técnico.  arguments'},
                    {'role': 'system', 'content': 'Dê respostas técnicas, estruturadas e detalhadas, preferindo manter as boas práticas de programação.'},
                    {'role': 'system', 'content': 'Prevaleça nas respostas para produção de código os princípios SOLID.'},
                    {'role': 'system', 'content': f'Histórico de conversação:\n {conversation_history}'},
                    {'role': 'user', 'content': f'{input}'}],
                # tools=functions_descriptions,
                # tool_choice=tool_choice)
            )
            print("Programador: get_response(): \n", completion)
            response = completion.choices[0].message.content

        except Exception as e:
            print(f"Programador: get_response() Error {e}")
            response = "I'm not feeling ok... Would you mind if we talk another time?"

        finally:
            return response

if __name__ == "__main__":
    programador = Programador()
    response = programador.get_response("Hello", conversation_history=[])
    print(response)