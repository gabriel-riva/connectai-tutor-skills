# O cérebro do aluno: manual do tutor

> Como cultivar a memória durável de trabalho do aluno. O cérebro é o que transforma "um app de IA" em "MEU assistente, que conhece meu mundo".

---

## O princípio: efeito colateral, nunca lição de casa

Pedir ao aluno que "documente sua empresa" antes de começar a usar IA é o caminho mais rápido para matar a motivação. Parece burocracia. Parece dever de casa. E o aluno ainda não sente por que aquilo importa.

O cérebro cresce de forma diferente: **o tutor escreve, o aluno revisa e aprova.**

Durante cada missão prática, o tutor observa o que o aluno compartilha: o nome da empresa, o segmento, os produtos, como ele se refere à equipe, qual é o tom que ele usa nos e-mails. No final da missão (ou na transição entre uma e outra), o tutor propõe um pequeno registro:

> "Você mencionou que a empresa atende distribuidoras regionais. Posso salvar isso em `empresa/contexto.md`? Confirma se está correto."

O aluno lê, ajusta se quiser, e aprova. Simples assim.

Esse fluxo tem três vantagens práticas:

1. **O aluno sente o valor imediatamente.** Na próxima missão, o tutor já sabe o que é a empresa. Não precisa perguntar de novo. Isso é o momento "percebeu?" (detalhado abaixo).
2. **O esforço cai para zero.** O aluno não escreveu nada, só confirmou. A barreira de entrada é mínima.
3. **O contexto é validado.** O que vai para o cérebro foi aprovado pelo próprio aluno, então é preciso.

A regra de ouro: **nunca peça ao aluno que preencha o cérebro como tarefa separada.** Se a informação não surgiu naturalmente numa missão, ela não está pronta para entrar no cérebro.

---

## A estrutura

A oficina tem uma pasta `cérebro/` com cinco subpastas. Cada uma tem um propósito claro.

```
cérebro/
├── pessoal/
├── profissional/
└── empresa/
├── departamento/
└── equipe/
```

### `pessoal/`

O que define o jeito do aluno de comunicar e trabalhar. Não é sobre a empresa; é sobre a pessoa.

Exemplos de arquivos:
- `como-escrevo.md`: tom preferido (formal, direto, com ou sem emoji), expressões que usa, o que evita.
- `preferencias.md`: prefere listas ou parágrafos? Bullet points curtos ou explicações completas?
- `como-aprendo.md`: prefere passo a passo, exploração livre ou escolha entre caminhos? Quais exemplos e analogias funcionam melhor?
- `contexto-pessoal.md`: fuso horário, idioma de trabalho, se lidera equipe ou trabalha sozinho.

**O que NÃO guardar aqui:** dados pessoais sensíveis (CPF, endereço, dados médicos), senhas ou credenciais de qualquer tipo.

### `profissional/`

A função do aluno dentro da organização.

Exemplos de arquivos:
- `quem-sou.md`: cargo, tempo na empresa, área de atuação, a quem reporta.
- `responsabilidades.md`: o que o aluno é responsável por entregar, quais decisões estão na sua alçada.
- `rotina.md`: rituais semanais, cadência de reuniões, ciclos de fechamento ou revisão.

**O que NÃO guardar aqui:** detalhes salariais, avaliações de desempenho, conflitos internos.

### `empresa/`

O contexto da organização que o aluno representa.

Exemplos de arquivos:
- `contexto.md`: segmento, tamanho aproximado, região de atuação, proposta de valor principal.
- `produtos-servicos.md`: o que a empresa vende, para quem, diferenciais percebidos.
- `branding.md`: tom de voz institucional, termos que a empresa usa (e os que evita), cores e identidade se relevante.

**O que NÃO guardar aqui:** dados financeiros confidenciais, informações de clientes identificáveis, segredos comerciais sensíveis.

### `departamento/`

O funcionamento da área do aluno.

Exemplos de arquivos:
- `processos.md`: fluxos principais que o departamento executa, ferramentas usadas.
- `indicadores.md`: métricas que o departamento acompanha, metas em vigor, ciclo de reporte.
- `sistemas.md`: quais softwares e plataformas o departamento usa no dia a dia.

**O que NÃO guardar aqui:** dados pessoais de clientes ou funcionários, contratos em vigor com valores, informações sob NDA específico.

### `equipe/`

As pessoas com quem o aluno trabalha diretamente.

Exemplos de arquivos:
- `quem-e-quem.md`: nomes, funções e papéis principais das pessoas da equipe imediata.
- `interacoes.md`: como a equipe se comunica (reuniões, canais, frequência), quem decide o quê.
- `estilos.md`: observações sobre preferências de comunicação de colegas-chave (útil para rascunhar mensagens ou preparar reuniões).

**O que NÃO guardar aqui:** opiniões negativas sobre colegas, conflitos interpessoais, avaliações de desempenho de terceiros. Dados de terceiros entram com parcimônia: só o que o aluno precisaria dizer em voz alta num contexto profissional normal.

---

## As cinco regras de cultivo

### 1. Memória durável de trabalho

O cérebro guarda o que precisa sobreviver entre sessões. A pergunta-filtro é: "Se essa sessão fosse encerrada agora e eu voltasse daqui a duas semanas, o que eu precisaria saber para continuar de onde parei?" Só isso entra.

Não é um diário. Não é arquivo morto. É um conjunto enxuto de verdades que o tutor pode carregar no o CLAUDE.md da oficina para ter o contexto do aluno disponível imediatamente.

### 2. Notas canônicas, não proliferação

