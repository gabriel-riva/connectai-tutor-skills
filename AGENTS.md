# Instruções Para Agentes

Este repositório distribui tutores em formato de skill. A raiz do repositório não é uma skill instalável.

## Regra crítica para o link raiz

Se o usuário pedir apenas para instalar este repositório, colar `https://github.com/gabriel-riva/connectai-tutor-skills`, ou disser algo como "instala esse repo", instale exatamente uma skill, escolhida pelo ambiente atual.

1. Se este agente estiver rodando no Codex, instale somente `codextutor/` em `.agents/skills/codextutor/`.
2. Se este agente estiver rodando no Claude Code, instale somente `claudecodetutor/` em `.claude/skills/claudecodetutor/`.
3. Se não conseguir identificar o ambiente, pergunte: "Você está instalando no Codex ou no Claude Code?"
4. Nunca instale as duas skills no mesmo projeto, salvo se o usuário pedir explicitamente "instale as duas".
5. Nunca instale a raiz do repositório nem a pasta `_comum/`.

## Quando o usuário pedir para instalar o CodexTutor

Instale a subpasta `codextutor/` como skill de projeto do Codex, dentro da pasta atual da Oficina de Aprendizado.

Não instale em `$CODEX_HOME/skills`, `%USERPROFILE%\.codex\skills` nem `%USERPROFILE%\.agents\skills`. A skill deve ficar em:

```text
.agents/skills/codextutor/
```

Se a pasta atual não parecer uma oficina nova ou vazia, pergunte ao usuário antes de instalar.

Use o instalador nativo de skills do Codex, equivalente a:

```text
install-skill-from-github --repo gabriel-riva/connectai-tutor-skills --path codextutor --dest .agents/skills
```

Depois da instalação, diga ao usuário para reiniciar o Codex para garantir que a nova skill foi carregada. Em seguida, na pasta escolhida como Oficina de Aprendizado, ele deve escrever:

```text
iniciar tutor
```

A própria skill cria `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md` e `AGENTS.md` na primeira ativação.

## Quando o usuário pedir para instalar o ClaudeCodeTutor

Instale a subpasta `claudecodetutor/` como skill de projeto do Claude Code, dentro da pasta atual da Oficina de Aprendizado.

Não instale em `%USERPROFILE%\.claude\skills`. A skill deve ficar em:

```text
.claude/skills/claudecodetutor/
```

Se a pasta atual não parecer uma oficina nova ou vazia, pergunte ao usuário antes de instalar.

Depois da instalação, diga ao usuário para abrir a pasta escolhida como Oficina de Aprendizado e escrever:

```text
iniciar tutor
```

A própria skill cria `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md`, `CLAUDE.md` e `.claude/settings.local.json` na primeira ativação.

Se a skill não aparecer ou não ativar no Claude Code, oriente o usuário a iniciar uma nova sessão ou reiniciar o app.

## Arquivos de desenvolvimento

A pasta `_comum/` é fonte compartilhada usada por `sync.py`. Ela não precisa ser instalada na máquina do aluno.

Antes de publicar mudanças, rode:

```powershell
python sync.py
python "%USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py" codextutor
python "%USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py" claudecodetutor
```
