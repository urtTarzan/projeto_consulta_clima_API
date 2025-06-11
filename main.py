import requests
import json
from os import path
from datetime import datetime

nome= str(input("digite o nome da cidade: "))


# 2 _____________puxando dados da API_________________
url = f"https://api.openweathermap.org/data/2.5/weather"

parametros= {
    "q": nome,
    "appid": "7b354dfb2b8646fae950f09d021bd7e5",
    "lang": "pt_br",
    "units": "metric"
}

headers = {
    "User-Agent": "Mozilla/5.0" #simula uma requisição de um navegador
}
response = requests.get(url , params=parametros , headers=headers)
dados = response.json()
status = response.status_code

# 1 ____________tratando os dados_______________________
if status == 200:
    horario =datetime.now().strftime("%d/%m/%Y %H:%M:%S") #conventendo o horario para string

    #criando um resumo com base no retorno da API base
    resumo = {
        "cidade":dados["name"],
        "clima":dados['weather'][0]['description'],
        "temperatura":dados['main']['temp'],
        "humidade":dados['main']['humidity'],
        "horario": horario
    }
    print(f"como esta o clima em {resumo['cidade']}: {resumo['clima']}")
    print(f"temperatura: {resumo['temperatura']} graus")
    print(f"humidade: {resumo['humidade']}%")

    #criando um historico acessivel em json
    if path.exists("arquivo.json"):
        with open("arquivo.json" , "r" ,encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
    else:
        historico = []
    
    historico.append(resumo)

    with open("arquivo.json", "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4, ensure_ascii=False)
elif status == 401:
    print("key invalida")
else:
    print("cidade não encontrada")
