# Referência: Automações e Agendamento no Claude Code Desktop

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.

---

## Três formas de agendar trabalho

O Claude Code oferece três abordagens distintas para automatizar tarefas recorrentes:

| | Routines (nuvem) | Tarefas agendadas (desktop) | `/loop` (sessão) |
|---|---|---|---|
| **Roda em** | Infraestrutura Anthropic | Seu computador | Seu computador |
| **Precisa do computador ligado?** | Não | Sim | Sim |
| **Precisa de sessão aberta?** | Não | Não | Sim |
| **Persiste ao reiniciar** | Sim | Sim | Restaura com `--resume` se não expirado |
| **Acesso a arquivos locais** | Não (clone do repositório) | Sim | Sim |
| **Intervalo mínimo** | 1 hora | 1 minuto | 1 minuto |

Escolha a abordagem de acordo com o que você precisa: nuvem para confiabilidade sem computador; desktop para acesso a arquivos locais; `/loop` para polling rápido durante uma sessão ativa.

---

## Routines: tarefas agendadas na nuvem

### O que são

Routines são configurações salvas do Claude Code que rodam automaticamente na infraestrutura da Anthropic. Funcionam mesmo com seu computador desligado. Cada routine combina: um prompt, um ou mais repositórios GitHub, conectores (MCP) e um ou mais gatilhos.

**Disponibilidade:** planos Pro, Max, Team e Enterprise com Claude Code na web habilitado.

