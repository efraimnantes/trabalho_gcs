## Estrutura inicial do repositório

A estrutura inicial do repositório foi criada no commit de bootstrap do projeto. Nesta baseline `v0.1-functional`, a equipe revisou a organização dos diretórios e arquivos principais para verificar aderência ao enunciado do trabalho.

Foram identificados os seguintes grupos principais de artefatos:

* Código-fonte das classes em `javalang/`;
* Testes automatizados em `tests/`;
* Documentação do processo em `docs/`;
* Configurações do GitHub em `.github/`;
* Workflow de integração contínua em `.github/workflows/ci.yml`;
* Arquivos de apoio como `README.md`, `CHANGELOG.md` e `pyproject.toml`.

A estrutura atende ao objetivo da baseline inicial, pois fornece uma base mínima para implementação das classes, execução de testes, documentação das decisões técnicas e rastreabilidade do processo de GCS.

## Issues Resolvidas e PRs Mesclados
* Foram resolvidas as issues de configuração inicial e estruturação documental (Issues 1 a 10).
* Os Pull Requests relacionados a essas issues foram revisados e mesclados pela equipe.

## Adaptações Documentadas
* Foram documentadas as diferenças e limitações iniciais na transição de Java para Python, como sobrecarga de métodos, tipos primitivos, `StringBuilder`, `Locale` e `Charset`.

## Métricas Iniciais do CI
* Workflow validado e rodando automaticamente em push e PR.
* `ruff`, `pytest` e `coverage` configurados.
* CI Verde: Testes iniciais de fumaça das classes principais estão passando sem erros.

## Pendências para a próxima baseline
* Iniciar a implementação das constantes, construtores e métodos da classe `JInteger` para a baseline `v0.2-jinteger`.