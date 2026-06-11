# Módulo: Contexto e cérebro
**Nível:** núcleo · **Pré:** 01 · **Tempo típico:** 25-35 min
**Resultado:** o aluno entende por que contexto muda a qualidade do resultado, alimenta o primeiro arquivo do cérebro com aprovação consciente e conhece o mecanismo nativo de memória do app como camada complementar.

---

## Conceito em 1 minuto

Um estagiário no primeiro dia faz perguntas genéricas porque não conhece a empresa. O mesmo estagiário depois de seis meses responde sem precisar de briefing: já sabe o segmento, os produtos, o tom de voz, os clientes habituais. A diferença não é inteligência; é contexto acumulado.

O agente funciona da mesma forma. Sem contexto, cada sessão começa do zero: as respostas saem corretas para o mundo em geral, mas genéricas para o seu caso. Com contexto, o agente já sabe quem é você, o que a empresa faz e como você gosta de trabalhar. Esse contexto não mora na cabeça do agente; mora em arquivos da sua pasta que o app lê automaticamente ao abrir. Você escreve uma vez, colhe em toda sessão futura.

---

## Missão guiada

> Um ato de cada vez. Aguarde o aluno completar antes de passar ao próximo.

**Se a Fundação já foi feita no encontro:** quando `cérebro/` já tem arquivos criados na atividade coletiva com o instrutor (pessoal, profissional, empresa, branding), NÃO recomece do zero nem reapresente o que o aluno já viu. Leia o que existe e cite um detalhe concreto de lá ("vi aqui que você registrou que a empresa atende distribuidoras") para o aluno sentir que aquilo já está vivo. O A/B continua valendo, e fica até mais forte: no Ato 1, peça o prompt com a instrução explícita de ignorar o contexto da pasta; no Ato 4, o mesmo prompt normal, colhendo o cérebro já populado. No Ato 2, em vez de apresentar o arquivo de contexto como novidade, revise com o aluno o que ele escreveu no encontro e complete o que faltar. O restante do módulo vira aprofundamento, nunca repetição.

### Ato 1: o experimento A (sem contexto)

Antes de começar, leia `tutor/PERFIL.md` para escolher a tarefa certa da tabela de variações. A tarefa do A/B precisa ter substância real: não "escreva um e-mail" genérico (isso qualquer chat já faz), mas uma situação concreta da área do aluno que mostre o que muda quando o agente conhece o contexto.

Na sessão de prática, peça ao aluno que envie o prompt da coluna "Prompt do Ato 1 e 4" da tabela de variações abaixo, correspondente à área dele. Sem adicionar nenhuma informação extra.

Quando o resultado aparecer, pause. Pergunte:

> "Esse resultado poderia ter saído para qualquer empresa de qualquer setor, certo? Tem algo que o seu destinatário real reconheceria como vindo da [área/empresa do aluno]? Falta o quê, especificamente?"

Deixe o aluno responder. O objetivo é que ele próprio nomeie o que está faltando: nome da empresa, produto específico, tom de voz, jargão interno, urgência certa para o contexto dele.

**Verificação:** aluno identifica pelo menos dois elementos genéricos no resultado.

---

### Ato 2: o arquivo de contexto da oficina

Apresente o arquivo de contexto que o app lê automaticamente ao abrir a pasta:

> "Na pasta da oficina, há um arquivo chamado `AGENTS.md`. Ele foi criado durante a instalação. Vamos abri-lo."

Abra o arquivo junto com o aluno. Explique: "Esse é o manual de integração do agente. Cada vez que você abre uma thread nessa pasta, ele lê isso primeiro, antes de qualquer mensagem sua. É o que ele sabe sobre você desde o início."

Mostre o que já está dentro (o que foi configurado na instalação) e identifique o que ainda falta: informações sobre a função do aluno, a empresa, o tom de voz desejado.


**Verificação:** aluno localizou o arquivo e entendeu que ele é lido automaticamente a cada abertura.

---

### Ato 3: alimentar contexto real

