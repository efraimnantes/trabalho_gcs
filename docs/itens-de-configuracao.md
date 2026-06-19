# Itens de Configuração do Projeto

Este documento lista os principais itens de configuração (ICs) controlados ao longo do ciclo de vida do projeto.

| Item de Configuração | Responsável | Formato | Periodicidade de Mudança | Dependências |
| :--- | :--- | :--- | :--- | :--- |
| **Módulo JString** | Mantenedor / Equipe | `.py` (Código Python) | Contínua (v0.4) | `adaptacoes.md`, ADRs |
| **Módulo JInteger** | Eng. de Qualidade | `.py` (Código Python) | Contínua (v0.2) | `adaptacoes.md`, ADRs |
| **Módulo JFloat** | Gerente de Config. | `.py` (Código Python) | Contínua (v0.3) | `adaptacoes.md`, ADRs |
| **Suíte de Testes (pytest)** | Eng. de Qualidade | `.py` (Código Python) | A cada novo método | Código fonte das classes |
| **Documentos de Decisão (ADRs)** | Gerente de Config. | `.md` (Markdown) | Sob demanda | Arquitetura geral |
| **Doc. de Adaptações Python/Java** | Gerente de Config. | `.md` (Markdown) | Sob demanda | Especificação Java SE 8 |
| **Configuração de CI (GitHub Actions)** | Eng. de Qualidade | `.yml` (YAML) | Baixa (configuração inicial) | GitHub |
| *README.md* | Mantenedor / Relator | .md (Markdown) | Média | ADRs, decisões da equipe e baselines |
| *CHANGELOG.md* | Relator / Mantenedor | .md (Markdown) | A cada baseline/release | Issues, PRs, tags e releases |
| *Documento de Uso de IA* | Desenvolvedor de apoio / Equipe | .md (Markdown) | Contínua | Prompts, métodos apoiados por IA e revisão humana |
| *Relatórios de Status das Baselines* | Relator | .md (Markdown) | A cada baseline | Issues resolvidas, PRs, CI, coverage e release notes |
| *Auditoria Interna* | Gerente de Configuração | .md (Markdown) | Final do projeto | Issues, PRs, commits, tags, releases e CI |
| *Auditoria Cruzada* | Gerente de Configuração | .md (Markdown) | Final do projeto | Equipe auditada, evidências e conclusão da auditoria |
| *Template de Pull Request* | Mantenedor / Gerente de Configuração | .md (Markdown) | Baixa | Processo de revisão, rastreabilidade e critérios de aceite |
| *Templates de Issues* | Mantenedor / Gerente de Configuração | .md (Markdown) | Baixa | Tipos de tarefa, bug, decisão e documentação |
| *Issues do GitHub* | Mantenedor / Equipe | Registro no GitHub | Contínua | Labels, milestones, responsáveis e PRs |
| *Pull Requests do GitHub* | Mantenedor / Revisores | Registro no GitHub | Contínua | Issues, commits, CI, revisões e merges |
| *Tags e Releases* | Mantenedor | Registro no GitHub | A cada baseline | Relatórios de status, CHANGELOG e CI verde |
| *Regra de Proteção da Branch Principal* | Mantenedor | Configuração do GitHub | Baixa | CI obrigatório, revisões obrigatórias e bloqueio de merge |
