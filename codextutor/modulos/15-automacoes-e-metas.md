# Módulo: Automações e metas
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 30-40 min
**Resultado:** o aluno entende a diferença entre os tipos de automação disponíveis, configura a primeira automação inofensiva da sua área (resumo diário de uma pasta) e sabe formular metas com critério de verificação real.

---

## Conceito em 1 minuto

Automação é uma instrução que o agente executa sem você precisar estar presente. Você define o que ele faz, quando faz e o que entrega. Quando você chega, o trabalho de coleta e organização já está pronto na sua mesa.

Há dois tipos disponíveis. O primeiro começa do zero no horário marcado: ideal para trabalhos que não precisam de histórico anterior. O segundo retorna a uma conversa que estava em andamento, com todo o contexto acumulado: ideal para acompanhamentos de vários dias, onde "lembrar o que aconteceu antes" importa.

A regra que nenhum gestor deve quebrar: o agente pesquisa, organiza e rascunha. O humano decide e envia. Automação que age sobre outros sem sua aprovação não é eficiência, é risco. O padrão seguro se chama chefe de gabinete: tudo preparado na mesa, nada enviado sem você ver.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: entender os tipos de automação

Antes de configurar qualquer coisa, localize o recurso no app e mostre os tipos ao aluno. O conteúdo exato depende da plataforma:

> "No app, existe uma aba chamada Automations. Vamos abrir juntos."

Com a aba aberta, explique:

> "Existem dois tipos. O primeiro começa do zero toda vez que roda: ideal para resumos, listagens e qualquer trabalho que não precisa lembrar de execuções anteriores. O segundo retorna à mesma conversa que estava em andamento: é como um colega que pediu para checar algo todo dia e continua de onde parou. Para começar, vamos usar o primeiro tipo: mais simples e já resolve a maioria dos casos de negócio."

Confirme que o aluno encontrou a aba Automations.


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

### Ato 3: configurar a primeira automação com resultado real

Use a resposta do Ato 2 para escolher a automação. A lógica: começa inofensiva (só lê, só resumo, nunca envia), mas precisa produzir algo que o aluno USARIA de verdade.

Versão para quem monitorou arquivos de trabalho:

> "Toda manhã, leia os arquivos da pasta [pasta escolhida pelo aluno: downloads, relatórios, área de trabalho]. Para cada arquivo novo ou modificado nas últimas 24 horas: escreva o nome do arquivo, uma linha sobre o que parece conter e se há algum prazo ou número relevante visível. Salve o resumo como `resumo-AAAA-MM-DD.md` na mesma pasta. Não envie nada, não altere nenhum arquivo existente."

Versão para quem tem uma pasta de e-mails exportados ou mensagens de equipe:

> "Toda manhã, leia os arquivos de mensagens da pasta [pasta de mensagens]. Classifique o que chegou em: (1) ação necessária hoje, (2) aguardando resposta de terceiros, (3) informação apenas. Para cada item de ação, escreva uma linha com o assunto e o próximo passo sugerido. Salve como `briefing-AAAA-MM-DD.md` na pasta missões/. Não envie nada."

Configure a automação juntos:

Na aba Automations, crie uma nova automação com o prompt escolhido. Configure a cadência para diária no horário que o aluno chega ao trabalho. Antes de ativar, rode manualmente: clique em "Run now" ou equivalente. Mostre ao aluno onde o resultado aparece (seção Triage ou histórico da automação).


Após o teste manual rodar:

> "Veja o que chegou na pasta. Isso é o que você vai encontrar na mesa amanhã de manhã, sem precisar abrir o sistema ou varre a pasta manualmente. O agente trabalhou; você decide o que fazer com o briefing."

**Verificação:** automação configurada, teste manual executado com sucesso, resultado visível e aluno consegue dizer para que usaria o arquivo gerado.

---

### Ato 4: metas com critério verificável

Feche o módulo com o conceito de metas. A ideia é simples: qualquer instrução fica mais poderosa quando você diz ao agente como ele vai saber que terminou.

> "Automação sem critério de conclusão vira instrução aberta. O que diferencia uma meta de uma vontade é o seguinte: como você vai saber, sem dúvida, que o trabalho está pronto? Se a resposta é 'quando eu olhar e gostar', ainda não é uma meta. Meta é quando a condição é objetiva."

Mostre a diferença com um exemplo da área do aluno (adapte pela tabela de variações):

> "Uma instrução fraca: 'limpe os dados do relatório.' O agente para quando achar que fez o suficiente. Uma instrução forte: 'verifique todos os campos obrigatórios do relatório; o trabalho está pronto quando nenhum campo obrigatório estiver vazio e todas as datas estiverem no formato DD/MM/AAAA, confirmado linha por linha no final.' O critério de verificação é o que transforma a instrução em meta."

O recurso que aplica isso formalmente na plataforma:

> "No Codex, o comando `/goal` define a condição de conclusão antes de iniciar: o agente trabalha em ciclos até a condição ser satisfeita e para sozinho. Para usar: escreva `/goal [condição verificável]` no campo de mensagem, antes de qualquer instrução de tarefa. A habilitação depende da versão do seu app: veja em Configurações > Funcionalidades."

Se o recurso não estiver disponível na versão atual, a condição de verificação ainda funciona como instrução no prompt: o aluno inclui "ao final, verifique [condição] e me diga se está correto".


Na sessão de prática, peça ao aluno:

> "Pega um tipo de trabalho que você delegaria se tivesse alguém disponível. Escreva a condição de conclusão: como essa pessoa saberia, sem nenhuma dúvida, que o trabalho está pronto para você ver? Testa essa condição no campo de mensagem com o resultado da automação que configuramos."

> "Quando terminar, me manda um ok que eu confiro o resultado direto."

**Verificação:** aluno formulou pelo menos uma meta com critério verificável e testou a condição no app.

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
