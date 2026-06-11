# Referência: Skills, Plugins e MCP no Claude Code Desktop

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.

---

## Skills: instruções reutilizáveis sob demanda

### O que são

Skills estendem o que o Claude sabe fazer. Crie um arquivo `SKILL.md` com instruções e o Claude o adiciona ao seu repertório. O Claude usa skills quando julga relevante, ou você invoca diretamente com `/nome-da-skill`.

**Por que usar skills em vez de CLAUDE.md?**
CLAUDE.md carrega em toda sessão (consome tokens sempre). Skills carregam apenas quando invocadas ou relevantes (custo zero quando não usadas). Use skills para procedimentos longos, fluxos de trabalho passo a passo ou conteúdo de referência que só importa às vezes.

### Onde ficam

| Local | Caminho | Aplica a |
|-------|---------|----------|
| Pessoal | `%USERPROFILE%\.claude\skills\<nome>\SKILL.md` | Todos os seus projetos |
| Projeto | `.claude\skills\<nome>\SKILL.md` | Este projeto |
| Plugin | Dentro do plugin | Onde o plugin está habilitado |

### Estrutura de uma skill

Cada skill é uma pasta com `SKILL.md` como arquivo principal:

```
minha-skill/
├── SKILL.md          # Instruções principais (obrigatório)
├── template.md       # Template para o Claude preencher
├── examples/
│   └── sample.md     # Exemplo de saída esperada
└── scripts/
    └── validate.sh   # Script que o Claude pode executar
```

### Frontmatter do SKILL.md

```yaml
---
name: nome-da-skill
description: O que a skill faz e quando usá-la. O Claude usa isso para decidir quando ativar automaticamente.
disable-model-invocation: true  # Apenas você invoca; o Claude não ativa sozinho
allowed-tools: Bash(git add *) Bash(git commit *)  # Ferramentas pré-aprovadas
---

Conteúdo das instruções aqui...
```

Campos principais:

| Campo | Uso |
|-------|-----|
| `description` | Descreve quando usar. O Claude lê para decidir se ativa automaticamente. |
| `disable-model-invocation` | `true`: só você invoca com `/nome`. Útil para deploys, commits, ações com efeito colateral. |
| `user-invocable: false` | O Claude usa automaticamente, mas você não vê no menu `/`. |
| `allowed-tools` | Ferramentas que o Claude pode usar sem pedir aprovação quando esta skill está ativa. |
| `context: fork` | Executa em um subagente isolado. |
| `paths` | Padrões glob: skill só ativa quando o Claude trabalha com arquivos correspondentes. |

### Como invocar

- **Diretamente:** `/nome-da-skill` (ou `/nome-da-skill argumento`)
- **Automaticamente:** o Claude carrega a skill quando a `description` corresponde ao que você pediu
- **Com argumentos:** use `$ARGUMENTS` no corpo da skill; são substituídos pelo que você passa

```yaml
---
name: corrigir-issue
description: Corrige um issue do GitHub pelo número
disable-model-invocation: true
---

Analise e corrija o issue GitHub $ARGUMENTS seguindo nossos padrões.

1. Leia os detalhes do issue com `gh issue view`
2. Entenda o problema
3. Implemente a correção
4. Escreva testes
```

Ao rodar `/corrigir-issue 123`, o `$ARGUMENTS` é substituído por `123`.

### Injeção dinâmica de contexto

Use `` !`comando` `` para executar um comando antes de enviar a skill ao Claude. A saída substitui o marcador:

```yaml
---
description: Resumo das mudanças não commitadas
---

## Mudanças atuais

!`git diff HEAD`

## Instruções

Resuma as mudanças acima em 2-3 bullets, depois liste riscos como
tratamento de erros ausente, valores hardcoded ou testes precisando de atualização.
```

### Skills integradas (bundled)

O Claude Code inclui skills prontas: `/code-review`, `/debug`, `/loop`, `/batch`, `/run`, `/verify`. São invocadas como qualquer outra skill.

### Boa prática na oficina: revisar antes de instalar

Para alunos em capacitação, a recomendação padrão é não instalar diretamente uma skill pública encontrada em GitHub, `skills.sh` ou outro catálogo. Mesmo quando houver comando de instalação em uma linha, trate a skill como código de terceiros: leia antes, entenda antes e adapte antes.

