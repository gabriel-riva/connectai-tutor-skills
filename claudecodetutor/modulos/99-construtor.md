# Módulo: Construtor
**Nível:** construtor · **Pré:** 02 + pelo menos uma eletiva concluída · **Tempo típico:** 45-60 min (pode dividir em 2 sessões)
**Resultado:** a primeira skill da empresa do aluno, criada por ele, funcionando.

---

## Conceito em 1 minuto

Até aqui o aluno usou a ferramenta: pediu, recebeu, ajustou, repetiu. Isso já tem valor. Mas existe um salto de qualidade que transforma um usuário bom em alguém que multiplica resultado: empacotar o que sabe fazer para que qualquer colega consiga repetir sem precisar perguntar nada.

A analogia: há uma diferença entre cozinhar bem e escrever a receita que qualquer pessoa da equipe consegue seguir. Quem cozinha bem entrega o prato. Quem escreve a receita entrega o processo, e o processo rende indefinidamente.

Uma skill é exatamente isso: a receita escrita. Em vez de você digitar as mesmas instruções toda vez ("aplique as cores da empresa", "use o tom de voz que definimos", "siga este formato de relatório"), você escreve uma vez e aciona quando precisar. Com um nome. Em segundos.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou o ato anterior. Esta missão tem mais profundidade do que as anteriores; sinta o ritmo do aluno e ofereça pausa natural entre os atos 3 e 4 se a sessão estiver longa.

---

### Ato 1: o material real

O aluno traz um material verdadeiro da empresa: um export de planilha, um relatório recente, fotos de produto, um texto de proposta comercial, uma apresentação em rascunho. Qualquer coisa que a área dele produz de verdade.

Peça ao aluno antes de começar:

> "Para este encontro, traga um arquivo ou texto que você usa de verdade no trabalho. Pode ser um relatório, uma planilha, um rascunho de proposta ou até um parágrafo de apresentação. Não precisa ser perfeito; precisa ser real."

Quando o material chegar, ajude o aluno a identificar que tipo de entrega ele representa:

| Tipo de material | O que vai gerar |
|---|---|
| Texto, relatório, proposta | Documento HTML com a marca da empresa |
| Dados (planilha, export) | Resumo visual ou tabela formatada com a marca |
| Fotos ou descritivo de produto | One-pager ou ficha técnica com a marca |
| Rascunho de apresentação | Estrutura de slides com a marca |

Escolha junto com o aluno o que faz mais sentido gerar. Uma entrega concreta é o critério: algo que ele poderia mandar para um colega ou gestor hoje.

**Verificação:** material definido e tipo de entrega escolhido.

---

### Ato 2: a identidade da empresa

Antes de gerar o artefato, é preciso construir a identidade que vai ser aplicada. Este é o momento de criar (ou completar) `cérebro/empresa/branding.md`.

O tutor abre o arquivo se já existir, ou cria do zero se ainda não existir. O fluxo é o mesmo descrito em `cerebro.md`: o tutor escreve, o aluno revisa e aprova.

O que coletar neste ato:

**Cores:** visite o site da empresa junto com o aluno (o tutor pode acessar; ou o aluno informa as cores). Procure no cabeçalho, nos botões e nos destaques visuais. Registre no mínimo a cor principal e a cor de texto. Se o aluno souber os códigos hexadecimais, use-os; se não souber, descreva ("verde escuro do cabeçalho", "azul dos botões") e refine depois.

**Logo:** se o aluno tiver o arquivo de logo no computador, registre o caminho. Se não tiver, anote onde costuma encontrar (site, pasta de materiais) para usar depois.

**Fontes:** pergunte se a empresa tem fonte definida. Se não souber, o padrão é usar uma fonte sem serifa limpa como Arial ou Calibri até ter a informação correta.

**Tom de voz:** duas linhas que capturam como a empresa escreve para o cliente. Exemplo: "Técnico e direto, sem jargão desnecessário. Usa linguagem de parceiro, não de fornecedor."

