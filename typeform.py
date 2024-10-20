import os
from dotenv import load_dotenv
import requests
from pprint import pprint

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente
api_token = os.getenv("TYPEFORM_API_TOKEN")
form_id = os.getenv("TYPEFORM_FORM_ID")

# Verifica se as variáveis de ambiente foram definidas
if not api_token or not form_id:
    raise ValueError("As variáveis de ambiente TYPEFORM_API_TOKEN e TYPEFORM_FORM_ID devem ser definidas no arquivo .env")

# URL da API de respostas do Typeform
url = f"https://api.typeform.com/forms/{form_id}/responses"
headers = {"Authorization": f"Bearer {api_token}"}
params = {"page_size": 100}

# Fazendo a requisição à API do Typeform
response = requests.get(url, headers=headers, params=params)

pprint(response.json())
