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
