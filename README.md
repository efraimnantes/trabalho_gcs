# JavaLang Python - GCS 2026.1

Projeto final da disciplina de Gerência de Configuração de Software.

O objetivo é implementar, em Python 3.10+, classes inspiradas nas classes `String`, `Integer` e `Float` da especificação Java SE 8.

## Classes do projeto

- `JString`
- `JInteger`
- `JFloat`

## Organização da equipe

| Integrante | Papel | Responsabilidades |
|---|---|---|
| Efraim Nantes | Mantenedor | Criação do repositório, proteção da branch main, criação de tags e releases, revisão de PRs e implementação de métodos da JString. |
| Pessoa 2 | Engenheiro de Qualidade | Configuração da CI, testes, cobertura e implementação de métodos da JInteger. |
| Pessoa 3 | Gerente de Configuração | Documentação de itens de configuração, ADRs, adaptações, auditoria e implementação da JFloat. |
| Pessoa 4 | Relator | Relatórios de status, release notes, CHANGELOG e métodos simples da JInteger. |
| Pessoa 5 | Desenvolvedor de apoio | Documentação de uso de IA, testes simples e métodos simples de JString e JFloat. |

## Como executar os testes

```bash
pytest

```

## Como executar o linter
```bash
ruff check .
```
