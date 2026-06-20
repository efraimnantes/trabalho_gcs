# Adaptações Técnicas: Java SE 8 para Python 3.10+

Devido às diferenças estruturais e paradigmáticas entre Java e Python, algumas adaptações e concessões foram necessárias na implementação das classes `JString`, `JInteger` e `JFloat`.

## 1. Sobrecarga de Métodos
Diferente do Java, Python não suporta sobrecarga de métodos nativamente baseada na assinatura de tipos. 
* **Adaptação:** Utilizamos parâmetros opcionais (`None`) ou checagem de tipos em tempo de execução (usando `isinstance()`) para simular o comportamento de métodos sobrecarregados (ex: `valueOf(String)` vs `valueOf(String, int radix)`).

## 2. Tipos Primitivos
Enquanto o Java diferencia tipos primitivos (`int`, `float`) de classes *wrapper* (`Integer`, `Float`), o Python trata tudo como objeto.
* **Adaptação:** Nossas classes emulam o comportamento de objetos Java, encapsulando os tipos nativos `int`, `float` e `str` do Python internamente.

## 3. Limitações de Manipulação de Strings
* **StringBuilder / StringBuffer:** Java utiliza essas classes para mutabilidade eficiente de strings. Como strings em Python também são imutáveis, métodos concatenativos gerarão novas instâncias em memória.
* **String.intern():** Python possui a função `sys.intern()`, mas o controle da *String Pool* do Java é muito específico. Nossa implementação fará uma adaptação simplificada ou não implementará suporte total à *String Pool* nativa da JVM.

## 4. Limitações de Localização (Locale) e Charset
* O tratamento nativo de `Locale` e `Charset` em Java é extenso. Em Python, dependeremos das bibliotecas nativas `locale` e da codificação padrão (UTF-8). Métodos complexos de conversão de bytes serão simplificados ou deixados como não implementados nesta fase.

## 5. Tabela de Métodos Adaptados ou Não Implementados

| Classe     | Método Original            | Status               | Motivo / Alternativa em Python                                                                                                                       |
| :--------- | :------------------------- | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| JString  | String(StringBuilder)    | Não implementado     | Python não possui StringBuilder nativo equivalente. Usar str() quando necessário.                                                                |
| JString  | intern()                 | Adaptado/documentado | O pool de strings da JVM não se aplica diretamente ao runtime Python. Pode-se usar a string normalmente; sys.intern() será avaliado se necessário. |
| JString  | getBytes(String charset) | Adaptado             | Python utiliza encoding por string, como UTF-8. Alternativa: encode(encoding).                                                                     |
| JInteger | TYPE                     | Adaptado             | No Java, Integer.TYPE retorna a classe que representa o tipo primitivo int; em Python foi adaptado para retornar o tipo embutido int.          |
| JInteger | parseInt(String s)       | Adaptado             | Usa conversão com int() e exceções ValueError para simular comportamento de entrada inválida.                                                    |
| JInteger | valueOf(String s)        | Adaptado             | Retorna uma instância de JInteger a partir da conversão nativa com int().                                                                         |

## JInteger - Baseline v0.2

### Métodos Implementados

- parseInt(String s): implementado utilizando conversão nativa do Python com int().
- valueOf(String s): implementado encapsulando o valor convertido em uma instância de JInteger.

### Métodos Não Implementados ou Parcialmente Adaptados

- Métodos que dependem de manipulação estrita de bits, como highestOneBit, poderão ser adaptados para funções nativas do Python ou deixados para implementações futuras, devido às diferenças no tratamento de números inteiros entre Java e Python.