Um arquivo bom por assunto, atualizado, vale mais do que dez notinhas espalhadas. Quando uma nova informação surge que complementa algo já registrado, o tutor atualiza o arquivo existente. Quando surge algo novo sem lar, o tutor cria um arquivo e propõe o nome ao aluno.

A regra: antes de criar um arquivo novo, verificar se a informação não pertence a um arquivo já existente.

### 3. Roteamento explícito

Decisões, pessoas, projetos e pendências têm lugar certo no cérebro. O tutor não guarda nada "em algum lugar". A cada registro, o caminho é declarado:

> "Vou salvar isso em `departamento/indicadores.md` porque é uma meta da área."

Isso treina o aluno a pensar em roteamento, o que será útil quando ele começar a organizar informações por conta própria.

### 4. Preservar o que dói perder

Algumas informações têm vida curta na memória do aluno, mas impacto duradouro no trabalho: uma decisão tomada numa reunião, um bloqueio que foi resolvido de forma não óbvia, um link útil que levou tempo para encontrar. O tutor tem o radar ligado para esses momentos e propõe o registro na hora.

Formato sugerido para decisões: `data | decisão | quem aprovou | contexto em uma frase`.

### 5. Anti-churn

Se nada relevante mudou desde a última sessão, o tutor não mexe no cérebro. Atualização por atualização gera ruído. O cérebro só cresce quando há algo genuinamente novo para registrar.

A pergunta-filtro antes de qualquer edição: "O que está registrado ainda é verdade e suficiente?" Se sim, não tocar.

---

## Tabela: missão a o que ela alimenta no cérebro

| Missão | Arquivo alimentado | O que capturar |
|---|---|---|
| Entrevista inicial (onboarding) | `profissional/quem-sou.md` | Cargo, área, responsabilidades principais |
| Primeiras sessões de aprendizado | `pessoal/como-aprendo.md` | Ritmo, autonomia, analogias úteis, tipo de condução preferida |
| Missão de branding ou apresentação | `empresa/branding.md` | Tom de voz, termos oficiais, identidade |
| Missão de relatório ou dashboard | `departamento/indicadores.md` | Métricas acompanhadas, ciclo de reporte |
| Missão de e-mail ou comunicação | `pessoal/como-escrevo.md` | Tom preferido, expressões recorrentes |
| Missão de reunião ou pauta | `equipe/quem-e-quem.md` | Participantes, papéis, decisões tomadas |
| Missão de processo ou fluxo | `departamento/processos.md` | Etapas, ferramentas, responsáveis |
| Missão sobre produtos ou serviços | `empresa/produtos-servicos.md` | O que vende, para quem, diferencial |
| Missão de rotina ou checklist | `profissional/rotina.md` | Rituais, cadências, ciclos fixos |
| Missão com uso de sistemas internos | `departamento/sistemas.md` | Ferramentas usadas, integrações relevantes |
| Missão com contexto de clientes | `empresa/contexto.md` | Segmento atendido, perfil do cliente típico |

---

## O momento "percebeu?"

Este é um dos momentos mais importantes de toda a trilha. Ele não precisa ser agendado; precisa ser reconhecido quando acontece naturalmente.

**Quando acontece:** a partir da segunda missão que reutiliza um contexto já salvo no cérebro. O tutor executa a missão sem perguntar algo que já está registrado. O aluno raramente nota na primeira vez. Na segunda ou terceira, nota.

**O que o tutor faz:** parar um instante e apontar explicitamente.

Fala pronta (adaptar ao tom da relação):

> "Repara numa coisa: essa missão eu não perguntei nada sobre a empresa. Já sabia o segmento, o nome dos produtos e o tom que você usa. Isso veio do cérebro que a gente foi montando juntos. É assim que o assistente para de ser genérico e começa a ser seu."

**Por que esse momento importa:** explicar "contexto" antes de mostrar o efeito não funciona. O conceito fica abstrato. Quando o aluno vive o antes e o depois (perguntas repetidas versus fluência imediata), ele internaliza o valor de forma visceral. Não precisa acreditar na promessa; ele já viu acontecer.

**Frequência:** uma vez com cuidado vale mais do que várias vezes correndo. Se o momento natural não surgir até a quarta sessão, o tutor pode criar uma pequena demonstração contrastiva: executar uma tarefa sem contexto (mostrando as perguntas que seriam necessárias) e depois com o cérebro carregado.

---

## Revisão periódica

A cada três ou quatro sessões, o tutor reserva cinco minutos ao final para uma revisão rápida do cérebro.

**Roteiro:**

1. Abrir os arquivos principais com o aluno presente.
2. Perguntar: "Isso ainda é verdade?" para cada ponto relevante.
3. Perguntar: "Tem algo que mudou desde a última vez que deveria estar aqui?"
4. Atualizar o que for necessário, sempre com aprovação do aluno.
5. Arquivar (ou deletar) o que ficou obsoleto.

**Tom:** leve e prático, nunca burocrático. Não é uma auditoria. É uma manutenção de dois minutos de algo que pertence ao aluno.

**Resultado esperado:** ao final de oito a dez sessões, o cérebro já tem densidade suficiente para que qualquer missão nova parta de um contexto rico. O aluno percebe que o assistente "sabe muito" sobre seu trabalho, e isso reforça o hábito de manter o cérebro vivo.

A revisão periódica também é o momento de celebrar o crescimento: mostrar como o arquivo `empresa/contexto.md` evoluiu da primeira linha para um retrato completo do negócio, construído sem esforço extra, missão por missão.
