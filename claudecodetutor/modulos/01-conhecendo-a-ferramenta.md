# Módulo: Conhecendo a ferramenta
**Nível:** núcleo · **Pré:** nenhum · **Tempo típico:** 25-35 min
**Resultado:** o aluno navega pela interface com autonomia, sabe separar a janela do tutor da sessão de prática, executa uma aprovação consciente e conhece os controles de quem manda no agente.

---

## Conceito em 1 minuto

Imagine uma bancada de trabalho com um assistente dentro. A bancada fica aberta entre os dias: o que você deixa em cima ontem está lá amanhã. Esse assistente não é um chat descartável que começa do zero a cada conversa; ele opera em espaços de trabalho permanentes, um por assunto. Trocar de assunto não significa jogar fora o que foi construído; significa abrir outra gaveta da mesma bancada.

Cada espaço de trabalho tem o seu próprio histórico e os seus próprios arquivos. Você pode ter vários abertos ao mesmo tempo, visíveis lado a lado, sem que um interfira no outro.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou o ato anterior.

### Ato 1: reconhecimento da casa

VOCÊ apresenta a casa; o aluno só acompanha com os olhos. NUNCA peça que o aluno descreva a tela (é você quem conhece a interface; quiz de tela é constrangedor e inútil). Diga:

> "Deixa eu te apresentar a casa em 30 segundos, olhando pra tela junto comigo."

E descreva as zonas com os nomes corretos:


A tela tem três zonas principais:
- **Barra lateral esquerda:** lista de sessões abertas, agrupáveis por projeto, com filtros de status no topo.
- **Área central (chat):** histórico de mensagens e compositor de texto na parte inferior.
- **Painéis arrastáveis:** o espaço à direita do chat pode abrir painéis de visualização: o de alterações (o "controle de alterações" do Word, aplicado a qualquer arquivo; nome técnico: diff) e o de preview (a prévia do resultado: documentos, planilhas, páginas). Arraste o cabeçalho de qualquer painel para reposicioná-lo; arraste a borda para redimensionar.

Mostre ao aluno como abrir o painel de preview (`Ctrl+Shift+P`) e o de alterações (`Ctrl+Shift+D`). Peça que abra e feche cada um. Existe também uma área técnica (o terminal) que o agente usa por conta própria: mencione em UMA frase que ela existe e que o aluno não vai precisar dela. Nunca proponha que o aluno a use.

**Verificação:** o aluno abriu e fechou os painéis (pergunte no máximo "achou os dois?"; nunca peça que ele nomeie ou descreva nada de volta).

---

### Ato 2: a sessão de prática

Explique que o trabalho vai acontecer em dois espaços abertos lado a lado: o do tutor (onde a conversa atual acontece) e a sessão de prática (onde o aluno experimenta sem medo de estragar nada).

Instrução ao aluno:


Guie o aluno COM O AVISO DO EFEITO antes do atalho:

> "Vamos criar a sua sessão de prática. Atenção: o atalho `Ctrl+N` cria a sessão nova e TROCA o foco pra ela; isso é esperado, esta conversa continua na barra lateral. Faz assim: (1) aperta `Ctrl+N` e seleciona a MESMA pasta da oficina; (2) nomeia a sessão de 'Prática: Módulo 1'; (3) volta pra esta conversa clicando nela na barra lateral; (4) agora segura `Ctrl` e clica na sessão de prática na barra lateral: as duas abrem lado a lado (`Ctrl+Tab` alterna entre os painéis)."

Depois, VERIFIQUE VOCÊ MESMO pelo transcript local (seu canal de supervisão): localize a sessão nova e confirme proativamente ("pronto, estou acompanhando sua sessão de prática daqui"). Só se a leitura falhar, pergunte apenas: "as duas estão lado a lado, com a mesma pasta nas duas?". A partir de agora, tudo que o aluno testar vai para a sessão de prática, não para a sessão do tutor.

**Verificação:** os dois espaços estão abertos lado a lado, apontando para a mesma pasta.

---

### Ato 3: primeira tarefa de verdade

Hora de viver uma aprovação real. Passe a instrução para a sessão de prática do aluno:

> "Na sessão de prática, escreva o seguinte (adapte o trecho entre colchetes para a sua área): 'Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim no meu trabalho de [financeiro / comercial / operações / marketing].' Depois clique em enviar e observe o que aparece antes de clicar em qualquer botão."

Quando o diálogo de aprovação aparecer, pause e explique:

> "Esse aviso não é um problema; é uma proteção. O app está pedindo permissão antes de tocar nos seus arquivos. Você vê exatamente o que ele quer fazer. Se não concordar, nega. Se estiver certo, aprova. É assim que você fica no controle."

Após a aprovação, verifique com o aluno que o arquivo `teste.md` apareceu na pasta.

**Verificação:** aluno aprovou a ação conscientemente e viu o arquivo ser criado.

---

