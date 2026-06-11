# Módulo: Automações e metas
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 30-40 min
**Resultado:** o aluno entende a diferença entre os tipos de automação disponíveis, configura a primeira automação inofensiva da sua área (resumo diário de uma pasta) e sabe formular metas com critério de verificação real.

---

## Conceito em 1 minuto

Automação é uma instrução que o agente executa sem você precisar estar presente. A diferença entre deixar algo agendado e ter um assistente de verdade é o seguinte: uma tarefa agendada começa do zero na hora marcada. Uma thread automation (ou routine) retorna a uma conversa que já estava em andamento, com todo o histórico de contexto, como se um colega voltasse para a mesa depois de uma pausa.

Ambas são úteis. A escolha depende de uma pergunta simples: esse trabalho precisa "lembrar" o que aconteceu nas execuções anteriores?

E tem uma regra de ouro que nenhum gestor deve quebrar: o agente pesquisa, organiza e rascunha. O humano decide e envia. Automação sem supervisão humana nas ações que afetam outros não é eficiência, é risco.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: entender os tipos de automação

Antes de configurar qualquer coisa, mostre os tipos disponíveis. O conteúdo exato depende da plataforma:

<!-- @codex -->
> "No Codex, existem dois tipos de automação. O primeiro é a automação standalone: cada execução começa do zero, sem memória do que aconteceu antes. Funciona como um alarme que dispara e executa um trabalho novo toda vez. O segundo é a thread automation (ou automação de heartbeat): ela retorna à mesma thread no horário marcado, com acesso a todo o histórico da conversa. Funciona como um colega que você pediu para checar algo a cada hora e te mandar uma mensagem quando encontrar.

Para criar: vá na aba `Automations` no app. Lá você define o prompt, a cadência (diária, semanal, ou horário personalizado com cron) e se deve rodar no projeto local ou num worktree isolado."

Confirme que o aluno encontrou a aba Automations no app.
<!-- @/codex -->

<!-- @claude -->
> "No Claude Code Desktop, existem três formas de agendar trabalho. A mais simples é a tarefa agendada no desktop: roda no seu computador em horário definido, precisa do app aberto. A segunda é a Routine na nuvem: roda na infraestrutura da Anthropic mesmo com seu computador desligado, acessa repositórios via GitHub. A terceira é o `/loop` dentro de uma sessão: repete um prompt em intervalo enquanto a sessão está aberta.

Para criar uma tarefa agendada no desktop: acesse a seção `Routines` na barra lateral, clique em `New routine` e escolha `Local`. Preencha o nome, as instruções, a pasta de trabalho e o agendamento."

Confirme que o aluno encontrou a seção Routines na barra lateral.
<!-- @/claude -->

**Verificação:** aluno localizou o recurso de automação no app e entendeu a diferença básica entre os tipos.

---

### Ato 2: o padrão chefe de gabinete

Antes de criar a primeira automação, apresente o padrão mais importante de qualquer automação que envolve comunicação:

> "Existe um padrão que chamo de chefe de gabinete. O agente faz o trabalho custoso de pesquisa, organização e rascunho. Quando você volta, tudo está preparado. O que ele nunca faz sem a sua aprovação: enviar e-mails, postar mensagens, confirmar reuniões, assinar documentos. Rascunhar sim; enviar, nunca.

Esse padrão não é limitação, é design. Um assistente que age antes que você decida não é eficiente: é um problema esperando acontecer."

Pergunte ao aluno:

> "Na sua rotina, qual tipo de trabalho de coleta ou organização consome mais tempo antes de você tomar uma decisão? Montar uma pauta? Checar o que chegou por e-mail? Atualizar um relatório?"

Anote a resposta para a próxima etapa.

**Verificação:** aluno entendeu o padrão e identificou um trabalho de coleta recorrente.

---

### Ato 3: configurar a primeira automação inofensiva

Comece com algo seguro e de resultado imediato: um resumo diário de uma pasta. Passe o prompt-modelo, adaptando com o aluno:

> "Toda manhã, leia os arquivos da pasta [caminho da pasta: pode ser a pasta de downloads, missões ou documentos]. Liste o que chegou ou mudou nas últimas 24 horas. Para cada arquivo novo, escreva uma linha descrevendo o que parece ser o conteúdo. Salve o resumo como `resumo-AAAA-MM-DD.md` na mesma pasta. Não envie nada, não altere nenhum arquivo existente."

Configure a automação juntos:

<!-- @codex -->
Na aba Automations, crie uma nova automação standalone com esse prompt. Configure a cadência para diária no horário que o aluno chegaria ao trabalho. Antes de ativar, rode manualmente uma vez para confirmar o comportamento. Mostre ao aluno onde o resultado aparece na seção Triage.
<!-- @/codex -->

<!-- @claude -->
Na seção Routines, crie uma nova tarefa local com esse prompt. Configure o agendamento para `Diário` no horário desejado. Configure a pasta de trabalho correta. Antes de ativar, use o botão `Run now` para confirmar o comportamento. Mostre ao aluno onde aparece a execução na seção `Scheduled` da barra lateral.
<!-- @/claude -->

