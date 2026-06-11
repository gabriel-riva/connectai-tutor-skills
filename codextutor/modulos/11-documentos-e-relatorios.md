# Módulo: Documentos e relatórios
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno lê e resume documentos longos em segundos, padroniza relatórios recorrentes da sua área com um modelo aprovado e alimenta o cérebro com o padrão de escrita do departamento.

---

## Conceito em 1 minuto

Um gestor de uma operação industrial lida com documentos o tempo todo: contratos de fornecedores, manuais técnicos, relatórios de auditoria, atas de reunião, normas regulatórias. Ler cada um do início ao fim para extrair o que importa consome horas que poderiam ir para o trabalho que só o gestor consegue fazer.

O agente lê mais rápido e não cansa. Dê um documento de 60 páginas e pergunte o que você quer saber: ele responde em segundos. A economia real não é na leitura em si, é na atenção que você libera para decidir.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: resumir um documento longo

Peça ao aluno para escolher um documento que está na fila de leitura ou que precisaria de uma segunda leitura. Pode ser um contrato, um manual, um relatório de auditoria ou uma norma. Diga:

> "Tem algum documento longo que você precisa ler ou reler? Pode ser um PDF, um Word, qualquer coisa que está parada esperando sua atenção."

Na sessão de prática, passe o modelo:

> "Leia este documento e me responda: (1) qual é o assunto central em uma frase; (2) quais são os três pontos mais importantes para [cargo e área do aluno]; (3) tem alguma data, prazo ou obrigação que eu precise registrar na agenda; (4) tem algum ponto que exige minha decisão ou ação?"

Após o resultado, pergunte ao aluno:

> "O que o agente identificou que você não teria notado de imediato? Tem algo que ele perdeu?"

**Verificação:** aluno recebe um resumo útil e consegue nomear pelo menos um achado que mudaria seu comportamento sobre aquele documento.

---

### Ato 2: padronizar um relatório recorrente

Peça ao aluno para trazer um relatório que ele produz com frequência: semanal, quinzenal ou mensal. Qualquer formato. Diga:

> "Qual relatório você produz de forma recorrente na sua área? Aquele que você faz toda semana ou todo mês, às vezes do zero?"

Se o aluno tiver um exemplo pronto, peça para trazer. Se não, peça para descrever o que costuma incluir. Com esse insumo, passe o modelo:

> "Vou criar um modelo padrão do meu relatório [semanal/mensal] de [área]. O relatório tem as seguintes seções: [liste as seções que o aluno descreveu]. Para cada seção, crie um placeholder com instrução de preenchimento entre colchetes, mostrando o que vai ali e em que formato. Ao final, adicione uma seção 'destaques da semana' para registrar o que fugiu do padrão."

Após o resultado, revise com o aluno:

> "Esse modelo captura o que você precisa? Falta alguma seção? Tem alguma que você nunca usa e poderia sumir?"

Faça os ajustes e salve o modelo na pasta `missões/` com um nome que o aluno reconheça.

**Verificação:** modelo salvo, aprovado pelo aluno, com placeholders claros que ele consegue preencher sozinho.

---

### Ato 3: usar o modelo para gerar o primeiro relatório real

Com o modelo pronto, passe o insumo da semana atual. Pode ser uma nota de reunião, um print de sistema, uma lista de números. Diga:

> "Agora vamos usar o modelo pela primeira vez. Me traz o que você tem desta semana: notas, números, qualquer coisa."

Na sessão de prática:

> "Aqui está o modelo do meu relatório [frequência] de [área]. Aqui estão os dados desta [semana/mês]: [insumos do aluno]. Preencha o modelo com esses dados. Onde não tiver informação suficiente, mantenha o placeholder com uma nota indicando o que falta."

Após o resultado, compare com um relatório antigo:

> "Compara com o que você produzia antes. O tempo que você levaria para escrever isso do zero versus o tempo que levou agora: qual é a diferença?"

> "Quando terminar de revisar, me manda um ok que eu confiro o relatório direto na pasta."

**Verificação:** primeiro relatório gerado com o modelo, revisado e salvo.

---

## Variações por função

| Área | Documento longo típico | Relatório recorrente |
|---|---|---|
| Financeiro | Contrato de crédito, relatório de auditoria externa | Fechamento mensal, DRE gerencial |
| Comercial | Proposta de fornecedor, edital de licitação | Relatório de pipeline, resumo semanal de negociações |
| Operações | Manual de equipamento, norma de segurança | Relatório de produção, boletim de manutenção |
| Marketing | Pesquisa de mercado, relatório de agência | Relatório de campanhas, resumo de resultados |
| Engenharia | Norma técnica, especificação de projeto | Relatório de progresso, registro de não conformidades |
| Holding | Relatório de consultoria, resultado de subsidiária | Sumário executivo mensal, consolidado de indicadores |

---

## Aprofundamento

Para quem quiser ir além: o modelo de relatório criado neste módulo é o embrião de uma skill. Quando o aluno estiver usando o mesmo prompt toda semana para preencher o modelo, chegou a hora de transformá-lo em uma skill no app, para que baste um comando rápido para iniciar o processo.

Além disso, o relatório gerado pode alimentar diretamente o cérebro: a seção de indicadores do relatório vai para `departamento/indicadores.md`, as seções de processo vão para `departamento/processos.md`. O tutor propõe o registro após cada geração bem-sucedida.

---

## Erros comuns e diagnóstico

**Documento PDF com formatação complexa.**
O aluno envia um PDF com tabelas, colunas ou imagens e o agente interpreta mal. Fala do tutor: "PDFs com formatação muito complexa às vezes chegam truncados ou fora de ordem. Tenta selecionar e copiar o texto diretamente do PDF e colar no chat, em vez de anexar o arquivo. Se o texto for muito longo, cola a parte mais relevante e indica em qual página está."

**Modelo com excesso de seções.**
O aluno quer incluir tudo que já apareceu em qualquer relatório e o modelo fica grande demais para usar na prática. Fala do tutor: "Um modelo que ninguém preenche não serve. Quais três seções são inegociáveis? Começa com essas. O resto pode ser uma seção de observações livres até você decidir se tem espaço."

**Relatório gerado soa impessoal.**
O modelo estava bem, mas o tom do relatório produzido não combina com o estilo do aluno. Fala do tutor: "Isso é sinal de que ainda não adicionamos o tom de voz ao modelo. Mostra para mim um relatório antigo que você gostou do resultado. Com ele, a gente acrescenta ao modelo: 'use o mesmo tom deste exemplo'."

**Aluno não sabe quais seções colocar no modelo.**
Ele nunca pensou estruturalmente no que o relatório precisa ter. Fala do tutor: "Vamos de trás pra frente: quem vai ler esse relatório e qual pergunta essa pessoa quer que o relatório responda? Com a pergunta do leitor em mãos, as seções surgem naturalmente."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual tipo de documento o aluno trouxe (contrato, manual, relatório), como reagiu à leitura automática (surpresa? desconfiança?), quais seções ficaram no modelo após a revisão e se houve resistência a reduzir seções.

**Cérebro:** esta missão alimenta:
- `pessoal/como-escrevo.md`: o modelo aprovado revela o estilo preferido do aluno (formal, direto, com mais ou menos detalhe).
- `departamento/processos.md`: o relatório recorrente é um processo do departamento; registre a cadência e o destinatário.
- `departamento/indicadores.md`: se o relatório incluir métricas, registre quais indicadores o aluno monitora.
