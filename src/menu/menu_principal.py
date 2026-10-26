from src.modelos.modelo_google import ModeloGoogle
from src.modelos.modelo_groq import ModeloGroq 
from src.modelos.modelo_local import ModeloLocal 
from src.modelos.modelo_llama import ModeloLlama
from src.modelos.prompt_01 import Prompt01
from src.modelos.prompt_02 import Prompt02

#pip install rich
import os
from rich.console import Console
from rich.markdown import Markdown

class MenuPrincipal():
    def __init__(self):
        self.console = Console()
        self.opcion= 0

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresiona Enter para volver al menu...")

    def mostrar_menu(self):
        print("===MENU PRINCIPAL===")
        print("1.Modelo google API KEY")
        print("2.Modelo groq API KEY")
        print("3.Modelo local (Ollama)")
        print("4.Modelo llama.cpp")
        print("5.Prompt Basico")
        print("6.Prompt Template")
        print("0.Salir")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion=input("Seleccione una opcion: ")

            if self.opcion=="1":
                modelo_google=ModeloGoogle()
                prompt=input("Ingrese su prompt: ")
                respuesta=modelo_google.generar_respuesta(prompt)
                print("Respuesta del modelo Google:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))
                
            elif self.opcion=="2":
                modelo_groq=ModeloGroq()
                prompt=input("Ingrese su prompt: ")
                respuesta=modelo_groq.generar_respuesta(prompt)
                print("Respuesta del modelo Groq:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion=="3":
                modelo_local=ModeloLocal()
                prompt=input("Ingrese su prompt: ")
                respuesta=modelo_local.generar_respuesta(prompt)
                print("Respuesta del modelo Local:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion=="4":
                modelo_llama=ModeloLlama()
                prompt=input("Ingrese su prompt: ")
                respuesta=modelo_llama.generar_respuesta(prompt)
                print("Respuesta del modelo Llama.cpp:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion=="5":
                prompt_01=Prompt01()
                respuesta=prompt_01.generar_respuesta()
                print("Respuesta del Prompt Basico:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion=="6":
                prompt_02=Prompt02()
                respuesta=prompt_02.generar_respuesta()
                print("Respuesta del Prompt Template:")
                #print(respuesta)
                self.console.print(Markdown(respuesta))

            elif self.opcion=="0":
                print("Saliendo del programa...")
                break
            else:
                print("Opcion invalida. Por favor seleccione una opcion valida")

            self.pausar()