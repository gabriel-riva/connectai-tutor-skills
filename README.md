# Tutores de IA para capacitação corporativa: CodexTutor e ClaudeCodeTutor

Dois professores particulares de IA: um para o **Codex** (OpenAI) e outro para o **Claude Code** (Anthropic). Cada tutor vive como uma skill no respectivo app e conduz o aluno por aulas, trilhas personalizadas e missões práticas.

## O que é

**Professor particular como skill.** Ao contrário de tutoriais genéricos, cada tutor aprende quem é o aluno: seu cargo, sua empresa, como ele escreve, o que ele produz no dia a dia. As missões partem desse contexto e evoluem conforme o aluno avança. A trilha é montada na primeira conversa e ajustada a cada sessão.

**Oficina permanente do aluno.** A instalação cria uma pasta de trabalho (a "Oficina de Aprendizado") onde o aluno pratica. Nessa pasta ficam o diário de progresso, a trilha personalizada e o "cérebro" do aluno: arquivos de contexto sobre sua empresa, sua rotina e seu estilo de trabalho. Com o tempo, o assistente passa a conhecer o mundo do aluno sem precisar perguntar as mesmas coisas toda vez.

## Para quem

Gestores e profissionais que querem aprender a usar ferramentas de IA no trabalho com acompanhamento estruturado, exemplos do seu próprio dia a dia e progressão clara de habilidades.

---

## Instalação no Codex

Abra o Codex numa **pasta nova e vazia** que será sua Oficina de Aprendizado. Cole o prompt abaixo:

```
Instale meu professor de Codex. Faça exatamente isto, nesta ordem:
1. Confirme que estamos numa pasta nova ou vazia (ela será minha "Oficina de Aprendizado"). Se a pasta atual tiver outros arquivos, PARE e me avise antes de qualquer coisa.
2. Baixe https://github.com/{CONTA}/{REPO}/archive/refs/heads/main.zip e extraia numa pasta temporária fora daqui. Use o download do zip mesmo que o git esteja instalado (a oficina NÃO deve virar repositório git).
3. Copie a pasta codextutor/ do zip para .agents/skills/codextutor/ aqui na oficina.
4. Crie aqui as pastas: tutor/, missões/, cérebro/pessoal/, cérebro/profissional/, cérebro/empresa/, cérebro/departamento/, cérebro/equipe/.
5. Se houver um bloco <turma>...</turma> no final desta mensagem, salve o conteúdo dele (sem as tags) em tutor/turma.md.
6. Copie .agents/skills/codextutor/oficina/AGENTS-oficina.md para a raiz da oficina com o nome AGENTS.md.
7. Apague a pasta temporária do zip, mostre a estrutura final da oficina em forma de árvore e termine exatamente com: "Pronto! Digite $codextutor para conhecer seu professor."
```

---

## Instalação no Claude Code

Abra o Claude Code numa **pasta nova e vazia** que será sua Oficina de Aprendizado. Cole o prompt abaixo:

```
Instale meu professor de Claude Code. Faça exatamente isto, nesta ordem:
1. Confirme que estamos numa pasta nova ou vazia (ela será minha "Oficina de Aprendizado"). Se a pasta atual tiver outros arquivos, PARE e me avise antes de qualquer coisa.
2. Baixe https://github.com/{CONTA}/{REPO}/archive/refs/heads/main.zip e extraia numa pasta temporária fora daqui. Use o download do zip mesmo que o git esteja instalado (a oficina NÃO deve virar repositório git).
3. Copie a pasta claudecodetutor/ do zip para .claude/skills/claudecodetutor/ aqui na oficina.
4. Crie aqui as pastas: tutor/, missões/, cérebro/pessoal/, cérebro/profissional/, cérebro/empresa/, cérebro/departamento/, cérebro/equipe/.
5. Se houver um bloco <turma>...</turma> no final desta mensagem, salve o conteúdo dele (sem as tags) em tutor/turma.md.
6. Copie .claude/skills/claudecodetutor/oficina/CLAUDE-oficina.md para a raiz da oficina com o nome CLAUDE.md E copie .claude/skills/claudecodetutor/oficina/settings.local.json para .claude/settings.local.json aqui na oficina.
7. Apague a pasta temporária do zip, mostre a estrutura final da oficina em forma de árvore e termine exatamente com: "Pronto! Digite /claudecodetutor para conhecer seu professor."
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

Para atualizar o tutor com uma versão mais recente do repositório, reinstale usando o mesmo prompt de instalação na pasta da oficina existente. O instalador substitui apenas os arquivos da skill; os arquivos do aluno (tutor/, missões/, cérebro/) não são afetados.

---

## Idioma

Todo o conteúdo educacional deste repositório está em **português brasileiro**. Fontes em inglês são traduzidas pelo tutor antes de apresentar ao aluno.

## Licença

MIT License. Veja o arquivo `LICENSE` para os termos completos.

---

Desenvolvido por **Cognix360**: Consultoria em Tecnologia para PMEs.
