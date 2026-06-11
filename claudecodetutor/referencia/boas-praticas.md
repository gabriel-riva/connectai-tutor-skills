# Referência: Boas Práticas, Segurança e Custos no Claude Code

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.

---

## A restrição fundamental: a janela de contexto

Antes de qualquer boas práticas, entenda a restrição central: **a janela de contexto do Claude enche rápido, e o desempenho piora conforme ela enche.**

A janela de contexto guarda toda a conversa: cada mensagem, cada arquivo lido, cada saída de comando. Uma única sessão de depuração ou exploração de código pode consumir dezenas de milhares de tokens. Quando a janela está quase cheia, o Claude pode começar a "esquecer" instruções anteriores ou cometer mais erros.

Toda estratégia de boas práticas existe para gerenciar essa restrição.

---

## Dar ao Claude uma forma de verificar o próprio trabalho

**Forneça uma checagem que o Claude possa rodar:** testes, um build, um screenshot para comparar. É a diferença entre uma sessão que você precisa observar e uma que você pode deixar rodar.

Sem uma checagem, "parece pronto" é o único sinal disponível. Você se torna o loop de verificação: cada erro espera por você notar. Com uma checagem que retorna aprovado/reprovado, o loop fecha sozinho.

| Estratégia | Antes (vago) | Depois (verificável) |
|-----------|--------------|---------------------|
| Critérios de verificação | "Implemente validação de e-mail" | "Escreva uma função validateEmail. Casos de teste: user@exemplo.com é true, inválido é false. Rode os testes ao terminar." |
| UI visualmente | "Deixe o dashboard melhor" | "[Cole screenshot] Implemente este design. Tire screenshot do resultado e compare. Liste diferenças e corrija." |
| Causa raiz, não sintoma | "O build está falhando" | "O build falha com este erro: [cole]. Corrija e verifique que o build funciona. Trate a causa raiz, não suprima o erro." |

---

## Explorar primeiro, planejar, depois codificar

Deixar o Claude pular direto para o código pode produzir código que resolve o problema errado. Use o **modo Plan** para separar exploração de execução.

**Fluxo recomendado:**

1. **Explorar (modo Plan):** o Claude lê arquivos e responde perguntas sem fazer mudanças. Ative com Ctrl+Shift+P no app ou `Shift+Tab` para navegar até o modo Plan.

2. **Planejar (modo Plan):** peça ao Claude para criar um plano detalhado de implementação.

3. **Implementar (modo padrão):** saia do modo Plan e deixe o Claude codificar, verificando contra o plano.

4. **Commitar:** peça ao Claude para commitar com mensagem descritiva e criar um PR.

**Quando pular o planejamento:** para tarefas onde o escopo é claro e a correção é pequena (corrigir um typo, adicionar um log, renomear uma variável), vá direto. Planejamento é mais útil quando a mudança modifica múltiplos arquivos ou você não está familiarizado com o código.

---

## Fornecer contexto específico nos prompts

O Claude pode inferir intenção, mas não lê mentes. Referencie arquivos específicos, mencione restrições e aponte padrões existentes.

| Estratégia | Antes | Depois |
|-----------|-------|--------|
| Escopo a tarefa | "adicione testes para foo.py" | "escreva um teste para foo.py cobrindo o caso em que o usuário está deslogado. Evite mocks." |
| Aponte fontes | "por que ExecutionFactory tem uma API tão estranha?" | "olhe o histórico de git do ExecutionFactory e resuma como essa API surgiu" |
| Referencie padrões existentes | "adicione um widget de calendário" | "veja como os widgets existentes são implementados na home page. Widget.php é um bom exemplo. Siga o padrão para implementar um widget de calendário." |
| Descreva o sintoma | "corrija o bug de login" | "usuários relatam que o login falha após timeout de sessão. Verifique o fluxo de auth em src/auth/, especialmente o token refresh. Escreva um teste que reproduz o problema, depois corrija." |

### Fornecer conteúdo rico

- Use `@` para referenciar arquivos em vez de descrever onde o código fica.
- Cole imagens diretamente (Ctrl+V ou arrastar para o chat).
- Peça ao Claude para buscar o que precisar usando suas ferramentas.

---

## Configurar o ambiente

### Escrever um CLAUDE.md eficaz

Use `/init` para gerar um CLAUDE.md inicial baseado na estrutura do projeto. O Claude analisa o projeto e cria um arquivo com comandos de build, instruções de teste e convenções descobertas.

**O que incluir:**
- Comandos Bash que o Claude não conseguiria adivinhar
- Regras de estilo de código que diferem do padrão
- Instruções de teste e executores de teste preferidos
- Convenções do repositório (nomenclatura de branches, convenções de PR)
- Decisões arquiteturais específicas do projeto
- Peculiaridades do ambiente de desenvolvimento (variáveis de ambiente necessárias)

