import os
import json
import openai
from pathlib import Path

class OpenAICodeGenerator:
    """
    Classe para interagir com a API da OpenAI e gerar descrições e exemplos de uso
    das funções e propriedades do Flet a partir de arquivos Python extraídos.
    """
    def __init__(self, api_key: str, input_folder: str, output_folder: str):
        self.api_key = api_key
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(exist_ok=True, parents=True)
        openai.api_key = self.api_key

    def read_python_file(self, file_path: Path) -> str:
        """Lê o conteúdo de um arquivo Python."""
        with file_path.open("r", encoding="utf-8") as file:
            return file.read()

    def generate_code_description(self, code):
        """Gera uma descrição detalhada do código usando a API OpenAI"""
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em Python e Flet."},
                {"role": "user", "content": f"Descreva o seguinte código e explique suas funções e propriedades:\n{code}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    def generate_code_examples(self, code):
        """Gera exemplos adicionais do código"""
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em Python e Flet."},
                {"role": "user", "content": f"Crie exemplos adicionais para o seguinte código, destacando diferentes formas de uso:\n{code}"}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content

    def process_files(self):
        """Processa todos os arquivos Python na pasta de entrada."""
        for file_path in self.input_folder.glob("*.py"):
            print(f"Processando {file_path.name}...")
            code = self.read_python_file(file_path)
            description = self.generate_code_description(code)
            examples = self.generate_code_examples(code)
            output_data = {
                "file": file_path.name,
                "description": description,
                "examples": examples
            }
            output_file = self.output_folder / f"{file_path.stem}.json"
            with output_file.open("w", encoding="utf-8") as json_file:
                json.dump(output_data, json_file, indent=4, ensure_ascii=False)
            print(f"✅ Arquivo {output_file.name} salvo!")

if __name__ == "__main__":
    API_KEY = "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"  # Substitua pela sua chave da OpenAI
    INPUT_FOLDER = "__organized_code"
    OUTPUT_FOLDER = "__generated_json"
    
    generator = OpenAICodeGenerator(API_KEY, INPUT_FOLDER, OUTPUT_FOLDER)
    generator.process_files()
