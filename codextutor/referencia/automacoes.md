# Referência: Automações (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

As automações permitem que o Codex execute trabalho em segundo plano, de forma recorrente, sem que você precise estar presente. Esta referência cobre os dois tipos principais de automação e o padrão de uso com Goals.

---

## 1. Dois tipos de automação

O Codex oferece dois tipos distintos, com finalidades diferentes:

| Tipo | Quando usar | Contexto da conversa |
|---|---|---|
| **Automação standalone** | Cada execução começa do zero | Não preserva histórico entre execuções |
| **Thread automation** | Retorna à mesma thread com contexto vivo | Preserva todo o histórico da conversa |

A escolha entre os dois depende de uma pergunta simples: o trabalho precisa "lembrar" o que aconteceu nas execuções anteriores? Se sim, use thread automation. Se cada execução é independente (um relatório diário, por exemplo), use a standalone.

---

## 2. Automações standalone

### O que fazem

Iniciam uma execução nova a cada ciclo. Cada rodada parte do zero, sem acesso ao que aconteceu na rodada anterior. Os resultados aparecem na seção **Triage**, que funciona como uma caixa de entrada de descobertas.

**Casos de uso típicos:**

- Relatório diário de commits recentes
- Verificação periódica de bugs prováveis em novos PRs
- Resumo semanal de atividade do repositório
- Geração automática de notas de lançamento

### Configuração

Acesse a aba **Automations** no app e clique em criar. Defina:

- O prompt descrevendo o que o Codex deve fazer
- A cadência: diária, semanal, ou usando sintaxe cron para horários personalizados
- Se deve rodar no projeto local ou em worktree isolado (recomendado para repositórios Git)
- O modelo e esforço de raciocínio (você pode deixar nos padrões do app)

**Múltiplos projetos:** a mesma automação standalone pode ser configurada para rodar em vários projetos.

### Gerenciamento de worktrees

Com cadências frequentes, muitos worktrees podem se acumular. Archive execuções que não são mais necessárias. Evite fixar (pin) execuções a menos que queira manter o worktree correspondente.

### Segurança (configurações de sandbox)

As automações herdam as configurações de sandbox do projeto:

- **Somente leitura:** falha se tentar modificar arquivos, acessar rede ou aplicativos
- **Workspace-write:** pode modificar arquivos dentro do workspace; falha para rede ou fora do workspace
- **Acesso completo:** pode modificar arquivos e acessar rede sem perguntar (maior risco)

As automações usam `approval_policy = "never"` quando a política organizacional permite.

---

## 3. Thread automations (automações de heartbeat)

### O que fazem

Thread automations são chamadas de "acordar" recorrentes que retornam à mesma thread em um ritmo definido. Pense nisso como um alarme que reativa uma conversa específica no horário combinado.

Quando a thread acorda, o Codex retoma de onde parou: tem acesso a todo o histórico da conversa, ao contexto do projeto e aos plugins instalados. Isso é fundamentalmente diferente de uma automação standalone.

### Casos de uso

- Verificar um comando de longa duração até a conclusão
- Buscar novas mensagens no Slack, GitHub ou outros serviços conectados
- Manter um loop de revisão em cadência fixa
- Executar workflows baseados em skills periodicamente
- Manter um chat focado em uma tarefa de pesquisa ou triagem contínua

### Intervalos suportados

- Baseados em minutos (para acompanhamento ativo)
- Diários e semanais (para check-ins em horários específicos)

### Como criar uma thread automation

Você pode criar a partir de um thread regular, descrevendo a tarefa, a cadência e se deve estar vinculada à thread atual. O Codex rascunha o prompt, escolhe o tipo correto e configura tudo.

Skills também podem criar ou atualizar automações, como uma skill que configura verificação de status de PR em cronograma recorrente.

---

## 4. O padrão "chefe de gabinete"

Um dos padrões mais úteis de thread automation é o "chefe de gabinete": uma thread que monitora canais de comunicação, pesquisa contexto e prepara respostas, mas **nunca envia nada sem a aprovação do usuário**.

Exemplo de prompt para uma thread automation de 30 em 30 minutos:

> "A cada 30 minutos, verifique o Slack e o Gmail em busca de mensagens sem resposta que precisam da minha atenção. Me ajude a priorizar o que importa. Se alguém fizer uma pergunta, pesquise a resposta o mais profundamente que puder e rascunhe uma resposta para mim, mas não a envie."

Quando você retorna, a parte custosa de reunir contexto já foi feita. A decisão do que enviar fica com você.

Esse padrão funciona bem para: responder a comentários de PR, acompanhar comentários no Google Docs, monitorar respostas no Slack.

---

## 5. Goals: objetivos com verificador

### O que são

Goals são objetivos duráveis que o Codex persegue ao longo de múltiplos turnos, até atingir uma condição de parada verificável. A diferença em relação a um prompt comum é que o Goal define o critério de sucesso, não apenas a tarefa.

**Um goal fraco:** "Implemente o plano neste arquivo Markdown."

**Um goal forte:** tem uma condição de parada mensurável, um mecanismo de verificação e instruções sobre como reportar progresso.

### Como ativar

Habilite no `config.toml`:

```toml
[features]
goals = true
```

Ou execute: `codex features enable goals`

### Como usar

No compositor, use o comando `/goal`:

```
/goal Complete [objetivo] without stopping until [estado final verificável].
```

**Controles durante a execução:**

| Ação | Comando |
|---|---|
| Verificar goal atual | `/goal` |
| Pausar | `/goal pause` |
| Retomar | `/goal resume` |
| Limpar | `/goal clear` |

No app, uma barra aparece acima do compositor com botões de pausar, retomar, editar e limpar.

### O que torna um bom Goal

Um objetivo eficaz:

- É maior que um único prompt, mas menor que um backlog aberto
- Define claramente o resultado esperado
- Especifica o que não deve ser alterado
- Inclui como verificar progresso (um conjunto de testes, um benchmark, um workflow que deve continuar passando)
- Tem uma condição de parada explícita

**Verifiers úteis:** suite de testes, benchmark, reprodução de bug, matriz de validação, workflow de ponta a ponta.

> "Ambição importa, mas sem verificação é apenas um desejo."

### Exemplos de Goals

**Migração de stack:**
```
/goal Migrate this project from [legacy stack] to [target stack].
Make sure all screens stay exactly the same visually, using playwright
interactive to verify the output.
```

**Implementação de plano:**
```
/goal Implement PLAN.md, creating tests for each milestone and
verifying the output with playwright interactive.
```

**Otimização de prompts:**
```
/goal Optimize the prompts in [arquivo] until the eval suite reaches
[pontuação alvo]. After each change, run [eval command], inspect failing
cases, and keep edits minimal and targeted.
```

---

## 6. Testar antes de automatizar

Antes de configurar uma automação, teste o prompt manualmente em uma thread regular para confirmar:

- Clareza e escopo correto do prompt
- Comportamento esperado do modelo e das ferramentas
- O diff resultante é revisável e razoável

Revise as primeiras execuções agendadas e ajuste conforme necessário.

**Filosofia prática:** "Skills definem o método, automações definem o cronograma." Use skills para empacotarar o que deve ser feito; use automações para definir quando e com qual frequência.

---

## 7. Requisitos de funcionamento

Para automações com escopo de projeto, a máquina que roda o app Codex precisa estar:

- Ligada e conectada à internet
- Com o app Codex em execução
- Com o projeto disponível no disco no horário agendado

Configure a opção de manter o computador acordado (Settings > Geral > "Prevent sleep while running") para evitar que o agendamento seja perdido por suspensão do sistema.
