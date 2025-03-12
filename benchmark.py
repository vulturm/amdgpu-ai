import time
import requests
import json

def measure_tokens_per_second(model: str, prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True  # Enable streaming for incremental JSON response
    }

    start_time = time.time()
    total_tokens = 0

    with requests.post(url, json=payload, stream=True) as response:
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            return

        for line in response.iter_lines():
#            print(line)
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))  # Correct JSON decoding
                    total_tokens += data.get("eval_count", 0)
                except json.JSONDecodeError:
                    print("Warning: Failed to decode JSON chunk")

    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time > 0:
        tokens_per_second = total_tokens / elapsed_time
    else:
        tokens_per_second = 0

    print(f"Generated {total_tokens} tokens in {elapsed_time:.2f} seconds.")
    print(f"Tokens per second: {tokens_per_second:.2f}")

if __name__ == "__main__":
    model_name = "deepseek-coder-v2:16b-lite-base-q4_0"
    prompt_text = "write a bash script that calculates size of files in a folder"
    measure_tokens_per_second(model_name, prompt_text)

