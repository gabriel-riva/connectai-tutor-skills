# Referência: Remoto e Orquestração (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

Esta referência cobre como acompanhar e dirigir tarefas do Codex à distância (via celular ou outro computador), como usar subagentes para trabalho paralelo e a gestão de threads, incluindo os limites do que está confirmado nas docs oficiais.

---

## 1. Conexão remota: trabalhar de qualquer lugar

### O que é

O app do ChatGPT no celular (iOS e Android) permite controlar o Codex em execução em outro computador. Você pode iniciar tarefas, enviar instruções, aprovar ações e revisar resultados do celular, enquanto o ambiente de trabalho (arquivos, configurações, plugins) permanece na máquina host.

**Analogia:** é como ter um piloto automático no seu computador. Você define a rota pelo celular, o computador executa.

### O que você pode fazer remotamente

- Iniciar novas threads em projetos do host ou continuar threads existentes
- Enviar instruções de acompanhamento e responder perguntas
- Aprovar comandos e ações que o Codex solicitar
- Revisar outputs, diffs, resultados de testes e screenshots
- Receber notificações quando tarefas concluem
- Alternar entre hosts e threads conectados

### Requisitos

- Acesso ao Codex na conta ChatGPT
- App ChatGPT atualizado (iOS ou Android)
- App Codex atualizado no computador host (macOS ou Windows)
- Máquina host ligada, online e autenticada
- Autenticação multifator, SSO ou passkey configurados

**Restrição importante:** o Windows não pode atualmente controlar outro computador Windows via conexão remota. Um Mac ou celular pode controlar um Windows, mas Windows não controla outro Windows.

### Como configurar (conexão mobile)

1. Abra o Codex no host e selecione **Set up Codex mobile** na barra lateral
2. Use o celular para escanear o QR code exibido
3. No ChatGPT mobile, confirme a conta e workspace, complete a autenticação
4. O host aparecerá no Codex do celular

Para gerenciar dispositivos conectados: **Settings > Connections** no host.

### Tipos de host

- **Laptop pessoal:** mesmo ambiente do trabalho diário; o acesso para quando o computador dorme
- **Computador sempre ligado:** uma máquina dedicada para tarefas mais longas
- **Host SSH:** para projetos que já vivem em servidor remoto

### Conexão SSH

Adicione o host ao `~/.ssh/config`:

```
Host devbox
  HostName devbox.example.com
  User seu_usuario
  IdentityFile ~/.ssh/id_ed25519
```

Depois, em **Settings > Connections** no app, adicione e habilite o host SSH.

> Conexões remotas usam SSH para iniciar e gerenciar o servidor remoto. Não exponha o servidor do app em redes compartilhadas ou públicas. Use VPN ou rede mesh para acesso fora da sua rede local.

---

## 2. Subagentes: trabalho paralelo

### O que são

Subagentes são instâncias adicionais do Codex que trabalham em tarefas especializadas em paralelo. O Codex cria ("spawna") esses agentes quando você pede explicitamente, coordena a execução entre eles e consolida os resultados em uma resposta unificada.

**Analogia:** é como montar um time temporário para um projeto específico. Você define os papéis, o Codex recruta e coordena.

**Importante:** o Codex só cria subagentes quando você pede explicitamente. Não acontece automaticamente.

### Agentes nativos disponíveis

| Agente | Foco |
|---|---|
| `default` | Uso geral |
| `worker` | Execução e implementação |
| `explorer` | Leitura e exploração de codebase |

### Criar agentes customizados

Adicione arquivos TOML em `~/.codex/agents/` (pessoal) ou `.codex/agents/` (repositório):

```toml
name = "revisor"
description = "Revisa PRs focando em correção, segurança e testes"
model = "gpt-5.4"
sandbox_mode = "read-only"
developer_instructions = """
Revise código como um proprietário. Priorize correção, segurança,
regressões de comportamento e cobertura de testes ausente.
"""
```

**Campos disponíveis:** `name`, `description`, `developer_instructions` (obrigatórios); `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config` (opcionais).

### Configurações globais de subagentes

No `config.toml`:

| Parâmetro | Padrão | Função |
|---|---|---|
| `agents.max_threads` | 6 | Limite de threads de agente concorrentes |
| `agents.max_depth` | 1 | Profundidade de aninhamento de subagentes |
| `agents.job_max_runtime_seconds` | 1800 | Timeout por worker (30 min) |

### Gerenciar subagentes em execução

- No CLI: `/agent` para alternar entre threads de agente ativas
- No app: solicite ao Codex para dirigir um subagente em execução, interrompê-lo ou fechar threads concluídas
- Aprovações de subagentes mostram o rótulo da thread de origem no overlay

