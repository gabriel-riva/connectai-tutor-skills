# A escada de acesso aos dados do ERP

> Guia do tutor para missões que envolvem dados de sistemas da empresa. Usar sempre que o
> aluno mencionar ERP, relatório de sistema, planilha exportada ou "os dados ficam no sistema".

---

## Por que isso importa

A grande maioria dos ERPs usados por empresas industriais de médio porte no Brasil não oferece integração via API. Esses sistemas foram construídos para registrar operações, não para conversar com outros softwares. Isso não é um problema do aluno: é simplesmente a realidade do mercado onde a empresa opera hoje.

O custo mais ignorado dessa situação é o trabalho manual repetido: alguém precisa entrar no sistema, gerar o relatório, salvar o arquivo, abrir a planilha e então começar a análise. Feito uma vez, parece razoável. Feito toda semana, durante meses, por várias pessoas, esse tempo acumulado é substancial, e quase ninguém o contabiliza.

A regra de ouro do tutor neste tema é: partir sempre do degrau onde o aluno está hoje. Não existe ponto de partida "atrasado" ou "ruim". Um gestor que exporta planilhas do ERP e quer melhorar a análise já está à frente da maioria. O tutor celebra isso, e só propõe o degrau seguinte quando o aluno sentir, por conta própria, a limitação do degrau atual.

Nenhuma missão deve constranger o aluno pela infraestrutura da empresa. O foco é sempre: o que é possível fazer agora, com o que está disponível hoje?

---

## Como descobrir o degrau atual do aluno

Antes de propor qualquer automação ou integração, o tutor faz três perguntas simples. O objetivo não é diagnosticar limitações, mas entender o ponto de partida para construir a missão certa.

**Pergunta 1: "Como você acessa os dados quando precisa analisar algo do sistema?"**

Exemplos de resposta e o que indicam:
- "Eu entro no sistema e exporto um relatório em Excel" → Degrau 1 (export manual).
- "A gente tem um arquivo que o sistema gera toda manhã e fica numa pasta" → Degrau 2 (pasta quente).
- "Temos um banco de dados separado para consultas, a TI configurou" → Degrau 3 (banco espelho).
- "Não sei exatamente, a TI cuida disso" → Investigar com a segunda pergunta.

**Pergunta 2: "Esse relatório muda de formato ou de nome quando você exporta?"**

Exemplos de resposta e o que indicam:
- "Depende de como eu configurar na hora" → Degrau 1, sem padrão estabelecido.
- "Não, é sempre o mesmo arquivo, com o mesmo cabeçalho" → Potencial para Degrau 2.
- "Nunca exporto, os dados chegam automaticamente" → Degrau 3 ou 4.

**Pergunta 3: "Você ou alguém da equipe precisaria pedir ajuda à TI ou ao fornecedor do sistema para mudar alguma coisa na forma como os dados são gerados?"**

Exemplos de resposta e o que indicam:
- "Sim, a gente não mexe no sistema" → O aluno está nos degraus 1 ou 2; degraus 3 e 4 dependem de TI.
- "Tenho acesso de administrador" → Há mais autonomia; investigar o que é possível.
- "Temos contrato de suporte com o fornecedor" → Canal aberto para pedir o degrau 3.

---

## Degrau 1: Export manual (Excel, CSV ou PDF)

**O que é:** o aluno entra no ERP, seleciona o relatório desejado, exporta para um arquivo (Excel, CSV ou PDF) e trabalha com esse arquivo para fazer a análise.

**Por que é o ponto de partida digno:** todo gestor com acesso ao sistema consegue fazer isso hoje, sem depender de TI, de configuração especial ou de aprovação de ninguém. Não é uma solução provisória com vergonha: é um método real e funcional, usado por equipes competentes no mundo inteiro. O tutor trata com respeito qualquer aluno que chegue neste degrau.

**O que o tutor ensina aqui:** a arte está em usar bem o arquivo exportado. O app consegue limpar cabeçalhos bagunçados, cruzar dados de mais de uma planilha, calcular indicadores, identificar anomalias e gerar um resumo executivo. O aluno aprende a transformar o export num ponto de partida para análise, não num ponto final.

**Exemplo de missão 1: análise de faturamento mensal**

O aluno exporta o relatório de faturamento do mês como Excel. O prompt-modelo que o tutor prepara com ele:

> "Aqui está meu relatório de faturamento exportado do sistema. Por favor: (1) identifique os 10 clientes com maior volume no período; (2) compare com o mês anterior se eu anexar o arquivo anterior também; (3) sinalize qualquer cliente que tenha caído mais de 20% em relação ao mês anterior. Apresente o resultado em uma tabela e depois em um parágrafo executivo."

**Exemplo de missão 2: estoque com alerta de ruptura**

O aluno exporta o relatório de posição de estoque como CSV. O prompt-modelo:

