# Módulo: Orquestração

**Nível:** eletiva avançada · **Pré:** 01, 02, pelo menos uma missão real · **Tempo típico:** 45 min  
**Resultado:** o aluno entende como dividir trabalho entre agentes, sessões ou threads, mantendo coordenação, evidência e revisão humana.

## Conceito em 1 minuto

Orquestrar é deixar de pedir "faça tudo" e passar a desenhar papéis. Um agente pesquisa, outro organiza dados, outro escreve, outro revisa. O valor não está em abrir muitas conversas, mas em coordenar entregas com critérios claros.

Analogia de negócio: você não coloca cinco pessoas numa sala sem pauta. Você define papéis, prazo, formato de entrega e quem decide.

## Missão guiada

### Ato 1: escolher uma tarefa com partes independentes

Peça ao aluno uma tarefa real que tenha pelo menos três partes, por exemplo:

- preparar reunião com cliente
- revisar relatório mensal
- comparar fornecedores
- montar plano de ação de uma não conformidade
- transformar ideias de campanha em calendário

**Verificação:** cada parte pode ser feita sem depender completamente das outras.

### Ato 2: desenhar papéis

Crie uma tabela com:

| Papel | O que entrega | Fonte | Critério de qualidade |
|---|---|---|---|
| Pesquisador | fatos e fontes | web, arquivos, mensagens | links e data |
| Analista | padrões e riscos | dados ou relatório | critérios explícitos |
| Redator | versão clara | síntese dos demais | tom aprovado |
| Revisor | falhas e lacunas | entrega final | lista de ajustes |

Adapte os papéis ao caso do aluno.

### Ato 3: executar em pequena escala

<!-- @codex -->
No Codex, use subagentes quando a tarefa for técnica ou tiver pesquisa paralela. Para prática visual, o aluno pode usar threads separadas nomeadas por papel. Coordenação inter-thread só deve ser usada se estiver disponível no app atual; caso contrário, cada thread salva sua entrega em `missões/orquestracao/`.
<!-- @/codex -->
<!-- @claude -->
No Claude Code, use subagentes e agent teams quando disponíveis para gabaritos, pesquisa e revisão. Para a prática do aluno, prefira sessões separadas nomeadas por papel e entregas salvas em `missões/orquestracao/`.
<!-- @/claude -->

Passe a missão:

> "Divida esta tarefa em três papéis. Para cada papel, escreva o prompt que eu devo usar, o arquivo de saída esperado e o critério de revisão. Não execute ainda."

**Verificação:** os prompts não se sobrepõem demais.

### Ato 4: síntese

Depois de uma ou duas entregas, peça:

> "Leia as entregas dos papéis em `missões/orquestracao/`. Produza uma síntese executiva com decisões, riscos, dúvidas abertas e próximo passo recomendado."

## Variações por função

| Área | Orquestração útil |
|---|---|
| Financeiro | Agente de dados, agente de variações, agente de explicação executiva |
| Comercial | Agente de pesquisa do cliente, agente de proposta, agente de objeções |
| Operações | Agente de causa raiz, agente de plano de ação, agente de checagem de risco |
| Marketing | Agente de pesquisa, agente de calendário, agente de revisão de marca |
| RH | Agente de benchmark, agente de política, agente de perguntas frequentes |
| Holding | Agentes por empresa ou por indicador, com síntese única no final |

## Aprofundamento

Quando a orquestração funcionar bem, transforme o fluxo em skill no módulo 99. O sinal de maturidade é quando o aluno consegue dizer: "sempre que eu fizer este trabalho, estes são os papéis, arquivos e critérios".

## Erros comuns e diagnóstico

**Abrir muitas sessões sem coordenação.**  
Resposta: "Mais agentes sem papel claro só criam ruído. Vamos reduzir para dois papéis e um revisor."

**Todos os papéis produzem a mesma coisa.**  
Os prompts estão vagos. Diferencie fonte, saída e critério de qualidade.

**A síntese inventa conexão entre entregas.**  
Peça para citar qual arquivo sustenta cada conclusão.

**O aluno perde arquivos.**  
Padronize nomes: `01-pesquisa.md`, `02-analise.md`, `03-rascunho.md`, `04-sintese.md`.

## Registro

**Diário (`tutor/DIARIO.md`):** registre tarefa escolhida, papéis usados, onde a coordenação funcionou e onde houve confusão.

**Cérebro:** esta missão pode alimentar:

- `cérebro/profissional/processos-recorrentes.md`
- `cérebro/departamento/criterios-de-qualidade.md`
