# Instruções Para Agentes

Este repositório distribui tutores em formato de skill. A raiz do repositório não é uma skill instalável.

## Quando o usuário pedir para instalar o CodexTutor

Instale a subpasta `codextutor/` como skill do Codex.

Use o instalador nativo de skills do Codex, equivalente a:

```text
install-skill-from-github --repo gabriel-riva/connectai-tutor-skills --path codextutor
```

Depois da instalação, diga ao usuário para reiniciar o Codex e, na pasta escolhida como Oficina de Aprendizado, escrever:

```text
iniciar tutor
```

A própria skill cria `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md` e `AGENTS.md` na primeira ativação.

## Quando o usuário pedir para instalar o ClaudeCodeTutor

Instale a subpasta `claudecodetutor/` como skill do Claude Code.

Depois da instalação, diga ao usuário para abrir a pasta escolhida como Oficina de Aprendizado e escrever:

```text
iniciar tutor
```

A própria skill cria `tutor/`, `missões/`, `cérebro/`, `tutor/AMBIENTE.md`, `CLAUDE.md` e `.claude/settings.local.json` na primeira ativação.

## Arquivos de desenvolvimento

A pasta `_comum/` é fonte compartilhada usada por `sync.py`. Ela não precisa ser instalada na máquina do aluno.

Antes de publicar mudanças, rode:

```powershell
python sync.py
python "%USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py" codextutor
python "%USERPROFILE%\.codex\skills\.system\skill-creator\scripts\quick_validate.py" claudecodetutor
```