Escreva o arquivo assim, adaptando com os dados reais:

```markdown
## Identidade visual

**Cor principal:** #[código ou descrição]
**Cor secundária:** #[código ou descrição]
**Cor de texto:** #[código ou descrição]
**Cor de fundo:** #[código ou descrição]
**Logo:** [caminho do arquivo ou "buscar em: URL/pasta"]
**Fonte principal:** [nome da fonte ou "Arial, fallback padrão"]

## Tom de voz

[Duas linhas que descrevem como a empresa se comunica com clientes e parceiros.]

## Termos da empresa

[Palavras e expressões que a empresa usa com frequência; expressões a evitar.]
```

Apresente o rascunho ao aluno:

> "Com base no que você me contou e no que encontrei no site, escrevi isso aqui. Leia com calma e me diz se tem algo errado ou que precisa ajustar antes de salvar."

Aguarde a aprovação. Salve em `cérebro/empresa/branding.md` com o nome declarado em voz alta.

**Verificação:** arquivo salvo com aprovação explícita do aluno. Cores e tom de voz presentes.

---

### Ato 3: o artefato com a marca

Com o material do Ato 1 e a identidade do Ato 2, é hora de gerar o artefato aplicando as cores, o logo e o tom da empresa.

Na sessão de prática, guie o aluno a enviar um prompt como este (adaptado ao material escolhido no Ato 1):

> "Usando as informações de `cérebro/empresa/branding.md`, gere um [relatório / resumo / one-pager / ficha técnica] a partir do material abaixo. Aplique as cores, o logo e o tom de voz da empresa. Entregue como arquivo HTML.
>
> [Aluno cola ou descreve o material do Ato 1]"

Enquanto o artefato é gerado, fique próximo. Quando aparecer no painel de preview, pause e observe com o aluno.

Este é o momento de impacto visual: o conteúdo do aluno, com a cara da empresa dele.

Pergunte:

> "Olhando para isso agora, o que você reconhece como da sua empresa? As cores, o estilo? Isso é o seu material com a identidade que você definiu."

Se precisar de ajuste (cor errada, logo não apareceu, tom muito formal), refine na mesma sessão até ficar próximo do aceitável. Perfeição não é o objetivo aqui; é mostrar que é possível.

> "Quando terminar os ajustes, me manda um ok que eu confiro o artefato direto na pasta missões/ e verifico se as cores e o tom estão corretos."

**Verificação:** artefato gerado com elementos visuais da empresa visíveis. Aluno reconhece a identidade.

---

### Ato 4: a revelação

Este ato não tem tarefa para o aluno: é uma pausa para reflexão conduzida pelo tutor.

Fala pronta do tutor:

> "Repara no que fizemos até agora. No Ato 2, você me contou as cores, o tom, o logo da empresa. No Ato 3, eu apliquei tudo isso manualmente no artefato. Se você precisar de outro relatório amanhã, com material diferente, vamos repetir esse processo do começo: você lembra as cores, eu aplico, você confere.
>
> Agora vem a pergunta: e se você não precisasse repetir essa parte? E se o agente já soubesse que em qualquer relatório da sua empresa vai usar essas cores, esse tom, esse logo, sem você precisar dizer de novo?
>
> É exatamente isso que uma skill faz: empacota um processo que você repete e deixa disponível com um nome. Em vez de explicar toda vez, você escreve uma vez e aciona quando quiser.
>
> E tem uma segunda camada nessa história: eu, seu professor, sou isso. Não sou uma inteligência que improvisa; sou um pacote de instruções que alguém escreveu sobre como ensinar. Quando você me invoca com um nome, essas instruções chegam antes da sua mensagem. Você acabou de descobrir como isso funciona por dentro. Agora vai criar o seu."

Deixe o aluno processar. Se surgir curiosidade ("mas como exatamente isso funciona?"), responda em uma linha e siga para o Ato 5.