> "Esse é meu relatório de estoque exportado do sistema. Analise e: (1) liste todos os itens com quantidade abaixo do ponto de reposição (coluna 'Estoque Mín'); (2) estime quantos dias de cobertura restam para cada um usando a coluna 'Consumo Médio Diário'; (3) ordene por urgência e apresente como uma lista pronta para eu encaminhar ao comprador."

**Armadilhas comuns e como o tutor orienta:**

- **Cabeçalho bagunçado:** muitos ERPs exportam com linhas de título antes dos dados reais, ou com células mescladas. O tutor orienta o aluno a descrever o formato no prompt ("o cabeçalho começa na linha 4, as colunas são: Data, Cliente, Produto, Qtd, Valor") ou a limpar o arquivo antes de anexar.
- **Datas no formato brasileiro:** o app pode interpretar 31/12/2025 como texto. O tutor avisa o aluno sobre isso e inclui no prompt: "as datas estão no formato DD/MM/AAAA".
- **Números com vírgula como separador decimal:** o CSV exportado do ERP geralmente usa vírgula para decimal e ponto-e-vírgula como separador de colunas. O tutor orienta o aluno a mencionar isso no prompt ou a salvar como XLSX antes de anexar.

---

## Degrau 2: Pasta quente (export recorrente padronizado)

**O que é:** o mesmo relatório, exportado com o mesmo nome de arquivo, no mesmo formato, salvo sempre na mesma pasta, no mesmo horário, com a mesma frequência. Pode ser feito por uma pessoa da equipe, por uma rotina do próprio ERP ou por um agendamento simples no computador.

**O que destrava:** quando o formato e o local do arquivo são previsíveis, automações conseguem trabalhar sem que ninguém precise acionar nada. O app sabe onde procurar o arquivo, sabe o que esperar dentro dele e consegue processar, cruzar e gerar o relatório sozinho, de forma recorrente.

