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

| Classe | Método Original | Status | Motivo / Alternativa em Python |
| :--- | :--- | :--- | :--- |
| `JString` | `intern()` | A definir | Dificuldade em replicar a String Pool da JVM exatamente. Avaliando `sys.intern()`. |
| `JInteger` | `parseInt(String s)` | Adaptado | Lida com exceções `ValueError` do Python para emular `NumberFormatException`. |

## 6. JFloat (v0.3-jfloat)
- Implementada usando `float` nativo do Python.
- Constantes IEEE 754 (MAX_VALUE, MIN_VALUE, NaN, etc.) mapeadas usando a biblioteca `math`.
- Conversões numéricas (`intValue`, `longValue`, `byteValue`) ajustadas para simular os limites do Java (ex: estouro de limite no byte).
- Validações `isNaN()`, `isInfinite()` e `isFinite()` funcionais.