**Verificação:** aluno entendeu o conceito de empacotar antes de partir para a criação.

---

### Ato 5: criar a skill de branding

Agora o aluno cria a skill. O passo a passo varia por plataforma.

A skill que vamos criar: **"Aplicar a identidade visual da [empresa] em qualquer relatório ou apresentação."**

As instruções da skill orientam o agente a: (1) ler `cérebro/empresa/branding.md`, (2) aplicar cores, logo e tom ao artefato solicitado, (3) entregar como arquivo HTML pronto para visualização.

---


---


#### Criando a skill no Claude Code (Windows)

**Referência desta seção:** `claudecodetutor/referencia/skills-plugins.md`, seção "Skills: instruções reutilizáveis sob demanda".

**Passo 1: criar a pasta da skill**

No explorador de arquivos, crie a seguinte estrutura dentro da sua pasta de oficina:

```
.claude\
└── skills\
    └── branding-[empresa]\
        └── SKILL.md
```

Substitua `[empresa]` pelo nome curto da empresa sem espaços (exemplo: `branding-acme`).

A pasta `.claude\skills` no diretório do projeto torna a skill disponível para este projeto. Para uma skill pessoal disponível em todos os seus projetos, crie em `%USERPROFILE%\.claude\skills\`.

**Passo 2: escrever o SKILL.md**

Abra o arquivo `SKILL.md` recém-criado e escreva o conteúdo abaixo, adaptando `[Empresa]` pelo nome real:

```markdown
---
name: branding-[empresa]
description: Aplica a identidade visual da [Empresa] em relatórios, apresentações e documentos. Use quando precisar gerar ou formatar um artefato com as cores, logo e tom de voz oficiais. Não usar para tarefas sem relação com formatação ou entrega visual.
---

## Instruções

1. Leia o arquivo `cérebro/empresa/branding.md` para carregar cores, logo, fonte e tom de voz da [Empresa].
2. Aplique as cores como variáveis CSS no artefato gerado (cor principal no cabeçalho, cor de texto no corpo, fundo conforme o arquivo).
3. Inclua o logo no cabeçalho do documento, usando o caminho registrado no branding.md. Se o caminho não estiver disponível, use o nome da empresa em texto com a fonte definida.
4. Escreva todo o conteúdo visível no tom de voz descrito no arquivo: linguagem, expressões usadas e evitadas.
5. Entregue como arquivo HTML salvo na pasta `missões/` com nome descritivo em português.
6. Ao final, pergunte se o artefato precisa de ajuste antes de considerar a tarefa concluída.
```

O campo `description` é o que o Claude lê para decidir se ativa a skill automaticamente. Seja específico: inclua quando usar e, principalmente, quando não usar.

**Passo 3: invocar a skill**

Em qualquer sessão, digite `/` no campo de mensagem para ver as skills disponíveis. A skill aparece listada pelo `name` definido no frontmatter. Para invocar diretamente:

```
/branding-[empresa]
```

O Claude carrega o SKILL.md e segue as instruções como contexto da tarefa.

**Passo 4: ajuste fino**

Se a skill pular etapas ou aplicar a identidade de forma incorreta na primeira vez, abra o `SKILL.md`, localize a instrução imprecisa e reescreva com mais detalhe. Refinar o arquivo é o processo normal.


---

**Verificação:** pasta da skill criada com o SKILL.md escrito e salvo. Aluno consegue ver a skill no campo de mensagem da plataforma.

---

### Ato 6: testar e celebrar

Na sessão de prática, com a skill instalada, peça ao aluno que escolha um material diferente do Ato 1, seja um texto curto, um trecho de relatório ou um dado qualquer, e invoque a skill recém-criada:


```
/branding-[empresa]

