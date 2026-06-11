# Módulo: Pesquisa na web
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno conduz uma pesquisa real de mercado, fornecedores, preços ou normas com fontes citadas e resultado em tabela comparativa, e cria um modelo de monitoramento de tema para repetir sem esforço manual.

---

## Conceito em 1 minuto

No primeiro módulo você viu o agente fazer uma pesquisa com fontes rodando alguns minutos sozinha. Aqui você aprofunda isso: aprende a construir comparativos que apoiam decisões reais, a verificar o que chegou e a transformar pesquisa pontual em monitoramento de tema.

A diferença entre pesquisa manual e pesquisa com agente não está na velocidade, está no que você consegue fazer com o resultado: em vez de vinte abas para fechar, você recebe uma tabela com fontes anotadas, pronta para levar a uma reunião ou usar numa decisão de compra.

A regra de ouro de qualquer pesquisa assistida: fontes importam. Peça sempre a origem de cada afirmação. Informação sem fonte é rascunho, não pesquisa.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: escolher a pesquisa real

Pergunte ao aluno qual pesquisa ele precisaria fazer nos próximos dias: um fornecedor novo, um preço de referência, uma norma regulatória, um concorrente. Diga:

> "Pensa numa pesquisa de mercado ou de fornecedor que você deveria fazer esta semana e ainda não fez. Qualquer assunto da sua área: preço de insumo, alternativa de fornecedor, norma técnica, tendência de mercado."

Registre o tema. A pesquisa será feita de verdade, não como exercício fictício.

**Verificação:** aluno nomeou um tema real.

---

### Ato 2: a pesquisa com fontes citadas

Na sessão de prática, passe o modelo com o tema do aluno:

> "Pesquise [tema exato] com foco em [objetivo: preço de referência / fornecedores no mercado brasileiro / requisitos regulatórios / tendências recentes]. Para cada informação relevante que você encontrar: cite a fonte com o nome do site e a URL. Organize o resultado em uma tabela com as colunas: [Item ou Fornecedor], [Informação Principal], [Fonte]. Ao final, adicione um parágrafo com as suas conclusões principais."

Após o resultado, verifique com o aluno:

> "Tem alguma informação que surpreendeu você? Alguma fonte que você reconhece e outra que não conhecia? Vale a pena clicar em uma ou duas para confirmar?"

O objetivo é que o aluno entenda que a pesquisa é um ponto de partida para verificação, não a palavra final.

**Verificação:** tabela com fontes gerada, aluno conferiu pelo menos uma fonte.

---

### Ato 3: monitorar um tema ao longo do tempo

A pesquisa pontual já está feita. Agora avance para o diferencial que o módulo 01 plantou como promessa: o agente pode repetir uma pesquisa em datas definidas e entregar as novidades sem você precisar pedir de novo.

Na sessão de prática, passe o modelo adaptado ao tema que o aluno escolheu no Ato 1:

> "Pesquise [tema] com foco em [objetivo]. Para cada novidade dos últimos 30 dias, cite a fonte com nome do site e URL. Organize em tabela: [Item], [Novidade], [Fonte], [Data]. No final, liste em uma linha o que mudou desde a última vez que esse assunto foi pesquisado. Salve o resultado como `monitoramento-[tema]-AAAA-MM-DD.md` na pasta missões/."

Após o resultado, mostre que esse mesmo prompt pode virar a base de uma automação agendada (módulo 15): o agente roda sozinho na frequência que o aluno quiser e entrega o resumo de novidades. Por enquanto, salve o prompt em `missões/` como modelo reutilizável.

> "Quando terminar, me manda um ok que eu confiro o arquivo direto."

**Nota de bastidor (não compartilhar com o aluno como "aula"):** quando a pesquisa precisar entrar em portais com login, o caminho muda dependendo da plataforma:

