# Referência: Contexto e Memória no Claude Code Desktop

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.

---

## O que é contexto no Claude Code

Cada sessão começa com uma janela de contexto vazia. Duas coisas carregam conhecimento entre sessões:

- **Arquivos CLAUDE.md**: instruções que você escreve para o Claude ter contexto persistente.
- **Auto memory**: notas que o Claude escreve automaticamente com base nas suas correções e preferências.

Pense assim: CLAUDE.md é o que você quer que o Claude saiba sempre; auto memory é o que o Claude aprendeu sozinho com o tempo.

---

## CLAUDE.md: instruções persistentes

### O que é

Um arquivo de texto simples em Markdown. O Claude lê no início de cada sessão. Use para:

- Padrões de código do projeto (indentação, imports, nomeclatura)
- Comandos de build e teste
- Decisões de arquitetura que o Claude não consegue descobrir sozinho
- Regras de fluxo de trabalho ("sempre rode o lint antes de commitar")
- Convenções que seriam necessárias explicar a um novo desenvolvedor

### Onde colocar (escopos, do mais amplo ao mais específico)

| Escopo | Localização | Compartilhado com |
|--------|-------------|-------------------|
| Organização (gerenciado por TI) | `C:\Program Files\ClaudeCode\CLAUDE.md` | Todos na empresa |
| Pessoal (todos os projetos) | `%USERPROFILE%\.claude\CLAUDE.md` | Só você |
| Projeto (equipe) | `./CLAUDE.md` ou `./.claude/CLAUDE.md` | Equipe (via git) |
| Pessoal local (projeto atual) | `./CLAUDE.local.md` | Só você (não commitar) |

Todos são carregados ao mesmo tempo, concatenados. Instruções mais próximas da pasta atual têm precedência.

### Como escrever bem

Use markdown com cabeçalhos e bullets. Seja concreto e verificável:

- "Use indentação de 2 espaços" (bom) vs. "Formate o código corretamente" (vago)
- "Rode `npm test` antes de commitar" (bom) vs. "Teste as mudanças" (vago)
- "Handlers de API ficam em `src/api/handlers/`" (bom) vs. "Mantenha os arquivos organizados" (vago)

**Tamanho recomendado**: menos de 200 linhas por arquivo. Arquivos maiores reduzem a aderência.

**O que incluir:**
- Comandos que o Claude não conseguiria adivinhar
- Regras de estilo que diferem do padrão
- Decisões arquiteturais específicas do projeto
- Variáveis de ambiente necessárias
- Armadilhas não óbvias do projeto

**O que não incluir:**
- Coisas que o Claude já sabe pelas convenções da linguagem
- Documentação detalhada de APIs (coloque um link)
- Informações que mudam frequentemente

### Como criar o CLAUDE.md inicial

Rode `/init` em qualquer sessão. O Claude analisa o projeto e gera um arquivo com comandos de build, instruções de teste e convenções descobertas. Se o arquivo já existe, o `/init` sugere melhorias.

### Importar outros arquivos

Use a sintaxe `@caminho/do/arquivo` dentro do CLAUDE.md para importar outros arquivos:

```
Veja @README.md para visão geral do projeto e @package.json para comandos npm.

# Instruções adicionais
- Fluxo de git: @docs/instrucoes-git.md
```

Os arquivos importados são carregados no contexto junto com o CLAUDE.md.

### Regras por pasta: `.claude/rules/`