**Onde gerenciar:** [claude.ai/code/routines](https://claude.ai/code/routines) ou pelo comando `/schedule` no CLI.

No app desktop, acesse a seção **Routines** na barra lateral, depois **New routine** e escolha **Remote** para criar uma routine em nuvem (escolhendo **Local** você cria uma tarefa agendada no desktop, que roda localmente).

### Tipos de gatilho

- **Agendado:** recorrente (a cada hora, diário, dias úteis, semanal) ou uma vez em data/hora específica.
- **API:** um endpoint HTTP dedicado; qualquer sistema pode disparar a routine com um POST autenticado.
- **GitHub:** reage a eventos do repositório (pull request aberto, fechado, release, etc.).

Uma única routine pode combinar os três tipos.

### Casos de uso típicos

- **Triagem de backlog:** roda toda noite, lê issues abertos, aplica labels, atribui responsáveis e posta resumo no Slack.
- **Review de PR:** dispara quando um PR é aberto; aplica seu checklist de revisão; deixa comentários inline.
- **Verificação de deploy:** seu pipeline de CI/CD chama o endpoint da routine após cada deploy; ela roda verificações de fumaça e posta resultado no canal de release.
- **Sincronização de documentação:** roda semanalmente; identifica docs desatualizadas após merges recentes; abre PRs de atualização.

### Importante saber

- Routines rodam autonomamente (sem prompts de permissão durante a execução).
- Ações aparecem com sua identidade (commits, PRs, mensagens Slack).
- Por padrão, o Claude só pode fazer push em branches com prefixo `claude/`. Para liberar push em branches existentes, habilite a opção "Allow unrestricted branch pushes" na configuração da routine.
- Routines usam o mesmo saldo de uso da assinatura que sessões interativas.

---

## Tarefas agendadas no desktop

### O que são

Tarefas que rodam no seu computador em horário e frequência configurados. Requerem o app desktop aberto e o computador acordado.

No app desktop: acesse **Routines** na barra lateral, depois **New routine** e escolha **Local**.

Você também pode criar tarefas pedindo ao Claude em linguagem natural: "configure uma revisão de código diária às 9h" ou "lembre-me às 15h de amanhã de verificar o deploy".

### Configurar uma tarefa

Campos principais:

| Campo | Descrição |
|-------|-----------|
| Nome | Identificador da tarefa |
| Instruções | O que o Claude deve fazer. Inclui o seletor de modo de permissão e modelo. |
| Pasta de trabalho | Pasta onde a tarefa vai rodar |
| Agendamento | Intervalo (Manual, A cada hora, Diário, Dias úteis, Semanal) |
| Worktree isolado | Opção para dar ao Claude uma cópia git isolada a cada execução |

Para intervalos não disponíveis no seletor (a cada 15 minutos, primeiro do mês), peça ao Claude em qualquer sessão usando linguagem natural.

### Como as tarefas rodam

O app verifica o agendamento a cada minuto. Quando uma tarefa vence:

1. Uma notificação de desktop aparece.
2. Uma nova sessão é criada na seção **Scheduled** da barra lateral.
3. Você pode abrir para ver o que o Claude fez, revisar mudanças ou responder a prompts de permissão.

Se o computador dormiu durante o horário agendado, a próxima vez que o app abrir, uma execução de recuperação é iniciada para o período perdido mais recente (máximo uma por dia por tarefa).

### Permissões para tarefas agendadas

Cada tarefa tem seu próprio modo de permissão. Para evitar que a tarefa trave esperando aprovação:

1. Rode **Run now** após criar a tarefa.
2. Observe os prompts de permissão.
3. Selecione "always allow" para cada ferramenta necessária.

Execuções futuras aprovam automaticamente as mesmas ferramentas.

### Gerenciar tarefas

Na página de detalhes da tarefa:

- **Run now:** executa imediatamente sem esperar o próximo horário.
- **Status:** alternar entre Ativo e Pausado.
- **Edit:** alterar instruções, agendamento, pasta ou configurações.
- **Histórico:** ver cada execução passada (incluindo as puladas).
- **Always allowed:** ver e revogar permissões salvas para esta tarefa.
- **Delete:** remover a tarefa e arquivar todas as sessões criadas.

---

## `/loop`: repetição dentro de uma sessão

### O que é

O `/loop` é uma skill integrada que re-executa um prompt automaticamente em intervalo enquanto a sessão está aberta. Use para monitorar um deploy, acompanhar um PR, verificar um build demorado ou se lembrar de algo mais tarde na sessão.

Tarefas criadas com `/loop` são escopadas à sessão: param quando você inicia uma nova. Retomando com `--resume` restaura tarefas não expiradas (tarefas recorrentes dentro de 7 dias da criação).

### Formas de uso

| O que você fornece | Exemplo | O que acontece |
|---|---|---|
| Intervalo e prompt | `/loop 5m verificar o deploy` | Seu prompt roda em agendamento fixo |
| Só o prompt | `/loop verificar o deploy` | Seu prompt roda em intervalo que o Claude escolhe |
| Só o intervalo (ou nada) | `/loop` | Prompt de manutenção integrado roda; ou seu `loop.md` se existir |

### Comportamento do intervalo dinâmico

Quando você omite o intervalo, o Claude escolhe um intervalo entre 1 minuto e 1 hora baseado no que observa: espera mais curta enquanto uma tarefa está ativa, mais longa quando está quieto.

### Prompt de manutenção integrado

`/loop` sem prompt usa um prompt integrado que:

- Continua trabalho inacabado da conversa
- Cuida do PR do branch atual (comentários de revisão, CI com falha, conflitos de merge)
- Realiza limpezas (busca de bugs, simplificações) quando nada mais está pendente

### Parar um loop

Para um `/loop` aguardando a próxima iteração: pressione `Esc`. O loop não dispara novamente.

### Personalizar com `loop.md`

Crie `.claude/loop.md` (nível de projeto) ou `%USERPROFILE%\.claude\loop.md` (nível pessoal) para substituir o prompt de manutenção integrado. O arquivo é Markdown simples, como qualquer prompt.

### Expiração de 7 dias

Tarefas recorrentes expiram automaticamente 7 dias após a criação, disparam uma última vez e se deletam. Para trabalho recorrente de longo prazo, use Routines ou tarefas agendadas no desktop.

### Lembrete único

Para lembretes de uma vez, use linguagem natural ao invés de `/loop`:

```
Lembre-me às 15h de fazer push do branch de release
```

O Claude cria uma tarefa de disparo único que se deleta após rodar.

---

## Hooks: automações por eventos do ciclo de vida

### O que são

Hooks são comandos de shell definidos pelo usuário que executam em pontos específicos do ciclo de vida do Claude Code. Diferente de instruções no CLAUDE.md (que são sugestões), hooks são determinísticos: garantem que certas ações sempre aconteçam.

Use hooks para: formatar arquivos após edições, bloquear comandos antes de executar, notificações quando o Claude precisa de input, reinjetar contexto ao iniciar sessão, auditar mudanças de configuração.

### Eventos disponíveis

| Evento | Quando dispara |
|--------|----------------|
| `PreToolUse` | Antes de cada chamada de ferramenta |
| `PostToolUse` | Após cada chamada de ferramenta |
| `Stop` | Quando o Claude termina uma resposta |
| `Notification` | Quando o Claude aguarda input ou permissão |
| `SessionStart` | Ao iniciar uma sessão |
| `InstructionsLoaded` | Quando arquivos de instrução são carregados |

### Como configurar

Adicione um bloco `hooks` em qualquer arquivo de settings (ex: `.claude/settings.json`):

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
          }
        ]
      }
    ]
  }
}
```

### Exemplos práticos

**Notificação no Windows quando o Claude precisa de input:**

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "powershell.exe -Command \"[System.Reflection.Assembly]::LoadWithPartialName('System.Windows.Forms'); [System.Windows.Forms.MessageBox]::Show('Claude Code precisa da sua atenção', 'Claude Code')\""
          }
        ]
      }
    ]
  }
}
```

