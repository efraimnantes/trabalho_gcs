# ADR 0001 - Nomenclatura das Classes

## Status

Aceito

## Contexto

O projeto busca reproduzir funcionalidades inspiradas em classes da linguagem Java utilizando Python.

Existem possíveis conflitos entre nomes utilizados pelo Java e tipos nativos do Python.

## Decisão

As classes do projeto utilizarão o prefixo "J":

- JString
- JInteger
- JFloat

Os métodos seguirão o padrão camelCase para manter compatibilidade conceitual com a API Java.

## Justificativa

A utilização dos nomes String, Integer e Float poderia gerar confusão com tipos já existentes na linguagem Python.

O prefixo J identifica claramente que se trata de uma implementação inspirada na API Java.

## Consequências

- Maior clareza no código.
- Evita colisões com tipos nativos.
- Facilita futuras expansões do projeto.
- Mantém proximidade com a nomenclatura utilizada no Java.

## Arquivos Impactados

- javalang/jstring.py
- javalang/jinteger.py
- javalang/jfloat.py
- README.md