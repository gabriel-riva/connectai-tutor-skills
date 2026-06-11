# Módulo: Planilhas e dados do ERP
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 30-40 min
**Resultado:** o aluno transforma um export real do seu sistema em análise e relatório em menos de dez minutos, sabe contornar as armadilhas brasileiras de formatação e conhece o caminho para pedir à TI mais acesso quando a dor justificar.

---

## Conceito em 1 minuto

Imagine que o sistema da empresa é uma biblioteca enorme, mas com chave. Você só consegue ler um livro de cada vez, copiando à mão as páginas que quer analisar. O export que você faz hoje é isso: uma cópia manual. Neste módulo você aprende a usar essa cópia com muito mais eficiência, e no aprofundamento vemos como pedir à TI uma chave que deixa o agente consultar direto, sem precisar copiar nada.

A limitação não é sua e não é do sistema: é simplesmente como a maioria dos ERPs industriais foram construídos. O foco é sempre no que dá para fazer hoje, com o que você já tem.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: trazer o arquivo real

Peça ao aluno para exportar um relatório do sistema que ele usa toda semana. Qualquer formato serve: Excel, CSV ou PDF. Diga:

> "Antes de abrir qualquer prompt, preciso que você exporte um relatório do seu sistema. Qualquer relatório que você já usa com frequência. Salva na pasta da oficina."

Enquanto o aluno exporta, confirme com ele:

- O cabeçalho começa em qual linha? (Muitos ERPs colocam título e informações antes dos dados reais.)
- As datas estão no formato DD/MM/AAAA?
- Os números usam vírgula como decimal e ponto-e-vírgula como separador de colunas (padrão CSV brasileiro)?

Anote as respostas. Elas vão dentro do primeiro prompt.

**Verificação:** arquivo exportado na pasta da oficina.

---

### Ato 2: o primeiro prompt com contexto de formato

Na sessão de prática, passe o modelo abaixo. Ajuste os colchetes com o aluno antes de enviar:

> "Aqui está meu relatório exportado do [nome do sistema]. Antes de analisar, observe que: o cabeçalho dos dados começa na linha [N]; as datas estão no formato DD/MM/AAAA; os números usam vírgula decimal e ponto-e-vírgula como separador de colunas no CSV. Com base nesse arquivo, me diz: (1) quantas linhas de dados existem; (2) quais são as colunas disponíveis; (3) quais colunas têm dados faltando ou inconsistentes."

Após o resultado, pergunte ao aluno:

> "O que ele identificou bate com o que você esperava? Tem alguma inconsistência que você já conhecia?"

**Verificação:** o aluno recebe uma leitura correta da estrutura do arquivo sem precisar reexplicar o formato.

---

### Ato 3: cruzar duas fontes

Peça ao aluno um segundo arquivo relacionado. Pode ser o mesmo relatório do mês anterior, uma planilha de metas ou uma lista de cadastro. Diga:

> "Agora vamos cruzar dois arquivos. Qual segundo arquivo você quer comparar com o primeiro? Pode ser o mês anterior, uma planilha de metas, qualquer coisa relacionada."

Com os dois arquivos na pasta, passe o modelo:

> "Tenho dois arquivos: [arquivo-1] e [arquivo-2]. Cruze os dados pela coluna [nome da coluna em comum nos dois]. Me mostre: (1) o que aparece no primeiro mas não no segundo; (2) o que aparece no segundo mas não no primeiro; (3) os itens que aparecem nos dois com alguma diferença de valor."

**Verificação:** o aluno vê um cruzamento útil e identifica pelo menos uma discrepância real.

---

### Ato 4: gerar o relatório

Com a análise em mãos, passe o modelo de relatório:

> "Com base nessa análise, gere um relatório de uma página para [destinatário: minha diretoria / meu gestor / minha equipe]. O relatório deve ter: um parágrafo de resumo executivo; uma tabela com os [N] itens mais relevantes que você identificou; e uma seção 'atenção' com no máximo três pontos que precisam de acompanhamento."

Após o resultado, peça ao aluno para revisar:

> "Leia o relatório como se você fosse o destinatário. Tem algo que faltou? Tem algo que precisaria ser mais específico?"

Faça um ajuste junto com o aluno baseado no feedback dele.

**Verificação:** relatório pronto, revisado pelo aluno e salvo na pasta `missões/`.

---

## Variações por função

| Área | Arquivo de partida | Cruzamento útil | Destino do relatório |
|---|---|---|---|
| Financeiro | Faturamento do mês (XLSX) | Metas mensais ou período anterior | Diretoria |
| Comercial | Pedidos em aberto (CSV) | Carteira de clientes ou ciclo de vendas | Gerente comercial |
| Operações | Posição de estoque (XLSX) | Ponto de reposição ou consumo médio | Comprador ou gestor de produção |
| Marketing | Relatório de campanhas (CSV) | Metas de resultado ou investimento | Diretor de marketing |
| Engenharia | Ordens de serviço (XLSX) | SLA contratado ou tempos históricos | Gestor de manutenção |
| Holding | Resultado consolidado (XLSX) | Metas por unidade ou período anterior | Conselho ou diretoria |

---

## Aprofundamento

Para quem quer ir além: a progressão natural a partir do export manual é a escada de quatro degraus descrita em `dados-erp.md`. Este módulo cobre o Degrau 1 (export manual). O Degrau 2 (pasta quente com arquivos padronizados) já é possível sem TI, combinando um ritual de export com a equipe. Os Degraus 3 e 4 precisam de TI, mas o pedido de uma página que abre essa conversa está pronto em `dados-erp.md`.

O tutor usa a ferramenta do aprofundamento quando o aluno verbaliza a dor: "esse export toda segunda é um pé no saco" ou "quando fulano falta, os dados não chegam". Antes disso, não plante a semente.

---

## Erros comuns e diagnóstico

**Arquivo com cabeçalho bagunçado.**
O aluno envia o arquivo e o agente confunde linhas de título com linhas de dados. Fala do tutor: "Descreve para mim como o arquivo está organizado: o título está em qual linha, os dados começam em qual linha, e as colunas têm nome na primeira linha de dados?" Com essa informação, o aluno refaz o prompt incluindo o formato.

**Datas ou números interpretados como texto.**
O agente não consegue calcular com os valores. Fala do tutor: "Adiciona no prompt: 'as datas estão no formato DD/MM/AAAA e os números usam vírgula como decimal'. Isso diz ao agente como tratar os valores antes de calcular."

**Planilha com células mescladas.**
O agente trata células mescladas como dados faltando. Fala do tutor: "Antes de enviar, tenta descomplicar a planilha: remove as células mescladas e salva como XLSX simples. Se não souber fazer, descreve para mim como está e a gente inclui a explicação no prompt."

**Comparação com período anterior gera confusão de nome de colunas.**
Os dois arquivos têm colunas com nomes levemente diferentes. Fala do tutor: "No prompt, especifica qual coluna do primeiro arquivo corresponde a qual coluna do segundo. O agente não adivinha que 'Cod_Cliente' e 'Código do Cliente' são a mesma coisa."

**Relatório sai genérico demais.**
O aluno está satisfeito com o rascunho mas o tutor percebe que poderia ser mais específico. Fala do tutor: "Olha esse parágrafo de resumo: ele poderia ter sido escrito para qualquer empresa. Qual é o dado mais importante que você quer que a diretoria saiba? Vamos adicionar esse dado com o número real."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual sistema o aluno exporta, como estava o formato do arquivo (problema de cabeçalho? datas? separador decimal?), em qual degrau da escada o aluno está hoje, se verbalizou a dor do export manual e se houve resistência ao cruzamento de dados.

**Cérebro:** esta missão alimenta dois arquivos.
- `departamento/sistemas.md`: o sistema que o aluno usa, o formato padrão de export e quaisquer peculiaridades de formato descobertas.
- `departamento/indicadores.md`: as métricas que aparecem no relatório gerado (o que o aluno monitora, a que frequência e para quem reporta).
