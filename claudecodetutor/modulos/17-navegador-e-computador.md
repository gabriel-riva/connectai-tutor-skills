# Módulo: Navegador e computador
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno entende as camadas de alcance disponíveis na sua plataforma, sabe quando usar cada uma versus quando há um caminho melhor, e executa uma tarefa real em um sistema que não tem integração direta.

---

## Conceito em 1 minuto

Há sistemas no trabalho que nunca vão se conectar diretamente ao agente: portais de fornecedores com login próprio, ERPs que só funcionam no navegador, plataformas de cotação, sistemas legados da empresa. Para esses casos, o agente vai até onde o dado está, da mesma forma que você faria: abre o navegador, acessa o portal, lê o que precisa e traz o resultado.

Esse módulo cobre exatamente esse caso: o que fazer quando não há integração, plugin nem export disponível, e a tarefa precisa ser feita hoje.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: mapear o sistema sem integração

Pergunte ao aluno:

> "Tem algum sistema que você acessa todo dia que não tem conector disponível? Um portal de fornecedor, um sistema de gestão que funciona só no navegador, alguma ferramenta interna da empresa que não está no marketplace de plugins?"

Liste o que o aluno citou. Escolha o mais simples para o exercício: de preferência um portal público ou com login simples, onde a tarefa seja de leitura ou preenchimento de formulário básico.

**Verificação:** sistema-alvo identificado para o exercício.

---

### Ato 2: identificar como o agente vai chegar até lá

Antes de executar a tarefa, pergunte ao aluno sobre o sistema escolhido no Ato 1:

> "Esse sistema abre no navegador ou é um software instalado no computador?"

Com a resposta, escolha o caminho certo para a missão e explique em uma frase:


Se for site com login: "Vamos usar a extensão Claude in Chrome, que acessa o site com o seu perfil já logado. Ela precisa estar instalada no Chrome ou Edge (não funciona no Brave nem no Arc). Se não tiver, instalamos agora antes de continuar."

Se for aplicativo desktop: "Vamos usar o computer use, que é o agente vendo a tela e clicando como você faria. Ative em Configurações > General > Desktop app antes de começar. Na primeira vez, um pedido de aprovação vai aparecer para o aplicativo específico."

Se for página pública sem login: "Para páginas públicas, o agente acessa diretamente pela navegação integrada, sem nenhuma configuração extra."

Detalhes técnicos de bastidor (use para verificar antes de começar, não como aula para o aluno):
- Hierarquia de escolha: MCP se disponível > navegador integrado > Claude in Chrome > computer use
- Computer use: tiers por categoria (navegadores: só visualização; terminais e IDEs: só clique; demais apps: controle completo)

**Verificação:** caminho correto identificado e configuração necessária verificada antes de avançar para a execução.

---

### Ato 3: executar uma tarefa real

Com o sistema-alvo definido no Ato 1, monte a tarefa junto com o aluno. Diga:

> "Agora vamos executar uma tarefa real nesse sistema. Qual é a tarefa de menor risco que você faria nele? De preferência, algo que seja só de leitura ou de consulta."

Na sessão de prática, passe o modelo adaptado:


Para sistemas no navegador com extensão: `"Acesse [URL do sistema] usando Claude in Chrome. Encontre [o que o aluno quer consultar] e me traga as informações em forma de lista."`

Para aplicativos desktop com computer use: `"Use computer use para abrir [nome do aplicativo]. Acesse a tela de [área relevante] e me diga [informação que o aluno quer]. Não altere nenhum dado, apenas leia e me informe."`

Lembre ao aluno: ao usar computer use, o agente assume o mouse e o teclado. Fique presente e pressione `Esc` a qualquer momento para interromper e retomar o controle.

> "Quando terminar, me manda um ok que eu confiro o resultado direto."

**Verificação:** tarefa executada, aluno conferiu o resultado.

---

### Ato 4: quando essa abordagem faz sentido

