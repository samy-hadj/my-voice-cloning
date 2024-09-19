import os
from dotenv import load_dotenv
from langchain_openai import OpenAI,ChatOpenAI  # Importer OpenAI de langchain_openai
import sys
import subprocess
import platform
from typing import Optional

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer la valeur des variables d'environnement
openai_api_key = os.getenv("OPENAI_API_KEY")
gpt_key = os.getenv("GPT_KEY")

# Configurer l'instance OpenAI de LangChain
llm = OpenAI(api_key=gpt_key)
llm2=ChatOpenAI(model="gpt-4o",temperature=0)