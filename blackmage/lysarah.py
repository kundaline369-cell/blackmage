from rich.console import Console
from rich.prompt import Prompt
import requests
import os

console = Console()

def introducao():
    console.print("[bold red]🩸 BlackMage ativo[/bold red]")

def menu():
    while True:
        console.print("\n1. Testar API\n2. Abrir painel web\n3. Sair")
        op = Prompt.ask("Escolha", choices=["1","2","3"])

        if op == "1":
            try:
                r = requests.post("http://127.0.0.1:8000/query", json={"prompt":"teste"})
                console.print(r.json()["resposta"])
            except Exception as e:
                console.print(f"[red]Erro: {e}[/red]")

        elif op == "2":
            console.print("Abra no navegador: http://127.0.0.1:8000")

        elif op == "3":
            break

if __name__ == "__main__":
    introducao()
    menu()