Feche o módulo com a lógica de quando usar:

> "O controle de interface visual é o que você usa quando não há caminho melhor disponível: o sistema não tem export útil, não tem plugin e a tarefa precisa ser feita agora. É mais lento e mais sensível a mudanças de tela do que uma integração direta. Mas funciona nos sistemas que o resto das ferramentas não alcança. A pergunta antes de usar: existe um botão de export, um plugin ou uma API? Se sim, use. Se não, essa abordagem é a certa."

Pergunte ao aluno:

> "Pensando nos sistemas que você usa no dia a dia: qual deles seria candidato para esse tipo de acesso? E qual teria um caminho mais simples?"

**Verificação:** aluno consegue nomear um caso em que usaria essa abordagem versus um caso em que há caminho mais simples disponível.

---

## Variações por função

| Área | Sistema sem integração típico | Tarefa de leitura de menor risco |
|---|---|---|
| Financeiro | Portal bancário, sistema de cobrança | Consultar extrato ou posição de boletos |
| Comercial | CRM ou portal do cliente da empresa | Verificar status de pedidos ou histórico de compras |
| Operações | ERP com interface web, portal de fornecedor | Consultar estoque ou prazo de entrega de um pedido |
| Marketing | Plataforma de anúncios, ferramenta de automação | Verificar resultado de campanha ou custo por resultado |
| Engenharia | Sistema de gestão de manutenção, portal técnico | Consultar histórico de chamados ou SLA de abertura |
| Holding | Portal de banco de dados setorial, plataforma de benchmarking | Verificar indicadores publicados para o setor |

---

## Aprofundamento

Para tarefas repetitivas em sistemas sem integração (consultar estoque toda manhã, checar status de pedidos toda tarde), a combinação de computer use com uma automação agendada (módulo 15) é o próximo passo natural. O agente executa a tarefa no horário definido e entrega o resultado sem que o aluno precise abrir o sistema manualmente.

Mas vale a pena revisar antes de automatizar: se o sistema tem um botão de export ou um relatório programável, configurar isso junto com a TI é mais robusto do que automatizar a GUI.

---

## Erros comuns e diagnóstico

**Agente não consegue se conectar ao sistema.**
Fala do tutor: "Verifica se a extensão Claude in Chrome está instalada, conectada e se você está usando o Chrome ou Edge (não Brave, não Arc). Se o sistema requer login, abra o site no Chrome e faça login manualmente primeiro. Depois peça ao agente para acessar com a extensão."

**Agente alterou algo que não deveria.**
O aluno pediu para consultar e o agente clicou em algo errado. Fala do tutor: "Para tarefas de consulta, sempre inclua no prompt: 'não altere nenhum dado, apenas leia e me informe'. E para tarefas em sistemas com dados reais da empresa, faça o primeiro teste com algo não crítico, como um cadastro de teste ou um pedido de baixo valor."

**Computer use travou ou ficou em loop.**
Fala do tutor: "Pressione `Esc` para interromper imediatamente. O controle volta para você. Olha o que estava na tela naquele momento e tenta entender por que o agente travou. Depois refaz o prompt sendo mais específico sobre o que ele deveria clicar."

**Aluno ficou desconfortável com o agente controlando o computador.**
Fala do tutor: "Esse desconforto é saudável. O controle de computador é a camada com mais poder e mais responsabilidade. Você pode interromper a qualquer momento com Esc. E você sempre pode fazer o trabalho manualmente se preferir: essa ferramenta existe para quando você quer delegar, não para quando você prefere fazer."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual sistema foi acessado, qual camada foi usada, se houve hesitação em conceder acesso ao computer use ou à extensão Chrome, e se a tarefa foi concluída com sucesso.

**Cérebro:** esta missão alimenta:
- `departamento/sistemas.md`: os sistemas acessados por GUI que não têm conector direto representam oportunidades futuras de integração via MCP; registre o nome do sistema e o que o aluno costuma consultar nele.
