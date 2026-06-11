# Módulo: Conhecendo a ferramenta
**Nível:** núcleo · **Pré:** nenhum · **Tempo típico:** 25-35 min
**Resultado:** o aluno navega pela interface com autonomia, sabe separar a janela do tutor da sessão de prática, executa uma aprovação consciente e conhece os controles de quem manda no agente.

---

## Conceito em 1 minuto

Imagine uma bancada de trabalho com um assistente dentro. A bancada fica aberta entre os dias: o que você deixa em cima ontem está lá amanhã. Esse assistente não é um chat descartável que começa do zero a cada conversa; ele opera em espaços de trabalho permanentes, um por assunto. Trocar de assunto não significa jogar fora o que foi construído; significa abrir outra gaveta da mesma bancada.

Cada espaço de trabalho tem o seu próprio histórico e os seus próprios arquivos. Você pode ter vários abertos ao mesmo tempo, visíveis lado a lado, sem que um interfira no outro.

---

## Missão guiada

> A lógica deste módulo: o aluno JÁ usa chat de IA (quase todos usam). Então nada aqui ensina o que o chat já faz. A missão é uma ESCALADA DE DEMONSTRAÇÕES do que só um agente faz: trabalho completo num pedido, arquivos da máquina, pesquisa autônoma. A interface (aprovações, painel, voz, steering) se aprende POR DENTRO das demonstrações, um toque cada, nunca como assunto. Conduza um ato de cada vez e mantenha o ritmo: a primeira demonstração de impacto precisa acontecer nos primeiros 10 minutos.

### Ato 1: reconhecimento da casa

VOCÊ apresenta a casa; o aluno só acompanha com os olhos. NUNCA peça que o aluno descreva a tela (é você quem conhece a interface; quiz de tela é constrangedor e inútil). Diga:

> "Deixa eu te apresentar a casa em 30 segundos, olhando pra tela junto comigo."

E descreva as zonas com os nomes corretos:

<!-- @codex -->
A tela tem três zonas principais:
- **Barra lateral esquerda:** lista de threads (espaços de trabalho) organizadas por projeto. No topo há o nome do projeto aberto e o botão para adicionar projetos (Add new project).
- **Área central (chat):** onde as mensagens trocadas ficam e onde o compositor de texto fica na parte inferior.
- **Painel lateral direito (preview):** aparece ao criar ou abrir um artefato (arquivo HTML, planilha, PDF). Abra e feche com `Ctrl+B`.

Mostre ao aluno como abrir e fechar o painel lateral (`Ctrl+B`), que é onde os resultados aparecem (documentos, planilhas, apresentações). Existe também uma área técnica (o terminal) que o agente usa por conta própria: mencione em UMA frase que ela existe e que o aluno não vai precisar dela. Nunca proponha que o aluno a use.
<!-- @/codex -->

<!-- @claude -->
A tela tem três zonas principais:
- **Barra lateral esquerda:** lista de sessões abertas, agrupáveis por projeto, com filtros de status no topo.
- **Área central (chat):** histórico de mensagens e compositor de texto na parte inferior.
- **Painéis arrastáveis:** o espaço à direita do chat pode abrir painéis de visualização: o de alterações (o "controle de alterações" do Word, aplicado a qualquer arquivo; nome técnico: diff) e o de preview (a prévia do resultado: documentos, planilhas, páginas). Arraste o cabeçalho de qualquer painel para reposicioná-lo; arraste a borda para redimensionar.

Mostre ao aluno como abrir o painel de preview (`Ctrl+Shift+P`) e o de alterações (`Ctrl+Shift+D`). Peça que abra e feche cada um. Existe também uma área técnica (o terminal) que o agente usa por conta própria: mencione em UMA frase que ela existe e que o aluno não vai precisar dela. Nunca proponha que o aluno a use.
<!-- @/claude -->

**Verificação:** o aluno abriu e fechou os painéis (pergunte no máximo "achou os dois?"; nunca peça que ele nomeie ou descreva nada de volta).

