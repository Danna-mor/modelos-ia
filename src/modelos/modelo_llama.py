#ollama pull llama3.2:1b
from langchain_ollama import ChatOllama

class ModeloLlama:
    def __init__(self):
            self.modelo= ChatOllama(model="llama3.2:1b",temperature=0.1)
    
    def generar_respuesta(self, prompt):
        respuesta = self.modelo.invoke(prompt)
        return respuesta.text