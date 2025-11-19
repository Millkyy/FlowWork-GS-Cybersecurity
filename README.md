# FlowWork – GS Cybersecurity

Repositório da entrega de **Cybersecurity** da GS, aplicada ao projeto **FlowWork**.

O **FlowWork** é uma plataforma gamificada para equipes presenciais ou distribuídas que registra:
- tarefas concluídas (peças lavadas, tickets resolvidos, pedidos embalados, etc.);
- atividades de bem-estar (pausas, alongamentos, hidratação, check-ins de humor).

O objetivo da solução é **aumentar engajamento sem sacrificar a saúde mental**, valorizando ritmo sustentável e qualidade, e não apenas volume de produção.  
Este repositório mostra como aplicar princípios de **DevSecOps** e boas práticas de **codificação segura** nesse contexto.

---

## 🎯 Objetivo da atividade

> “Escolher quatro vulnerabilidades de segurança, explicá-las, demonstrar um ataque simples em Python e apresentar o código corrigido (‘defesa’), além de explicar como essas falhas seriam detectadas em um pipeline CI/CD moderno (SAST, SCA, DAST).”

As vulnerabilidades analisadas aqui são:

1. **SQL Injection**  
2. **Quebra de Controle de Acesso (Broken Access Control / IDOR)**  
3. **Desserialização Insegura em Python**  
4. **Injeção de Comando (Command Injection)**  

Todas foram contextualizadas dentro do FlowWork e implementadas em scripts didáticos em Python.

---

## 📁 Estrutura do repositório

```text
FlowWork-GS-Cybersecurity/
├── Broken_Acess_Control.py      # Exemplo de Broken Access Control / IDOR (ataque + defesa)
├── Command_Injection.py         # Exemplo de Command Injection (ataque + defesa)
├── Insecure_Deserialization.py  # Exemplo de desserialização insegura em Python (ataque + defesa)
├── SQL_Injection.py             # Exemplo de SQL Injection (ataque + defesa)
├── flowwork.db                  # Banco SQLite de apoio aos exemplos (SQL / tarefas)
└── .github/
    └── workflows/
        └── codeql.yml           # Workflow de SAST com GitHub CodeQL (Code Scanning)
        └── dast-zap.yml         # Workflow de DAST com OWASP ZAP Baseline
```

>Obs.: os scripts são **exemplos didáticos** para demonstrar as falhas e as correções, e não um backend completo do FlowWork.
        
---

## 🧾 Relatório da GS

O relatório completo da atividade (conceitos, riscos detalhados, explicações das correções e relação com SAST/DAST/SCA no CI/CD) foi elaborado com base neste código e no contexto do FlowWork.

---

## 👥 Integrantes

- Camilly Ishida - RM551474
  
- Jessica Witzler Costacurta - RM99068
