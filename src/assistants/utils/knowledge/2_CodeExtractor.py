import os
import json

class CodeExtractor:
    def __init__(self, input_folder: str, output_folder: str):
        self.input_folder = input_folder
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def extract_and_save(self):
        for file_name in os.listdir(self.input_folder):
            if file_name.endswith(".json"):
                self.process_file(file_name)

    def process_file(self, file_name: str):
        input_path = os.path.join(self.input_folder, file_name)
        
        with open(input_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            
        if "code_snippets" in data:
            base_name = os.path.splitext(file_name)[0]  # Remove .json
            output_path = os.path.join(self.output_folder, f"{base_name}.py")
            
            with open(output_path, "w", encoding="utf-8") as py_file:
                for snippet in data["code_snippets"]:
                    py_file.write(snippet + "\n\n")
            
            print(f"✅ Código extraído para {output_path}")

if __name__ == "__main__":
    extractor = CodeExtractor("__extracted_code", "__organized_code")
    extractor.extract_and_save()
    print("🚀 Extração concluída!")
