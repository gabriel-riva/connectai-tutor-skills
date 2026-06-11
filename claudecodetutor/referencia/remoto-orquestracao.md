# Referência: Remoto, Mobile e Orquestração no Claude Code Desktop

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.
> Fact verificado em 10/06/2026 (teste empírico, app desktop): teammates criados via agent teams aparecem no app como "Tarefa em segundo plano" com link "Ver transcrição" (somente leitura), NÃO como sessão interativa na sidebar. Agent teams são funcionalidade experimental do CLI.

---

## Remote Control: continuar do celular ou de outro dispositivo

### O que é

Remote Control conecta [claude.ai/code](https://claude.ai/code) ou o aplicativo Claude (iOS e Android) a uma sessão do Claude Code rodando no seu computador. Comece uma tarefa na sua mesa e continue do celular ou de outro computador.

A sessão roda 100% localmente no seu computador. O Remote Control é apenas uma janela para essa sessão local.

**Disponibilidade:** todos os planos (Pro, Max, Team, Enterprise). Em Team e Enterprise, um admin precisa habilitar o toggle de Remote Control nas configurações de admin. Requer Claude Code v2.1.51 ou posterior.

### Como iniciar (via CLI)

```bash
# Modo servidor: aguarda conexões, mostra URL e QR code
claude remote-control

# Sessão interativa com Remote Control habilitado
claude --remote-control

# A partir de uma sessão existente
/remote-control
```

No app desktop, acesse **Settings > Claude Code > Enable remote control by default** para habilitar em todas as sessões.

### Como conectar de outro dispositivo

Após iniciar uma sessão com Remote Control:

- Abra a URL da sessão em qualquer navegador.
- Escaneie o QR code para abrir diretamente no app Claude.
- Vá para [claude.ai/code](https://claude.ai/code) e encontre a sessão na lista. Sessões com Remote Control ativo mostram um ícone de computador com ponto verde.
- No app mobile, toque em **Code** na navegação.

### O que funciona remotamente

- Enviar mensagens e continuar a conversa.
- Comandos que produzem saída em texto: `/compact`, `/clear`, `/context`, `/usage`, `/mcp`, `/reload-plugins`, `/recap`.
- O `@` para autocomplete de caminhos de arquivo do projeto local.

### O que só funciona localmente

- Comandos que abrem seletores interativos no terminal: `/plugin`, `/resume`.

### Notificações push mobile

Com Remote Control ativo, o Claude pode enviar notificações push para o seu celular quando uma tarefa longa termina ou quando precisa de uma decisão sua. Configure em `/config` > "Push when Claude decides".

---

## Dispatch: delegar tarefas pelo celular

O Dispatch permite que você envie uma tarefa pelo aplicativo Claude no celular e o app desktop cria uma sessão para executá-la. É para delegar trabalho enquanto você está longe do computador.

Para configurar, emparelhe o app mobile com o app desktop seguindo as instruções de suporte da Anthropic.

---

## Claude Code na web

[claude.ai/code](https://claude.ai/code) oferece sessões do Claude Code rodando na infraestrutura da Anthropic (não no seu computador). Útil quando você quer:

- Iniciar uma tarefa sem configuração local.
- Trabalhar em um repositório que você não tem clonado.
- Rodar múltiplas tarefas em paralelo em ambientes isolados.

Diferente do Remote Control (que executa no seu computador), sessões na web rodam na nuvem e têm acesso a repositórios via GitHub.

---

## Channels: Telegram, Discord, Slack

O Claude Code pode receber mensagens de plataformas de comunicação como Telegram, Discord, Slack e webhooks. Um canal conectado envia eventos diretamente para a sessão, permitindo que o Claude reaja a mensagens ou alertas externos.

**Como funciona:** um servidor MCP que suporta o protocolo de canal (`claude/channel`) envia mensagens para a sessão. Plugins de canal ficam disponíveis no marketplace oficial.

Exemplos de uso: notificações de CI/CD sendo enviadas à sessão, alertas de monitoramento disparando o Claude, mensagens do Telegram ativando tarefas automáticas.

Para o **Slack**: após configurar o app Claude no Slack, mencione `@Claude` em um canal. O Claude roda em infraestrutura da Anthropic (não localmente) e pode revisar PRs e realizar tarefas de desenvolvimento a partir do chat da equipe.

---

## Subagentes: delegação dentro de uma sessão

### O que são

Subagentes são assistentes especializados que rodam dentro de uma sessão, cada um com sua própria janela de contexto, prompt de sistema, restrições de ferramentas e permissões independentes. O Claude os usa automaticamente quando adequado para a tarefa.

**Onde rodam:** dentro de uma única sessão (não são sessões separadas visíveis na sidebar).

### Subagentes integrados

| Subagente | Modelo | Quando é usado |
|-----------|--------|----------------|
| **Explore** | Haiku (rápido) | Busca e análise de código sem fazer mudanças |
| **Plan** | Igual à sessão | Pesquisa para planejamento (modo Plan) |
| **general-purpose** | Igual à sessão | Tarefas complexas com múltiplos passos |

Explore e Plan pulam CLAUDE.md e status do git para manter a pesquisa rápida e econômica.

### Criar subagentes personalizados

Defina um subagente criando um arquivo Markdown com frontmatter em `.claude/agents/` (projeto) ou `%USERPROFILE%\.claude\agents\` (pessoal):

```markdown
---
name: revisor-de-segurança
description: Revisa código em busca de vulnerabilidades de segurança
tools: Read, Grep, Glob, Bash
model: opus
---

Você é um engenheiro de segurança sênior. Revise o código em busca de:
- Vulnerabilidades de injeção (SQL, XSS, injeção de comando)
- Falhas de autenticação e autorização
- Segredos ou credenciais no código
- Tratamento inseguro de dados

Forneça referências a linhas específicas e correções sugeridas.
```

Para usar: "Use um subagente para revisar este código por questões de segurança."

### Subagentes vs. sessões paralelas

Os subagentes rodam dentro da sessão principal e retornam apenas os resultados, mantendo sua conversa principal limpa. Use para tarefas de pesquisa e verificação que inundaria o contexto principal com arquivos lidos.

---

## Supervisão via transcript local

### Onde ficam os transcripts

Cada sessão do Claude Code (tanto da aba Code do app desktop quanto da CLI) grava um transcript local em:

```
%USERPROFILE%\.claude\projects\<projeto-achatado>\<sessionId>.jsonl
```

O `<projeto-achatado>` usa `--` como separador, substituindo `:` e `\`. Por exemplo, `E:\projetos\meu-app` vira `E--projetos--meu-app`.

### Formato do transcript

Cada linha é um objeto JSON com campos:
- `type`: tipo do evento
- `sessionId`: ID da sessão
- `cwd`: diretório de trabalho
- `message.role`: `user` ou `assistant`
- `message.content`: conteúdo da mensagem
- `entrypoint`: `"claude-desktop"` para sessões do app desktop

### Para que serve

O transcript é a fonte primária de supervisão. Em oficinas com o tutor ClaudeCodeTutor, o tutor pode monitorar o progresso dos alunos lendo os transcripts das sessões de prática (com permissão pre-aprovada em `settings.local.json`).

---

## Agent teams: times de sessões coordenadas

### O que são (e onde estão disponíveis)

Agent teams coordenam múltiplas instâncias do Claude Code trabalhando juntas, com lista de tarefas compartilhada e comunicação direta entre agentes. Uma sessão atua como líder, coordenando o trabalho e atribuindo tarefas.

**Agent teams são uma funcionalidade experimental, disponível no CLI.** Para usar, é necessário habilitar a variável de ambiente `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

### O que aparece no app desktop

Quando o tutor (ou qualquer sessão CLI) cria agent teams, os teammates criados aparecem no app desktop como **"Tarefa em segundo plano"** com um link **"Ver transcrição"** (somente leitura). Eles NÃO aparecem como sessões interativas na sidebar do app desktop.

Isso significa: na prática de oficina, os alunos criam sessões de prática manualmente (Ctrl+N, mesma pasta) no app desktop. O tutor usa agent teams para paralelismo e gabaritos no lado do CLI, supervisionando os alunos via transcript local.

### Para que servem (contexto)

Agent teams são mais eficazes para:
- Revisão de código paralela (cada teammate revisa um aspecto diferente: segurança, performance, cobertura de testes).
- Novas funcionalidades independentes (cada teammate trabalha em um módulo separado).
- Investigação com hipóteses concorrentes (cada teammate testa uma teoria de bug diferente).

### Comparação: subagentes vs. agent teams

| | Subagentes | Agent teams |
|---|---|---|
| **Contexto** | Própria janela, resultado volta ao chamador | Própria janela, totalmente independente |
| **Comunicação** | Reportam resultados apenas ao agente principal | Teammates se comunicam diretamente entre si |
| **Coordenação** | Agente principal gerencia todo o trabalho | Lista de tarefas compartilhada, auto-coordenação |
| **Custo de tokens** | Menor: resultados resumidos de volta | Maior: cada teammate é uma instância separada |
| **Disponível no app desktop** | Sim (funcionam dentro de uma sessão) | Não como sessão interativa (aparecem como tarefa em segundo plano) |

---

## Comparativo: como trabalhar remotamente

| Opção | Claude roda em | Ideal para |
|-------|----------------|------------|
| Dispatch (app mobile) | Seu computador (app desktop) | Delegar tarefas enquanto fora |
| Remote Control | Seu computador (CLI ou VS Code) | Continuar trabalho em andamento de outro dispositivo |
| Channels (Telegram, Discord) | Seu computador (CLI) | Reagir a eventos externos como alertas de CI |
| Slack | Infraestrutura Anthropic | PRs e revisões a partir do chat da equipe |
| Tarefas agendadas desktop | Seu computador | Automação recorrente com acesso a arquivos locais |
| Routines (nuvem) | Infraestrutura Anthropic | Automação confiável sem computador ligado |
