# Módulo: Conectores, plugins e MCP
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno instala e usa pelo menos um conector pronto (e-mail, agenda ou mensagens), entende o que é MCP em linguagem de gestor e sabe qual é o papel do MCP como ponte para os dados do ERP.

---

## Conceito em 1 minuto

Imagine que o agente mora em um escritório bem equipado, mas com a porta fechada para o mundo externo. Conectores e plugins são as portas: cada um que você instala abre uma passagem para um sistema específico, como o e-mail, a agenda ou o Slack. O agente passa a usar esses sistemas como qualquer pessoa usaria, mas sem que você precise copiar e colar manualmente.

MCP (Model Context Protocol) é o padrão técnico que define como essas portas são construídas. Para o gestor, o que importa não é o padrão em si, mas o que ele permite: um agente que consegue perguntar diretamente para o ERP sem precisar de export manual. Esse é o degrau 4 da escada de dados descrita em `dados-erp.md`.

A regra de cautela, que vale para qualquer conector: conecte só o necessário. Cada conexão é um canal de acesso que deve ter um propósito claro. Instalar todos os plugins disponíveis por curiosidade não é uma boa prática.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: mapear o que o aluno usa no dia a dia

Antes de instalar qualquer coisa, pergunte:

> "Quais ferramentas de comunicação você usa no trabalho? E-mail, agenda, algum sistema de mensagens como Teams ou WhatsApp Web, alguma plataforma de gestão de tarefas?"

Liste o que o aluno citou. Isso define quais conectores fazem sentido instalar.

Depois pergunte:

> "Qual dessas ferramentas consome mais tempo por ser acessada manualmente o dia todo, quando você precisaria que o agente consultasse por você?"

A resposta indica por onde começar.

**Verificação:** lista de ferramentas levantada, prioridade definida.

---

### Ato 2: instalar e usar o primeiro conector

Com a prioridade em mãos, mostre como instalar o conector escolhido:


Vá no menu `/plugin` e acesse a aba `Discover`. Navegue pelas categorias ou busque pelo nome. Conectores disponíveis incluem GitHub, GitLab, Jira, Slack, Notion, Figma, Sentry e outros. Cada plugin exibe uma descrição. Clique para instalar e siga o fluxo de autenticação.

Após instalar, use `/reload-plugins` para que as mudanças entrem em vigor. Então mostre como usar:

> "Plugins instalados são ativados com `/nome-do-plugin` ou descrevendo naturalmente o que você quer. Por exemplo: 'Use o plugin do GitHub para me listar os pull requests abertos há mais de 3 dias sem resposta'."

Se o aluno usa principalmente e-mail e agenda e não está na lista do marketplace atual, explique que servidores MCP para Gmail e Google Calendar podem ser adicionados manualmente via `claude mcp add` no CLI. Mas para o app desktop, verifique quais estão disponíveis diretamente no marketplace antes de propor a configuração manual.

**Verificação:** pelo menos um conector instalado e testado com uma consulta real.

---

### Ato 3: o que é MCP em linguagem de gestor

Após a experiência prática com um conector, apresente o conceito de MCP de forma acessível:

> "Cada plugin que instalamos usa por baixo um protocolo chamado MCP. MCP é simplesmente um padrão que define como o agente se conecta a sistemas externos de forma organizada e segura. Pense no MCP como o encanamento: você não precisa saber como o cano foi instalado para abrir a torneira, mas é bom saber que ele existe, porque é o que permite ligar qualquer sistema a qualquer agente que use o mesmo padrão."

Conecte com a realidade do aluno:

> "O sistema que sua empresa usa para pedidos, estoque ou faturamento provavelmente não tem um plugin pronto no marketplace. Mas se a TI ou o fornecedor do sistema configurar um servidor MCP com acesso de leitura, o agente passa a conseguir consultar esses dados diretamente, sem export manual. Esse é o Degrau 4 da escada que vimos no módulo de dados."

Referencie `dados-erp.md` sem repetir o conteúdo:

> "O pedido de uma página para fazer essa conversa com a TI está pronto em `dados-erp.md`. Quando o aluno estiver sentindo a dor do export manual toda semana, esse é o momento de usar aquele documento."

**Verificação:** aluno consegue explicar com as próprias palavras o que MCP permite fazer com o ERP da empresa.

---

### Ato 4: permissões mínimas como regra de ouro