---

## 3. Gestão de threads: o que está confirmado

As docs oficiais confirmam os seguintes recursos de gestão de threads:

### Confirmado nas docs oficiais

**Gestão conversacional:** você pode pedir ao Codex, em linguagem natural, para:
- Encontrar uma thread relacionada
- Continuar uma thread existente
- Fixar (pin) uma thread
- Arquivar uma thread

Exemplo citado na documentação: "Create a separate background thread in a worktree for this project to update the tests."

**Atalhos de teclado:**

| Ação | Atalho |
|---|---|
| Nova thread | `Ctrl+N` ou `Ctrl+Shift+O` |
| Buscar threads | `Ctrl+G` |
| Thread anterior | `Ctrl+Shift+[` |
| Próxima thread | `Ctrl+Shift+]` |
| Thread fixada 1-9 | `Ctrl+1` a `Ctrl+9` |

**Deep links (para automações e scripts):**

- `codex://threads/new`: cria nova thread local
- `codex://threads/<thread-id>`: abre thread específica
- `codex://new?prompt=<texto>&path=<caminho>`: nova thread com parâmetros

### Não confirmado nas docs oficiais (recurso recente)

A newsletter de Owain Lewis (junho de 2026) descreve um conjunto de ferramentas de coordenação de threads: criar threads, listar threads, ler seu conteúdo, enviar mensagens de uma thread para outra, fixar, arquivar e definir títulos.

**Essas capacidades não encontraram correspondência completa nas docs oficiais consultadas** (app/features, app/commands, subagents). O gerenciamento conversacional (pedir ao Codex para fixar, arquivar, continuar) e a navegação por atalhos estão confirmados. A comunicação inter-thread (enviar mensagem de uma thread para outra) e a listagem ou leitura programática de threads não aparecem nas docs.

**Recomendação para o tutor:** ao tentar usar coordenação inter-thread, tente no app e verifique se a funcionalidade está disponível. Se não estiver, use o fallback via transcript descrito abaixo.

---

## 4. Fallback: ler histórico via transcripts locais

Quando a gestão inter-thread não estiver disponível, o tutor pode supervisionar sessões lendo os arquivos de transcript que o Codex grava automaticamente no disco.

### Onde ficam os transcripts

```
%USERPROFILE%\.codex\sessions\<AAAA>\<MM>\<DD>\rollout-<timestamp>-<uuid>.jsonl
```

Exemplo real:
```
C:\Users\User\.codex\sessions\2026\06\10\rollout-2026-06-10T16-55-04-019eb31a.jsonl
```

### O índice de sessões

O arquivo `%USERPROFILE%\.codex\session_index.jsonl` lista todas as sessões com os campos:

- `id`: identificador único da sessão
- `thread_name`: nome da thread
- `updated_at`: data da última atualização

Use este índice para localizar uma sessão por nome de thread sem varrer todas as pastas.

### Formato do arquivo de transcript

O arquivo começa com uma linha obrigatória de metadados (`session_meta`), seguida dos eventos da conversa:

```json
// Linha 1: sempre "session_meta"
{
  "type": "session_meta",
  "payload": {
    "id": "uuid-da-sessão",
    "cwd": "E:\\caminho\\do\\projeto",
    "originator": "Codex Desktop",
    "cli_version": "0.137.0-alpha.4",
    "model_provider": "openai"
  }
}
```

### Como identificar sessões de um projeto

1. Leia apenas a primeira linha de cada arquivo `rollout-*.jsonl`
2. Filtre por `payload.cwd` igual ao caminho do projeto
3. Alternativa mais rápida: use o `session_index.jsonl` para obter o `id` e monte o caminho `sessions/<AAAA>/<MM>/<DD>/rollout-*<id>.jsonl`

### Campos úteis

- `payload.cwd`: diretório do projeto (identificação primária)
- `payload.id`: UUID da sessão
- `payload.originator`: `"Codex Desktop"` (confirma que é app, não CLI)
- `payload.model_provider`: `"openai"` (confirma Codex)
- `payload.cli_version`: versão instalada

**Observação:** threads em nuvem não têm arquivo local. Os transcripts existem apenas para sessões locais.

---

## 5. Tarefas em nuvem

O Codex permite executar tarefas em ambientes de nuvem configurados (modo Cloud nas threads). Nesse modo, a execução ocorre no ambiente remoto configurado, não na máquina local. As configurações de ambiente, credenciais e projetos precisam estar disponíveis no ambiente remoto.

Para configurar: **Settings > Agent Configuration** (ou edite `.codex/config.toml` para opções avançadas de ambiente remoto).
