# 🚀 Agente de Validação Automática de Deploy

Este projeto é um script em Python desenvolvido para atuar como um filtro de segurança antes de um deploy. Ele analisa logs e relatórios para garantir que nenhum erro crítico passe despercebido.

A ideia principal é automatizar a revisão de arquivos de saída, verificando padrões de erro e a presença de variáveis obrigatórias, indicando de forma clara se o deploy pode seguir ou deve ser bloqueado.

---

## 📁 Estrutura do Projeto

Estrutura simples e direta:

- tests/
  - sucesso.log
  - erro_critico.log
  - dados_incompletos.log
- deploy_agent.py -> código principal do agente

---

## 🛠️ Critérios de Validação

O agente realiza três validações principais:

1. Erros Críticos  
   Varredura no log em busca de termos como ERROR, FATAL, EXCEPTION ou FAILED.

2. Variáveis Obrigatórias  
   Verifica se as seguintes variáveis estão presentes no log:
   - DATABASE_URL
   - SECRET_KEY
   - API_KEY

3. Decisão Automática  
   Caso qualquer critério falhe, o deploy é automaticamente bloqueado.

---

## ▶️ Como Executar os Testes

1. Cenário de Sucesso (Deploy Aprovado)

   python deploy_agent.py tests/sucesso.log

2. Cenário de Erro Crítico (Deploy Bloqueado)

   python deploy_agent.py tests/erro_critico.log

3. Cenário de Dados Incompletos (Deploy Bloqueado)

   python deploy_agent.py tests/dados_incompletos.log

---

## 📄 Requisitos do Log

Para que o deploy seja aprovado, o arquivo de log deve conter obrigatoriamente as seguintes chaves:

- DATABASE_URL
- SECRET_KEY
- API_KEY
