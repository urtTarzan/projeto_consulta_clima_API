# Projeto Clima - Consulta de Clima via API OpenWeather

Este projeto em Python consulta o clima atual de uma cidade usando a API do OpenWeather, exibe as informações na tela e salva um histórico em arquivo JSON.

## Como usar

1. Execute o script `clima.py`.
2. Digite o nome da cidade quando solicitado.
3. O programa mostrará a descrição do clima, temperatura e umidade.
4. Os dados serão salvos no arquivo `arquivo.json` com histórico de consultas.

## Tecnologias

- Python 3
- Biblioteca requests
- Biblioteca json
- Biblioteca datetime

## Instalando dependências

Antes de rodar, instale a biblioteca `requests` com o comando:

```bash
pip install requests
