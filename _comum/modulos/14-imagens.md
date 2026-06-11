# Módulo: Imagens
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 20-30 min
**Resultado:** o aluno sabe analisar imagens (fotos, prints, gráficos, documentos escaneados) e criar visuais úteis para a área, sabendo exatamente o que é possível em cada plataforma sem precisar de software de design.

---

## Conceito em 1 minuto

Imagem é dado. Uma foto de uma peça com defeito carrega informação que palavras não transmitem com a mesma precisão. Um gráfico que você viu numa reunião mas não tem o arquivo original ainda pode ser analisado. Um logo de fornecedor, um print de tela, um documento escaneado: tudo é insumo que o agente consegue ler e trabalhar.

A diferença importante entre as plataformas é que uma gera imagens a pedido e a outra cria visuais por código. Nenhuma é melhor ou pior em absoluto: cada uma serve um propósito diferente, e o módulo mostra os dois caminhos.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: analisar uma imagem real

Peça ao aluno para escolher uma imagem do trabalho. Pode ser um print de relatório, uma foto de produto, um gráfico de reunião, um documento escaneado. Qualquer coisa que tenha chegado em formato de imagem e contenha informação útil. Diga:

> "Traz uma imagem do seu trabalho, qualquer imagem. Um print de sistema, uma foto de produto, um gráfico que apareceu numa reunião. Qualquer coisa que você teria que descrever em palavras para outra pessoa, mas que ficaria mais fácil mostrar."

Na sessão de prática, peça ao aluno para enviar a imagem diretamente no chat:

<!-- @codex -->
> "Arraste a imagem para o chat ou cole com `Ctrl+V`. Depois envie o prompt: 'Descreva o que está nesta imagem. Identifique todos os dados, números ou informações estruturadas que aparecem. Se houver gráficos, tabelas ou textos, transcreva o conteúdo de forma organizada.'"
<!-- @/codex -->

<!-- @claude -->
> "Arraste a imagem para o chat ou cole com `Ctrl+V`. Depois envie o prompt: 'Descreva o que está nesta imagem. Identifique todos os dados, números ou informações estruturadas que aparecem. Se houver gráficos, tabelas ou textos, transcreva o conteúdo de forma organizada.'"
<!-- @/claude -->

Após o resultado, pergunte ao aluno:

> "O que o agente identificou na imagem? Tem algo que ele percebeu que você não teria notado de imediato? Tem algum dado que ele errou ou que ficou impreciso?"

**Verificação:** análise de imagem concluída, aluno consegue avaliar a qualidade do resultado.

---

### Ato 2: criar um visual útil para a área

Agora a criação. O caminho é diferente dependendo da plataforma:

<!-- @codex -->
O Codex pode gerar imagens diretamente usando o modelo `gpt-image-2`. Você pode pedir uma imagem descrevendo o que quer, ou usar `$imagegen` explicitamente no prompt. O uso conta no limite geral de tokens.

Passe o modelo:

> "Crie uma imagem de [descrição do que o aluno precisa para a área dele]. [Detalhes de estilo: fundo branco, estilo minimalista, cores da empresa se souber]. Use `$imagegen`."

Exemplos calibrados por área estão na seção de variações. Após o resultado aparecer no painel lateral, mostre ao aluno como salvar: clique com o botão direito na imagem ou peça ao agente para salvar o arquivo na pasta `missões/`.

Se o resultado não ficou bom na primeira tentativa, reescreva a descrição com mais detalhes: dimensões aproximadas, o que deve estar em destaque, o que deve aparecer em segundo plano.
<!-- @/codex -->

<!-- @claude -->
O Claude Code não gera imagens diretamente. Mas consegue criar visuais muito úteis por código: gráficos HTML/JavaScript, diagramas SVG, tabelas estilizadas, infográficos, organogramas. O resultado é um arquivo que abre no navegador com qualidade profissional.

Para criar um visual por código:

> "Crie um gráfico de barras em HTML e JavaScript com os seguintes dados: [dados do aluno]. Use cores simples, fundo branco, rótulos claros em português. Salva como `visual.html` na pasta missões/."

Após o arquivo ser salvo, clique no caminho do arquivo no chat para abrir no painel de preview. Se o aluno preferir outro tipo de visual (pizza, linha, infográfico, diagrama), adapte o prompt.

Se o aluno precisar de uma imagem em formato de arquivo (PNG, JPG), o caminho mais simples é abrir o HTML no navegador e tirar um print. O agente pode também gerar código SVG que é exportável como imagem em qualquer editor vetorial.
<!-- @/claude -->

