# ADR 0002: Modelo de Ramificação e Fluxo de Trabalho

* **Status:** Aceito
* **Data:** 19/06/2026

## Contexto
Para que toda a equipe consiga trabalhar no mesmo repositório sem que um apague o código do outro e para garantir que a branch `main` esteja sempre funcionando (CI verde), precisamos oficializar um modelo de ramificação e regras de envio de código.

## Decisão
Decidimos adotar o **GitHub Flow** associado a práticas de rastreabilidade (vínculo com Issues) e revisão por pares. As regras estabelecidas são:

1. **Proteção da Main:** Commits diretos na branch `main` são proibidos após o bootstrap (commit inicial)[cite: 1].
2. **Fluxo Obrigatório:** Toda alteração deve seguir o fluxo: Criar uma branch a partir da main ➔ Commitar usando padrão semântico com `refs #N` ➔ Abrir Pull Request com `Closes #N` ➔ Passar por revisão de outro membro ➔ Validar o CI ➔ Fazer o Merge[cite: 1].
3. **Padrão de Commits:** Uso de prefixos semânticos (ex: `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`)[cite: 1].
4. **Governança:**
   * É proibido aprovar o próprio Pull Request (autoaprovação)[cite: 1].
   * Pull Requests com testes falhando ou erros de linter (CI Vermelho) não podem ser mesclados em hipótese alguma[cite: 1].

## Consequências

### Positivas:
* Histórico de commits limpo, organizado e fácil de entender[cite: 1].
* Rastreabilidade total: qualquer alteração na `main` estará ligada a uma issue e a um Pull Request[cite: 1].
* Código da `main` sempre estável devido à barreira das revisões e do CI automatizado[cite: 1].

### Negativas / Desafios:
* O processo exige mais passos antes de o código chegar na branch principal[cite: 1].
* Requer disciplina de todos os integrantes para não esquecer os padrões de mensagens de commit e tags de fechamento de issue[cite: 1].