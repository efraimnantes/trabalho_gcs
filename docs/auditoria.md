# Relatório de Auditoria Interna de GCS

Este documento registra a auditoria interna realizada pela equipe, evidenciando a aplicação prática dos conceitos de Gerência de Configuração de Software (GCS) ao longo do desenvolvimento do projeto de conversão de classes Java para Python.

## 1. Processos Definidos vs. Executados
Os processos definidos no plano de configuração (criação de issues, branches baseadas em features, commits padronizados, Pull Requests com revisão e geração de baselines/tags) foram seguidos em sua grande maioria. O fluxo de trabalho permitiu um desenvolvimento organizado e minimizou conflitos no código.

## 2. Desvios e Justificativas
Durante a execução, ocorreram os seguintes desvios menores em relação ao plano original:
* **Commits diretos/Ajustes Rápidos:** Em alguns momentos iniciais (ou para pequenas correções de documentação), commits podem ter sido feitos sem um PR formal. *Justificativa:* Agilidade na correção de erros críticos que impediam o avanço de outras tarefas.
* **Sobrecarga em alguns Pull Requests:** Alguns PRs acabaram englobando mais alterações do que o estritamente planejado em uma única issue. *Justificativa:* Ocorrência de dependências diretas entre as implementações (ex: métodos que dependiam de correções de indentação conjuntas).

## 3. Rastreabilidade (Issues, PRs e Commits)
Garantimos a rastreabilidade interligando Issues aos seus respectivos Pull Requests e listando o número da Issue nas mensagens de commit. Exemplos de evidências do nosso fluxo:

* **Comparação Simples (JString):**
  * Issue: #63
  * Branch: `feature/jstring-comparacao-simples`
  * O PR encerrou a issue correspondente utilizando a palavra-chave `Closes #63`, e os commits utilizaram `refs #63`.
* **Recortes (Substring JString):**
  * Issue: #64
  * Branch: `feature/jstring-substring`
* **Concatenação e Substituição (JString):**
  * Issue: #65
  * Branch: `feature/jstring-concat-replace`
* **Busca Simples (JString):**
  * Issue: #66
  * Branch: `feature/jstring-busca-simples`

*(Nota da auditoria: O histórico completo pode ser verificado nas abas "Issues" e "Pull Requests" fechados do repositório).*

## 4. Respeito às Baselines (Tags)
O versionamento semântico foi respeitado. As baselines foram geradas ao alcançar marcos estáveis (ex: fechamento de um conjunto de features da `JFloat` ou `JString`).
* O histórico de Tags reflete entregas funcionais e testadas no ramo `main`.
* As liberações (Releases) correspondem a fotos do código naqueles momentos específicos.

## 5. Limitações de Proteção da Branch Main
*Devido a restrições de contas gratuitas do GitHub em organizações, regras rígidas de "Branch Protection" (como exigir revisão obrigatória de 1 pessoa e bloquear merges de administradores) podem não ter sido aplicadas de forma sistêmica e bloqueante.* Para contornar isso, a equipe adotou a **proteção por convenção social**: os membros combinaram de não fazer push direto na `main` para as features de código, utilizando sempre o fluxo de PR e marcando um colega como `Reviewer`.

## 6. Lições Aprendidas
* **A importância da rastreabilidade:** Relacionar commits com issues salvou muito tempo na hora de entender o motivo de uma alteração de código semanas depois.
* **Revisão de código (Code Review):** Encontramos pequenos erros (como indentação fora do padrão do Python) antes de integrar na `main`, evitando quebras em cadeia.
* **Granularidade das branches:** Criar branches pequenas e de curta duração (uma para cada issue) facilitou a aprovação dos Pull Requests e evitou grandes conflitos de *merge*.
