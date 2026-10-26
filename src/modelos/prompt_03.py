from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

class Prompt03:
    def __init__(self):
            self.modelo= ChatOllama(model="qwen2.5:3b",temperature=0.1)
    
    def generar_respuesta(self):
        prompt_template = PromptTemplate.from_messages([
             "system",
             """
                Eres un profesor 
            """
        ])
        
        print("Prompt generado:", prompt)
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text