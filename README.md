
# JavaLang Python - GCS 2026.1

Projeto final da disciplina de Gerência de Configuração de Software.

O objetivo é implementar, em Python 3.10+, classes inspiradas nas classes `JString`, `JInteger` e `JFloat` da especificação Java SE 8.

## Classes do projeto

- `JString`
- `JInteger`
- `JFloat`

## Organização da equipe

| Integrante | Papel | Responsabilidades |
|---|---|---|
| Efraim Nantes | Mantenedor | Criação do repositório, proteção da branch main, criação de tags e releases, revisão de PRs e implementação de métodos da JString. |
| Pedro Henrique Mendes | Engenheiro de Qualidade | Configuração da CI, testes, cobertura e implementação de métodos da JInteger. |
| Thiago Nogueira | Gerente de Configuração | Documentação de itens de configuração, ADRs, adaptações, auditoria e implementação da JFloat. |
| Rudimar Neves| Relator | Relatórios de status, release notes, CHANGELOG e métodos simples da JInteger. |
| Arthur Yano | Desenvolvedor de apoio | Documentação de uso de IA, testes simples e métodos simples de JString e JFloat. |

## Como executar os testes

```bash
pytest

```
## Documentação e Decisões Técnicas
Para entender as diferenças arquiteturais e os motivos pelos quais alguns métodos foram adaptados, consulte nossa [Documentação de Adaptações Java para Python](docs/adaptacoes.md).

## Como executar o linter
```bash
ruff check .
```
