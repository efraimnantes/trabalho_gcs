# ADR 0002 — Modelo de Ramificação, Pull Requests e Baselines

## Status

Aceito

## Contexto

O projeto precisa seguir um processo controlado de Gerência de Configuração de Software, garantindo rastreabilidade entre issues, branches, commits, Pull Requests, revisões, merges e baselines.

Como o trabalho envolve múltiplos integrantes, diferentes módulos e várias entregas incrementais, a equipe adotará um fluxo padronizado para evitar alterações diretas na branch principal e manter histórico claro das decisões e mudanças.

## Decisão

A equipe adotará o modelo GitHub Flow, com a branch `main` como branch principal protegida.

Toda alteração relevante deve seguir o fluxo:

`Issue → Branch → Commit → Pull Request → Review → Merge`

## Regras definidas

* Toda tarefa deve possuir uma issue associada.
* Cada issue deve ter uma branch própria.
* Commits devem seguir padrão semântico e referenciar a issue com `refs #N`.
* Pull Requests devem conter `Closes #N` na descrição para fechar a issue automaticamente após o merge.
* Nenhum integrante deve aprovar o próprio Pull Request.
* Commits diretos na `main` não devem ocorrer após o bootstrap inicial.
* Pull Requests só devem ser mesclados após revisão e aprovação de outro integrante.
* Pull Requests só devem ser mesclados com o CI verde.
* Um commit não deve implementar mais de 3 métodos.
* Uma Pull Request não deve implementar mais de 7 métodos.

## Padrão de branches

As branches devem indicar o tipo de alteração realizada:

* `docs/...` para documentação;
* `feature/...` para implementação de funcionalidades ou métodos;
* `test/...` para testes;
* `ci/...` para integração contínua;
* `audit/...` para auditorias;
* `release/...` para preparação de releases.

Exemplos:

* `docs/revisar-estrutura-inicial`
* `ci/validar-workflow-inicial`
* `feature/jinteger-constantes-construtor`
* `test/smoke-tests-iniciais`
* `docs/status-v0-1-functional`

## Baselines do projeto

As entregas serão organizadas em baselines:

* `v0.1-functional`: configuração inicial, documentação base, CI, papéis, itens de configuração e processo de trabalho;
* `v0.2-jinteger`: implementação e testes da classe `JInteger`;
* `v0.3-jfloat`: implementação e testes da classe `JFloat`;
* `v0.4-jstring`: implementação e testes da classe `JString`;
* `v1.0.0`: entrega final, documentação consolidada, auditorias, apresentação e release final.

Cada baseline deve possuir relatório de status, CI verde, issues resolvidas, PRs mesclados e, quando aplicável, tag/release no GitHub.

## Consequências

Esse processo aumenta a rastreabilidade das mudanças e facilita a auditoria do projeto. Também evita alterações sem revisão e permite que a equipe demonstre uso adequado de Gerência de Configuração de Software durante o desenvolvimento.