Feche o módulo com a regra de cautela:

> "Cada conector que você instala recebe acesso a um sistema real. Alguns pedem acesso a leitura (ler e-mails), outros a leitura e escrita (enviar e-mails, criar eventos, postar mensagens). A regra prática: sempre que houver escolha, peça o mínimo necessário. Se você precisa só ler e-mails, não autorize o envio. Se você precisa de uma pasta específica do Drive, não autorize o Drive inteiro.

Isso não é desconfiança do agente, é proteção do aluno: se algum prompt sair errado, o dano possível é proporcional ao acesso concedido. Acesso mínimo, risco mínimo."

Revise com o aluno os conectores que instalou: qual nível de permissão cada um recebeu? Há algum que poderia ter permissão mais restrita?

> "Quando terminar a revisão, me manda um ok que eu anoto os conectores ativos no perfil."

**Verificação:** aluno revisou as permissões dos conectores instalados e entende o princípio de acesso mínimo.

---

## Variações por função

| Área | Conector de maior impacto imediato | Consulta típica de teste |
|---|---|---|
| Financeiro | E-mail (Gmail ou Outlook) | "Me lista e-mails de fornecedores com assunto de boleto ou cobrança das últimas 48h" |
| Comercial | E-mail + agenda | "Me lista reuniões de amanhã com os nomes dos participantes" |
| Operações | Slack ou Teams (se disponível) | "Me mostra mensagens do canal de produção das últimas 4 horas" |
| Marketing | Google Drive ou plataforma de conteúdo | "Me lista arquivos de campanha modificados esta semana" |
| Engenharia | GitHub ou GitLab (se aplicável) | "Me lista issues abertos há mais de 5 dias sem atualização" |
| Holding | E-mail + Google Drive | "Me mostra relatórios recebidos esta semana de qualquer subsidiária" |

---

## Aprofundamento

Para empresas que usam sistemas com APIs abertas (alguns ERPs modernos, plataformas de gestão), o MCP permite conexões diretas além dos plugins prontos do marketplace.
No Claude Code, o diretório oficial de servidores e plugins aparece no ecossistema de plugins e MCP da plataforma.A maioria requer configuração técnica pela TI, mas o gestor pode identificar quais seriam mais úteis e fazer o pedido.

Para quem usa muito Google Workspace (Gmail, Calendar, Drive, Docs, Sheets), os conectores nativos cobrem grande parte do trabalho. A prioridade de instalação para um gestor típico é: (1) e-mail, (2) agenda, (3) Drive.

---

## Erros comuns e diagnóstico

**Plugin instalado mas não funcionando.**
O aluno instalou mas o agente não está usando o conector. Fala do tutor:
"Use `/reload-plugins` na sessão atual, ou inicie uma nova sessão. Se persistir, vá em `/plugin`, aba `Errors`, para ver se há algum problema de carregamento."

**Aluno quer conectar o ERP diretamente no primeiro contato.**
Fala do tutor: "Para o ERP específico da empresa, precisaríamos de um servidor MCP configurado pela TI ou pelo fornecedor, o que não é um processo de alguns minutos. Vamos começar com e-mail ou agenda, que têm plugins prontos. O ERP fica como próximo passo quando a TI estiver pronta para a conversa."

**Preocupação com privacidade ao conectar e-mail.**
Fala do tutor: "A preocupação é legítima. O agente acessa os e-mails que você pede, não todos automaticamente. Você controla o que ele vê em cada prompt. E o acesso pode ser revogado a qualquer momento removendo o plugin. Mas se preferir começar sem e-mail, podemos testar com um arquivo de Drive ou com a agenda, que têm um perfil de dados menos sensível."

**Aluno não entende por que não deve instalar todos os plugins de uma vez.**
Fala do tutor: "Cada plugin é uma conexão ativa com um sistema real. Conexões que você não usa consomem permissões sem agregar valor. Quando você precisar de um novo, instale. Por enquanto, só o que resolve um problema que você já tem hoje."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre qual conector foi instalado, qual consulta o aluno testou, se houve resistência à ideia de conectar e-mail, e se o conceito de MCP ficou claro sem precisar de detalhes técnicos.

**Cérebro:** esta missão alimenta:
- `departamento/sistemas.md`: os conectores instalados representam as integrações ativas do departamento; registre quais foram configurados e para qual finalidade.
