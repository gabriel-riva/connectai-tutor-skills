# Referência: App Claude Code Desktop e Sessões (app Claude Code desktop, Windows)

> Destilado das docs oficiais em 10/06/2026

---

## O que é o Claude Code Desktop

O Claude Code Desktop é o aplicativo de mesa da Anthropic disponível para Windows e macOS. O app tem três abas: **Chat** (conversa geral sem acesso a arquivos), **Cowork** (trabalho autônomo em nuvem) e **Code** (assistente de desenvolvimento com acesso direto aos seus arquivos locais). Esta referência cobre exclusivamente a aba **Code**.

O app não está disponível para Linux. No Linux, existe somente a versão de linha de comando (CLI), que não é o foco desta skill.

**Requisito no Windows:** Git for Windows precisa estar instalado antes de abrir a aba Code. Reinicie o app após instalar o Git.

**Versão mínima para recursos avançados:** Claude Desktop v1.2581.0 ou superior para sistema de painéis e visualização dupla de sessões. Acesse "Help > Check for Updates" no Windows para verificar.

---

## Sessões: a unidade de trabalho

Na aba Code, cada conversa é uma **sessão**. Cada sessão tem seu próprio histórico de chat, pasta de projeto e alterações de código, completamente independente de outras sessões abertas ao mesmo tempo.

**Analogia:** pense em cada sessão como uma mesa de trabalho separada. Você pode ter várias mesas abertas ao mesmo tempo, cada uma com seu próprio projeto e contexto.

### Criar uma nova sessão

- Clique em **+ New session** na barra lateral, ou
- Pressione **Ctrl+N** no Windows.

Antes de enviar a primeira mensagem, configure:

1. **Ambiente:** escolha **Local** (arquivos do seu computador), **Remote** (nuvem da Anthropic) ou **SSH** (servidor remoto).
2. **Pasta do projeto:** selecione a pasta ou repositório onde o Claude vai trabalhar.
3. **Modelo:** escolha o modelo na lista próxima ao botão de envio.
4. **Modo de permissão:** define quanto o Claude pode fazer sozinho (veja seção abaixo).

### Isolamento entre sessões em repositórios Git

Quando a pasta do projeto é um repositório Git, cada sessão paralela recebe uma cópia isolada chamada **worktree**. As alterações de uma sessão não afetam as outras até que você as confirme (commit). Em pastas comuns sem Git, todas as sessões trabalham diretamente na mesma pasta, o que pode causar conflitos se duas sessões editarem o mesmo arquivo.

**Implicação importante para oficinas e treinamentos:** nunca use uma pasta Git para sessões de prática paralelas com alunos. Use pastas simples (sem git init).

---

## Barra lateral e navegação entre sessões

A barra lateral lista todas as sessões abertas. Use os controles no topo para filtrar por status, projeto ou ambiente, e para agrupar sessões por projeto.

**Atalhos de navegação:**

| Atalho | Ação |
|--------|------|
| Ctrl+Tab / Ctrl+Shift+Tab | Próxima ou sessão anterior |
| Ctrl+N | Nova sessão |
| Ctrl+W | Fechar sessão |

### Visualização de duas sessões lado a lado (split view)

Para ver duas sessões ao mesmo tempo:

1. Segure **Ctrl** e clique em uma sessão na barra lateral.
2. A sessão abre em um segundo painel ao lado da sessão já aberta.
3. Enquanto o split está ativo, clicar em outra sessão na barra lateral substitui o painel que está com foco.
4. Pressione **Ctrl+\\** para fechar o painel com foco e voltar a uma única sessão.

**Ctrl+Tab** alterna entre os painéis abertos.

---

## Sistema de painéis (workspace)

A aba Code é construída em torno de painéis que você pode organizar como quiser: chat, diff, preview, terminal, arquivo, plano, tarefas e subagente.

- **Arrastar** um painel pelo cabeçalho para reposicioná-lo.
- **Arrastar** a borda de um painel para redimensioná-lo.
- **Ctrl+\\** fecha o painel com foco.
- Menu **Views** na barra de ferramentas da sessão para abrir painéis adicionais.

**Acesso rápido:**