**Verificação:** visual criado, salvo e visualizado pelo aluno.

---

### Ato 3: usar o visual em contexto

Para fechar o módulo, peça ao aluno para conectar o visual com uma necessidade real:

> "Onde você usaria esse visual? Numa apresentação? Num relatório? Num e-mail para a equipe?"

Se for para uma apresentação, mostre como incluir o HTML ou imagem nos slides criados no módulo 13. Se for para um relatório, peça ao agente para embutir o visual diretamente no relatório. Se for para um e-mail, basta salvar como imagem e anexar.

> "Quando terminar de conectar o visual ao destino final, me manda um ok que eu confiro."

**Verificação:** aluno sabe onde e como usar o visual criado.

---

## Variações por função

| Área | Análise de imagem útil | Visual para criar |
|---|---|---|
| Financeiro | Analisar gráfico de resultado de reunião | Gráfico de barras com evolução de faturamento |
| Comercial | Analisar print de proposta de concorrente | Gráfico de funil de vendas ou tabela comparativa |
| Operações | Analisar foto de peça com defeito ou painel de equipamento | Diagrama de fluxo de processo ou gráfico de OEE |
| Marketing | Analisar arte de campanha de concorrente | Infográfico de resultado de campanha |
| Engenharia | Analisar esquema técnico ou laudo escaneado | Diagrama de planta simplificado ou gráfico de SLA |
| Holding | Analisar gráfico de resultado de subsidiária | Painel comparativo de indicadores por unidade |

---

## Aprofundamento

Para quem quiser criar visuais mais elaborados: SVG permite criar diagramas, ícones e ilustrações vetoriais escaláveis que ficam nítidos em qualquer tamanho. O agente escreve SVG da mesma forma que escreve código, e o resultado abre em qualquer navegador sem dependência de software.

Para análise de imagens de documentos escaneados (notas fiscais, laudos, formulários físicos), a qualidade da análise depende da qualidade do escaneamento. Imagens com resolução mínima de 150 DPI costumam dar bons resultados. Imagens muito escuras, inclinadas ou com texto manuscrito podem exigir ajuste de expectativa.

---

## Erros comuns e diagnóstico

**Análise de imagem imprecisa em dados numéricos.**
O agente transcreveu um número errado de um gráfico. Fala do tutor: "Para dados numéricos críticos, sempre confirme no arquivo original ou na fonte. A leitura de imagem é muito boa para entender o que está representado, mas pode ter pequenas imprecisões em números específicos, especialmente em gráficos de baixa resolução."

<!-- @codex -->
**Imagem gerada não correspondeu à descrição.**
O resultado ficou diferente do esperado. Fala do tutor: "Descrição de imagem funciona melhor com detalhes específicos: o que está em primeiro plano, o que está em segundo, o estilo (fotorrealista, minimalista, diagrama), as cores. Vamos refazer o prompt com mais detalhes sobre o que você esperava."
<!-- @/codex -->

<!-- @claude -->
**Aluno esperava uma imagem mas recebeu código HTML.**
Fala do tutor: "O Claude não gera imagens diretamente, mas o código HTML que ele gerou produz exatamente o visual que você pediu. Clica no link do arquivo no chat para ver no painel. O resultado é o mesmo, o caminho é diferente."
<!-- @/claude -->

**Visual criado ficou muito simples ou muito complexo.**
Fala do tutor: "Me descreve o que você esperava ver que não apareceu, ou o que apareceu que você não queria. Com isso eu ajusto o prompt para refinar o visual."

**Aluno não tem imagem disponível neste momento.**
Fala do tutor: "Sem problema. Pode ser um print de qualquer tela que você usa no trabalho: um gráfico do sistema, uma tabela de relatório, uma foto de produto. Qualquer coisa que tenha chegado como imagem. Se não tiver nada agora, fazemos só a criação do visual e a análise de imagem fica como dever de casa para a próxima sessão."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual tipo de imagem o aluno trouxe para análise, qual visual foi criado e para qual uso, se a plataforma (geração direta versus código) gerou alguma resistência ou surpresa.

**Cérebro:** esta missão pode alimentar:
- `departamento/processos.md`: se o visual criado representa um processo do departamento (fluxograma, organograma).
- `empresa/branding.md`: se na criação do visual o aluno mencionou cores ou padrões visuais da empresa.