**O que não incluir:**
- Coisas que o Claude já sabe pelas convenções da linguagem
- Documentação detalhada de APIs (coloque um link)
- Informações que mudam frequentemente
- Práticas óbvias como "escreva código limpo"

**Tamanho:** se o CLAUDE.md estiver longo demais, o Claude ignora metade. Poda sem piedade. Se o Claude já faz algo corretamente sem a instrução, delete-a.

### Configurar permissões e modos

Por padrão, o Claude solicita permissão para ações que podem modificar o sistema. Depois da décima aprovação, você não está mais revisando de verdade, só clicando. Três formas de reduzir interrupções:

- **Auto mode:** um classificador separado revisa comandos e bloqueia apenas o que parece arriscado. Melhor quando você confia na direção geral de uma tarefa mas não quer clicar em cada passo.
- **Allowlists de permissão:** permita ferramentas específicas que você sabe que são seguras.
- **Sandboxing:** isola o filesystem e rede, permitindo ao Claude trabalhar com mais liberdade dentro dos limites definidos.

### Usar subagentes para investigação

Subagentes rodam em janelas de contexto separadas e reportam resumos. Quando o Claude pesquisa um codebase, lê muitos arquivos que consomem seu contexto. Subagentes exploram sem poluir a conversa principal:

```
Use subagentes para investigar como nosso sistema de autenticação trata
o refresh de token, e se temos utilitários OAuth existentes que eu deveria reusar.
```

---

## Gerenciar a sessão

### Corrigir o curso cedo e com frequência

Os melhores resultados vêm de loops de feedback curtos. Corrija o Claude assim que notar que está indo na direção errada:

- **Esc:** para o Claude no meio de uma ação. O contexto é preservado, você pode redirecionar.
- **Esc + Esc ou `/rewind`:** abre o menu de rewind para restaurar estado anterior de conversa e código.
- **"Desfaça isso":** peça ao Claude para reverter mudanças.
- **`/clear`:** reseta o contexto entre tarefas não relacionadas.

Se você corrigiu o Claude mais de duas vezes pelo mesmo problema em uma sessão, o contexto está poluído com abordagens falhadas. Use `/clear` e comece de novo com um prompt mais específico que incorpora o que você aprendeu.

### Usar `/compact` com frequência

Durante sessões longas, a janela de contexto do Claude pode ficar cheia de conversa irrelevante, conteúdo de arquivos e saídas de comandos:

- Use `/clear` entre tarefas não relacionadas para resetar completamente.
- `/compact` resume a conversa mantendo o que mais importa. Use `/compact <instruções>` para guiar o que preservar.
- Para perguntas rápidas que não precisam ficar no contexto, use `Ctrl+;` (side chat) ou `/btw`. A resposta aparece em overlay e nunca entra no histórico da conversa.

### Retomar conversas

O Claude Code salva conversas localmente. Quando uma tarefa dura múltiplas sessões, você não precisa re-explicar o contexto. Nomeie sessões com `/rename` para encontrá-las facilmente depois.

---

## Boas práticas para gestores não técnicos

### Perguntar ao codebase como a um engenheiro sênior

Ao se familiarizar com um projeto, use o Claude Code para aprendizado:

- "Como o sistema de log funciona?"
- "Como crio um novo endpoint de API?"
- "Por que esse código chama foo() em vez de bar() na linha 333?"
- "Quais casos extremos o CustomerOnboardingFlow trata?"

### Deixar o Claude te entrevistar

Para funcionalidades maiores, peça ao Claude para te entrevistar primeiro:

```
Quero construir [descrição breve]. Me entreviste em detalhes usando a ferramenta AskUserQuestion.

Pergunte sobre implementação técnica, UX, casos extremos e tradeoffs. Não faça perguntas óbvias,
aprofunde nas partes difíceis que posso não ter considerado.

Continue entrevistando até cobrir tudo, depois escreva uma especificação completa em SPEC.md.
```

Após a especificação pronta, inicie uma sessão nova para executá-la. A nova sessão tem contexto limpo focado na implementação.

---

## Permissões e segurança

### Modos de permissão

| Modo | Comportamento |
|------|---------------|
| **Ask (padrão)** | Solicita aprovação para cada ação que modifica o sistema |
| **Auto accept edits** | Aceita automaticamente edições em arquivos; ainda pede para comandos |
| **Plan mode** | Apenas lê, não faz mudanças; apresenta plano para revisão |
| **Auto** | Um classificador revisa comandos; bloqueia apenas o que parece arriscado |
| **Bypass permissions** | Sem prompts de permissão; use com cuidado |

### Configurar regras de permissão