Use `@chrome` no prompt para acessar o Chrome com o perfil do aluno (sessões ativas incluídas). O navegador integrado (`$browser`) serve apenas para páginas públicas. Só mencione isso se o aluno perguntar ou se a tarefa exigir portal autenticado.


**Verificação:** arquivo de monitoramento salvo, aluno entende que o mesmo prompt pode ser repetido automaticamente.

---

### Ato 4: o comparativo em tabela

Com a pesquisa feita, finalize gerando um comparativo estruturado para uso real. Passe o modelo:

> "Com base na pesquisa que fizemos, crie uma tabela comparativa de [fornecedores / opções / normas] com as colunas mais relevantes para uma decisão. Inclua na última linha uma recomendação de qual opção você avaliaria primeiro e por quê, com base apenas nas informações encontradas."

Salve o resultado na pasta `missões/` com a data.

> "Quando terminar, me manda um ok que eu confiro o comparativo direto na pasta."

**Verificação:** comparativo salvo, pronto para uso em uma reunião ou decisão real.

---

## Variações por função

| Área | Pesquisa típica | Comparativo útil |
|---|---|---|
| Financeiro | Taxas de linhas de crédito ou fornecedores financeiros | Banco ou modalidade por custo efetivo |
| Comercial | Concorrentes, preços de referência do mercado | Posicionamento de preço por produto |
| Operações | Fornecedores de insumo, cotação de peça específica | Fornecedor por preço, prazo e localização |
| Marketing | Agências, plataformas de mídia, tendências de segmento | Plataforma por alcance, custo e formato |
| Engenharia | Normas técnicas, especificações de equipamento | Equipamento por especificação e custo |
| Holding | Tendências de setor, benchmarks de gestão | Práticas por segmento e resultado reportado |

---

## Aprofundamento

Para pesquisas que precisam de dados por trás de um login (portal de fornecedor, sistema de cotações, extranet de cliente), o acesso autenticado ao navegador é o caminho, conforme descrito no módulo 17. Há um cuidado importante: sites que exigem login têm termos de uso. Alguns permitem automação, outros não. O aluno deve verificar os termos antes de automatizar qualquer coisa em portais de terceiros.

Para pesquisas recorrentes (cotação semanal de insumos, por exemplo), o módulo 15 sobre automações mostra como transformar uma pesquisa manual em rotina agendada.

---

## Erros comuns e diagnóstico

**Resultado sem fontes ou com fontes vagas.**
O agente listou informações mas sem URL ou nome de site. Fala do tutor: "Inclui no prompt a instrução 'cite o nome do site e a URL completa para cada informação'. Pesquisa sem fonte é rascunho. Com a URL, você consegue verificar se a informação ainda é válida."

**Resultado com informações desatualizadas.**
O agente trouxe dados de anos atrás. Fala do tutor: "Adiciona no prompt: 'priorize fontes de [ano atual] e [ano anterior]; se encontrar uma fonte mais antiga, indique a data e sinalize que pode estar desatualizada'."

**Aluno quer pesquisar em site com login mas não tem a extensão.**
Fala do tutor: "Para esse site específico, vamos precisar da extensão Chrome instalada. Essa é uma configuração de alguns minutos. Quer fazer agora ou continuar com a pesquisa em páginas públicas e agendamos a instalação?"

**Tabela comparativa fica grande demais para ser útil.**
O aluno pediu muitas colunas e o resultado é difícil de ler. Fala do tutor: "Qual é a decisão que você precisa tomar com base nessa tabela? Com essa pergunta em mãos, quais colunas são realmente necessárias para a decisão? Elimina o resto."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre o tema da pesquisa real feita, se o aluno verificou alguma fonte, se teve dificuldade em formular a pesquisa com clareza e se a camada de acesso web foi compreendida.

**Cérebro:** esta missão pode alimentar:
- `empresa/contexto.md`: se a pesquisa trouxe dados sobre o segmento de atuação ou concorrentes.
- `departamento/sistemas.md`: se o aluno tem portais de fornecedores ou plataformas com login que usa regularmente.