Fluxo recomendado:

1. Copie o link da skill, repositório ou página de catálogo.
2. Peça ao Claude para analisar o `SKILL.md`, scripts, arquivos auxiliares, frontmatter e permissões.
3. Peça uma explicação em português: objetivo, público, dependências, riscos e partes aproveitáveis.
4. Crie uma skill nova, menor e específica para a rotina do aluno, em `.claude\skills`.
5. Teste com uma missão pequena antes de usar em trabalho real.

Prompt seguro:

```text
Analise esta skill pública como referência, sem instalar nada: [link].

Quero que você:
1. explique o objetivo da skill em português;
2. identifique scripts, allowed-tools, comandos e dependências;
3. aponte riscos para meus arquivos, dados ou tokens;
4. diga quais ideias servem para minha rotina;
5. crie uma skill própria para [meu processo], em vez de copiar a original inteira.
```

Referências úteis para inspiração:

| Fonte | Melhor uso | Observação |
|---|---|---|
| `https://github.com/coreyhaines31/marketingskills` | Marketing, comunicação, CRO, SEO, copywriting, anúncios e growth | Usar como biblioteca de ideias, não como pacote para instalar inteiro |
| `https://www.skills.sh/` | Descoberta por tema | O site incentiva instalação rápida; na oficina, copie o link e revise antes |
| `https://github.com/anthropics/skills` | Padrões oficiais e exemplos variados | Bom para aprender formatos e possibilidades |

Sinais de alerta antes de instalar qualquer skill externa:

- Scripts que executam comandos sem necessidade clara.
- `allowed-tools` amplo demais ou com comandos destrutivos.
- Downloads ou chamadas de rede que buscam instruções em tempo de execução.
- Pedido de tokens, senhas, chaves de API ou acesso amplo a arquivos.
- `description` genérica demais, que pode ativar a skill em momentos errados.
- Instruções que tentam substituir regras do usuário, do projeto ou do tutor.

---

## Plugins: pacotes de extensão

### O que são

Plugins agrupam skills, subagentes, hooks e servidores MCP em uma unidade instalável. Um plugin instalado adiciona tudo junto de uma vez.

### Marketplace oficial da Anthropic