| Atalho | Painel |
|--------|--------|
| Ctrl+` | Terminal integrado |
| Ctrl+Shift+D | Painel de diff |
| Ctrl+Shift+P | Painel de preview |
| Ctrl+O | Alterna modos de visualização |

---

## Preview de artefatos

O painel de preview abre arquivos do projeto diretamente:

- Clique em um caminho de arquivo HTML, PDF, imagem ou vídeo no chat para abrir no painel de preview.
- O Claude pode iniciar um servidor de desenvolvimento e abrir o app em execução no preview para verificar suas próprias alterações.

O preview também permite que o Claude verifique automaticamente as mudanças após cada edição (auto-verify), tirando screenshots, inspecionando o DOM e corrigindo problemas que ele mesmo encontra.

---

## Side chats (perguntas rápidas sem desviar a sessão)

Um side chat permite fazer uma pergunta que usa o contexto da sessão atual sem adicionar nada de volta à conversa principal. Use quando quiser entender um trecho de código ou checar uma suposição sem desviar o fio da sessão.

- Pressione **Ctrl+;** ou digite **/btw** no campo de mensagem.
- O side chat pode ler tudo do chat principal até aquele ponto.
- Ao fechar o side chat, a sessão principal continua exatamente onde estava.

---

## Ditado por voz

O ditado por voz transcreve a fala diretamente no campo de mensagem. Funciona no app desktop no Windows (requer autenticação com conta claude.ai, não apenas chave de API).

Como usar:

1. Ative com o comando `/voice` em uma sessão (atenção: este é um comando da CLI; no app desktop, verifique no app se existe botão de microfone ou configuração equivalente).
2. Dois modos disponíveis: **hold** (segure a tecla para gravar, solte para finalizar) e **tap** (toque para começar, toque novamente para enviar).

O áudio é enviado aos servidores da Anthropic para transcrição. Não há processamento local de áudio.

---

## Fast mode

Fast mode é uma configuração de alta velocidade para o modelo Claude Opus, tornando-o até 2,5x mais rápido com custo por token maior.

- Use `/fast` para ativar ou desativar. No app desktop, há também o atalho **Meta+O**.
- Disponível somente com modelos Opus (4.6, 4.7 e 4.8).
- Requer créditos de uso ativados na conta.
- O indicador `↯` aparece no campo de mensagem quando fast mode está ativo.

Use fast mode para iterações rápidas e depuração ao vivo. Para tarefas longas e autônomas, o custo adicional raramente compensa.

---

## Checkpointing: desfazer alterações

O Claude Code rastreia automaticamente as alterações de arquivo antes de cada edição. Esse mecanismo permite desfazer mudanças e retornar a estados anteriores.

- Cada mensagem enviada cria um novo checkpoint.
- Os checkpoints persistem entre sessões.

**Como usar:**

1. Pressione **Esc duas vezes** com o campo de mensagem vazio, ou
2. Digite `/rewind` no campo de mensagem.

O menu de rewind lista cada mensagem enviada na sessão. Selecione o ponto desejado e escolha uma ação:

| Ação | O que faz |
|------|-----------|
| Restore code and conversation | Reverte código e conversa para aquele ponto |
| Restore conversation | Reverte só a conversa, mantém o código atual |
| Restore code | Reverte só o código, mantém a conversa |
| Summarize from here | Comprime a conversa a partir desse ponto (libera espaço de contexto) |
| Summarize up to here | Comprime a conversa até esse ponto |

**Limitação importante:** o checkpointing rastreia apenas arquivos editados pelas ferramentas do Claude. Arquivos modificados por comandos Bash (como `rm`, `mv`, `cp`) não são rastreados. O checkpointing complementa o Git, mas não substitui o controle de versão.

---

## Modos de permissão

Os modos de permissão controlam quanto autonomia o Claude tem durante a sessão.

| Modo | Comportamento |
|------|---------------|
| **Ask permissions** (padrão) | O Claude pede aprovação antes de editar arquivos ou executar comandos. Recomendado para iniciantes. |
| **Auto accept edits** | O Claude aceita automaticamente edições de arquivo e comandos básicos de sistema de arquivos (mkdir, touch, mv). Outros comandos ainda pedem aprovação. |
| **Plan mode** | O Claude lê arquivos e propõe um plano sem editar o código. Bom para tarefas complexas onde você quer revisar a abordagem primeiro. |
| **Auto** | O Claude executa ações com verificações de segurança em segundo plano. Pesquisa prévia disponível para usuários com API Anthropic e Opus 4.6 ou mais recente. |
| **Bypass permissions** | O Claude executa sem prompts de permissão. Use somente em ambientes isolados (contêineres ou VMs). |

O modo `dontAsk` está disponível somente na CLI, não no app desktop.

---

## Comandos e atalhos no app desktop

### Atalhos principais (Windows)

| Atalho | Ação |
|--------|------|
| Ctrl+/ | Mostrar todos os atalhos |
| Ctrl+N | Nova sessão |
| Ctrl+W | Fechar sessão |
| Ctrl+Tab | Próxima sessão |
| Ctrl+Shift+Tab | Sessão anterior |
| Esc | Interromper resposta do Claude |
| Ctrl+Shift+D | Alternar painel de diff |
| Ctrl+Shift+P | Alternar painel de preview |
| Ctrl+` | Alternar terminal |
| Ctrl+\\ | Fechar painel com foco |
| Ctrl+; | Abrir side chat |
| Ctrl+O | Alternar modos de visualização |
| Ctrl+Shift+M | Menu de modo de permissão |
| Ctrl+Shift+I | Menu de modelo |