---

### Ato 2: a sessão de prática

Explique que o trabalho vai acontecer em dois espaços abertos lado a lado: o do tutor (onde a conversa atual acontece) e a sessão de prática (onde o aluno experimenta sem medo de estragar nada).

Instrução ao aluno:

<!-- @codex -->
PRIMEIRO, tente VOCÊ criar a thread de prática (gestão de threads): crie silenciosamente uma thread chamada "Prática: Módulo 1" neste projeto e fixe-a. Se conseguir, o aluno não precisa criar nada; diga:

> "Já criei e fixei a sua thread de prática, olha ela na barra lateral: 'Prática: Módulo 1'. Agora abre uma segunda janela do app: aperta `Ctrl+Shift+N` (abre uma janela NOVA do Codex, esta conversa continua intacta aqui). Na janela nova, clica na 'Prática: Módulo 1' na barra lateral. Aí coloca as duas janelas lado a lado: `Win+←` numa, `Win+→` na outra."

Se NÃO conseguir criar (recurso indisponível na versão), a segunda janela continua resolvendo:

> "Vamos montar a sua bancada. Aperta `Ctrl+Shift+N`: abre uma segunda janela do Codex, e esta conversa continua intacta aqui. Na janela NOVA, aperta `Ctrl+N` pra criar a thread de prática e nomeia ela de 'Prática: Módulo 1'. Aí coloca as duas janelas lado a lado: `Win+←` numa, `Win+→` na outra."

NUNCA mande o aluno apertar `Ctrl+N` na janela do tutor: o atalho cria a thread nova POR CIMA desta conversa e o aluno sente que foi expulso da aula. Thread nova, só na segunda janela.

Depois, VERIFIQUE VOCÊ MESMO: tente localizar e ler a thread de prática pelo seu canal de supervisão. Se conseguir, confirme proativamente ("pronto, estou enxergando sua thread de prática daqui"). Só se não conseguir, pergunte apenas: "as duas janelas estão lado a lado, com a mesma pasta nas duas?". A partir de agora, tudo que o aluno testar vai para a thread de prática, não para a thread do tutor.
<!-- @/codex -->

<!-- @claude -->
Guie o aluno COM O AVISO DO EFEITO antes do atalho:

> "Vamos criar a sua sessão de prática. Atenção: o atalho `Ctrl+N` cria a sessão nova e TROCA o foco pra ela; isso é esperado, esta conversa continua na barra lateral. Faz assim: (1) aperta `Ctrl+N` e seleciona a MESMA pasta da oficina; (2) nomeia a sessão de 'Prática: Módulo 1'; (3) volta pra esta conversa clicando nela na barra lateral; (4) agora segura `Ctrl` e clica na sessão de prática na barra lateral: as duas abrem lado a lado (`Ctrl+Tab` alterna entre os painéis)."

Depois, VERIFIQUE VOCÊ MESMO pelo transcript local (seu canal de supervisão): localize a sessão nova e confirme proativamente ("pronto, estou acompanhando sua sessão de prática daqui"). Só se a leitura falhar, pergunte apenas: "as duas estão lado a lado, com a mesma pasta nas duas?". A partir de agora, tudo que o aluno testar vai para a sessão de prática, não para a sessão do tutor.
<!-- @/claude -->

REGRA DE RITMO deste ato: o setup da bancada e a primeira demonstração saem na MESMA mensagem sua. Nunca gaste um turno só com setup e outro só com missão: a instrução de destacar/abrir a janela já termina com "e cola isso lá:" seguido do prompt da Demonstração 1 (Ato 3). É também NESSA mensagem que a transparência da supervisão entra, como declaração com saída fácil ("eu acompanho tua janela de prática daqui pra te dar feedback do que você realmente fez; tudo fica na tua máquina; se preferir que eu não acompanhe, só dizer"), nunca como pergunta separada.

**Verificação:** os dois espaços estão abertos lado a lado E a primeira missão já está rodando na prática.

---

