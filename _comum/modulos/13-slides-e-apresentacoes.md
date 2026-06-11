# Módulo: Slides e apresentações
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno transforma conteúdo bruto (relatório, ata de reunião, conjunto de dados) em uma apresentação com estrutura narrativa clara, revisada no painel do app, e sabe qual formato de entrega usar em cada plataforma.

---

## Conceito em 1 minuto

Uma apresentação ruim tem slides onde cada um é uma página de texto. Uma apresentação boa tem slides que sustentam uma conversa: cada um responde uma pergunta antes que o próximo seja aberto. O agente não resolve o que você quer dizer, mas resolve como organizar o que você já sabe. Você traz o conteúdo, ele estrutura a narrativa.

A estrutura mais simples e mais eficaz para qualquer apresentação de negócio: contexto (onde estamos), achado (o que descobrimos ou aconteceu), recomendação (o que precisamos fazer). Três perguntas, três partes, o mínimo que o ouvinte precisa para tomar uma decisão.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: escolher o conteúdo bruto

Peça ao aluno para trazer algo que precisaria virar apresentação. Pode ser um relatório que ele mesmo escreveu, a ata de uma reunião recente, um conjunto de números ou uma análise que fez. Diga:

> "Traz para mim um conteúdo que você precisaria apresentar em algum momento: um relatório que você escreveu, uma ata, uma análise. Qualquer formato, qualquer tamanho."

Enquanto o aluno busca o material, confirme o contexto:

- Para quem vai ser apresentado?
- Quanto tempo de apresentação?
- Qual é a decisão ou ação esperada ao final?

**Verificação:** conteúdo bruto em mãos, contexto de apresentação definido.

---

### Ato 2: estruturar a narrativa

Na sessão de prática, passe o modelo:

> "Aqui está o conteúdo que preciso transformar em apresentação. A apresentação é para [destinatário: minha diretoria / minha equipe / um cliente]. O objetivo é que ao final eles [decisão ou ação esperada]. Tempo disponível: [N minutos]. Organize o conteúdo em três partes: (1) contexto: onde estamos e por que estamos tendo essa conversa; (2) achado: o que descobrimos, aconteceu ou precisamos comunicar; (3) recomendação: o que proponho que façamos. Para cada parte, sugira de dois a quatro slides com título e tópicos principais. Seja conciso: máximo de quatro tópicos por slide."

Após o resultado, revise a estrutura com o aluno:

> "Essa sequência conta a história que você quer contar? Tem alguma parte que está na ordem errada? Falta algum contexto que o público precisaria para entender a recomendação?"

Faça ajustes antes de avançar.

**Verificação:** estrutura de slides aprovada pelo aluno, narrativa com começo, meio e fim claro.

---

### Ato 3: gerar os slides e revisar no painel

Com a estrutura aprovada, gere os slides em formato que o app consegue exibir:

<!-- @codex -->
> "Com base nessa estrutura aprovada, gere os slides como uma página HTML com efeito de apresentação. Cada slide deve ter um título grande, no máximo quatro tópicos e espaço em branco suficiente para respirar. Use um estilo visual simples, sem imagens, com fundo branco e texto escuro."

Quando o resultado aparecer, abra o painel lateral com `Ctrl+B` para ver a apresentação renderizada. Mostre ao aluno como navegar pelos slides no painel. Peça para ele anotar o que quer ajustar.

Para fazer ajustes visuais, use o modo de anotação: clique no elemento que quer mudar, escreva o feedback diretamente na página e envie. Por exemplo: "esse título ficou grande demais" ou "esse slide está com tópicos demais".

Para exportar como arquivo: peça ao agente para salvar o HTML na pasta `missões/`. O arquivo abre no navegador como uma apresentação funcional, sem precisar de software de apresentação instalado.
<!-- @/codex -->

<!-- @claude -->
> "Com base nessa estrutura aprovada, gere os slides como uma página HTML com efeito de apresentação. Cada slide deve ter um título grande, no máximo quatro tópicos e espaço em branco suficiente para respirar. Use um estilo visual simples, sem imagens, com fundo branco e texto escuro."

