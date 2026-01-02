Agente de Validação de Deploy 🚀
Este projeto nasceu da necessidade de automatizar aquela conferência chata (e arriscada) que fazemos antes de subir um código para produção. Em vez de ler logs gigantes manualmente, criei este script em Python que faz o trabalho sujo de procurar erros e validar variáveis essenciais.

 O que ele faz na prática?
O script funciona como um "filtro" de segurança. Ele lê um arquivo de log (que você indica no terminal) e verifica:

Erros Críticos: Se encontrar palavras como ERROR ou FAIL, ele trava tudo na hora.

Configurações: Ele checa se as variáveis obrigatórias (como chaves de API e URLs de banco de dados) estão presentes.

Resultado: No fim, ele te dá um relatório visual: Aprovado ou Bloqueado.

 Como testar?
Deixei uma pasta chamada tests/ com três cenários reais para você testar como o agente se comporta:

Cenário de Sucesso: python deploy_agent.py tests/sucesso.log

Cenário de Erro Crítico: python deploy_agent.py tests/erro_critico.log

Cenário de Dados Incompletos: python deploy_agent.py tests/dados_incompletos.log

 Tecnologias
Python 3

Manipulação de arquivos e lógica de automação.

