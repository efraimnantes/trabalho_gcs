# Auditoria Cruzada

## 1. Identificação

*Projeto auditado:* https://github.com/efraimnantes/trabalho_gcs.git

*Equipe auditada:* Arthur Yano, Efraim Nantes, Pedro Henrique Mendes, Rudimar Neves, Thiago Nogueira.

*Equipe auditora:* Equipe JavaLang Python — GCS 2026.1

*Auditor responsável:* Thiago Nogueira.

*Data da auditoria:* 21/06/2026

*Repositório auditado:* https://github.com/efraimnantes/trabalho_gcs.git

## 2. Objetivo da auditoria

Esta auditoria cruzada tem como objetivo avaliar se o repositório da equipe auditada apresenta evidências adequadas da aplicação das práticas de Gerência de Configuração de Software, incluindo controle de versão, controle de mudanças, rastreabilidade, uso de issues, pull requests, commits semânticos, integração contínua, baselines, documentação e releases.

## 3. Critérios avaliados

Foram avaliados os seguintes critérios:

* Existência e organização das issues.
* Relação entre issues, branches, commits e pull requests.
* Uso de commits semânticos.
* Uso de pull requests com descrição adequada.
* Evidência de revisão por pares.
* Execução de integração contínua.
* Existência de tags e releases para baselines.
* Documentação do processo de GCS.
* Documentação de adaptações técnicas.
* Presença de relatórios de status e auditoria.
* Organização geral do repositório.

## 4. Evidências analisadas

### 4.1 Issues

Foram analisadas as issues do repositório auditado para verificar se as alterações foram planejadas e registradas antes da implementação.

*Evidências observadas:*

* Issues abertas para funcionalidades, correções e documentação.
* Uso de labels e milestones.
* Descrições com objetivo, tarefas e critérios de aceite.
* Fechamento de issues por meio de pull requests.

*Links/evidências:*

* [Issue analisada 1] https://github.com/efraimnantes/trabalho_gcs/issues/79
* 
* [Issue analisada 2] https://github.com/efraimnantes/trabalho_gcs/issues/77
* 
* [Issue analisada 3] https://github.com/efraimnantes/trabalho_gcs/issues/78

## 4.2 Pull requests

Foram avaliados pull requests para verificar rastreabilidade, revisão e integração com a branch principal.

*Evidências observadas:*

* Pull requests vinculados a issues.
* Uso de Closes #N ou referência equivalente.
* Descrições indicando alterações realizadas e impacto.
* Revisão por outro integrante da equipe.
* Integração com a branch principal após validação.

*Links/evidências:*

* [Pull request analisado 1] https://github.com/efraimnantes/trabalho_gcs/pull/96
* 
* [Pull request analisado 2] https://github.com/efraimnantes/trabalho_gcs/pull/56
* 
* [Pull request analisado 3] https://github.com/efraimnantes/trabalho_gcs/pull/58

## 4.3 Commits

Foram avaliados commits para verificar se seguem padrão semântico e se apresentam vínculo com issues.

*Evidências observadas:*

* Commits com prefixos como feat:, fix:, docs: e test:.
* Commits referenciando issues com refs #N.
* Histórico preservado no repositório.

*Links/evidências:*

* [Commit analisado 1] https://github.com/efraimnantes/trabalho_gcs/pull/100/changes/7879be7f22745f81c322471932028051a52726b6
* 
* [Commit analisado 2] https://github.com/efraimnantes/trabalho_gcs/pull/99/changes/f2a79eb6b98115fb512d1cf8b610a4950a03ae3c

## 4.4 Baselines e releases

Foram verificadas tags e releases para avaliar se o projeto possui marcos formais de evolução.

*Evidências observadas:*

* Tags criadas para baselines.
* Releases com descrição do conteúdo entregue.
* Organização por marcos do projeto.

*Links/evidências:*

* [Release analisada 1] https://github.com/efraimnantes/trabalho_gcs/releases/tag/v0.4-jstring
* 
* [Release analisada 2] https://github.com/efraimnantes/trabalho_gcs/releases/tag/v0.3-jfloat

## 4.5 Integração contínua

