# Referência: App Codex, Windows (desktop)

> Destilado das docs oficiais em 10/06/2026

O Codex é um aplicativo desktop disponível para macOS e Windows. Ele permite trabalhar em várias tarefas ao mesmo tempo, em projetos diferentes, com suporte nativo a Git, automações e ferramentas integradas. Esta referência cobre a interface, os recursos e o comportamento esperado no Windows.

---

## 1. Janelas e projetos

O Codex organiza o trabalho em **projetos**: cada projeto corresponde a uma pasta no seu computador. Você pode adicionar projetos clicando em **Add new project** ou pressionando `Ctrl+O`. Para remover um projeto da barra lateral, passe o mouse sobre o nome, clique nos três pontos e escolha **Remove**.

**Múltiplas janelas:** threads ativas podem ser destacadas em janelas flutuantes separadas. A janela pode ser configurada para ficar sempre visível por cima de outros aplicativos (modo "always on top"), útil para acompanhar progresso enquanto trabalha em outra ferramenta.

**Projetos e monorepos:** se o repositório contém vários serviços, abra cada diretório como um projeto separado para manter o isolamento correto do sandbox.

---

## 2. Threads: organização e navegação

Uma thread (conversa) é a unidade básica de trabalho. Cada thread tem um modo de execução, um histórico de mensagens e um terminal próprio.

**Criar uma thread:** `Ctrl+N` ou `Ctrl+Shift+O`.

**Navegar entre threads:** `Ctrl+Shift+[` (anterior) e `Ctrl+Shift+]` (próxima).

**Buscar threads:** `Ctrl+G`.

**Fixar (pin):** threads importantes podem ser fixadas na barra lateral para acesso rápido. Threads fixadas recebem atalhos numéricos: `Ctrl+1` a `Ctrl+9` navegam diretamente para as primeiras nove threads fixadas.

**Renomear:** clique no nome da thread ou peça ao Codex para renomeá-la diretamente no chat.

**Arquivar:** threads concluídas podem ser arquivadas para manter a barra lateral limpa. Threads arquivadas ficam acessíveis em **Settings > Archived Threads**. Para restaurar, use **Unarchive**.

**Chats:** threads que não precisam de pasta de projeto ou Git ficam na seção **Chats**, armazenadas por padrão em `~/.codex/threads`.

---

## 3. Modos de execução (Local, Worktree, Cloud)

Cada thread opera em um de três modos, escolhido antes de enviar o primeiro prompt:

- **Local:** o Codex trabalha diretamente na pasta do projeto. As alterações afetam os arquivos imediatamente.
- **Worktree:** cria uma cópia isolada via Git worktree. Ideal para testar ideias sem afetar o trabalho em andamento. O worktree é descartado ou integrado ao final.
- **Cloud:** execução em ambiente remoto configurado. Útil quando o projeto já vive em servidor ou quando a máquina local não deve ser usada para processamento pesado.

**Sandbox no Windows:** o agente roda nativamente em PowerShell com sandbox próprio (sem exigir WSL), com permissões delimitadas.