### Ato 3 · Demonstração 1: trabalho completo num pedido

O primeiro "isso o meu chat não faz". UM pedido, UM resultado completo e bonito. O tema vem da área do aluno (tabela de variações abaixo); o conteúdo pode ser fictício, desde que RICO e verossímil (fictício de brinquedo, tipo "3 linhas sobre", é proibido). Anuncie o ganho, não a função:

> "Primeira demonstração: você vai pedir UMA vez e receber um documento pronto, com cara de entrega. Cola na janela de prática: 'Monte um relatório de acompanhamento de [tema da área do aluno], com 5 indicadores numa tabela, análise curta de cada um e 3 recomendações no final. Capriche no visual e salve como página (HTML) na pasta missões/ para eu abrir no painel.'"

Enquanto roda (1-3 minutos), prepare o aluno para os dois toques de interface que vão acontecer naturalmente:

- Se aparecer pedido de aprovação: "esse aviso é proteção: o app pede permissão antes de tocar nos seus arquivos e mostra o que vai fazer; você decide". Um toque, segue.
- Quando terminar: "clica no nome do arquivo que apareceu; ele abre no painel de visualização do lado". O aluno vê um relatório formatado, com tabela e recomendações, nascido de uma frase.

Verifique o resultado você mesmo pelo canal de supervisão e comente algo específico do conteúdo. Feche o ato com a comparação explícita:

> "Repara no que acabou de acontecer: você não recebeu um texto pra copiar e colar. Recebeu um ARQUIVO pronto, salvo na sua pasta, formatado. É essa a diferença entre conversar com IA e ter um agente trabalhando."

**Verificação:** existe um documento completo em `missões/`, o aluno abriu no painel e reagiu.

---

### Ato 4 · Demonstração 2: os SEUS arquivos

Agora o agente entra no mundo real do aluno. Prefira material verdadeiro (é o que mais converte), sem drama se não houver:

> "Agora com uma coisa SUA: me traz uma planilha, um PDF ou um relatório do teu trabalho. Copia (não move) pra pasta da oficina, ou arrasta pra janela de prática. Pode ser bagunçado; quanto mais real, melhor."

Missão na prática, em duas batidas:

> "Leia o arquivo [nome] e me diga o que entendeu em 3 frases, mais três observações que alguém de [área] acharia úteis."

E, com a leitura aprovada pelo aluno, a transformação em algo que ele USARIA (escolha pelo arquivo e pela área, tabela abaixo):

> "A partir desse arquivo, crie [entregável da área] e salve em missões/. É pra eu usar de verdade."

Se o aluno não tiver nenhum arquivo à mão, use a voz como ponte: "segura o ditado e me conta por 1 minuto um processo teu, do teu jeito" e a missão vira transformar o despejo falado em documento estruturado. O que este ato persegue: "ele entendeu o MEU mundo".

**Verificação:** material do aluno (arquivo ou fala) virou um entregável que ele admitiu que usaria, com ou sem ajustes.

---

### Ato 5 · Demonstração 3: pesquisa que trabalha sozinha (e você no comando)

A última demonstração junta autonomia e controle. Anuncie o ganho:

> "Última demonstração de hoje: ele vai trabalhar uns minutos SOZINHO pra você, pesquisando na internet com fontes. Cola na prática: 'Pesquise [tema quente da área do aluno: fornecedores de X, normas de Y, tendências de Z no Brasil] e monte um comparativo em tabela com fontes linkadas no final.'"

IMPORTANTE: anuncie só a missão e espere o aluno ENVIAR. Os controles abaixo se ensinam DEPOIS do envio, enquanto a pesquisa roda (é o que dá motivo real a eles); explicar antes do envio duplica a explicação e quebra o ritmo. Com a pesquisa rodando, ensine um controle de cada vez:

- **Steering (corrigir em voo):** "manda agora, no meio do trabalho: 'foca só em empresas brasileiras' ou 'põe em tabela'. Ele ajusta sem recomeçar."
- **Queuing (enfileirar):** "agora manda: 'quando terminar, resume em 5 linhas pra eu mandar no grupo'. Ele guarda e executa quando acabar."
- **Voz:** <!-- @codex -->"o próximo pedido, dita em vez de digitar: segura `Ctrl+M` e fala do teu jeito; o texto aparece no campo pra você revisar antes de enviar."<!-- @/codex --><!-- @claude -->"se o botão de microfone aparecer no campo de mensagem, dita o próximo pedido em vez de digitar: fala do teu jeito e revisa o texto antes de enviar."<!-- @/claude -->
- E a observação que muda a relação com a ferramenta: "repara que você não precisou ficar olhando. Ele trabalha; você volta quando quiser. Semana que vem te mostro isso rodando sozinho em horário marcado, e até do celular."

**Verificação:** o comparativo chegou com fontes, o aluno usou steering ao menos uma vez e percebeu que não precisa supervisionar cada segundo.

---

### Fechamento do módulo

Sem quiz. VOCÊ resume os três "isso o chat não faz" que o aluno viveu (arquivo pronto e salvo; o material DELE lido e transformado; trabalho autônomo com fontes), em três frases. Depois, organização em um toque:

<!-- @codex -->
"Última coisa: vamos fixar a tua thread de prática pra ela ficar sempre à mão. Três pontos nela na barra lateral, opção Pin. Pronto: ela sobe pro topo."
<!-- @/codex --><!-- @claude -->
"Última coisa: renomeia a sessão de prática com um nome claro (o comando `/rename` no campo de mensagem resolve) pra ela ficar fácil de achar na barra lateral."
<!-- @/claude -->

E a ponte: "isso foi a primeira prova do que ele faz. Sua trilha tem [eletivas do aluno] na frente; e quando chegar no módulo Construtor, você vai empacotar um processo SEU pra rodar sempre. Bora pro próximo passo ou quer repetir alguma dessas com outro material teu?"

**Verificação:** trilha atualizada com o módulo concluído e o aluno escolheu o próximo passo.

---

## Variações por função

Use a área do aluno para calibrar as três demonstrações:

| Área | Demonstração 1: tema do relatório | Demonstração 2: arquivo real típico → entregável | Demonstração 3: pesquisa |
|---|---|---|---|
| Financeiro | Acompanhamento de fechamento mensal (receita, custos, inadimplência, margem, caixa) | Export do sistema ou planilha de contas → resumo do mês com pontos de atenção | Indicadores de referência do setor, linhas de crédito, taxas atuais |
| Comercial | Funil de vendas (leads, propostas, conversão, ticket, ciclo) | Lista de clientes/propostas → tabela de follow-ups com prioridade + rascunho do e-mail mais urgente | Concorrentes e preços praticados no segmento |
| Operações | Acompanhamento de produção (volume, refugo, paradas, prazo, produtividade) | Planilha de produção/apontamentos → quadro de pendências com responsável e prazo | Fornecedores de um insumo crítico, comparados |
| Marketing | Desempenho de campanhas (alcance, cliques, leads, custo, conversão) | Planilha de campanha/conteúdo → calendário organizado ou variações no tom da marca | Tendências e benchmarks do setor no Brasil |
| Engenharia | Indicadores técnicos (medições, conformidade, manutenção, retrabalho) | Dados de medição/relatório técnico → tabela limpa e comparada ou resumo de uma página | Normas aplicáveis ou fornecedores técnicos, comparados |
| Holding/direção | Painel executivo multiempresa (receita, margem, caixa, pendências por empresa) | Relatórios de empresas diferentes → consolidado com os 5 pontos que pedem decisão | Editais de fomento ou referências de mercado para o grupo |

---

## Aprofundamento

Para quem quiser ir além: o app opera em modos de execução diferentes, que definem onde o trabalho acontece.

