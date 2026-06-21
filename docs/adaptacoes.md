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
| `JInteger` | `valueOf(String s)`        | Adaptado             | Retorna uma instância de `JInteger` a partir da conversão nativa com `int()`.                                                                        |
| `JInteger` | `toBinaryString(int i)`    | Adaptado             | Usa máscara de 32 bits (`i & 0xFFFFFFFF`) para simular a representação unsigned do Java em valores negativos.                                        |
| `JInteger` | `toOctalString(int i)`     | Adaptado             | Usa máscara de 32 bits e remove o prefixo `0o` gerado pelo Python.                                                                                   |
| `JInteger` | `toHexString(int i)`       | Adaptado             | Usa máscara de 32 bits e remove o prefixo `0x` gerado pelo Python.                                                                                   |
| `JInteger` | `floatValue()`             | Adaptado             | Retorna o valor interno convertido para `float`, permitindo interoperabilidade com `JFloat`.                                                         |
| `JInteger` | `doubleValue()`            | Adaptado             | Retorna o valor interno convertido para `float`, pois Python não diferencia `float` e `double` como Java.                                            |
| `JInteger` | `byteValue()`              | Adaptado             | Usa máscara de 8 bits (`0xFF`) para simular o comportamento de conversão para `byte` do Java.                                                        |
| `JInteger` | `shortValue()`             | Adaptado             | Usa máscara de 16 bits (`0xFFFF`) para simular o comportamento de conversão para `short` do Java.                                                    |
| `JFloat`   | `intValue()`               | Adaptado             | Retorna o valor interno convertido para `int`, permitindo interoperabilidade com `JInteger`.                                                         |
| `JFloat`   | `longValue()`              | Adaptado             | Retorna o valor interno convertido para `int`, simulando o comportamento de conversão para `long` do Java.                                           |
| `JFloat`   | `byteValue()`              | Adaptado             | Simula o comportamento de overflow do tipo `byte` do Java usando cálculo modular.                                                                    |
| `JFloat`   | `isNaN()`                  | Adaptado             | Usa `math.isnan()` para verificar valores `NaN`.                                                                                                     |
| `JFloat`   | `isInfinite()`             | Adaptado             | Usa `math.isinf()` para verificar infinitos positivos e negativos.                                                                                   |
| `JFloat`   | `isFinite()`               | Adaptado             | Usa `math.isfinite()` para verificar se o valor é finito.                                                                                            |
| `JFloat`   | `compare(float, float)`    | Adaptado             | Usa comparação nativa de `float` do Python; casos específicos como `NaN`, `0.0` e `-0.0` são tratados como adaptação simplificada em relação ao Java. |
| `JFloat`   | `max(float, float)`        | Adaptado             | Usa a função nativa `max()` do Python para retornar o maior valor entre dois números de ponto flutuante. |
| `JFloat`   | `min(float, float)`        | Adaptado             | Usa a função nativa `min()` do Python para retornar o menor valor entre dois números de ponto flutuante. |

## 6. Conversões Numéricas Complementares

Como o Python possui precisão arbitrária para inteiros, a simulação do comportamento de overflow dos tipos primitivos `byte` e `short` do Java foi adaptada por meio de operações bit a bit.

Para `byteValue()`, é usada a máscara `0xFF` ou cálculo modular, simulando um inteiro de 8 bits.
Para `shortValue()`, é usada a máscara `0xFFFF`, simulando um inteiro de 16 bits.

Essa adaptação permite representar valores fora do intervalo padrão de `byte` e `short` de forma semelhante ao comportamento do Java.

## 7. JFloat (v0.3-jfloat)

A classe `JFloat` foi implementada usando o tipo `float` nativo do Python.

Principais adaptações realizadas:

* Constantes IEEE 754, como `MAX_VALUE`, `MIN_VALUE`, `NaN`, `POSITIVE_INFINITY` e `NEGATIVE_INFINITY`, foram mapeadas usando recursos nativos do Python e da biblioteca `math`.
* Conversões numéricas como `intValue()`, `longValue()` e `byteValue()` foram ajustadas para simular o comportamento da classe `Float` do Java SE 8.
* O método `byteValue()` simula o estouro de limite do tipo `byte`, mantendo compatibilidade conceitual com Java.
* As validações `isNaN()`, `isInfinite()` e `isFinite()` foram implementadas com apoio da biblioteca `math`.
* O método `doubleValue()` não exige distinção específica, pois Python utiliza `float` com precisão equivalente ao `double` em muitos contextos.

Essas decisões permitem representar o comportamento principal da classe `Float` do Java SE 8 dentro das limitações e características do Python.


Essas decisões permitem representar o comportamento principal da classe `Float` do Java SE 8 dentro das limitações e características do Python.

### JString: Adaptação do método `replace`
Na implementação da classe `JString`, os métodos `replace(char, char)` e `replace(CharSequence, CharSequence)` do Java foram unificados em um único método `replace(target, replacement)`. Isso ocorre porque o Python não suporta sobrecarga de métodos por assinatura e não possui um tipo primitivo `char` distinto de `str`.


# Adaptações do Java para Python

## JString - Tratamento de Charsets (getBytes)
- **Comportamento Padrão:** No Java, `getBytes()` sem argumentos utiliza o *charset* padrão do sistema operativo (o que muitas vezes causa bugs de portabilidade). No Python, optámos por definir explicitamente o **UTF-8** como padrão no método `.getBytes()`, garantindo um comportamento previsível em qualquer sistema.
- **Exceções:** No Java, passar um charset inválido como argumento lança uma `UnsupportedEncodingException`. Na nossa implementação Python, delegamos a conversão para o método `.encode()` nativo da linguagem, que lançará um erro `LookupError` caso o charset não seja reconhecido. Decidimos manter a exceção nativa do Python por questões de simplicidade e integração com a linguagem.


## JString - Métodos de Expressão Regular (Regex)
- **Correspondência Total (`matches`):** No Java, o método `matches()` exige que a string inteira obedeça à expressão regular passada. Em Python, a função `re.match()` avalia apenas o início da string, enquanto `re.search()` busca em qualquer parte. Para replicar o comportamento exato do Java sem forçar âncoras (`^` e `$`), utilizámos o método nativo `re.fullmatch()`.
- **Substituições (`replaceFirst` e `replaceAll`):** Estes métodos foram mapeados diretamente para a função `re.sub()` do Python. A limitação de `replaceFirst` foi alcançada facilmente através da flag nativa `count=1` no próprio método `sub()`.


## JString: split() e valueOf()
* O método `split(String regex, int limit)` foi adaptado unificando a assinatura e utilizando a função `re.split` do Python. O comportamento de limite do Java foi simulado usando o parâmetro `maxsplit`.
* O método `valueOf(Object)` converte os tipos booleanos primitivos do Python (`True`/`False`) para strings minúsculas (`"true"`/`"false"`), visando manter o comportamento estrito de conversão do Java.