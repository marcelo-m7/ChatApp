import json
import os
import re

class JSONToPythonConverter:
    def __init__(self, json_folder: str, output_folder: str):
        """
        Inicializa o conversor de JSON para Python.

        Parameters:
        - json_folder (str): Pasta contendo os arquivos JSON.
        - output_folder (str): Pasta onde os arquivos .py serão salvos.
        """
        self.json_folder = json_folder
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def extract_code_blocks(self, text: str):
        """
        Extrai blocos de código Python de um texto.

        Returns:
        - List[str]: Lista de trechos de código encontrados.
        """
        # Captura blocos de código dentro de ```python e ``` (evita capturar texto extra)
        code_blocks = re.findall(r"```python\n(.*?)\n```", text, re.DOTALL)
        return [block.strip() for block in code_blocks if block.strip()]

    def sanitize_filename(self, filename: str):
        """
        Gera um nome de arquivo seguro a partir do nome do JSON.

        Returns:
        - str: Nome de arquivo seguro.
        """
        return re.sub(r"[^\w\-]", "_", filename).replace(".json", ".py")

    def process_json_files(self):
        """
        Processa os arquivos JSON na pasta especificada e cria arquivos .py formatados.
        """
        for file_name in os.listdir(self.json_folder):
            if file_name.endswith(".json"):
                json_path = os.path.join(self.json_folder, file_name)
                with open(json_path, "r", encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    self.create_python_file(data, file_name)

    def create_python_file(self, data: dict, json_filename: str):
        """
        Cria um arquivo .py a partir dos blocos de código extraídos.

        Parameters:
        - data (dict): Dados extraídos do JSON.
        - json_filename (str): Nome do arquivo JSON original.
        """
        file_name = self.sanitize_filename(json_filename)
        file_name = str(file_name)
        file_name = f"{file_name}.py"
        output_path = os.path.join(self.output_folder, file_name, )

        # Extrai e formata o código
        code_blocks = self.extract_code_blocks(data.get("description", "") + "\n" + data.get("examples", ""))
        formatted_code = "\n\n".join(sorted(set(code_blocks)))  # Remove duplicados e mantém a formatação

        if formatted_code:
            with open(output_path, "w", encoding="utf-8") as py_file:
                py_file.write(formatted_code + "\n")
            print(f"Arquivo gerado: {output_path}")
        else:
            print(f"Aviso: Nenhum código válido encontrado em {json_filename}")


# Exemplo de uso
if __name__ == "__main__":
    input_folder = "src/assistants/data/knowledge/flet/__generated_json"  # Pasta onde os arquivos JSON estão armazenados
    output_folder = "src/assistants/data/knowledge/flet/__generated_python"  # Pasta onde os arquivos .py serão salvos
    converter = JSONToPythonConverter(json_folder=input_folder, output_folder=output_folder)
    converter.process_json_files()
    print("Conversão concluída!")