Foi verificado se o repositório auditado utiliza integração contínua para validar código e testes.

*Evidências observadas:*

* Existência de workflow no GitHub Actions.
* Execução automática de testes.
* Indicação de sucesso ou falha nos pull requests.
* Uso de validações antes do merge.

*Links/evidências:*

* [Execução de CI analisada 1] https://github.com/efraimnantes/trabalho_gcs/actions/runs/27914765864/job/82598039428
* 
* [Execução de CI analisada 2] https://github.com/efraimnantes/trabalho_gcs/actions/runs/27914375137/job/82596986005

## 4.6 Documentação

Foi avaliada a documentação disponível no repositório.

*Evidências observadas:*

* README com instruções de execução.
* Documentação de decisões ou adaptações técnicas.
* Relatórios de status.
* Documentos de auditoria ou processo.

*Links/evidências:*

* [README] https://github.com/efraimnantes/trabalho_gcs/blob/main/README.md
* 
* [Documento de adaptações] https://github.com/efraimnantes/trabalho_gcs/tree/main/docs
* 
* [Relatório de status] https://github.com/efraimnantes/trabalho_gcs/tree/main/docs/relatorios

## 5. Pontos fortes encontrados

Durante a auditoria, foram identificados os seguintes pontos positivos:

* O repositório apresenta histórico de commits preservado.
* Há uso de issues para registrar mudanças.
* Os pull requests demonstram parte da rastreabilidade do processo.
* Existem evidências de organização por baselines ou marcos.
* A documentação permite compreender parte do processo adotado pela equipe.
* A integração contínua contribui para validação automática do projeto.

## 6. Problemas ou riscos encontrados

Foram observados os seguintes pontos de atenção:

Durante a análise do repositório auditado, foram identificados alguns pontos de melhoria relacionados à rastreabilidade, documentação e organização das evidências de GCS.

### 6.1 Rastreabilidade entre issues, commits e pull requests

Em alguns casos, a ligação entre issues, commits e pull requests poderia estar mais clara. Isso pode dificultar a identificação de qual alteração atende a cada solicitação.
### 6.2 Baselines, tags e releases

Foi observada a necessidade de maior padronização no registro das baselines, especialmente na relação entre tags, releases e documentação de cada entrega.
### 6.3 Evidências documentais

Alguns documentos poderiam conter mais links diretos para issues, pull requests, commits, execuções de CI e releases, facilitando a auditoria.

Apesar desses pontos, não foram encontrados problemas críticos que inviabilizem a avaliação do projeto. As observações são recomendações para melhorar a organização, a manutenção e a auditabilidade do repositório.

## 7. Recomendações

Recomenda-se que a equipe auditada:

* Mantenha as issues sempre vinculadas aos pull requests.
* Utilize descrições completas nos pull requests.
* Garanta que todas as baselines tenham tags e releases.
* Mantenha o README atualizado com instruções de execução.
* Registre desvios de processo quando ocorrerem.
* Evite merges sem CI verde ou sem revisão por pares.

## 8. Conclusão

Com base nas evidências analisadas, o repositório auditado apresenta indícios de aplicação das práticas de Gerência de Configuração de Software, incluindo controle de mudanças, rastreabilidade, versionamento e documentação.

A equipe auditada demonstrou organização no uso de issues, commits, pull requests e baselines. Os pontos de melhoria identificados não invalidam o processo, mas devem ser considerados para fortalecer a rastreabilidade e a maturidade do repositório.

Assim, a auditoria cruzada considera o projeto auditado *adequado*, com ressalvas documentadas quando aplicável.

## 9. Checklist da auditoria cruzada

* [✓ ] Equipe auditada registrada.
* [✓ ] Repositório auditado registrado.
* [✓ ] Issues avaliadas.
* [✓ ] Pull requests avaliados.
* [✓ ] Commits avaliados.
* [✓ ] Baselines e releases avaliadas.
* [✓ ] CI avaliado.
* [✓ ] Documentação avaliada.
* [✓ ] Pontos fortes registrados.
* [✓ ] Problemas encontrados registrados.
* [✓ ] Conclusão registrada.