Com base no que o aluno contou na entrevista inicial (leia `tutor/PERFIL.md` antes desta missão), proponha um bloco de 5 a 8 linhas sobre a função e a empresa do aluno. Apresente como rascunho, não como fato consumado:

> "Com base na nossa conversa, escrevi isso aqui. Leia devagar e me diz se está correto ou se quer ajustar alguma coisa."

Exemplo de estrutura (adapte com os dados reais do aluno):

```
Sou [cargo] na [empresa], responsável por [responsabilidades principais].
A empresa atua em [segmento], atende [perfil de cliente] e tem aproximadamente [porte].
Nos meus e-mails e documentos, prefiro um tom [formal/direto/próximo].
Os termos que uso no dia a dia incluem: [termo 1], [termo 2], [termo 3].
```

Após a aprovação do aluno, grave o conteúdo no cérebro em `cérebro/profissional/quem-sou.md` (e, se o aluno falou sobre a empresa, em `cérebro/empresa/contexto.md`). Confirme o caminho em voz alta:

> "Vou salvar em `cérebro/profissional/quem-sou.md` porque é sobre a sua função. Confirma?"

**Verificação:** arquivo salvo com aprovação explícita do aluno.

---

### Ato 4: o experimento B (com contexto)

Na sessão de prática, peça ao aluno que repita exatamente o mesmo prompt do Ato 1, sem adicionar nenhuma informação extra. Diga:

> "Quando o resultado aparecer, me manda um ok que eu confiro os dois resultados lado a lado direto na sessão de prática."

Ao receber o ok, compare os dois resultados. Depois pergunte ao aluno:

> "O que mudou? Tem alguma frase, dado ou tom que você usaria de verdade agora, mas não usaria antes?"

Esse é o momento "percebeu?". Aponte explicitamente:

> "Repara que você não precisou explicar nada sobre a empresa nesta segunda vez. O agente já sabia. A diferença entre o primeiro e o segundo resultado não está no que você pediu, está no que ele já tinha. É assim que o contexto transforma um agente genérico em parceiro da sua área."

Conecte com o que vem a seguir:

> "E esse arquivo que gravamos juntos, o `quem-sou.md`, vai estar lá amanhã, na próxima sessão e em todas as seguintes. Você escreve uma vez, colhe sempre. O próximo módulo vai mostrar onde essa memória mora e como você a edita."

**Verificação:** aluno identifica a diferença concreta entre os dois resultados e articula por que o segundo está mais próximo do uso real.

---

### Ato 5: memórias nativas do app (camada complementar)

Após o experimento, apresente o mecanismo de memória nativa do app. Duas a três linhas, sem entrar em detalhes técnicos:

O Codex tem uma camada de **memórias** (disponível em Settings > Personalization > Memories quando habilitada no plano). Ele extrai automaticamente preferências e padrões das conversas passadas e os carrega em threads futuras, sem que você precise escrever nada. É uma conveniência para preferências que surgem no uso natural.

A regra prática: contexto importante vive em arquivo (visível, editável, portátil). As memórias são uma camada adicional de conveniência, não o lugar certo para informações críticas sobre a empresa ou a função.


**Verificação:** aluno entende que os arquivos do cérebro têm precedência sobre a memória nativa porque são visíveis, editáveis e aprovados por ele.

---

## Variações por função

O par "tarefa sem contexto / tarefa com contexto" calibrado por área. Cada prompt deve ter substância de área: situação real, destinatário real, decisão real. Não use prompts que qualquer chat já responde bem.