Em `.claude/settings.json`, defina regras de allow e deny:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./secrets/**)"
    ]
  }
}
```

### Proteção contra injeção de prompt

Se o Claude estiver lendo conteúdo externo (e-mails, páginas web, logs), esse conteúdo pode tentar redirecionar o comportamento do Claude com instruções embutidas. Para mitigar:

- Use sandboxing para isolar filesystem e rede.
- Configure regras de deny para ferramentas e caminhos de arquivos sensíveis.
- Revise o que o Claude está prestes a fazer quando trabalha com conteúdo externo.

---

## Privacidade e uso de dados

### O que acontece com seus dados

Quando você usa o Claude Code com uma assinatura claude.ai:

- Suas conversas podem ser usadas para melhorar os modelos da Anthropic, conforme a política de privacidade.
- Nas assinaturas Team e Enterprise, os dados das conversas não são usados para treinamento por padrão.
- Arquivos locais só são enviados quando você explicitamente pede ao Claude para lê-los.
- O transcript das sessões fica salvo localmente em `%USERPROFILE%\.claude\projects\`.

Para configurações de privacidade específicas ao seu plano, consulte as configurações da sua conta em claude.ai.

---

## Custos e limites de uso

### Como o uso é cobrado

O Claude Code usa o mesmo saldo da sua assinatura claude.ai que conversas interativas. O uso é medido em tokens (tokens de entrada + tokens de saída).

Operações que consomem mais tokens:
- Leitura de arquivos grandes
- Histórico de conversa longo (contexto cheio)
- Respostas longas como código extenso
- Sessões com muitas ferramentas MCP carregadas

### Reduzir uso de tokens

- Use `/clear` entre tarefas não relacionadas (reseta o contexto).
- Use `/compact` para resumir antes que o contexto fique muito grande.
- Use subagentes para pesquisa (exploram em janela separada, retornam apenas o resumo).
- Prefira skills com `context: fork` para tarefas isoladas.
- Para MCP: use a opção de carregamento sob demanda (padrão) em vez de carregar todas as ferramentas de uma vez.

### Limites de uso

Cada plano tem limites de uso diário/mensal. Quando o limite é atingido:
- Você verá uma mensagem indicando que o limite foi atingido.
- A sessão atual pode continuar com o histórico existente, mas novas rodadas podem ser limitadas.
- O limite reseta no início do próximo período de cobrança.

Para ver o uso atual: use `/usage` em qualquer sessão.

---

## Configuração de modelo

O Claude Code usa por padrão o modelo mais capaz disponível para o seu plano. Para economizar ou ajustar o desempenho:

- Use `/model` para trocar de modelo durante uma sessão.
- Configure `model` em `settings.json` para uma preferência permanente.
- Modelos mais rápidos (como Haiku) custam menos e são adequados para tarefas simples.
- Modelos mais capazes (como Sonnet ou Opus) são melhores para tarefas complexas.

O campo `effortLevel` em settings.json ajusta quanto esforço (e tokens de raciocínio) o Claude usa: `"low"`, `"medium"`, `"high"`, `"xhigh"`.

---

## Champion kit: tornar-se um campeão interno de IA

A Anthropic mantém recursos para quem promove a adoção do Claude Code dentro de organizações:

**Champion kit** ([code.claude.com/docs/en/champion-kit](https://code.claude.com/docs/en/champion-kit)): kit oficial para campeões internos. Inclui materiais de apresentação, scripts de conversa, casos de uso para diferentes funções e respostas a objeções comuns.

**Communications kit** ([code.claude.com/docs/en/communications-kit](https://code.claude.com/docs/en/communications-kit)): materiais para comunicação interna de adoção. Templates de e-mail, mensagens de Slack, materiais de onboarding.

Como os times da Anthropic usam o Claude Code internamente: [anthropic.com/news/how-anthropic-teams-use-claude-code](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code).

---

## Armadilhas comuns a evitar

| Armadilha | Sintoma | Correção |
|-----------|---------|----------|
| **Sessão multi-propósito** | Começa com uma tarefa, desvio para outra, contexto cheio de irrelevâncias | `/clear` entre tarefas não relacionadas |
| **Correções em loop** | Claude faz algo errado, você corrige, ainda está errado | Depois de duas correções falhadas, `/clear` e reescreva o prompt inicial |
| **CLAUDE.md inflado** | O Claude ignora metade das instruções | Poda sem piedade. Se o Claude já faz corretamente sem a instrução, delete. |
| **Verificar sem provas** | Claude produz implementação que parece plausível mas tem casos extremos | Sempre forneça verificação (testes, scripts, screenshots). Se não dá para verificar, não entregue. |
| **Exploração infinita** | Claude lê centenas de arquivos, enchendo o contexto | Escreva investigações com escopo definido ou use subagentes para isolar a exploração. |
