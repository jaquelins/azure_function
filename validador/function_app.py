import azure.functions as func
import re
import json

def is_valid_cpf(cpf: str) -> bool:
    """Valida um CPF utilizando a lógica oficial."""
    cpf = re.sub(r'\D', '', cpf)  
    
    if len(cpf) != 11 or cpf in [str(i)PP * 11 for i in range(10)]:
        return False
    
    def calc_digit(digits):
        soma = sum(int(digit) * (pos + 1) for pos, digit in enumerate(digits))
        return soma % 11 % 10
    
    return calc_digit(cpf[:9]) == int(cpf[9]) and calc_digit(cpf[:10]) == int(cpf[10])

def main(req: func.HttpRequest) -> func.HttpResponse:
    """Função Azure que valida um CPF recebido via requisição HTTP."""
    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
            cpf = req_body.get('cpf')
        except ValueError:
            pass
    
    if not cpf:
        return func.HttpResponse(
            json.dumps({"error": "CPF não fornecido"}),
            status_code=400,
            mimetype="application/json"
        )
    
    is_valid = is_valid_cpf(cpf)
    return func.HttpResponse(
        json.dumps({"cpf": cpf, "valid": is_valid}),
        status_code=200,
        mimetype="application/json"
    )
