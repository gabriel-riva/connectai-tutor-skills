# Tutores de IA para capacitação corporativa: CodexTutor e ClaudeCodeTutor

Dois professores particulares de IA: um para o **Codex** (OpenAI) e outro para o **Claude Code** (Anthropic). Cada tutor vive como uma skill no respectivo app e conduz o aluno por aulas, trilhas personalizadas e missões práticas.

**Regra de instalação:** instale uma única skill por projeto. No Codex, instale somente `codextutor/`. No Claude Code, instale somente `claudecodetutor/`. Não instale as duas, salvo pedido explícito.

## O que é

**Professor particular como skill.** Ao contrário de tutoriais genéricos, cada tutor aprende quem é o aluno: seu cargo, sua empresa, como ele escreve, o que ele produz no dia a dia. As missões partem desse contexto e evoluem conforme o aluno avança. A trilha é montada na primeira conversa e ajustada a cada sessão.

**Oficina permanente do aluno.** O aluno usa uma pasta de trabalho própria (a "Oficina de Aprendizado") onde a skill é instalada em modo de projeto. Nessa pasta ficam o diário de progresso, a trilha personalizada e o "cérebro" do aluno: arquivos de contexto sobre sua empresa, sua rotina e seu estilo de trabalho. Com o tempo, o assistente passa a conhecer o mundo do aluno sem precisar perguntar as mesmas coisas toda vez.

## Para quem

Gestores e profissionais que querem aprender a usar ferramentas de IA no trabalho com acompanhamento estruturado, exemplos do seu próprio dia a dia e progressão clara de habilidades.

---

## Instalação rápida

No **Codex**, abra uma pasta nova ou vazia que será a Oficina de Aprendizado e diga:

```text
Instale este repositório neste projeto, não globalmente: https://github.com/gabriel-riva/connectai-tutor-skills
```

No Codex, esse pedido significa instalar somente `codextutor/` em `.agents/skills/codextutor/`.

No **Claude Code**, abra uma pasta nova ou vazia que será a Oficina de Aprendizado e diga:

```text
Instale este repositório neste projeto, não globalmente: https://github.com/gabriel-riva/connectai-tutor-skills
```

No Claude Code, esse pedido significa instalar somente `claudecodetutor/` em `.claude/skills/claudecodetutor/`.

Nunca instale as duas skills no mesmo projeto, salvo se você pedir explicitamente isso. Depois de instalar e reiniciar o app, use:

```text
iniciar tutor
```

---

## Instalação no Codex

Abra o Codex em uma pasta nova ou vazia que será a Oficina de Aprendizado. O aluno só precisa dizer ao Codex:

```text
Instale a skill CodexTutor deste repositório neste projeto, não globalmente: https://github.com/gabriel-riva/connectai-tutor-skills
```

Depois da instalação, reinicie o Codex para garantir que a nova skill foi carregada. Em seguida, abra a mesma pasta da Oficina de Aprendizado e escreva `iniciar tutor`. A própria skill prepara `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md` e `AGENTS.md` na primeira ativação.

Se o Codex pedir o caminho da skill dentro do repositório, use `codextutor/` ou o link direto:

```text
https://github.com/gabriel-riva/connectai-tutor-skills/tree/main/codextutor
```

### Instrução para o agente instalador

Quando um agente receber o link raiz deste repositório e o pedido para instalar o CodexTutor, ele deve instalar a subpasta `codextutor/` como skill de projeto, dentro da pasta atual da Oficina de Aprendizado. A raiz do repositório não é a skill. A pasta `_comum/` é fonte de desenvolvimento e não precisa ser instalada.

Não instale em `$CODEX_HOME/skills`, `%USERPROFILE%\.codex\skills` nem `%USERPROFILE%\.agents\skills`. A instalação correta é no projeto atual:

Use o instalador nativo de skills do Codex, equivalente a:

```text
install-skill-from-github --repo gabriel-riva/connectai-tutor-skills --path codextutor --dest .agents/skills
```

---

## Instalação no Claude Code

Abra o Claude Code em uma pasta nova ou vazia que será a Oficina de Aprendizado. O aluno só precisa dizer ao Claude Code:

```text
Instale a skill ClaudeCodeTutor deste repositório neste projeto, não globalmente: https://github.com/gabriel-riva/connectai-tutor-skills
```

Depois da instalação, abra ou crie uma pasta para a Oficina de Aprendizado e escreva `iniciar tutor`. Se a skill não aparecer ou não ativar, inicie uma nova sessão do Claude Code ou reinicie o app. A própria skill prepara `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md`, `CLAUDE.md` e `.claude/settings.local.json` na primeira ativação.

Se o Claude Code pedir o caminho da skill dentro do repositório, use `claudecodetutor/` ou o link direto:

```text
https://github.com/gabriel-riva/connectai-tutor-skills/tree/main/claudecodetutor
```

### Instrução para o agente instalador

Quando um agente receber o link raiz deste repositório e o pedido para instalar o ClaudeCodeTutor, ele deve instalar a subpasta `claudecodetutor/` como skill de projeto, dentro da pasta atual da Oficina de Aprendizado. A raiz do repositório não é a skill. A pasta `_comum/` é fonte de desenvolvimento e não precisa ser instalada.

Não instale em `%USERPROFILE%\.claude\skills`. A instalação correta é no projeto atual:

```text
.claude/skills/claudecodetutor/
```

---

## Estrutura do repositório

```
tutor-repo/
├── codextutor/
│   ├── SKILL.md                  # Skill do CodexTutor ($codextutor)
│   ├── oficina/
│   │   └── AGENTS-oficina.md     # AGENTS.md copiado para a raiz da oficina
│   ├── referencia/               # Documentação de referência do Codex
│   └── assets/
├── claudecodetutor/
│   ├── SKILL.md                  # Skill do ClaudeCodeTutor (/claudecodetutor)
│   ├── oficina/
│   │   ├── CLAUDE-oficina.md     # CLAUDE.md copiado para a raiz da oficina
│   │   ├── settings.local.json   # Permissões pré-aprovadas da oficina
│   │   └── LEIA-ME-settings.md   # Explicação do settings.local.json
│   ├── referencia/               # Documentação de referência do Claude Code
│   └── assets/
└── _comum/                       # Arquivos compartilhados (pedagogia, cérebro, módulos)
```

## Como atualizar

Para atualizar o tutor com uma versão mais recente do repositório, peça ao agente para atualizar a skill instalada a partir do mesmo link, substituindo apenas a pasta da skill dentro de `.agents/skills/` ou `.claude/skills/`. Os arquivos do aluno ficam na Oficina de Aprendizado (`tutor/`, `missões/`, `cérebro/`) e não devem ser apagados.

---

## Idioma

Todo o conteúdo educacional deste repositório está em **português brasileiro**. Fontes em inglês são traduzidas pelo tutor antes de apresentar ao aluno.

## Licença

MIT License. Veja o arquivo `LICENSE` para os termos completos.

---

Desenvolvido por **Cognix360**: Consultoria em Tecnologia para PMEs.