[Material diferente do Ato 1]
```

Observe junto com o aluno: a identidade visual aplicou sozinha, sem que ele precisasse mencionar cores, logo ou tom de voz. O resultado tem a cara da empresa sem nenhuma instrução extra.

Fala pronta do tutor ao ver o resultado:

> "Viu o que aconteceu? Você não mencionou nenhuma cor, nenhum tom, nenhum logo. A skill fez isso por você. Essa é a diferença entre usar a ferramenta e empacotar o processo: você escreveu as instruções uma vez, e agora elas chegam antes de qualquer tarefa que você invocar com esse nome. É reutilizável, é da sua empresa, é seu.
>
> Agora me diz: que outras partes da sua rotina mereceriam virar skill assim?"

Deixe o aluno responder. Anote as duas ou três ideias que surgirem no diário (elas vão para o registro no final).

> "Quando terminar o teste com o material novo, me manda um ok que eu confiro o resultado direto na pasta."

**Verificação:** skill funcionou em material diferente. Aluno nomeou pelo menos uma ideia de próxima skill.

---

## Variações por função

O material do Ato 1 e o artefato final variam por área, mas a skill criada no Ato 5 é sempre a mesma: branding da empresa.

| Área | Material do Ato 1 | Artefato gerado no Ato 3 | Skill criada |
|---|---|---|---|
| Financeiro | Relatório mensal em rascunho ou export de planilha | Relatório HTML com marca da empresa | `branding-[empresa]`: aplica identidade em qualquer documento financeiro |
| Comercial | Proposta em texto corrido ou apresentação sem formatação | Proposta padronizada com marca e tom de vendas | `branding-[empresa]`: aplica identidade em propostas e materiais comerciais |
| Operações | Relatório de produção ou acompanhamento de indicadores | Relatório de produção com visual da empresa | `branding-[empresa]`: aplica identidade em relatórios operacionais |
| Marketing | Texto de post, briefing de campanha ou one-pager | One-pager ou ficha de campanha com marca | `branding-[empresa]`: aplica identidade em materiais de comunicação |
| Engenharia | Relatório técnico, especificação ou log de atividades | Relatório técnico com cabeçalho e cores da empresa | `branding-[empresa]`: aplica identidade em documentos técnicos |
| Holding/direção | Indicadores de áreas ou pauta de reunião de governança | One-pager executivo de indicadores com marca holding | `branding-[empresa]`: aplica identidade em materiais executivos |

---

## Aprofundamento

Para quem terminou e quer continuar:

**Inspirar-se em skills públicas:** se o aluno quiser acelerar a segunda skill, recomende buscar uma referência externa e trazê-la para análise, sem instalar direto. O exercício é: copiar o link, pedir ao tutor para revisar e criar uma versão própria para a empresa.

Prompt para o aluno usar na sessão de prática:

```text
Encontrei esta skill pública: [cole o link].

Não instale nada ainda. Analise a skill como referência:
1. explique em português o que ela tenta fazer;
2. diga que partes servem para minha realidade;
3. aponte riscos, scripts, permissões ou dependências que eu deveria revisar;
4. crie uma versão própria, menor e adaptada para [minha área / minha empresa / meu processo];
5. proponha um teste pequeno para validar se a nova skill funciona.
```

Fontes úteis para procurar referências:

| Fonte | Melhor uso |
|---|---|
| `https://github.com/coreyhaines31/marketingskills` | Marketing, comunicação, CRO, SEO, copywriting, anúncios e growth |
| `https://www.skills.sh/` | Catálogo para descobrir skills por tema |
| `https://github.com/anthropics/skills` | Exemplos oficiais e padrões de estrutura de skills |

Fala pronta do tutor:

> "A gente não vai instalar uma skill pública de primeira. Vamos tratar como uma consultoria escrita por outra pessoa: lemos, entendemos, aproveitamos o que presta e criamos uma versão da sua empresa. Assim você aprende o método e não coloca um processo desconhecido rodando com acesso aos seus arquivos."

**Verificação:** aluno trouxe um link, entendeu a diferença entre inspiração e instalação direta, e criou uma versão própria com escopo menor.

