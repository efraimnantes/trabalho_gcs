
# JavaLang Python - GCS 2026.1

Projeto final da disciplina de Gerência de Configuração de Software.

O objetivo é implementar, em Python 3.10+, classes inspiradas nas classes `JString`, `JInteger` e `JFloat` da especificação Java SE 8.

## Estrutura do Projeto

A estrutura inicial do repositório foi criada no bootstrap do projeto e organizada para atender às exigências do trabalho de Gerência de Configuração de Software.

Principais diretórios e arquivos:

* `.github/`: contém configurações do GitHub, incluindo templates de issues, template de Pull Request e workflow de integração contínua.
* `.github/workflows/ci.yml`: define o pipeline de CI responsável por executar lint, testes e cobertura.
* `javalang/`: contém os módulos principais do projeto, com as classes `JString`, `JInteger` e `JFloat`.
* `tests/`: contém a suíte de testes automatizados do projeto.
* `docs/`: contém a documentação de apoio ao processo de GCS, incluindo ADRs, adaptações, relatórios, auditorias e uso de IA.
* `README.md`: apresenta o projeto, sua organização, instruções de execução e documentação principal.
* `CHANGELOG.md`: registra mudanças relevantes por baseline/release.
* `pyproject.toml`: contém configurações do projeto Python, testes, lint e cobertura.

Essa organização separa código, testes, documentação e automação, facilitando a rastreabilidade entre issues, commits, Pull Requests e baselines.


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
