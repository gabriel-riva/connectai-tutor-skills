# Referência: Skills e Plugins (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

Skills e plugins são as formas de estender o Codex com comportamentos e integrações reutilizáveis. Skills empacotam instruções para um fluxo de trabalho específico; plugins agrupam skills, integrações de apps e servidores MCP em pacotes instaláveis.

---

## 1. Skills: o que são

Uma skill é um conjunto de instruções empacotado em um diretório. Pense nela como uma "receita de como fazer X": o Codex a lê antes de executar uma tarefa e segue os passos descritos, sem que você precise repetir as instruções toda vez.

Exemplo: uma skill de "revisão de PR" pode conter os critérios de revisão do time, os comandos para rodar os testes e o formato esperado de comentários. Uma vez instalada, basta pedir `$revisão-pr` e o Codex segue o protocolo.

---

## 2. Estrutura de uma skill

Uma skill é uma pasta com pelo menos o arquivo `SKILL.md`:

```
minha-skill/
├── SKILL.md         (obrigatório)
├── scripts/         (opcional: scripts que a skill executa)
├── references/      (opcional: documentação de referência)
├── assets/          (opcional: templates, arquivos de exemplo)
└── agents/openai.yaml  (opcional: metadados de UI e dependências)
```

### O arquivo SKILL.md

O cabeçalho (frontmatter YAML) define nome e descrição. O corpo contém as instruções para o Codex:

```yaml
---
name: nome-da-skill
description: >
  Explica exatamente quando esta skill deve e não deve ser usada.
  A descrição é o que o Codex lê para decidir invocar implicitamente.
---

Instruções passo a passo para o Codex seguir quando esta skill for invocada.
```

A **descrição** é crítica: ela determina quando o Codex aplica a skill automaticamente. Descrições vagas causam ativações incorretas. Descrições precisas (com palavras-chave e casos que não se encaixam) funcionam melhor.

### O arquivo openai.yaml (opcional)

Permite definir metadados visuais e dependências:

```yaml
interface:
  display_name: "Nome amigável na UI"
  short_description: "Descrição curta"
  icon_small: "./assets/logo.svg"
  brand_color: "#3B82F6"

policy:
  allow_implicit_invocation: false   # desabilita invocação automática

dependencies:
  tools:
    - type: "mcp"
      value: "nomeDoServidor"
```

---

## 3. Onde instalar skills

O Codex busca skills em múltiplos locais, do mais específico para o mais geral:

| Escopo | Localização | Quando usar |
|---|---|---|
| Pasta atual | `.agents/skills` (diretório do projeto) | Skills específicas de um serviço ou subpasta |
| Pasta pai | `.agents/skills` (diretório pai) | Projetos com pastas aninhadas |
| Raiz do repositório | `$REPO_ROOT/.agents/skills` | Skills disponíveis em todo o repositório |
| Usuário | `$HOME/.agents/skills` | Skills pessoais reutilizáveis em qualquer projeto |
| Admin | `/etc/codex/skills` | Padrões de sistema ou administração |
| Nativas (bundled) | Embutidas no Codex | `skill-creator`, `skill-installer` e outras |

---

## 4. Como invocar uma skill

### Invocação explícita

Mencione o nome da skill no prompt, precedido de `$`:

```
$nome-da-skill
```

No app, você pode digitar `$` no compositor para ver as skills disponíveis.

### Invocação implícita

O Codex pode escolher e aplicar uma skill automaticamente quando a sua descrição corresponde à tarefa solicitada. Para desabilitar esse comportamento em uma skill específica, defina `allow_implicit_invocation: false` no `openai.yaml`.

---

## 5. Instalar skills da comunidade: $skill-installer

Para adicionar skills curadas:

```
$skill-installer nome-da-skill
```

Exemplo:

```
$skill-installer linear
```

O instalador baixa a skill do repositório oficial e a coloca no local correto.

---

## 6. Criar uma skill: $skill-creator

Para criar uma skill a partir de uma conversa existente ou de documentação:

```
Use $skill-creator para criar uma skill que [descreva a tarefa]
Use estas fontes:
- Exemplo funcionando: [cole o thread ou PR]
- Documentação: [cole o conteúdo relevante]
- Scripts: [liste os comandos que a skill deve usar]
- Resultado esperado: [mostre como deve parecer o output]
```

O criador gera a estrutura de pastas, o `SKILL.md` e valida o output. Criação típica leva cerca de 5 minutos.

Após criar, teste a skill em novas tarefas. Se ela pular etapas ou usar comandos incorretos, peça ao Codex para refinar o `SKILL.md` diretamente na mesma thread.

---

## 7. Habilitar e desabilitar skills

Edite `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/caminho/para/skill/SKILL.md"
enabled = false
```

Reinicie o Codex após a alteração.

---

## 8. Plugins: o que são

Um plugin agrupa três tipos de componentes em um pacote instalável:

- **Skills:** instruções reutilizáveis para tipos específicos de trabalho
- **Apps:** conexões com ferramentas externas (GitHub, Slack, Google Drive, etc.)
- **Servidores MCP:** serviços que fornecem ferramentas ou informações compartilhadas

Plugins são a forma de distribuir integrações além do repositório local. Uma skill isolada fica no disco; um plugin pode ser publicado e instalado por qualquer pessoa.

### Exemplos de plugins disponíveis

- **Gmail:** ler e gerenciar mensagens
- **Google Drive:** trabalhar com Docs, Sheets e Slides
- **Slack:** resumir canais ou rascunhar respostas
- **Sites:** criar e publicar websites e aplicações
- **GitHub:** integração com repositórios, PRs e issues

### Como instalar um plugin no app

1. Abra **Plugins** no menu lateral
2. Busque ou navegue pela categoria desejada
3. Clique em instalar
4. Autentique-se com o serviço externo, se necessário
5. Inicie uma nova thread e peça ao Codex para usar o plugin

### Como usar um plugin instalado

**Opção 1:** descreva a tarefa naturalmente ("Resumir threads não lidas do Gmail").

**Opção 2:** invoque explicitamente com `@` seguido do nome: `@Gmail`.

### Desinstalar

Abra o plugin no navegador de plugins e selecione **Uninstall plugin**. Para desabilitar sem remover, edite `enabled = false` no `config.toml`.

---

## 9. Boas práticas para skills

- Cada skill deve cobrir uma função específica, não múltiplas coisas ao mesmo tempo
- Prefira instruções a scripts, a menos que um script seja realmente necessário
- Use passos imperativos com entradas e saídas explícitas
- Teste o prompt da skill contra a sua descrição para confirmar o comportamento
- Mantenha a descrição concisa, com palavras-chave visíveis que representam quando invocar
- Guarde a skill localmente enquanto itera; compartilhe via repositório quando estabilizar
