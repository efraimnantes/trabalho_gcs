# Declaração de Uso de Inteligência Artificial Generativa

Este documento registra de forma transparente como ferramentas de Inteligência Artificial (IA) Generativa foram utilizadas durante o ciclo de vida deste projeto.

---

## 1. Princípios de Uso e Revisão Humana

A Inteligência Artificial foi adotada neste projeto estritamente como uma **ferramenta de apoio (co-piloto)** para ganho de produtividade. 

* **Não houve substituição da equipe:** A IA não substituiu a tomada de decisão técnica, o pensamento crítico ou o trabalho de engenharia da equipe.
* **Revisão Humana Obrigatória:** Todos os artefatos (código, documentação, testes) gerados ou sugeridos por IA passaram por análise crítica, revisão por pares (via *Pull Requests*) e adequação aos padrões do projeto antes de serem integrados.
* **Regra Anti-Atalho:** A IA não foi utilizada para pular etapas fundamentais do desenvolvimento ou terceirizar a compreensão do domínio de negócio. Toda a responsabilidade sobre o funcionamento, segurança e qualidade do projeto permanece integralmente com os desenvolvedores.

## 2. Ferramentas Utilizadas

As seguintes ferramentas de IA generativa apoiaram o desenvolvimento do projeto:

* **ChatGPT (OpenAI) / Gemini (Google):** Apoio no planejamento, brainstorming, pesquisa estruturada e redação de documentação.
* **GitHub Copilot:** Assistência direta na IDE para implementação de código, testes e refatoração.

## 3. Áreas de Apoio e Métodos

A tabela abaixo detalha as áreas do projeto em que a IA foi aplicada e de que forma ela auxiliou a equipe:

| Área do Projeto | Como a IA Apoiou a Equipe |
| :--- | :--- |
| **Planejamento** | Estruturação inicial de tarefas, quebra de épicos e brainstorming de requisitos técnicos com base no escopo fornecido. |
| **Documentação** | Geração de templates (arquitetura, manuais), revisão gramatical e formatação de arquivos Markdown. |
| **Implementação** | Autocompletar de trechos de código repetitivos (boilerplate), sugestões de refatoração, análise estática e explicação de mensagens de erro complexas. |
| **Testes** | Apoio no mapeamento de cenários de teste (*caminho feliz* e *edge cases*) e geração de *mocks* ou estruturas de dados para testes unitários. |

## 4. Exemplos de Prompts Representativos

Para garantir total transparência, abaixo estão os exemplos reais dos *prompts* (comandos) utilizados pela equipe durante a interação com a ferramenta de IA:

* **Documentação de Arquitetura:** *"Como documentar um ADR?"* *(Utilizado para entender o padrão de documentação de decisões arquiteturais e criar nossos próprios registros).*

* **Estruturação de Projeto:** *"Sugira uma estrutura para documentação de projeto."* *(Utilizado para gerar o esqueleto inicial do nosso repositório e organizar os arquivos de documentação).*

* **Apoio Técnico / Implementação:** *"Explique as diferenças entre Java e Python."* *(Utilizado como apoio conceitual para embasar discussões técnicas da equipe).*

## Métodos ou Artefatos com Apoio de IA

| Item | Tipo de apoio |
|--------|-------------|
| README | Revisão textual |
| ADRs | Sugestões de documentação |
| Planejamento | Organização das tarefas |

## Observações

A IA foi utilizada apenas como ferramenta de apoio e não substitui o trabalho dos integrantes da equipe.