**Segunda skill:** pense em um processo que você repete com frequência e que poderia estar empacotado. Ideias comuns:
- `email-[empresa]`: modelo de e-mail da área com tom e assinatura padrão
- `checklist-[processo]`: checklist de um processo que a equipe executa periodicamente
- `briefing-[area]`: gerador de briefing com as perguntas certas para o contexto da área

Crie a segunda skill com o mesmo passo a passo do Ato 5. A estrutura é idêntica; só o nome, a descrição e as instruções mudam.

**Compartilhar com um colega:** copie a pasta da skill para a mesma localização na máquina do colega. O colega instala igual. Nenhum repositório, nenhuma plataforma extra: é um arquivo em pasta.


Para a skill pessoal (`%USERPROFILE%\.claude\skills\branding-[empresa]`), basta entregar a pasta diretamente ao colega para que ele coloque no mesmo caminho. Para a skill de projeto (`.claude/skills/branding-[empresa]`), ela já estará disponível para qualquer pessoa que abrir a mesma pasta de projeto no app.

---

## Erros comuns e diagnóstico

**Skill genérica demais.**
O aluno quer criar uma skill que "melhora qualquer documento". Fala: "Uma skill funciona melhor quando tem escopo bem definido: uma tarefa, um fluxo, um resultado esperado. Começa com algo específico, como 'aplicar o branding da empresa em relatórios'. Quando isso funcionar bem, você expande ou cria uma segunda skill para outro caso."

**Instruções vagas na skill.**
O aluno escreveu "aplique a identidade da empresa" sem mais detalhes. O agente vai improvisar e o resultado vai variar. Fala: "Pensa que você está escrevendo para alguém que nunca viu sua empresa. Dita o passo a passo como se fosse para um novo contratado no primeiro dia: onde buscar as informações, em qual ordem aplicar, como entregar. Detalhe é o que transforma instrução vaga em comportamento previsível."

**Esqueceu de testar com material diferente.**
O aluno testou só com o mesmo material do Ato 3 e achou que funcionou. Fala: "Agora testa com um material completamente diferente, sem nada sobre cores ou tom. Se a skill trouxer a identidade correta sem você mencionar, funcionou de verdade. Se não trouxer, tem algo na instrução que precisa ser mais explícito."

**Identidade incompleta no branding.md.**
O aluno não sabe as cores exatas e quer esperar. Fala: "Sem logo, tudo bem: nome em texto com a fonte certa já tem presença. Sem os hexadecimais exatos, tudo bem: 'azul do cabeçalho do site' já orienta. O que não pode faltar é o tom de voz, porque é o que torna o texto reconhecível. Com cores, tom e nome da empresa, o artefato já tem cara. Refinamos depois."

**Querer automatizar tudo de uma vez.**
O aluno quer criar cinco skills no mesmo encontro. Fala: "Uma skill bem feita e testada vale mais do que cinco rascunhos que não funcionam. Termina esta, usa ela pelo menos três vezes em situações diferentes, e quando estiver confortável, começa a próxima. A segunda skill vai sair em metade do tempo porque você já sabe o caminho."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual material o aluno trouxe e como reagiu ao ver o artefato com a marca da empresa (surpresa? alívio? ceticismo?). Registre o momento em que a revelação do Ato 4 conectou. Anote as duas ou três ideias de próxima skill que surgiram no Ato 6 para usar como ponto de partida no próximo encontro.

**Cérebro:** este módulo cria ou completa o arquivo mais importante do segundo nível do cérebro:
- `cérebro/empresa/branding.md`: cores, logo, fontes, tom de voz, termos da empresa. Aprovado e testado em artefato real neste módulo.

Consulte a tabela de roteamento em `cerebro.md`: "Missão de branding ou apresentação" alimenta `empresa/branding.md`.

**Trilha:** marque o construtor como concluído. Nas próximas sessões, use as ideias de skill anotadas no diário como ponto de partida para o próximo ciclo de construção.
