# Adaptações documentadas

Este documento registra métodos da especificação Java SE 8 que não foram implementados integralmente em Python, além das justificativas técnicas.

## Critérios de adaptação

Alguns comportamentos da linguagem Java não possuem equivalência direta em Python, especialmente:

- sobrecarga de métodos por tipo primitivo;
- distinção entre `int`, `long`, `byte` e `short`;
- dependências de `Locale`, `Charset`, `StringBuilder` e `StringBuffer`;
- detalhes internos de runtime, como `String.intern()`.

## Métodos não implementados ou adaptados

| Classe | Método Java | Situação | Justificativa | Alternativa em Python |
|---|---|---|---|---|
| JString | String(StringBuilder) | Não implementado | Python não possui StringBuilder nativo equivalente | Usar `str()` |
| JString | intern() | Adaptado/documentado | O pool de strings do Java não se aplica diretamente ao runtime Python | Usar a string normalmente |
| JString | getBytes(String charset) | Adaptado | Python utiliza encoding por string, como UTF-8 | Usar `encode(encoding)` |