#!/usr/bin/env python3
import sys, subprocess, textwrap
from openai import OpenAI
import httpx

def run_local(prompt: str):
    # Uses your existing local model
    subprocess.run(["ollama", "run", "executive"], input=prompt, text=True)

def run_cloud(prompt: str):
    # Force HTTP/1.1 (your environment needed this)
    client = OpenAI(http_client=httpx.Client(http2=False))
    resp = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    print(resp.output_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: agent.py local|cloud  \"your prompt\"")
        sys.exit(1)

    mode = sys.argv[1].lower()
    prompt = " ".join(sys.argv[2:]).strip()

    if not prompt:
        print("Provide a prompt.")
        sys.exit(1)

    if mode == "local":
        run_local(prompt)
    elif mode == "cloud":
        run_cloud(prompt)
    else:
        print("Mode must be: local or cloud")
        sys.exit(1)

if __name__ == "__main__":
    main()