**Verificação:** automação configurada, teste manual executado com sucesso, resultado visível.

---

### Ato 4: metas com critério verificável

Feche o módulo com o conceito de metas:

> "Automação sem critério de parada é só uma tarefa infinita. O que diferencia uma meta de uma vontade é o critério de verificação: como você vai saber, sem nenhuma dúvida, que a meta foi atingida?"

Mostre a diferença:

<!-- @codex -->
> "No Codex, você pode usar o `/goal` para definir metas com condição de parada: 'complete isso sem parar até que [estado verificável]'. O sistema verifica automaticamente a condição após cada rodada. Uma meta fraca: 'implemente o relatório'. Uma meta forte: '/goal gerar o relatório de estoque com todas as colunas preenchidas e sem células vazias, verificando linha por linha ao final'."

Para ativar: edite o `config.toml` adicionando `[features] goals = true`, ou execute `codex features enable goals`. Depois use `/goal` no compositor.
<!-- @/codex -->

<!-- @claude -->
> "No Claude Code, o `/goal` define uma condição de conclusão e o agente trabalha em ciclos até atingir. Para usar: escreva `/goal [condição verificável]` no campo de mensagem. O agente inicia imediatamente e continua até a condição ser satisfeita. Requer Claude Code v2.1.139 ou posterior."

Mostre a diferença com um exemplo:

> "Uma meta fraca: 'limpe os dados do relatório'. Uma meta forte: '/goal todos os campos obrigatórios do relatório estão preenchidos e nenhuma linha tem data em formato incorreto, verificado ao final'. O critério de verificação é o que transforma a instrução em meta."
<!-- @/claude -->

Pergunte ao aluno:

> "Pega uma tarefa que você queria delegar mas nunca delegou porque precisaria explicar demais. Qual seria a condição verificável que diria 'isso está pronto'?"

**Verificação:** aluno formulou pelo menos uma meta com critério verificável.

---

## Variações por função

| Área | Primeira automação inofensiva | Meta com critério verificável |
|---|---|---|
| Financeiro | Resumo diário de arquivos de conciliação recebidos | Todos os lançamentos do dia têm conta contábil preenchida |
| Comercial | Resumo de e-mails de clientes recebidos nas últimas 24h | Todas as propostas com mais de 5 dias têm status atualizado |
| Operações | Resumo de arquivos de relatório de turno | Todos os registros de parada têm causa e duração preenchidas |
| Marketing | Resumo de arquivos de resultado de campanha | Todas as campanhas ativas têm gasto e resultado atualizados |
| Engenharia | Resumo de arquivos de OS abertos na pasta de trabalho | Todas as ordens de serviço abertas têm prazo estimado |
| Holding | Resumo de relatórios de subsidiárias recebidos | Todos os indicadores do dashboard têm valor do mês atual |

---

## Aprofundamento

O módulo 16 aprofunda conectores e MCP, que ampliam o que as automações conseguem acessar (e-mail, calendário, sistemas externos). A combinação de automação com um conector de e-mail, por exemplo, é o que transforma o padrão chefe de gabinete em algo que lida com a caixa de entrada de verdade.

O módulo 20 (orquestração) aprofunda como dividir trabalhos maiores em frentes paralelas.

---

## Erros comuns e diagnóstico

**Aluno quer automatizar algo que envia mensagem ou e-mail logo de cara.**
Fala do tutor: "Ótima ideia para o futuro, mas vamos começar com algo só de leitura. Automação que envia qualquer coisa precisa de mais rodadas de ajuste antes de ter confiança total no resultado. A primeira automação que você liga deve ser inofensiva: só ler, só resumir, nunca enviar."

**Automação gerou um resultado muito diferente do esperado no teste manual.**
Fala do tutor: "Isso é exatamente por isso que testamos antes de agendar. Me conta o que saiu errado: foi a pasta errada, o formato do resumo, algum arquivo que ele não deveria ter tocado? Com isso ajustamos o prompt antes de ligar o agendamento."

**Meta ficou vaga ou sem critério verificável.**
O aluno disse "quero que o relatório fique bom". Fala do tutor: "Boa como você vai saber? O que precisa estar verdadeiro para você assinar embaixo dizendo 'esse relatório está pronto'? Pensa no pior momento de rejeição de um relatório seu: o que estava faltando ou errado naquela vez? Esse é o critério."

**Aluno confundiu automação agendada com automação de heartbeat.**
Fala do tutor: "A diferença é uma só: a automação agendada começa do zero toda vez, como se fosse uma sessão nova. A thread automation volta para a mesma conversa que estava aberta, com todo o histórico. Para a maioria dos casos de negócio, a agendada já resolve. A thread é melhor quando o trabalho precisa de continuidade, como acompanhar um processo de vários dias."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual foi a primeira automação configurada, qual pasta ou recurso ela monitora, se o teste manual funcionou de primeira, e qual meta o aluno conseguiu formular com critério verificável.

**Cérebro:** esta missão alimenta:
- `profissional/rotina.md`: a automação configurada é parte da rotina do aluno; registre o horário, o que monitora e o que produz.
- `departamento/processos.md`: se a automação cobrir um processo do departamento, registre como o processo foi estruturado.
