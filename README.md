# Microsserviço de Validação de CPF com Azure Functions

Este projeto é um microsserviço serverless desenvolvido com **Azure Functions** para validar CPFs.

## 🚀 Como funciona?
- Recebe um CPF via requisição HTTP (query parameter ou JSON body)
- Valida o CPF conforme as regras oficiais
- Retorna um JSON informando se o CPF é válido ou não

## 📦 Como executar localmente?
1. Instale o **Azure Functions Core Tools** e **Python 3.8+**
2. Clone o repositório e instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Inicie a função localmente:
   ```sh
   func start
   ```

