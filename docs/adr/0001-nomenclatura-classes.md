

## `docs/adr/0001-nomenclatura-classes.md`

Coloque:

```markdown
# ADR 0001 — Nomenclatura das classes

## Status

Aprovado.

## Contexto

O projeto exige a implementação, em Python, de classes equivalentes às classes String, Integer e Float da especificação Java SE 8. Como Python já possui tipos nativos chamados `str`, `int` e `float`, utilizar os mesmos nomes poderia gerar ambiguidade.

## Decisão

A equipe decidiu utilizar os nomes `JString`, `JInteger` e `JFloat`.

## Justificativa

O prefixo `J` indica que as classes representam uma adaptação do comportamento das classes Java. Essa escolha evita colisões com tipos nativos do Python, mantém os nomes curtos e facilita a identificação dos módulos no código e nos testes.

## Consequências

Os arquivos principais do projeto serão:

- `javalang/jstring.py`
- `javalang/jinteger.py`
- `javalang/jfloat.py`

Os métodos manterão a grafia camelCase da especificação Java.