**WSL2 (opcional):** se o projeto vive no WSL2, acesse via `\\wsl$\` no explorador de arquivos e, em **Settings**, alterne o agente de "Windows nativo" para WSL antes de abrir o projeto.

---

## 4. Aprovações e sandbox

O Codex pode ser configurado para pedir confirmação antes de executar ações. As opções de aprovação controlam quando ele pausa:

- **Sempre pedir aprovação:** o Codex solicita permissão antes de cada ação significativa.
- **Aprovar automaticamente:** o Codex executa sem interrupção (recomendado apenas após conhecer bem o projeto).

O **sandbox** restringe acesso a diretórios e rede. Por padrão, o trabalho fica limitado à pasta do projeto atual.

---

## 5. Terminal integrado

Cada thread inclui um terminal próprio. Abra ou feche com `Ctrl+J`.

Usos comuns: verificar status do servidor, rodar testes, executar Git, inspecionar logs. O Codex pode ler o output atual do terminal para ajustar o trabalho (por exemplo: ver uma falha de build e corrigi-la automaticamente).

**Configuração do terminal (Windows):** em **Settings**, escolha entre PowerShell, Prompt de Comando, Git Bash ou WSL. A alteração vale para novas sessões de terminal.

---

## 6. Painel lateral e artefatos

O painel lateral (barra à direita da conversa) exibe o trabalho produzido: código, documentos, planilhas, apresentações e PDFs. Para abrir ou fechar: `Ctrl+B`.

O Codex pode gerar e exibir nesse painel:

- **Páginas HTML** estáticas (um arquivo `index.html` funciona como artefato interativo durável, sem servidor necessário)
- **PDFs e documentos**
- **Planilhas e tabelas de dados**
- **Decks de apresentação** (slides baseados em navegador)

Para **anotar** um artefato aberto (indicar o que mudar), use o modo de anotação do navegador integrado (detalhado na seção do browser).

O painel de **diff** mostra alterações de código com comentários inline. Para abrir: `Ctrl+Option+B`. Para comentar em uma linha específica: clique sobre ela no diff, escreva o feedback e envie.

---

## 7. Voz (ditado)

Mantenha pressionado `Ctrl+M` para ativar o ditado. O Codex transcreve o áudio em texto no compositor. Você pode editar o texto antes de enviar ou enviá-lo diretamente.

O ditado é especialmente útil para:

- Pensamentos vagos que são mais fáceis de falar do que escrever
- Dumps de contexto rápidos antes de uma tarefa estar totalmente formada
- Transcrições brutas de reuniões como insumo para uma tarefa

---

## 8. Steering e queuing (dirigir e enfileirar)

Enquanto o Codex trabalha em uma tarefa, você pode:

- **Steering (correção em voo):** enviar uma instrução que muda o que o Codex está fazendo agora, antes de terminar o passo atual. Exemplo: "deixa isso menor" ou "esse espaçamento está errado". O agente ajusta o rumo imediatamente.
- **Queuing (fila):** adicionar uma instrução para ser executada depois que o passo atual terminar, sem interromper. Exemplo: "quando terminar, manda o link de preview para o Slack". O Codex executa assim que concluir o passo em andamento.

Steering muda o que acontece agora. Queuing agenda o que vem a seguir.

---

## 9. Geração de imagens ($imagegen)

Dentro de uma thread, você pode pedir ao Codex para gerar ou editar imagens em linguagem natural, ou invocar explicitamente com `$imagegen`. O modelo usado é o `gpt-image-2`. O uso conta no limite geral de tokens do Codex.

---

## 10. Memórias

Quando disponível (verificar em **Settings > Personalization > Memories**), o Codex carrega contexto de sessões anteriores para a thread atual. Útil para preferências estáveis, convenções de projeto e padrões recorrentes.

As memórias complementam o arquivo `AGENTS.md` (instrução escrita e explícita) sem substituí-lo. Para contexto crítico, sempre escreva em arquivo; as memórias são uma camada adicional de conveniência.

---

## 11. Configurações principais

Acesse em `Ctrl+,` ou pelo menu do aplicativo.

| Seção | O que configura |
|---|---|
| Geral | Onde arquivos abrem, output de comandos, prevenção de suspensão |
| Atalhos de teclado | Revise, altere ou redefina atalhos |
| Notificações | Quando o app notifica conclusão ou pedido de aprovação |
| Git | Padrão de nomes de branch, force push, mensagens de commit |
| Integrações e MCP | Conectar ferramentas externas via Model Context Protocol |
| Uso do navegador | Plugin de browser, extensão Chrome, sites permitidos |
| Computer Use | Gerenciar acesso a apps desktop |
| Personalização | Personalidade (Friendly, Pragmatic, None), instruções personalizadas |
| Memórias | Ativar/desativar memória entre sessões |
| Threads arquivadas | Listar e restaurar threads arquivadas |

---

## 12. Appshots (macOS apenas)

Appshots capturam a janela frontal de qualquer app Mac (imagem + texto disponível) e enviam esse contexto para uma thread do Codex. Ativados com um atalho de teclado configurável. Útil para compartilhar erros, painéis de configuração ou visualizações difíceis de descrever em texto.

**Nota:** recurso exclusivo do macOS. Não disponível no Windows.

---

## 13. Atualização do app

O Codex atualiza automaticamente quando há nova versão. Para verificar a versão instalada: abra o menu do app. Se um recurso funciona no CLI mas não no app, verifique se ambos estão na mesma versão (o CLI pode ter recebido o recurso primeiro).

---

## 14. Troubleshooting básico no Windows

**Thread aparece travada:**
1. Verifique se o Codex aguarda aprovação (pode estar minimizado).
2. Execute um comando simples como `git status` no terminal da thread.
3. Se não resolver, inicie uma nova thread com um prompt menor e mais focado.

**Terminal travado:** feche o painel (`Ctrl+J`), reabra e execute `pwd` ou `git status`.

**Threads não aparecem na barra lateral:** clique no ícone de filtro ao lado de **Threads** e mude para "Chronological".

**Política de execução do PowerShell bloqueando scripts:**
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

**Permissões elevadas:** inicie o Codex como administrador para que o agente herde esse nível de permissão.

**Logs de sessão:** `%USERPROFILE%\.codex\sessions\AAAA\MM\DD\rollout-*.jsonl`

**Pasta home do Codex no Windows:** `%USERPROFILE%\.codex`

---

## 15. Atalhos de referência rápida

| Ação | Atalho |
|---|---|
| Menu de comandos | `Ctrl+Shift+P` ou `Ctrl+K` |
| Configurações | `Ctrl+,` |
| Abrir pasta | `Ctrl+O` |
| Nova thread | `Ctrl+N` ou `Ctrl+Shift+O` |
| Buscar threads | `Ctrl+G` |
| Thread anterior/próxima | `Ctrl+Shift+[` / `Ctrl+Shift+]` |
| Thread fixada 1-9 | `Ctrl+1` a `Ctrl+9` |
| Ditado por voz | `Ctrl+M` (manter pressionado) |
| Abrir/fechar terminal | `Ctrl+J` |
| Abrir/fechar painel lateral | `Ctrl+B` |
| Abrir/fechar painel de diff | `Ctrl+Option+B` |
| Limpar terminal | `Ctrl+L` |
| Browser integrado | `Ctrl+Shift+B` |