Para projetos grandes, organize instruções em múltiplos arquivos dentro de `.claude/rules/`. Cada arquivo cobre um tema (ex: `tests.md`, `api-design.md`). Você pode limitar quando uma regra é carregada por padrão de arquivo (frontmatter `paths`):

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# Regras para endpoints de API
- Todos os endpoints devem incluir validação de entrada
- Use o formato padrão de resposta de erro
```

Regras sem `paths` são carregadas em toda sessão. Regras com `paths` carregam apenas quando o Claude trabalha com arquivos correspondentes, economizando contexto.

### Ver e editar via `/memory`

O comando `/memory` lista todos os arquivos CLAUDE.md e CLAUDE.local.md carregados na sessão atual. Selecione um para abrir no editor.

**Nota sobre o app desktop:** o comando `/config` (diálogo interativo de configurações) não está disponível na aba Code do app desktop. Para editar configurações, edite os arquivos de settings diretamente ou use o `/memory`.

---

## Auto memory: o Claude aprende sozinho

### O que é

O Claude acumula conhecimento entre sessões sem você precisar escrever nada. Ele salva notas quando detecta algo útil para o futuro: comandos de build, padrões de depuração, preferências de código, fluxos de trabalho habituais.

**Requisito:** Claude Code v2.1.59 ou posterior.

### Onde fica

Cada projeto tem sua própria pasta:

```
%USERPROFILE%\.claude\projects\<projeto>\memory\
├── MEMORY.md        # Índice conciso, carregado em toda sessão
├── debugging.md     # Notas detalhadas sobre padrões de debug
├── api-conventions.md
└── ...outros arquivos por tema
```

O `<projeto>` é derivado do repositório git (ou da pasta raiz do projeto quando não há git). Todos os worktrees e subpastas do mesmo repositório compartilham a mesma pasta de memória.

### Como funciona

- As primeiras 200 linhas de `MEMORY.md` (ou 25 KB, o que vier primeiro) são carregadas em toda sessão.
- Arquivos de tema (`debugging.md`, etc.) só são carregados quando o Claude os busca sob demanda.
- O Claude decide o que vale lembrar. Não salva a cada sessão, apenas quando julga relevante para o futuro.
- Quando você vê "Writing memory" ou "Recalled memory" na interface, o Claude está atualizando ou lendo sua memória.

### Como ativar ou desativar

Auto memory é ativado por padrão. Para desativar, abra `/memory` em uma sessão e use o toggle, ou edite `.claude/settings.json`:

```json
{
  "autoMemoryEnabled": false
}
```

### Auditar e editar a memória

Os arquivos de memória são Markdown simples que você pode ler, editar ou apagar. Use `/memory` para navegar e abrir os arquivos de memória.

Quando você pede para o Claude lembrar algo ("sempre use pnpm, não npm"), ele salva na memória automática. Para adicionar ao CLAUDE.md em vez da memória automática, peça explicitamente: "adicione isso ao CLAUDE.md".

---

## Settings: arquivo de configuração

As configurações do Claude Code ficam em arquivos JSON com escopos:

| Escopo | Arquivo | Compartilhado com |
|--------|---------|-------------------|
| Gerenciado (TI) | `C:\Program Files\ClaudeCode\managed-settings.json` | Todos |
| Usuário | `%USERPROFILE%\.claude\settings.json` | Só você (todos projetos) |
| Projeto | `.claude/settings.json` | Equipe (via git) |
| Local | `.claude/settings.local.json` | Só você (projeto atual) |

**Prioridade:** Gerenciado > linha de comando > Local > Projeto > Usuário.

Configurações importantes:

| Chave | Função |
|-------|--------|
| `autoMemoryEnabled` | Ativa/desativa auto memory |
| `outputStyle` | Estilo de resposta (Default, Proactive, Explanatory, Learning) |
| `permissions.allow/deny` | Regras de permissão para ferramentas |
| `hooks` | Comandos automáticos em eventos do ciclo de vida |
| `env` | Variáveis de ambiente para todas as sessões |
| `language` | Idioma preferido para respostas |

A maioria das configurações recarrega automaticamente quando o arquivo muda, sem reiniciar. Exceção: `model` e `outputStyle` precisam de `/clear` ou nova sessão para ter efeito.

---

## Output styles: como o Claude responde

Os estilos de saída mudam como o Claude responde, não o que ele sabe. São quatro estilos integrados:

| Estilo | Comportamento |
|--------|---------------|
| **Default** | Comportamento padrão para tarefas de desenvolvimento |
| **Proactive** | Executa imediatamente, assume decisões razoáveis, prefere ação sobre planejamento |
| **Explanatory** | Adiciona insights educativos "entre" as tarefas; explica escolhas de implementação |
| **Learning** | Modo colaborativo: Claude deixa marcadores `TODO(human)` para você implementar partes estratégicas |

Para trocar o estilo: use `/config` (CLI) ou edite o campo `outputStyle` em qualquer arquivo de settings. A mudança tem efeito após `/clear` ou em nova sessão.

Estilos personalizados também são possíveis: crie um arquivo Markdown em `.claude/output-styles/` com frontmatter e instruções. Use `keep-coding-instructions: true` se quiser manter o comportamento de desenvolvimento e apenas mudar o tom ou formato.

---

## Ciclo de vida do contexto na sessão

1. **Na abertura da sessão:** CLAUDE.md de todos os escopos são carregados, as primeiras 200 linhas do MEMORY.md são carregadas.
2. **Ao longo da sessão:** Regras com `paths` carregam quando o Claude abre arquivos correspondentes. Arquivos de tema de memória carregam sob demanda.
3. **Ao compactar com `/compact`:** O CLAUDE.md da raiz do projeto é reinjetado. CLAUDE.md em subpastas recarregam quando o Claude trabalha em arquivos dessas pastas.
4. **Na auto memory:** Durante a sessão, o Claude pode escrever na pasta de memória. Ao final, pode salvar aprendizados relevantes.

---

## Perguntas frequentes

**O Claude não está seguindo meu CLAUDE.md. Por que?**
Use `/memory` para verificar se o arquivo está sendo carregado. Se estiver, verifique: o arquivo pode estar muito longo (acima de 200 linhas), as instruções podem estar vagas ou contraditórias. Torne-as mais específicas.

**O que acontece depois de `/compact`?**
O CLAUDE.md da raiz do projeto é reinjetado automaticamente. Instruções que só existiam na conversa (não em arquivo) são perdidas: adicione-as ao CLAUDE.md.

**Posso ter vários CLAUDE.md em subpastas?**
Sim. O Claude carrega os CLAUDE.md ao longo da árvore de diretórios. Os das subpastas carregam sob demanda quando o Claude trabalha em arquivos daquela pasta.

**Qual a diferença entre CLAUDE.md e skills?**
CLAUDE.md é carregado em toda sessão (custo sempre presente). Skills carregam apenas quando invocadas ou relevantes (custo zero quando não usadas). Use CLAUDE.md para fatos que precisam estar sempre presentes; skills para procedimentos e fluxos reutilizáveis.
