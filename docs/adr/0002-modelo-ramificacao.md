# ADR 0002 — Modelo de ramificação

## Status

Aprovado.

## Contexto

O trabalho exige controle de versão distribuído, uso de branches por funcionalidade, Pull Requests, revisão por pares e proteção da branch principal.

## Decisão

A equipe decidiu adotar o modelo GitHub Flow.

## Regras adotadas

- A branch `main` será protegida.
- Nenhum commit direto será feito na `main` após a configuração inicial.
- Toda mudança não trivial deverá nascer em uma issue.
- Cada issue será implementada em uma branch própria.
- Todo Pull Request deverá ser revisado por pelo menos um integrante que não seja o autor.
- Commits devem seguir o padrão semântico: `feat:`, `fix:`, `test:`, `docs:`, `refactor:` ou `chore:`.
- Pull Requests devem referenciar a issue correspondente usando `Closes #N`.

## Consequências

Esse modelo garante rastreabilidade entre issue, branch, commit e Pull Request.