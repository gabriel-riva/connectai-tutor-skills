# Referência: Boas Práticas (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

Esta referência condensa as melhores práticas de uso do Codex em dez pontos objetivos. A filosofia central: trate o Codex como um colega de equipe que você configura e melhora ao longo do tempo, não como uma ferramenta de uso único.

---

## 1. Contexto primeiro: dê ao Codex o que ele precisa para começar bem

Um prompt com contexto fraco leva a resultados genéricos. Um prompt com contexto forte economiza tempo de revisão. Inclua quatro elementos antes de iniciar uma tarefa:

- **Objetivo:** o que você quer mudar ou construir
- **Contexto:** quais arquivos, pastas, documentos ou exemplos são relevantes
- **Restrições:** quais padrões, convenções ou limites se aplicam
- **Critério de conclusão:** como saber quando a tarefa está pronta

Escolha o nível de raciocínio com base na complexidade:

| Nível | Quando usar |
|---|---|
| Baixo | Tarefas bem definidas, pequenas mudanças |
| Médio ou Alto | Mudanças complexas, múltiplos arquivos |
| Extra Alto | Trabalhos longos que exigem raciocínio profundo |

---

## 2. Planejamento antes da execução

Para problemas complexos ou ambíguos, planeje antes de executar. O modo Plan (`/plan` ou `Shift+Tab`) faz o Codex fazer perguntas e esboçar o plano antes de começar a implementar.

Outra abordagem: peça ao Codex para "desafiar suas suposições" antes de começar. Isso tende a revelar dependências ocultas e reduz retrabalho.

Para trabalho multi-etapa, configure um arquivo `PLANS.md` como guia de execução que o Codex pode consultar ao longo da sessão.

---

## 3. Orientação durável: escreva no AGENTS.md

Quando você percebe que repete as mesmas instruções toda semana, é sinal de que elas devem estar no `AGENTS.md`, não no prompt.

Um bom `AGENTS.md` cobre:

- Estrutura do repositório
- Comandos de build e teste
- Convenções de engenharia
- Restrições importantes

Use `/init` no CLI para gerar um modelo inicial com base no projeto. Mantenha o arquivo prático e atualizado com base em problemas reais que surgirem.

---

## 4. Threads duráveis como espaços de trabalho

Threads não são apenas chats: são espaços de trabalho com contexto acumulado. Mantenha uma thread por unidade coerente de trabalho, em vez de abrir uma thread nova para cada pergunta relacionada ao mesmo projeto.

**Comandos úteis para sessões longas:**

| Comando | Função |
|---|---|
| `/resume` | Retomar conversa salva |
| `/fork` | Nova thread preservando o transcript original |
| `/compact` | Resumir contexto anterior para liberar espaço |
| `/agent` | Alternar entre threads de agentes paralelos |

Threads fixadas ficam sempre a um toque de distância (material recente cita os atalhos `Ctrl+1` a `Ctrl+9`; confirme no seu app), transformando-se em espaços de trabalho persistentes.

---

## 5. Skills reutilizáveis: empacote o que funciona

Quando um workflow se torna repetitivo, transforme-o em uma skill. Skills evitam reaprender o mesmo processo do zero a cada sessão.

O momento certo para criar uma skill: quando você e o Codex já têm um fluxo funcionando bem em um thread, e você quer poder repeti-lo em outros projetos.

Use `$skill-creator` para criar a skill a partir da conversa existente. Cada skill deve focar em uma única função para manter clareza e evitar invocações incorretas.

---

## 6. Iteração: verifique, ajuste, repita

O Codex funciona melhor em ciclos curtos de iteração do que em prompts longos que tentam resolver tudo de uma vez. Para problemas difíceis, o padrão é:

1. Estabeleça métricas de sucesso antes de começar (testes, benchmarks, critérios visuais)
2. Execute uma rodada
3. Inspecione os artefatos diretamente, não apenas os logs
4. Identifique o maior ponto de falha
5. Faça uma mudança focada nesse ponto
6. Execute novamente
7. Continue até atingir o critério de conclusão

Não confie apenas nos logs de código. Para saídas visuais (páginas, documentos), inspecione o artefato diretamente.

---

## 7. Verificação: use testes e revisão

Peça ao Codex para:

- Criar ou atualizar testes junto com cada mudança
- Executar a suite de testes relevante
- Verificar lint, formatação e tipos
- Revisar as mudanças antes de aceitar

Use `/review` para revisar contra a branch base, mudanças não consolidadas ou commits específicos. Para times, crie um arquivo `code_review.md` e o referencie no `AGENTS.md` para manter consistência.

---

## 8. Automações para trabalho agendado

Quando um fluxo está funcionando bem manualmente, configure uma automação para ele rodar periodicamente. Bons candidatos:

- Resumos de commits recentes
- Busca de bugs prováveis em novos PRs
- Geração de notas de lançamento
- Resumos de standups

Padrão prático: "skills definem o método, automações definem o cronograma."

Antes de automatizar, teste o prompt manualmente e verifique as primeiras execuções agendadas.

---

## 9. Configuração consistente por camadas

Defina padrões em camadas para que a configuração se aplique onde é necessária:

- `~/.codex/config.toml`: preferências pessoais (vale em todos os projetos)
- `.codex/config.toml`: comportamento específico do repositório (versionável no Git)
- Linha de comando: para sobrescrever configurações em situações pontuais

Configure aprovações, sandboxing, modelos e servidores MCP para o seu fluxo real de trabalho, não para um fluxo hipotético.

---

## 10. Erros comuns a evitar

| Erro | Consequência | Solução |
|---|---|---|
| Colocar todas as regras no prompt | O prompt fica enorme e difícil de manter | Mover regras para `AGENTS.md` |
| Não deixar o Codex ver o trabalho completo | Contexto incompleto gera respostas parciais | Fornecer arquivos, pastas e exemplos relevantes |
| Pular planejamento em tarefas multi-etapa | Retrabalho e direção errada | Usar `/plan` antes de executar |
| Dar permissão total sem entender o fluxo | Alterações indesejadas nos arquivos | Começar com sandbox restrito e ampliar gradualmente |
| Executar em arquivos ativos sem worktrees | Conflitos e dificuldade de desfazer | Usar modo Worktree para exploração |
| Automatizar antes de ser confiável manualmente | Erros automatizados são difíceis de rastrear | Validar manualmente antes de agendar |
| Esperar passo a passo em vez de usar em paralelo | Velocidade abaixo do potencial | Usar subagentes para trabalho paralelizável |
| Uma thread por projeto em vez de por tarefa | Contexto misturado e threads longas demais | Uma thread por unidade coerente de trabalho |

---

## Síntese

O Codex entrega mais quando você investe um pouco de tempo em configuração: um `AGENTS.md` bem escrito, threads organizadas, skills para fluxos repetitivos e automações para trabalho previsível. Quanto mais clara a estrutura ao redor do Codex, menos tempo você gasta repetindo contexto e mais tempo o agente passa executando trabalho real.
