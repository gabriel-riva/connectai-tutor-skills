# Referência: Contexto e Memória (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

Para que o Codex trabalhe bem em um projeto, ele precisa de contexto: saber quais são as regras, o que o time espera e como o repositório está organizado. Esta referência cobre os dois mecanismos principais de contexto persistente: o arquivo `AGENTS.md` e as memórias nativas do app.

---

## 1. AGENTS.md: instruções escritas para o Codex

### O que é

O `AGENTS.md` é um arquivo de texto que contém instruções permanentes para o Codex. Pense nele como o "manual de integração" que você daria a um colega novo: descreve o projeto, as convenções do time, os comandos que ele deve rodar e os padrões que deve seguir.

Ao iniciar uma thread, o Codex lê automaticamente todos os arquivos `AGENTS.md` encontrados na cadeia de diretórios do projeto e os usa como contexto base, sem que você precise repetir essas instruções a cada conversa.

### Onde fica

O Codex busca instruções em três escopos, em ordem de precedência (mais geral para mais específico):

| Escopo | Localização |
|---|---|
| Global (pessoal) | `~/.codex/AGENTS.md` ou `~/.codex/AGENTS.override.md` |
| Repositório | Raiz do Git até o diretório atual, em cada nível |
| Subdiretório | `AGENTS.override.md` em pastas específicas |

Os arquivos são concatenados: o global define padrões gerais, o de repositório refina para o projeto e o de subdiretório aplica regras especializadas para uma parte do código.

**Nomes alternativos:** é possível configurar nomes como `TEAM_GUIDE.md` ou `.agents.md` como fallback, caso o time já use outra convenção de nome.

**Limite:** o total combinado de todos os arquivos `AGENTS.md` carregados é de 32 KiB por padrão. Arquivos vazios são ignorados.

### O que escrever

O `AGENTS.md` funciona melhor quando contém informações práticas e estáveis, não instruções de uma tarefa específica. Exemplos do que incluir:

- **Comandos de teste e build:** "Execute `npm test` após modificar arquivos JavaScript"
- **Dependências preferidas:** "Prefira `pnpm` ao instalar pacotes"
- **Fluxos de aprovação:** "Solicite confirmação antes de adicionar dependências de produção"
- **Convenções de código:** nomes de arquivos, estrutura de pastas, estilo de commits
- **Restrições:** "Nunca modificar arquivos em `src/legacy/`"
- **Documentação esperada:** o que documentar e onde

**Como começar:** no CLI do Codex, rode `/init` para gerar um modelo inicial com base no projeto atual.

### Verificar se foi carregado

```bash
codex --ask-for-approval never "Summarize the current instructions."
```

O Codex lista os arquivos carregados em ordem de precedência.

### Relação com as configurações do app

Em **Settings > Personalization**, há um campo de "instruções personalizadas". As instruções adicionadas ali atualizam o `AGENTS.md` pessoal (`~/.codex/AGENTS.md`). As duas formas são equivalentes: a interface gráfica é apenas um atalho para editar o arquivo.

---

## 2. Memórias nativas (Settings > Personalization > Memories)

### O que são

Memórias são fragmentos de contexto que o Codex extrai automaticamente de conversas passadas e carrega em threads futuras. Pense nisso como anotações que o próprio Codex faz sobre você: preferências, convenções que você corrigiu, padrões recorrentes, erros a evitar.

**Disponibilidade:** o recurso está disponível quando habilitado nas configurações (pode aparecer como "quando disponível" dependendo do plano).

### Para que servem

As memórias são úteis para:

- Preferências estáveis ("prefiro TypeScript a JavaScript")
- Padrões recorrentes de projeto ("esse repositório usa tabs, não espaços")
- Pitfalls conhecidos ("esse cliente sempre pede que os testes cubram casos extremos")

### Relação com o AGENTS.md

Memórias e `AGENTS.md` são complementares. A documentação oficial recomenda:

> "Elas complementam contexto escrito explícito, mas não o substituem."

Para contexto crítico (regras do time, comandos de build, restrições de segurança), escreva no `AGENTS.md`. As memórias são uma camada de conveniência para preferências que surgem naturalmente durante o uso, não o lugar certo para regras importantes.

---

## 3. O padrão de contexto em arquivos .md

Além do `AGENTS.md`, um padrão eficaz de uso do Codex é manter contexto durável em arquivos Markdown simples dentro do projeto. A ideia é tratar uma pasta de arquivos `.md` como "memória de trabalho" do projeto: as pessoas envolvidas, o que está bloqueado, o que foi decidido, o que precisa de acompanhamento.

Um exemplo de estrutura de vault (pasta de contexto):

```
vault/
├── TODO.md
├── people/
├── projects/
├── agent/
└── notes/
```

O `AGENTS.md` na raiz dessa pasta pode instruir o Codex sobre como usar e atualizar esses arquivos. Um bom conjunto de regras para esse arquivo inclui:

- Tratar a pasta como memória de trabalho durável
- Preferir notas canônicas a proliferação de notas novas
- Preservar decisões, bloqueios, responsáveis, datas e links úteis
- Não atualizar os arquivos se nada de significativo mudou (evitar "ruído de atualização")

Repositórios guardam código. A pasta de vault guarda contexto corrente: o que está em andamento, quem está envolvido, o que mudou recentemente.

> Contexto importante não deve viver apenas no transcript de uma conversa. Escreva em algum lugar que a próxima thread consiga retomar.