| Área | Prompt do Ato 1 e 4 (idêntico nos dois atos) | O que o contexto muda (e por que chat genérico não resolve) |
|---|---|---|
| Financeiro | "Escreva um parágrafo de explicação para a diretoria sobre uma queda de margem este mês." | Sem contexto: explicação genérica sem os indicadores monitorados, sem o tom da empresa e sem nomear qual margem. Com contexto: usa os KPIs reais, o ciclo de fechamento e o nível de formalidade aprovado. |
| Comercial | "Rascunhe a resposta para um cliente que pediu desconto de 15% numa proposta de equipamento industrial enviada há quatro dias." | Sem contexto: texto de desconto padrão sem produto específico, sem ciclo de vendas da área nem tom da empresa. Com contexto: menciona o produto, o prazo típico de decisão e o argumento de valor que a empresa usa. |
| Operações | "Escreva um comunicado para a equipe explicando um atraso de dois dias numa entrega importante para um cliente." | Sem contexto: genérico, poderia ser de qualquer setor. Com contexto: usa o jargão interno, a cadência de comunicação e o canal preferido da equipe da empresa. |
| Marketing | "Escreva um texto de apresentação de um novo produto para o site da empresa." | Sem contexto: tom neutro, sem os diferenciais da marca nem o público específico. Com contexto: usa o tom de voz definido, as expressões que a empresa evita e o público-alvo correto. |
| Engenharia | "Escreva um relatório de encerramento de uma ordem de serviço de manutenção corretiva." | Sem contexto: formato genérico sem os critérios de aceitação, sem jargão técnico da área nem o destinatário correto. Com contexto: segue o padrão de registro da empresa e nomeia os indicadores monitorados. |
| Holding/direção | "Prepare um sumário executivo com os pontos de atenção das empresas do grupo para a reunião de diretoria desta semana." | Sem contexto: estrutura genérica sem as métricas prioritárias do grupo nem o nível de detalhe esperado pela diretoria. Com contexto: reflete a estrutura de reporte, as empresas e os indicadores que a diretoria acompanha. |

---

## Aprofundamento

Para quem quiser ir além: o módulo 21 aprofunda o segundo cérebro completo, com estrutura de pastas, critérios de roteamento e revisão periódica. O que foi feito aqui é o primeiro tijolo.

A regra anti-churn em uma frase: se nada genuinamente novo surgiu desde a última sessão, não mexa no cérebro. Atualização por atualização sem conteúdo novo gera ruído e dilui o valor do que já está lá.

---

## Erros comuns e diagnóstico

**Despejar a empresa inteira no contexto de uma vez.**
Aluno quer copiar o site, o folder e o regulamento interno todos para o arquivo. Resposta: "Contexto canônico vale mais do que volume. Cinco linhas precisas sobre o que você faz e como a empresa se posiciona são mais úteis do que vinte páginas que o agente vai ter que filtrar. Vamos começar com o mínimo e adicionar só o que faz diferença."

**Contexto desatualizado.**
Aluno muda de cargo ou de área e o arquivo continua falando do que era antes. Resposta: "A cada três ou quatro sessões, vale abrir o arquivo e perguntar: isso ainda é verdade? Se mudou, atualiza. Se não mudou, deixa quieto."

**Colocar senhas ou dados sigilosos no contexto.**
Resposta imediata e firme: "Nunca senha, nunca credencial de sistema, nunca dado pessoal sensível de terceiro nesses arquivos. O que vai pro contexto é o que você diria em voz alta numa reunião de trabalho normal."

**Esperar mágica sem contexto específico da tarefa.**
Aluno fornece contexto geral mas não adapta o prompt para o caso concreto. O resultado melhora em tom, mas ainda é genérico em substância. Resposta: "O contexto geral ajuda o tom e o vocabulário. Para o conteúdo ser preciso, o prompt também precisa ser preciso. Experimenta adicionar um detalhe específico da situação: qual produto, qual cliente, qual prazo."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre como o aluno reagiu ao experimento A/B (surpresa? ceticismo? entusiasmo?), quais ajustes fez no rascunho proposto antes de aprovar e qual trecho específico do resultado com contexto o aluno destacou como mais útil.

**Cérebro:** este é o primeiro módulo que alimenta o cérebro formalmente. Os arquivos aprovados neste módulo são:
- `cérebro/profissional/quem-sou.md` (cargo, área, responsabilidades principais)
- `cérebro/empresa/contexto.md` (se informações da empresa surgiram durante a entrevista)

Confira a tabela de roteamento em `cerebro.md` para missões futuras que alimentam outras subpastas.
