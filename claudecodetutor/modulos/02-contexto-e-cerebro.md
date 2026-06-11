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

### Ato 1: o experimento A (sem contexto)

Na sessão de prática, peça ao aluno que envie o prompt abaixo como está, sem adicionar nenhuma informação extra:

> "Escreva um e-mail de follow-up para um cliente que pediu um orçamento há três dias e ainda não respondeu."

Quando o resultado aparecer, pause. Pergunte:

> "Esse e-mail poderia ter sido escrito para qualquer empresa de qualquer setor, certo? Tem algo que seu cliente real reconheceria como vindo da [área/empresa do aluno]?"

Deixe o aluno responder. O objetivo é que ele próprio nomeie o que está faltando: nome da empresa, produto específico, tom de voz, urgência certa para o contexto dele.

**Verificação:** aluno identifica pelo menos dois elementos genéricos no resultado.

---

### Ato 2: o arquivo de contexto da oficina

Apresente o arquivo de contexto que o app lê automaticamente ao abrir a pasta:


> "Na pasta da oficina, há um arquivo chamado `CLAUDE.md`. Ele foi criado durante a instalação. Vamos abri-lo."

Abra o arquivo junto com o aluno. Explique: "Esse é o manual de integração do agente. Cada vez que você abre uma sessão nessa pasta, ele lê isso primeiro, antes de qualquer mensagem sua. É o que ele sabe sobre você desde o início."

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

Na sessão de prática, peça ao aluno que repita o prompt do Ato 1 exatamente como estava:

> "Escreva um e-mail de follow-up para um cliente que pediu um orçamento há três dias e ainda não respondeu."

Quando o resultado aparecer, coloque os dois lado a lado (o do Ato 1 e o do Ato 4) e pergunte:

> "O que mudou? O que você usaria de verdade agora que não usaria antes?"

Esse é o momento "percebeu?". Se o aluno estiver animado, aponte explicitamente: "Repara que você não precisou explicar nada sobre a empresa nesta segunda vez. O agente já sabia. É assim que ele deixa de ser genérico e passa a ser seu."

**Verificação:** aluno identifica a diferença concreta entre os dois resultados e articula por que o segundo está mais próximo do uso real.

---

### Ato 5: memórias nativas do app (camada complementar)

Após o experimento, apresente o mecanismo de memória nativa do app. Duas a três linhas, sem entrar em detalhes técnicos:


O app tem um sistema de **auto memory**: ele extrai automaticamente aprendizados das sessões (padrões, preferências, correções que você deu) e os salva em arquivos na pasta de memória do projeto (`%USERPROFILE%\.claude\projects\...\memory\`). Esses arquivos são carregados automaticamente nas sessões seguintes. Quando você vê "Writing memory" ou "Recalled memory" na interface, é esse mecanismo trabalhando.

Você pode auditar e editar esses arquivos a qualquer momento com o comando `/memory`. A regra prática: contexto importante vive em arquivo que você aprovou (visível, editável, portátil). A auto memory é uma camada adicional de conveniência, não o lugar certo para informações críticas que precisam ser precisas.

**Verificação:** aluno entende que os arquivos do cérebro têm precedência sobre a memória nativa porque são visíveis, editáveis e aprovados por ele.

---

## Variações por função

O par "tarefa sem contexto / tarefa com contexto" calibrado por área:

| Área | Prompt do Ato 1 e 4 (idêntico nos dois atos) | O que o contexto muda |
|---|---|---|
| Financeiro | "Escreva um resumo executivo do fechamento do mês para a diretoria." | Período, indicadores monitorados, tom formal ou técnico da empresa |
| Comercial | "Escreva um e-mail de follow-up para um cliente que pediu um orçamento há três dias e ainda não respondeu." | Nome da empresa, produto/serviço, urgência adequada ao ciclo de vendas |
| Operações | "Escreva um comunicado interno informando um atraso na entrega de um pedido." | Jargão interno, nível de formalidade, canal preferido da equipe |
| Marketing | "Escreva uma legenda para um post no LinkedIn sobre um novo produto." | Tom de voz da marca, público-alvo, diferenciais do produto |
| Engenharia | "Escreva uma descrição de tarefa para a equipe implementar uma nova funcionalidade." | Stack técnica, convenções de nomenclatura, critérios de aceitação padrão |
| Holding/direção | "Escreva um sumário executivo com os pontos de atenção do mês para apresentar às áreas." | Estrutura de reporte, métricas priorizadas, tom para liderança sênior |

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