**Bloquear edições em arquivos protegidos:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"tool_input\":{\"file_path\":\"\"}}' | jq -r '.tool_input.file_path' | grep -q 'config/prodution' && echo '{\"decision\":\"block\",\"reason\":\"Arquivo de produção protegido\"}' || echo '{\"decision\":\"approve\"}'"
          }
        ]
      }
    ]
  }
}
```

### Hooks em settings vs. em plugins

Hooks podem ser configurados:

- Em `~/.claude/settings.json` (pessoal, todos os projetos)
- Em `.claude/settings.json` (projeto, compartilhado com a equipe)
- Em `.claude/settings.local.json` (pessoal, projeto atual)
- Dentro de um plugin (em `hooks/hooks.json`)

### Ver hooks configurados

Use `/hooks` em qualquer sessão para listar todos os eventos e ver quais hooks estão configurados em cada um.

---

## `/goal`: trabalhar até atingir o objetivo

### O que é

`/goal` define uma condição de conclusão e o Claude continua trabalhando em ciclos até que a condição seja satisfeita. Após cada resposta, um modelo rápido verifica se a condição foi atingida. Se não, o Claude inicia outra rodada.

**Requer:** Claude Code v2.1.139 ou posterior.

### Quando usar

Use para tarefas substanciais com estado verificável:

- "Migrar um módulo até que todos os testes compilem e passem"
- "Implementar um design doc até que todos os critérios de aceitação sejam satisfeitos"
- "Trabalhar pela fila de issues marcados até que a fila esteja vazia"

### Como usar

```
/goal todos os testes em test/auth passam e o lint está limpo
```

Definir um objetivo inicia uma rodada imediatamente, com a condição como diretiva. Enquanto o objetivo está ativo, um indicador mostra quanto tempo está rodando.

**Ver status:** `/goal` sem argumentos mostra condição, tempo rodando, rodadas e tokens gastos.

**Cancelar:** `/goal clear` (ou `stop`, `off`, `cancel`).

### Escrever uma condição eficaz

O avaliador julgará apenas o que o Claude apresentou na conversa. Escreva a condição como algo demonstrável pelo output do Claude:

- "Todos os testes em `test/auth` passam" (bom: o Claude roda os testes e o resultado aparece na conversa)
- "O código está melhor" (ruim: subjetivo, não verificável)

Para limitar duração: inclua uma cláusula de turno ou tempo na condição ("ou parar após 20 rodadas").

### Diferença em relação a `/loop`

| `/goal` | `/loop` |
|---------|---------|
| Próxima rodada inicia quando a anterior termina | Próxima rodada inicia em intervalo de tempo |
| Para quando a condição é atingida | Para quando você para ou o Claude decide que acabou |
| Usa um avaliador separado para verificar a condição | Depende do próprio Claude para decidir |
