# GPT Playground

This document describes how to work with GPT using Python

## Set up a virtual environment (optional)

**Reference:** openAI [website](https://platform.openai.com/docs/quickstart?context=python)

Running the command below will create a virtual environment named "playground-env" inside the current folder you have selected in your terminal / command line:
```
python3 -m venv playground-env
```

Activate virtual environment on Unix or MacOS, using:
```
source playground-env/bin/activate
```

## Install Ollama

Follow instructions on Ollama [website](https://ollama.com/download/linux)

```
curl -fsSL https://ollama.com/install.sh | sh
```

Pull the model you want to use (e.g. llama2)
```
ollama run llama2
```

## Install dependencies

```
pip3 install -r requirements.txt
```
