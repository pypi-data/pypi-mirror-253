#!/usr/bin/env python
import argparse
import json
import os
import tiktoken
import psutil
from pathlib import Path
from openai import OpenAI


def main():
    args = parse_arguments()

    # Load the config from the environment
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("CHATGPT_CLI_MODEL", "gpt-4-turbo-preview")
    timeout = int(os.getenv("CHATGPT_CLI_REQUEST_TIMEOUT_SECS", 12000))

    # Get the prompt from the user
    prompt = " ".join(args.prompt)

    # Get the boot time of the system
    boot_time_since_unix_epoch = int(psutil.boot_time())

    # Load the chatlog for this terminal window
    home_dir = Path.home()
    chatlog_path = (
        home_dir
        / ".chatgpt"
        / str(boot_time_since_unix_epoch)
        / str(os.getppid())
        / "chatlog.json"
    )
    chatlog_path.parent.mkdir(parents=True, exist_ok=True)

    if chatlog_path.exists():
        with open(chatlog_path, "r") as file:
            chatlog_text = file.read()
    else:
        chatlog_text = ""

    # Get the messages from the chatlog, limit the total number of tokens
    log = get_messages_from_chatlog(chatlog_text, 128000)

    messages = [{"role": l["role"], "content": l["content"]} for l in log]
    messages.append({"role": "user", "content": prompt})

    # Send the POST request to OpenAI
    data = {
        "model": model,
        "messages": messages,
    }

    answer, prompt_tokens, answer_tokens = send_request_to_openai(
        model, api_key, messages, timeout
    )

    # Save the new messages to the chatlog
    log += [
        {"role": "user", "content": prompt, "tokens": prompt_tokens},
        {"role": "assistant", "content": answer, "tokens": answer_tokens},
    ]

    # Write the chatlog to disk
    with open(chatlog_path, "w") as file:
        json.dump(log, file, indent=4)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", nargs="+", help="The prompt to send to ChatGPT")
    return parser.parse_args()


def get_messages_from_chatlog(chatlog_text, max_tokens):
    total_tokens = 0
    messages = []
    if chatlog_text:
        chatlog = json.loads(chatlog_text)
        for log in reversed(chatlog):
            if total_tokens + log["tokens"] > max_tokens:
                break
            total_tokens += log["tokens"]
            messages.insert(0, log)
    return messages


def send_request_to_openai(model, api_key, messages, timeout):
    client = OpenAI(api_key=api_key)

    stream = client.chat.completions.create(
        model=model, messages=messages, stream=True, timeout=timeout
    )

    # To get the tokeniser corresponding to a specific model in the OpenAI API:
    enc = tiktoken.encoding_for_model(model)

    response_content = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            print(content, end="")
            response_content += content

    return (
        response_content,
        len(enc.encode(messages[-1]["content"])),
        len(enc.encode(response_content)),
    )


if __name__ == "__main__":
    main()
