# Módulo: Navegador e computador
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno entende as camadas de alcance disponíveis na sua plataforma, sabe quando usar cada uma versus quando há um caminho melhor, e executa uma tarefa real em um sistema que não tem integração direta.

---

## Conceito em 1 minuto

Um agente que só trabalha com arquivos de texto tem um alcance limitado. Quando o trabalho precisa acontecer dentro de um sistema com interface visual, como um portal de fornecedor, um ERP sem API ou uma ferramenta de gestão da empresa, há duas alternativas: ou o agente usa o navegador para acessar o site, ou ele assume o controle do computador como se fosse você, clicando, digitando e navegando da mesma forma que um humano faria.

A escolha entre as camadas não é técnica: é prática. Use a mais simples que resolve o problema. A mais simples que resolve é sempre a melhor.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: mapear o sistema sem integração

Pergunte ao aluno:

> "Tem algum sistema que você acessa todo dia que não tem conector disponível? Um portal de fornecedor, um sistema de gestão que funciona só no navegador, alguma ferramenta interna da empresa que não está no marketplace de plugins?"

Liste o que o aluno citou. Escolha o mais simples para o exercício: de preferência um portal público ou com login simples, onde a tarefa seja de leitura ou preenchimento de formulário básico.

**Verificação:** sistema-alvo identificado para o exercício.

---

### Ato 2: entender as camadas disponíveis

Mostre as camadas antes de usar qualquer uma. O conteúdo depende da plataforma:

> "No Codex, existem três camadas de alcance para o que está fora dos seus arquivos. A primeira é o navegador integrado (`$browser`): um painel dentro do app que renderiza páginas web. Acesse com `Ctrl+Shift+B`. Ele funciona bem para páginas públicas sem login, mas não suporta autenticação. A segunda é a extensão Chrome (`@chrome`): acessa o Chrome com o seu perfil de usuário, incluindo cookies e sessões ativas. Use para qualquer site onde você já está logado. A terceira é o controle do computador (`@computer`): o agente vê a tela e opera o computador como um humano faria, clicando e digitando em qualquer aplicativo com interface gráfica. Não precisa de API, não precisa de conector, funciona em qualquer app visível na tela.

No Windows, o app que o agente deve controlar precisa estar visível na área de trabalho durante a execução. Acesse em Configurações > Computer Use para ativar."

Mostre a tabela prática ao aluno:
- Página pública sem login: use `$browser`
- Site com login (Gmail, portal de fornecedor): use `@chrome` com a extensão instalada
- Aplicativo desktop (ERP, Excel, qualquer software instalado): use `@computer`


**Verificação:** aluno entende as camadas disponíveis e quando usar cada uma.

---

### Ato 3: executar uma tarefa real

Com o sistema-alvo definido no Ato 1, monte a tarefa junto com o aluno. Diga:

> "Agora vamos executar uma tarefa real nesse sistema. Qual é a tarefa de menor risco que você faria nele? De preferência, algo que seja só de leitura ou de consulta."

Na sessão de prática, passe o modelo adaptado:

Para sistemas com login: `"@chrome, acesse [URL do sistema]. Encontre [o que o aluno quer consultar: o relatório de X, o status de Y, os preços de Z] e me traga as informações em forma de lista."`

Para aplicativos desktop: `"@computer, abra [nome do aplicativo] e acesse a tela de [área relevante]. Me diga [informação que o aluno quer]. Não altere nenhum dado, apenas leia e me informe."`

Acompanhe a execução junto com o aluno. Para `@computer`, o aplicativo precisa estar visível na tela durante a tarefa.


**Verificação:** tarefa executada, aluno conferiu o resultado.

---

### Ato 4: quando GUI versus quando há caminho melhor

Feche o módulo com a reflexão sobre quando usar versus quando evitar:

> "Controle de GUI é poderoso, mas é a ferramenta mais lenta e mais frágil. Se o sistema tem um botão de export de relatório, usá-lo é melhor do que pedir ao agente para navegar e copiar linha a linha. Se há um plugin ou MCP disponível para o sistema, ele vai ser mais rápido e mais confiável do que GUI.

Pense no controle de GUI como a ferramenta que você usa quando não há outro caminho, não como a primeira escolha. O momento de usar: o sistema não tem API, não tem export útil, não tem plugin, e a tarefa precisa ser feita agora."

**Verificação:** aluno consegue nomear um caso em que usaria GUI versus um caso em que usaria uma camada mais simples.

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
Fala do tutor: "Verifica se a extensão Chrome está instalada e mostrando 'Connected' no Chrome. Se for um sistema com autenticação, você precisa estar logado no Chrome nesse site antes de pedir ao agente para acessá-lo."

**Agente alterou algo que não deveria.**
O aluno pediu para consultar e o agente clicou em algo errado. Fala do tutor: "Para tarefas de consulta, sempre inclua no prompt: 'não altere nenhum dado, apenas leia e me informe'. E para tarefas em sistemas com dados reais da empresa, faça o primeiro teste com algo não crítico, como um cadastro de teste ou um pedido de baixo valor."

**Computer use travou ou ficou em loop.**

**Aluno ficou desconfortável com o agente controlando o computador.**
Fala do tutor: "Esse desconforto é saudável. O controle de computador é a camada com mais poder e mais responsabilidade. Você pode interromper a qualquer momento com Esc. E você sempre pode fazer o trabalho manualmente se preferir: essa ferramenta existe para quando você quer delegar, não para quando você prefere fazer."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual sistema foi acessado, qual camada foi usada, se houve hesitação em conceder acesso ao computer use ou à extensão Chrome, e se a tarefa foi concluída com sucesso.

**Cérebro:** esta missão alimenta:
- `departamento/sistemas.md`: os sistemas acessados por GUI que não têm conector direto representam oportunidades futuras de integração via MCP; registre o nome do sistema e o que o aluno costuma consultar nele.