O marketplace oficial (`claude-plugins-official`) está disponível automaticamente. Use `/plugin` e acesse a aba **Discover** para navegar, ou visite [claude.com/plugins](https://claude.com/plugins).

Para instalar:

```
/plugin install github@claude-plugins-official
```

### Categorias do marketplace

**Inteligência de código (LSP):** conectam servidores LSP para navegação precisa e diagnósticos automáticos após edições. Disponíveis para TypeScript, Python, Go, Rust, Java, C#, PHP, Kotlin, Lua, Swift e C/C++. Requerem o binário do servidor de linguagem instalado.

**Integrações externas:** GitHub, GitLab, Jira/Confluence, Asana, Linear, Notion, Figma, Vercel, Firebase, Supabase, Slack, Sentry.

**Workflows de desenvolvimento:** commit-commands (git), pr-review-toolkit, agent-sdk-dev, plugin-dev.

**Estilos de saída:** explanatory-output-style, learning-output-style.

**Segurança:** security-guidance (revisa cada mudança do Claude em busca de vulnerabilidades comuns).

### Gerenciar plugins

Abra `/plugin` para o gerenciador com quatro abas:

- **Discover:** navegar plugins disponíveis
- **Installed:** ver, habilitar, desabilitar ou desinstalar plugins instalados
- **Marketplaces:** adicionar, atualizar ou remover marketplaces
- **Errors:** ver erros de carregamento

Após instalar ou desabilitar um plugin, rode `/reload-plugins` para que as mudanças entrem em vigor sem reiniciar.

### Criar um plugin simples

Estrutura mínima:

```
meu-plugin/
├── .claude-plugin/
│   └── plugin.json         # Manifesto (metadados)
└── skills/
    └── saudacao/
        └── SKILL.md        # Skill do plugin
```

Manifesto `.claude-plugin/plugin.json`:

```json
{
  "name": "meu-plugin",
  "description": "Descrição do que o plugin faz",
  "version": "1.0.0",
  "author": { "name": "Seu Nome" }
}
```

Skills dentro de um plugin recebem namespace: `/meu-plugin:saudacao`. Para testar localmente, rode na CLI com `--plugin-dir ./meu-plugin`.

Plugins podem conter: `skills/`, `agents/`, `hooks/`, `.mcp.json` (servidores MCP), `.lsp.json` (servidores LSP), `output-styles/`, `monitors/` (monitores em segundo plano), `bin/` (executáveis adicionados ao PATH).

---

## MCP: conectar ferramentas externas

### O que é

MCP (Model Context Protocol) é um padrão aberto para conectar o Claude Code a ferramentas, bancos de dados e APIs externas. Com um servidor MCP conectado, o Claude pode ler e agir diretamente nesses sistemas.

**Exemplos do que dá para fazer:**
- "Implemente o que está no issue ENG-4521 do JIRA e crie um PR no GitHub."
- "Consulte o banco de dados PostgreSQL e encontre clientes inativos há 90 dias."
- "Atualize o template de e-mail com base no novo design do Figma compartilhado no Slack."
- "Verifique os erros mais comuns no Sentry nas últimas 24 horas."

### Encontrar servidores MCP

- Diretório revisado da Anthropic: [claude.ai/directory](https://claude.ai/directory)
- Plugins do marketplace oficial já incluem MCP pré-configurado (GitHub, Slack, Sentry, etc.)

### Escopos de configuração

| Escopo | Armazenado em | Compartilhado |
|--------|---------------|---------------|
| Local (padrão) | `%USERPROFILE%\.claude.json` | Não (só você, projeto atual) |
| Projeto | `.mcp.json` na raiz | Sim (via git, equipe) |
| Usuário | `%USERPROFILE%\.claude.json` | Não (todos os projetos seus) |

### Adicionar servidores MCP via CLI

Para servidores remotos HTTP (mais comuns):

```bash
claude mcp add --transport http nome https://url.do.servidor/mcp
```

Para servidores locais stdio:

```bash
claude mcp add --transport stdio airtable -- npx -y airtable-mcp-server
```

**Nota:** os comandos `claude mcp add` e similares são do CLI. No app desktop, servidores MCP adicionados via CLI ficam disponíveis nas sessões do Code tab. Servidores configurados em `.mcp.json` no projeto são carregados automaticamente (após aprovação).

### Autenticação OAuth

Para servidores que exigem login:

1. Rode `/mcp` em uma sessão
2. Selecione o servidor que precisa de autenticação
3. Siga o fluxo no navegador

Tokens ficam armazenados com segurança e são atualizados automaticamente.

### Visualizar status dos servidores

Dentro de qualquer sessão, use `/mcp` para ver todos os servidores conectados, o número de ferramentas disponíveis e o status de cada um.

Servidores em `.mcp.json` que aguardam aprovação aparecem como "Pending approval". A aprovação ocorre na primeira vez que você inicia uma sessão no projeto.

### Servidores disponíveis via Claude.ai

Se você estiver logado com uma conta claude.ai, os servidores MCP configurados em [claude.ai/customize/connectors](https://claude.ai/customize/connectors) ficam disponíveis automaticamente no Claude Code. Aparecem no `/mcp` com indicador de origem.

### MCP Tool Search

Por padrão, as definições de ferramentas MCP são carregadas sob demanda (não todas de uma vez no início da sessão). Isso mantém o uso de contexto baixo mesmo com muitos servidores conectados. O Claude busca as ferramentas relevantes quando precisa delas.

### Usar recursos MCP com @

Servidores MCP podem expor recursos que você referencia com `@`, como arquivos:

```
@github:issue://123
@docs:file://api/authentication
```

---

## Diferença entre skills, CLAUDE.md e plugins

| Mecanismo | Carrega quando | Ideal para |
|-----------|---------------|------------|
| CLAUDE.md | Toda sessão | Fatos permanentes, convenções do projeto |
| Rules (`.claude/rules/`) | Por sessão ou ao abrir arquivos correspondentes | Regras modulares por área do projeto |
| Skill | Quando invocada ou relevante | Procedimentos reutilizáveis, fluxos de trabalho, referências sob demanda |
| Plugin | Quando instalado e habilitado | Pacotes completos: skills + hooks + MCP + agentes |
| MCP | Quando o servidor está conectado | Ferramentas e dados de sistemas externos |
