# JavaLang Python — GCS 2026.1

Projeto desenvolvido para a disciplina de Gerência de Configuração de Software, com o objetivo de implementar em Python uma adaptação das classes String, Integer e Float da especificação Java SE 8.

O foco do trabalho não está apenas no código, mas também na aplicação prática de Gerência de Configuração de Software, incluindo controle de versão, issues, branches, commits semânticos, pull requests, revisão por pares, integração contínua, baselines, releases, auditoria e rastreabilidade.

## Equipe

* Efraim Nantes — Mantenedor
* Pedro Mendes — Engenheiro de Qualidade
* Thiago Nogueira — Gerente de Configuração
* Rudimar Neves — Relator
* Arthur Yano — Apoio em implementação e documentação

## Classes implementadas

O projeto utiliza o pacote javalang/ para concentrar as classes adaptadas:

* JInteger
* JFloat
* JString

As classes mantêm nomes de métodos em estilo Java, como parseInt, valueOf, charAt, compareTo, isNaN, entre outros, preservando a proposta de adaptação da especificação Java SE 8 para Python.

## Estrutura do projeto

text
.github/workflows/      Configuração de integração contínua
docs/                   Documentação do processo, auditorias, ADRs e relatórios
javalang/               Código-fonte das classes adaptadas
tests/                  Testes automatizados
README.md               Documentação principal do projeto
CHANGELOG.md            Histórico de mudanças por baseline
pyproject.toml          Configuração do projeto, pytest, coverage e ruff


## Instalação

Requisitos:

* Python 3.10 ou superior
* pip

Para instalar as dependências do projeto:

bash
python -m pip install -e .


Caso necessário, instalar ferramentas de teste e lint manualmente:

bash
python -m pip install pytest pytest-cov ruff


## Execução dos testes

Para executar toda a suíte de testes:

bash
python -m pytest


Para executar testes com relatório de cobertura:

bash
python -m pytest --cov=javalang


## Execução do lint

Para executar o Ruff:

bash
python -m ruff check javalang/ tests/


## Integração contínua

O projeto utiliza GitHub Actions para executar validações automáticas em pull requests e atualizações da branch principal.

O workflow executa:

* instalação das dependências;
* verificação com Ruff;
* execução dos testes com Pytest;
* verificação de cobertura.

Pull requests só devem ser mesclados quando o CI estiver verde e houver revisão aprovada por outro integrante.

## Processo de trabalho

O projeto segue o fluxo:

text
Issue → Branch → Commit → Pull Request → Review → CI → Merge → Baseline/Release


Regras adotadas:

* Toda alteração não trivial deve nascer em uma issue.
* Cada branch deve estar associada a uma issue.
* Commits devem seguir padrão semântico e referenciar a issue.
* Pull requests devem fechar issues com Closes #N.
* Autoaprovação de PR não é permitida.
* PRs com CI vermelho não devem ser mesclados.
* Baselines são formalizadas por tags e releases no GitHub.

## Baselines

As baselines do projeto são:

* v0.1-functional — estrutura inicial, processo de GCS, CI e documentação base.
* v0.2-jinteger — implementação, testes e documentação da classe JInteger.
* v0.3-jfloat — implementação, testes e documentação da classe JFloat.
* v0.4-jstring — implementação, testes e documentação da classe JString.
* v1.0.0 — entrega final, auditoria, apresentação e release final.

## Documentação

Documentos principais:

* docs/adaptacoes.md — adaptações técnicas entre Java SE 8 e Python.
* docs/itens-de-configuracao.md — itens de configuração do projeto.
* docs/uso-de-ia.md — registro de uso de IA generativa.
* docs/auditoria.md — auditoria interna final.
* docs/auditoria-cruzada.md — auditoria cruzada.
* docs/relatorios/status-v0.1.md — status da baseline inicial.
* docs/relatorios/status-v0.2.md — status da baseline JInteger.
* docs/relatorios/status-v0.3.md — status da baseline JFloat.
* docs/relatorios/status-v0.4.md — status da baseline JString.
* docs/relatorios/status-v1.0.md — relatório final da entrega.

## Adaptações Java para Python

Como Java e Python possuem diferenças importantes de tipagem, sobrecarga de métodos, representação numérica, Unicode, charset, locale e gerenciamento de memória, algumas funcionalidades foram adaptadas.

As decisões técnicas estão registradas em:

text
docs/adaptacoes.md


Métodos não implementados integralmente ou implementados de forma adaptada foram documentados com justificativa técnica e alternativa equivalente quando aplicável.

## Apresentação gravada

Link da apresentação final:

https://drive.google.com/file/d/1QPv6vNT5rdGM-ArVkuV_8yNytDHOngG2/view?usp=sharing

A apresentação deve demonstrar o processo de GCS, as baselines, a rastreabilidade, os principais artefatos do repositório, a auditoria e as funcionalidades implementadas.

## Como auditar o projeto

Para auditar o projeto, recomenda-se verificar:

1. Issues criadas por baseline.
2. Branches associadas às issues.
3. Commits com referência refs #N.
4. Pull requests com Closes #N.
5. Revisões feitas por outro integrante.
6. Execuções do GitHub Actions.
7. Tags e releases das baselines.
8. Documentos em docs/.
9. Relatórios de status por baseline.
10. Auditorias finais.

## Status final

O projeto consolida as classes JInteger, JFloat e JString com testes automatizados, documentação de adaptações, baselines versionadas e evidências do processo de Gerência de Configuração de Software.