**O que o tutor propõe ao aluno:** antes de qualquer automação técnica, sugerir que o aluno combine com a equipe um "ritual de export": todo dia útil, às 7h da manhã, alguém exporta o relatório X, salva com o nome padrão `vendas_AAAA-MM-DD.xlsx` na pasta `\\Servidor\Relatorios\Vendas\`. Esse ritual custa zero em tecnologia e transforma um processo manual em algo previsível o suficiente para automatizar o próximo passo.

**Exemplo de missão com automação:** o aluno tem o relatório de produção exportado toda manhã para uma pasta no servidor. O app processa o arquivo automaticamente ao detectar o novo arquivo, calcula os indicadores de eficiência (OEE, paradas, volumes por turno) e envia um resumo por mensagem para o gestor antes das 8h. O aluno não precisa abrir nenhuma planilha: o resumo chega pronto.

---

## Degrau 3: Usuário somente leitura em banco espelho

**O que é (explicado para o gestor):** imagine que o ERP da empresa é um arquivo físico guardado num cofre. Ninguém toca nesse cofre durante o dia de trabalho sem precisar. O banco espelho é uma cópia desse arquivo, atualizada automaticamente a cada hora (ou a cada dia, dependo da configuração), guardada num lugar separado. O usuário somente leitura é uma chave que abre apenas essa cópia, e só para ler: não há como alterar nada, não há como interferir com o sistema que está rodando a fábrica. O app usa essa chave para consultar dados frescos sem depender de export manual.

**Por que é seguro:**
- Somente leitura: fisicamente impossível alterar qualquer dado pelo app.
- Banco espelho: nunca o banco de produção; se algo der errado na consulta, o sistema que roda a fábrica não sofre impacto nenhum.
- Credencial própria: a senha é gerada exclusivamente para esse fim, guardada como segredo no sistema, não compartilhada com ninguém.

**O que destrava:** o dado sempre fresco chega ao app sem que ninguém precise exportar, salvar ou lembrar de fazer nada. Uma pergunta feita às 23h retorna o dado atualizado da última sincronização do espelho.

**Honestidade obrigatória do tutor:** o aluno não resolve isso sozinho. Configurar um banco espelho e criar um usuário somente leitura requer a participação de TI interna ou do fornecedor do ERP. O tutor não deve prometer que "é simples" nem que "qualquer um faz". O papel do tutor aqui é diferente: ajudar o aluno a preparar a conversa com quem pode aprovar e executar essa configuração.

**O papel do tutor:** quando o aluno estiver sentindo a dor do Degrau 1 ou 2 (export que esquece, dado desatualizado, processo que para quando a pessoa responsável falta), o tutor planta a semente do Degrau 3 e usa o modelo de pedido da seção final deste guia para ajudar o aluno a levar a proposta para TI ou para o fornecedor.

---

## Degrau 4: MCP no banco espelho

**O que é MCP (explicado para o gestor):** MCP é um padrão de conexão que permite que o app de IA converse com sistemas externos de forma estruturada e segura. Em vez de o app receber um arquivo avulso, ele consegue fazer perguntas diretamente ao sistema, na hora, usando regras claras de acesso. É como a diferença entre receber um extrato impresso por e-mail e ter o internet banking: o dado está disponível quando você pergunta, não quando alguém lembrou de enviar.

**A visão completa deste degrau:** o gestor abre o app, digita "como estão as vendas do mês comparado com a meta?" e o app consulta o banco espelho na hora, calcula a comparação e responde em segundos, com os dados mais recentes disponíveis. Nenhum export. Nenhum arquivo. Nenhum intermediário.

**O mesmo aviso de honestidade do Degrau 3 se aplica aqui:** a configuração do MCP depende de TI e/ou do fornecedor do ERP. O aluno não implementa isso sozinho. O tutor ajuda a construir o caso de negócio e a preparar a conversa, mas não deve criar a expectativa de que o aluno chegará ao Degrau 4 rapidamente ou sem suporte técnico especializado.

---

## Como o tutor sugere degraus

**Regras de conduta:**

1. **Partir sempre do degrau atual.** A primeira missão de dados é sempre construída sobre o que o aluno já consegue fazer hoje. Se ele exporta planilhas, a primeira missão usa planilhas.

2. **Plantar a semente do próximo degrau apenas quando o aluno sentir a dor do atual.** O tutor não fala sobre o Degrau 2 na primeira conversa. Espera o momento em que o aluno diz "isso é cansativo de fazer toda semana" ou "quando alguém falta, os dados não chegam". Esse é o momento de apresentar o próximo degrau.

3. **Nunca vender complexidade.** O tutor não descreve bancos espelho, MCP ou automações como objetivos a perseguir. Descreve como soluções para dores concretas que o aluno já verbalizou. A complexidade é um meio, nunca um fim em si.

4. **Celebrar o Degrau 1 como vitória real.** Um gestor que aprendeu a exportar o relatório correto, anexar ao app e obter uma análise que antes levava horas em segundos ganhou algo genuíno. O tutor reconhece isso explicitamente e sem condescendência. A vitória não é pequena por ser simples.

---

## Modelo: pedido de uma página para a TI ou fornecedor do ERP

O tutor usa este template quando o aluno está pronto para levar o pedido do Degrau 3 para a equipe de TI ou para o fornecedor do ERP. O tutor preenche os placeholders junto com o aluno e gera o documento como artefato para o aluno usar na conversa.

---

**PEDIDO DE CONFIGURAÇÃO: ACESSO DE CONSULTA AO BANCO DE DADOS**

**Para:** TI / Fornecedor do {SISTEMA/ERP}
**De:** {ÁREA} ({EMPRESA})
**Assunto:** Criação de usuário somente leitura em banco de dados espelho

---

**O que estamos pedindo**

Solicitamos a criação de um usuário de banco de dados com permissão somente leitura em um banco de dados espelho (cópia de leitura) do {SISTEMA/ERP}. O escopo de acesso seria limitado às tabelas e visões necessárias para as análises da {ÁREA}, equivalentes aos seguintes relatórios que já geramos hoje: {EXEMPLOS DE RELATÓRIOS HOJE}.

Não é necessário acesso ao banco de produção. O usuário deve ter permissão exclusivamente de SELECT (leitura), sem capacidade de inserir, alterar ou excluir registros.

---

**Por que é seguro**

- O acesso é somente leitura: tecnicamente impossível modificar qualquer dado pelo canal solicitado.
- O banco espelho é uma cópia separada do banco de produção: nenhuma consulta feita pelo app afeta o sistema que opera a empresa.
- A credencial será gerada exclusivamente para este fim, armazenada de forma segura no ambiente do app, e não será compartilhada com usuários individuais.

---

**O que isso destrava para a {EMPRESA}**

- Acesso a dados atualizados sem depender de export manual recorrente, eliminando retrabalho operacional da equipe.
- Possibilidade de análises em tempo real pela {ÁREA}, sem aguardar a disponibilidade de quem gerencia os relatórios.
- Base técnica para automatizar indicadores operacionais e relatórios gerenciais que hoje consomem tempo de profissionais qualificados em tarefas repetitivas.

---

**Próximo passo sugerido**

Propomos uma conversa de 30 minutos para alinhar: quais tabelas ou visões são necessárias, qual frequência de sincronização do espelho faz sentido para o caso de uso da {ÁREA}, e como a credencial será gerenciada de forma segura. A {EMPRESA} se compromete a usar o acesso apenas para as finalidades descritas neste pedido.

Fico à disposição para qualquer dúvida.

---

*Documento preparado com suporte do app de IA da {ÁREA}.*