### Comandos indisponíveis no app desktop

Os seguintes comandos existem na CLI mas não funcionam no app (respondem com "isn't available in this environment"):

- `/permissions` (gerenciar permissões)
- `/config` (abrir configurações interativas)
- `/agents` (gerenciar agentes)
- `/doctor` (diagnósticos)

Para configurar permissões e settings no app, edite os arquivos de configuração diretamente (veja seção Contexto e Memória).

---

## Glossário básico

| Termo | Significado |
|-------|-------------|
| **Sessão** | Uma conversa com o Claude ligada a uma pasta de projeto. Tem histórico, contexto e alterações próprios. |
| **Worktree** | Cópia isolada de um repositório Git criada automaticamente para cada sessão paralela. |
| **CLAUDE.md** | Arquivo de instruções persistentes que o Claude lê no início de cada sessão. |
| **MCP** | Model Context Protocol: protocolo para conectar ferramentas externas ao Claude. |
| **Skill** | Arquivo de instruções reutilizáveis que o Claude carrega quando relevante ou ao ser invocado com `/nome`. |
| **Plugin** | Pacote instalável que adiciona skills, agentes, hooks e servidores MCP ao Claude. |
| **Checkpoint** | Estado salvo do código antes de cada edição, usado para desfazer alterações. |
| **Contexto** | Tudo que está na janela de contexto do Claude: histórico da conversa, arquivos lidos, outputs de comandos. |
| **Diff** | Visualização das alterações de código linha por linha (o que foi adicionado e removido). |
| **Side chat** | Pergunta rápida com o contexto da sessão que não polui a conversa principal. |

---

## Troubleshooting básico

**Erro 403 ou falha de autenticação na aba Code:**
1. Saia e entre novamente pelo menu do app.
2. Verifique se tem assinatura ativa (Pro, Max, Team ou Enterprise).
3. Feche o app completamente (não só a janela) e reabra.

**Git is required / código de erro de Git:**
No Windows, Git for Windows precisa estar instalado. Baixe em git-scm.com/downloads/win, instale e reinicie o app.

**Tela em branco ou travada ao abrir:**
1. Reinicie o app.
2. Verifique atualizações pendentes (Help > Check for Updates).

**Ferramentas não encontradas (npm, node, etc.):**
Verifique se as ferramentas funcionam no terminal comum do Windows. Reinicie o app para recarregar variáveis de ambiente.

**Como verificar a versão do app:**
Help > About (Windows).

---

## Recursos adicionais mencionados nesta referência

- Sistema de permissões detalhado: ver `boas-praticas.md`
- Contexto e memória (CLAUDE.md, settings): ver `contexto.md`
- Skills, plugins e MCP: ver `skills-plugins.md`
- Automações e agendamento: ver `automacoes.md`
- Controle remoto e mobile: ver `remoto-orquestracao.md`
- Computer use e Chrome: ver `computer-browser.md`