Quando o resultado aparecer, clique no caminho do arquivo HTML no chat para abrir no painel de preview (`Ctrl+Shift+P`). Mostre ao aluno como navegar pelos slides no painel. Peça para ele anotar o que quer ajustar.

Para fazer ajustes: descreva o que quer mudar diretamente no chat. Por exemplo: "o segundo slide está com tópicos demais, reduz para três" ou "o título da recomendação precisa ser mais direto". O agente edita o arquivo e o painel atualiza.

Para exportar: o arquivo HTML já está na pasta da oficina. Ele abre em qualquer navegador como uma apresentação funcional. Se o aluno precisar de um arquivo PowerPoint, peça ao agente para gerar um HTML que simule o visual do PowerPoint, ou instrua o aluno a usar a opção "Importar do PowerPoint" se disponível no seu app de apresentação.
<!-- @/claude -->

**Verificação:** slides visualizados no painel, aluno fez pelo menos um ajuste e o resultado final está salvo.

---

## Variações por função

| Área | Conteúdo bruto típico | Decisão esperada ao final |
|---|---|---|
| Financeiro | DRE ou fechamento mensal | Aprovação de orçamento ou ação corretiva |
| Comercial | Pipeline ou resultado de negociações | Aprovação de proposta ou revisão de meta |
| Operações | Indicadores de produção ou relatório de parada | Priorização de manutenção ou ajuste de processo |
| Marketing | Resultado de campanha ou análise de concorrente | Aprovação de investimento ou mudança de estratégia |
| Engenharia | Avanço de projeto ou laudo técnico | Aprovação de solução ou orçamento de reparo |
| Holding | Resultado consolidado de subsidiárias | Direcionamento estratégico ou alocação de recursos |

---

## Aprofundamento

Para apresentações que precisam de elementos visuais como gráficos ou diagramas, o módulo 14 cobre a criação de visuais por HTML e SVG, que podem ser incorporados diretamente nos slides. A combinação dos dois módulos permite uma apresentação completa com dados e visuais sem precisar de software de design.

Para gestores que apresentam com frequência o mesmo tipo de conteúdo (fechamento mensal, resultado de vendas), o próximo passo é criar um modelo HTML fixo onde apenas os dados mudam a cada ciclo. Isso transforma o processo de "criar a apresentação" em "atualizar os dados e gerar".

---

## Erros comuns e diagnóstico

**Conteúdo bruto muito extenso e o resultado sai genérico.**
O aluno enviou um relatório de 30 páginas e os slides saíram com tópicos vagos. Fala do tutor: "Conteúdo muito extenso sem foco dilui o resultado. Antes de gerar os slides, peça ao agente para resumir o documento em dez pontos principais. Depois use esse resumo como insumo para a estrutura de slides."

**Narrativa sai com mais de dez slides para uma apresentação de dez minutos.**
Fala do tutor: "Um slide por minuto é uma boa referência. Para dez minutos, dez slides no máximo. Pede para o agente reduzir para esse limite, mantendo apenas o essencial de cada parte da narrativa."

**Aluno quer muitas informações em cada slide.**
Ele não consegue abrir mão de detalhes. Fala do tutor: "O que está nos slides é o que o público vê. O que não está nos slides é o que você fala. Tudo que precisa de explicação longa vai na sua fala, não no slide. Qual é o único ponto que esse slide precisa comunicar?"

**Arquivo HTML não abre corretamente no computador do aluno.**
Fala do tutor: "Tenta abrir no Chrome ou no Edge diretamente. Se mesmo assim não funcionar, me conta qual erro aparece e a gente resolve."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual tipo de conteúdo o aluno trouxe, se ele já tinha o hábito de montar apresentações com estrutura narrativa ou costumava adaptar slides antigos, e como reagiu ao processo de revisar no painel.

**Cérebro:** esta missão pode alimentar:
- `pessoal/como-escrevo.md`: o tom e nível de detalhe aprovados nos slides revelam como o aluno prefere se comunicar em apresentações formais.
- `departamento/processos.md`: se a apresentação for recorrente (fechamento mensal, reunião de equipe), registre a cadência e o destinatário.
