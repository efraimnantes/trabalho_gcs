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
| `JString`  | `String(StringBuilder)`    | Não implementado     | Python não possui `StringBuilder` nativo equivalente. Usar `str()` quando necessário.                                                                |
| `JString`  | `intern()`                 | Adaptado/documentado | O pool de strings da JVM não se aplica diretamente ao runtime Python. Pode-se usar a string normalmente; `sys.intern()` será avaliado se necessário. |
| `JString`  | `getBytes(String charset)` | Adaptado             | Python utiliza encoding por string, como UTF-8. Alternativa: `encode(encoding)`.                                                                     |
| `JInteger` | `TYPE`                     | Adaptado             | No Java, `Integer.TYPE` retorna a classe que representa o tipo primitivo `int`; em Python foi adaptado para retornar o tipo embutido `int`.          |
| `JInteger` | `parseInt(String s)`       | Adaptado             | Usa conversão com `int()` e exceções `ValueError` para simular comportamento de entrada inválida.                                                    |
| `JInteger` | `valueOf(String s)`        | Adaptado             | Retorna uma instância de `JInteger` a partir da conversão nativa com `int()`.                                                                         |
| `JInteger` | `toBinaryString(int i)`    | Adaptado             | Usa máscara de 32 bits (`i & 0xFFFFFFFF`) para simular a representação unsigned do Java em valores negativos.                                        |
| `JInteger` | `toOctalString(int i)`     | Adaptado             | Usa máscara de 32 bits e remove o prefixo `0o` gerado pelo Python.                                                                                   |
| `JInteger` | `toHexString(int i)`       | Adaptado             | Usa máscara de 32 bits e remove o prefixo `0x` gerado pelo Python.                                                                                   |
| `JInteger` | `floatValue()`             | Adaptado             | Retorna o valor interno convertido para `float`, permitindo interoperabilidade com `JFloat`.                                                         |
| `JFloat`   | `intValue()`               | Adaptado             | Retorna o valor interno convertido para `int`, permitindo interoperabilidade com `JInteger`.                                                         |

## JInteger - Baseline v0.2

### Métodos Implementados

- `parseInt(String s)`: implementado utilizando conversão nativa do Python com `int()`.
- `valueOf(String s)`: implementado encapsulando o valor convertido em uma instância de `JInteger`.
- `toBinaryString(int i)`: implementado com máscara de 32 bits para representar negativos como no Java.
- `toOctalString(int i)`: implementado com máscara de 32 bits e formatação octal.
- `toHexString(int i)`: implementado com máscara de 32 bits e formatação hexadecimal.
- `compare(int x, int y)`: implementado comparando dois inteiros e retornando negativo, zero ou positivo.
- `compareUnsigned(int x, int y)`: implementado usando máscara de 32 bits para simular comparação unsigned.
- `toUnsignedString(int i)`: implementado usando máscara de 32 bits para representar inteiros negativos como unsigned.
- `floatValue()`: implementado para converter o valor de `JInteger` para `float`.

### Métodos Não Implementados ou Parcialmente Adaptados

- Métodos que dependem de manipulação estrita de bits, como `highestOneBit`, poderão ser adaptados para funções nativas do Python ou deixados para implementações futuras, devido às diferenças no tratamento de números inteiros entre Java e Python.

### Formatação de Bases

Em Java, métodos como `toBinaryString`, `toOctalString` e `toHexString` retornam a representação unsigned de 32 bits para valores negativos. Como o Python utiliza inteiros de precisão arbitrária, foi aplicada a máscara `i & 0xFFFFFFFF` para simular o comportamento de inteiros de 32 bits do Java.

### Comparação e Operações Unsigned

Como o Python possui inteiros de precisão arbitrária e não possui tipo `unsigned int` de 32 bits como o Java, os métodos `compareUnsigned` e `toUnsignedString` foram adaptados usando a máscara `i & 0xFFFFFFFF`.

Essa máscara permite interpretar valores negativos no formato de complemento de dois de 32 bits. Por exemplo, `-1` passa a ser tratado como `4294967295`, simulando o comportamento de `Integer` no Java SE 8.

## Interoperabilidade entre Wrappers

No Java, o compilador realiza o auto-unboxing de objetos wrappers em expressões aritméticas. Como o Python não possui esse comportamento automaticamente para classes customizadas, a interoperabilidade entre `JInteger` e `JFloat` foi adaptada por meio de métodos explícitos de conversão, como `floatValue()` em `JInteger` e `intValue()` em `JFloat`.

Também é possível usar o atributo interno `.value` quando for necessário realizar operações matemáticas diretamente entre instâncias.