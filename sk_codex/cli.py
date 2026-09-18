import sys
import json
import urllib.request
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def query_ollama(prompt: str, model: str = "llama3:latest") -> str:
    url = "http://localhost:11434/api/generate"
    data = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res.get("response", "No response.")
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

def main():
    console.print("[bold purple]⚡ sk-codex (Offline AI Coding Assistant)[/bold purple]")
    console.print("Type your coding request below (or 'exit' to quit):\n")
    while True:
        try:
            user_input = input("sk-codex> ")
            if user_input.strip().lower() in ("exit", "quit"):
                break
            if not user_input.strip():
                continue
            console.print("[dim]Thinking...[/dim]")
            response = query_ollama(user_input)
            console.print(Markdown(response))
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
