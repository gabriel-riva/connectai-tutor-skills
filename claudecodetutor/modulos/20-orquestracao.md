# Módulo: Orquestração
**Nível:** eletiva avançada · **Pré:** 01, 02, pelo menos uma missão real · **Tempo típico:** 45 min
**Resultado:** o aluno divide uma entrega real em frentes paralelas, cada uma com papel e critério claros, e entrega o resultado final consolidado em menos tempo do que faria em sequência.

---

## Conceito em 1 minuto

Há um limite para o que um único pedido consegue entregar bem: quando o trabalho tem partes independentes que poderiam acontecer ao mesmo tempo, pedir tudo de uma vez gera resultado mediano em tudo. Dividir em frentes paralelas, cada uma com foco específico, gera resultado melhor em cada parte.

A diferença não é técnica. É a mesma lógica de qualquer time: você não coloca todos fazendo tudo ao mesmo tempo sem pauta. Você define quem pesquisa, quem organiza, quem escreve e quem revisa. Cada um sabe o que entrega, em qual formato e para quem.

---

## Missão guiada

> Um ato de cada vez. Aguarde o aluno completar antes de passar ao próximo.

### Ato 1: escolher a entrega real

Peça ao aluno uma entrega que ele precisaria fazer nos próximos dias e que tenha pelo menos duas partes independentes. Exemplos que funcionam:

- preparar reunião com cliente (pesquisa sobre o cliente + preparação de pauta + levantamento de objeções prováveis)
- revisar relatório mensal com contexto de mercado (análise dos dados internos + pesquisa de referências externas + versão executiva)
- comparar fornecedores (pesquisa de mercado + análise de critérios da empresa + recomendação)
- montar plano de ação de uma não conformidade (levantamento de causa raiz + plano de ação + checagem de riscos)

Peça ao aluno para escolher. Se hesitar, use o exemplo da tabela de variações mais próximo da área dele.

**Verificação:** entrega escolhida, aluno consegue nomear pelo menos duas partes que poderiam acontecer em paralelo.

### Ato 2: desenhar os papéis

Antes de o aluno executar qualquer coisa, o tutor demonstra o conceito de papéis criando a estrutura. Isso serve como gabarito visual antes de o aluno tentar.

Crie você mesmo uma sessão chamada "Orquestração: [nome da tarefa do aluno]" na mesma pasta da oficina. Na sessão, defina os papéis em tabela e mostre ao aluno como ficaria antes de ele criar as próprias. Depois de mostrar, oriente:

> "Repara na estrutura: cada papel tem uma responsabilidade específica, uma fonte diferente e um critério claro de entrega. Agora você vai criar as suas sessões de trabalho com a mesma lógica."

Modelo de tabela de papéis (adapte ao caso do aluno):

| Papel | O que entrega | Fonte de informação | Critério de entrega pronto |
|---|---|---|---|
| Pesquisador | fatos, dados, fontes | web, arquivos, mensagens | lista com link e data de cada item |
| Analista | padrões, riscos, comparações | dados ou pesquisa do papel anterior | critérios definidos explicitamente |
| Redator | versão clara para o destinatário | síntese dos demais papéis | tom aprovado, sem jargão, sem promessa indevida |
| Revisor | lacunas, inconsistências, ajustes | entrega do redator | lista numerada de ajustes |

**Verificação:** papéis definidos, aluno consegue explicar o que cada um entrega.

### Ato 3: executar em pequena escala

Na sessão de prática, passe a missão:

> "Divida a entrega '[nome da tarefa]' em dois papéis. Para cada papel, escreva: (1) o prompt que você usaria para aquele papel; (2) o nome do arquivo de saída esperado; (3) o critério que diz que aquele papel está pronto. Salve em `missões/orquestracao/00-plano.md`."

Após receber o plano, avalie: os prompts são distintos o suficiente? As fontes são diferentes? Faça um ajuste se necessário.

Para a execução: o aluno cria sessões separadas nomeadas por papel. Cada sessão salva a entrega em `missões/orquestracao/`. O aluno coordena manualmente entre as sessões.

Agora execute um papel de verdade:

> "Vamos rodar o primeiro papel agora. Abra uma [thread/sessão] nova chamada '[nome do papel 1]', cole o prompt desse papel e execute."

> "Quando terminar o primeiro papel, me manda um ok que eu confiro a entrega antes de passar para o segundo."

**Verificação:** pelo menos um papel executado, entrega salva em `missões/orquestracao/`, os prompts dos outros papéis não se sobrepõem ao que já foi feito.

### Ato 4: síntese

Com uma ou duas entregas em mão, passe a síntese:

> "Leia os arquivos em `missões/orquestracao/`. Produza uma síntese executiva de uma página com: decisões que já estão claras, riscos identificados, dúvidas ainda abertas e o próximo passo recomendado. Cite qual arquivo sustenta cada ponto."

> "Quando terminar, me manda um ok que eu confiro a síntese."

---

## Variações por função

| Área | Orquestração útil |
|---|---|
| Financeiro | Agente de dados, agente de variações, agente de explicação executiva |
| Comercial | Agente de pesquisa do cliente, agente de proposta, agente de objeções |
| Operações | Agente de causa raiz, agente de plano de ação, agente de checagem de risco |
| Marketing | Agente de pesquisa, agente de calendário, agente de revisão de marca |
| RH | Agente de benchmark, agente de política, agente de perguntas frequentes |
| Holding | Agentes por empresa ou por indicador, com síntese única no final |

---

## Aprofundamento

Quando a orquestração funcionar bem, transforme o fluxo em skill no módulo 99. O sinal de maturidade é quando o aluno consegue dizer: "sempre que eu fizer este trabalho, estes são os papéis, arquivos e critérios".

Nota sobre disponibilidade: coordenação direta entre threads ou sessões (um agente lendo o resultado de outro automaticamente) depende da versão do app. Verifique em `referencia/remoto-orquestracao.md` o que está disponível no ambiente do aluno antes de prometer esse comportamento. O fluxo com arquivos em `missões/orquestracao/` funciona em qualquer versão e já entrega o resultado esperado.

---

## Erros comuns e diagnóstico

**Abrir muitas sessões sem coordenação.**  
Resposta: "Mais agentes sem papel claro só criam ruído. Vamos reduzir para dois papéis e um revisor."

**Todos os papéis produzem a mesma coisa.**  
Os prompts estão vagos. Diferencie fonte, saída e critério de qualidade.

**A síntese inventa conexão entre entregas.**  
Peça para citar qual arquivo sustenta cada conclusão.

**O aluno perde arquivos.**  
Padronize nomes: `01-pesquisa.md`, `02-analise.md`, `03-rascunho.md`, `04-sintese.md`.

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre tarefa escolhida, papéis usados, onde a coordenação funcionou e onde houve confusão.

**Cérebro:** esta missão pode alimentar:

- `cérebro/profissional/processos-recorrentes.md`
- `cérebro/departamento/criterios-de-qualidade.md`
