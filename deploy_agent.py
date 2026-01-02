import sys
import re

CRITICAL_ERRORS = [
    "ERROR",
    "FATAL",
    "EXCEPTION",
    "FAILED"
]

REQUIRED_VARIABLES = [
    "DATABASE_URL",
    "SECRET_KEY",
    "API_KEY"
]


def read_log(file_path):
    # lê todo o conteúdo do arquivo de log
    # se o arquivo não existir, encerra o processo
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"log file not found: {file_path}")
        sys.exit(1)


def validate_errors(log_content):
    found_errors = []

    # percorre a lista de erros críticos
    # usa regex para evitar falso positivo (ex: error123)
    for error in CRITICAL_ERRORS:
        # o \b garante que ele encontre a palavra exata,
        # mesmo se vier seguida de ':' ou '.'
        if re.search(rf"\b{error}\b", log_content):
            found_errors.append(error)

    return found_errors


def validate_variables(log_content):
    missing = []

    # verifica se todas as variáveis obrigatórias
    # aparecem no conteúdo do log
    for var in REQUIRED_VARIABLES:
        if var not in log_content:
            missing.append(var)

    return missing


def run_validation(log_path):
    # carrega o log para memória
    log_content = read_log(log_path)

    # executa as validações
    errors = validate_errors(log_content)
    missing_vars = validate_variables(log_content)

    print("\n--- deploy validation report ---\n")

    # resultado da validação de erros
    if errors:
        print("❌ critical errors found:")
        for e in errors:
            print(f"- {e}")
    else:
        print("✅ no critical errors found")

    # resultado da validação de variáveis obrigatórias
    if missing_vars:
        print("\n❌ missing required variables:")
        for v in missing_vars:
            print(f"- {v}")
    else:
        print("\n✅ all required variables are present")

    # se existir qualquer problema, o deploy é bloqueado
    if errors or missing_vars:
        print("\n🚫 deploy blocked")
        sys.exit(1)

    # caso contrário, o deploy pode seguir normalmente
    print("\n🚀 deploy approved")
    sys.exit(0)


if __name__ == "__main__":
    # garante que o script seja executado com o parâmetro correto
    if len(sys.argv) != 2:
        print("usage: python deploy_agent.py deploy.log")
        sys.exit(1)

    run_validation(sys.argv[1])