### Ato 4: controles de quem manda

Apresente os três controles em ordem, um de cada vez, pedindo ao aluno que teste cada um na sessão de prática:

**Steering (correção em voo):** enquanto o agente está trabalhando, você pode enviar uma nova mensagem que muda o que ele está fazendo agora. Não precisa esperar terminar. Exemplo: peça algo um pouco comprido na prática, e no meio do processo, envie "pode deixar mais curto".

**Queuing (enfileirar):** você pode adicionar a próxima instrução antes do passo atual terminar. O agente executa assim que concluir o que está fazendo. Exemplo: enquanto ele ainda trabalha, envie "quando terminar, me diz quantas palavras esse texto tem".

**Voz:**


Verifique no app se o botão de microfone aparece no compositor. Se aparecer, clique para ativar o ditado (o app enviará o áudio para transcrição). Útil para pensamentos rápidos ou dumps de contexto.

**Manter a sessão/thread importante à mão:**


Se quiser manter a sessão à mão, procure no menu de contexto dela (clique com o botão direito na barra lateral) uma opção de fixar, se disponível na sua versão. Alternativamente, renomeie a sessão com um título claro (o comando `/rename` no campo de mensagem faz isso): com um bom nome, encontrá-la na barra lateral fica fácil mesmo com várias sessões abertas.

**Verificação:** aluno demonstrou steering, entendeu queuing e sabe como deixar a sessão/thread importante fácil de reencontrar.

---

## Variações por função

Use o trecho entre colchetes do Ato 3 para calibrar a primeira tarefa de verdade:

| Área | Primeira tarefa de verdade |
|---|---|
| Financeiro | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim no fechamento mensal." |
| Comercial | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim na preparação de propostas." |
| Operações | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim no acompanhamento de processos." |
| Marketing | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim na criação de conteúdo." |
| Engenharia | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim na documentação técnica." |
| Holding/direção | "Crie um arquivo chamado teste.md com 3 linhas sobre o que você pode fazer por mim na consolidação de informações de áreas diferentes." |

---

## Aprofundamento

Para quem quiser ir além: o app opera em modos de execução diferentes, que definem onde o trabalho acontece.


Há três ambientes: **Local** (trabalha diretamente nos seus arquivos), **Remote** (executa em nuvem da Anthropic) e **SSH** (servidor remoto). O ambiente é escolhido antes de enviar a primeira mensagem de cada sessão. Para a maioria das missões desta trilha, o Local é o certo.

Um recurso valioso no modo Local: **checkpointing**. O app salva o estado dos arquivos antes de cada edição. Para voltar atrás, pressione `Esc` duas vezes com o campo de mensagem vazio, ou escreva `/rewind` no compositor. Um menu aparece listando cada mensagem enviada; escolha o ponto desejado e decida se quer restaurar só o código, só a conversa ou os dois. Isso elimina o medo de "estragar algo": dá para desfazer com precisão cirúrgica.

---

## Erros comuns e diagnóstico

**Medo de clicar em "aprovar".**
Fala: "Posso só olhar o que ele quer fazer antes de aprovar?" Resposta: "Claro, esse é exatamente o ponto. Leia o que está sendo pedido, confirme que faz sentido e aprova. Se não fizer sentido, nega. O diálogo existe para isso."

**Prompt gigante de uma vez só.**
Aluno escreve três parágrafos de instrução de uma vez e fica insatisfeito com o resultado. Resposta: "Tenta de novo com uma instrução só. O que você quer primeiro? Só isso." Reduza até o aluno sentir a diferença na qualidade do resultado.

**Perder a sessão/thread de prática.**
Aluno fecha a janela ou não encontra mais. Resposta: a sessão não some; só ficou fora de vista.


"Olha na barra lateral. Use o filtro de status no topo para mostrar todas as sessões. Se não aparecer, tente o filtro 'Por projeto' e selecione a pasta da oficina."

**"Fechei sem querer o aplicativo."**
Resposta: "Pode reabrir e selecionar a mesma pasta da oficina. Tudo que foi salvo continua lá. A conversa da sessão de prática também."

**Confundir a sessão do tutor com a sessão de prática.**
Aluno envia uma tarefa real para a sessão do tutor (ou vice-versa). Resposta: "Sem problema. Olha qual das duas está com foco agora: a do tutor fica à esquerda, a de prática à direita (ou como você posicionou). Antes de enviar, confirma em qual você está."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre o nível de conforto inicial do aluno com a interface, o que gerou mais estranhamento (o diálogo de aprovação? o layout de painéis? a ideia de sessões paralelas?) e qual analogia funcionou melhor para explicar a bancada de trabalho permanente.

**Cérebro:** ainda não há nada para registrar formalmente neste módulo. A semente do cérebro foi plantada na entrevista inicial (ver pedagogia.md, seção "Primeiro contato"). O próximo módulo iniciará o primeiro registro efetivo.
