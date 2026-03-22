from textual.app import App
from textual.widgets import Header, Footer, Static
from textual.reactive import reactive
from rich.progress import Progress, SpinnerColumn, BarColumn
import requests

API_URL = "http://127.0.0.1:8000/query"

class Painel(App):
    prompt = reactive("")

    def compose(self):
        yield Header()
        yield Static("[bold red]Painel BlackMage ativo 🩸[/bold red]")
        yield Footer()

    def on_key(self, event):
        if event.key == "q":
            self.exit()
        elif event.key == "t":
            self.prompt = input("Digite prompt: ")
            try:
                with Progress(SpinnerColumn(), BarColumn(), transient=True) as progress:
                    task = progress.add_task("[red]Processando prompt...", total=100)
                    for i in range(100):
                        progress.update(task, advance=1)
                r = requests.post(API_URL, json={"prompt": self.prompt})
                print(f"Resposta: {r.json()['resposta']}")
            except Exception as e:
                print(f"[Erro ao acessar API] {e}")

if __name__ == "__main__":
    Painel().run()