<!-- @codex -->
Há três modos: **Local** (trabalha diretamente na sua pasta), **Worktree** (cria uma cópia isolada para testar sem afetar o original) e **Cloud** (executa em ambiente remoto). O modo é escolhido antes de enviar o primeiro prompt de cada thread. Para a maioria das missões desta trilha, o modo Local é o certo.

Um recurso valioso para aceitar mudanças com consciência: o botão **Revisar** (o "controle de alterações" do Word, aplicado a qualquer arquivo; o nome técnico disso é diff, mas apresente sempre pela analogia primeiro). Ele mostra exatamente o que o agente alterou: verde com `+` é o que entrou, vermelho com `-` é o que saiu. Também abre pelo painel com `Ctrl+Alt+B`, e dá para comentar numa linha específica: clique sobre ela, escreva o feedback e envie. Ensine a diferença em uma frase: "Abrir o arquivo mostra o resultado final, como abrir uma planilha pronta; Revisar mostra o que MUDOU, pra você não aceitar sem perceber que algo importante saiu."
<!-- @/codex -->

<!-- @claude -->
Há três ambientes: **Local** (trabalha diretamente nos seus arquivos), **Remote** (executa em nuvem da Anthropic) e **SSH** (servidor remoto). O ambiente é escolhido antes de enviar a primeira mensagem de cada sessão. Para a maioria das missões desta trilha, o Local é o certo.

Um recurso valioso no modo Local: **checkpointing**. O app salva o estado dos arquivos antes de cada edição. Para voltar atrás, pressione `Esc` duas vezes com o campo de mensagem vazio, ou escreva `/rewind` no compositor. Um menu aparece listando cada mensagem enviada; escolha o ponto desejado e decida se quer restaurar só o código, só a conversa ou os dois. Isso elimina o medo de "estragar algo": dá para desfazer com precisão cirúrgica.
<!-- @/claude -->

---

## Erros comuns e diagnóstico

**Medo de clicar em "aprovar".**
Fala: "Posso só olhar o que ele quer fazer antes de aprovar?" Resposta: "Claro, esse é exatamente o ponto. Leia o que está sendo pedido, confirme que faz sentido e aprova. Se não fizer sentido, nega. O diálogo existe para isso."

**Prompt gigante de uma vez só.**
Aluno escreve três parágrafos de instrução de uma vez e fica insatisfeito com o resultado. Resposta: "Tenta de novo com uma instrução só. O que você quer primeiro? Só isso." Reduza até o aluno sentir a diferença na qualidade do resultado.

**Perder a sessão/thread de prática.**
Aluno fecha a janela ou não encontra mais. Resposta: a sessão não some; só ficou fora de vista.

<!-- @codex -->
"Clique em 'Buscar threads' (`Ctrl+G`) e procure pelo nome que você deu. Se ela estava em um projeto específico, abra o projeto primeiro pela barra lateral."
<!-- @/codex -->

<!-- @claude -->
"Olha na barra lateral. Use o filtro de status no topo para mostrar todas as sessões. Se não aparecer, tente o filtro 'Por projeto' e selecione a pasta da oficina."
<!-- @/claude -->

**"Fechei sem querer o aplicativo."**
Resposta: "Pode reabrir e selecionar a mesma pasta da oficina. Tudo que foi salvo continua lá. A conversa da sessão de prática também."

**Confundir a sessão do tutor com a sessão de prática.**
Aluno envia uma tarefa real para a sessão do tutor (ou vice-versa). Resposta: "Sem problema. Olha qual das duas está com foco agora: a do tutor fica à esquerda, a de prática à direita (ou como você posicionou). Antes de enviar, confirma em qual você está."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre o nível de conforto inicial do aluno com a interface, o que gerou mais estranhamento (o diálogo de aprovação? o layout de painéis? a ideia de sessões paralelas?) e qual analogia funcionou melhor para explicar a bancada de trabalho permanente.

**Cérebro:** ainda não há nada para registrar formalmente neste módulo. A semente do cérebro foi plantada na entrevista inicial (ver pedagogia.md, seção "Primeiro contato"). O próximo módulo iniciará o primeiro registro efetivo.
