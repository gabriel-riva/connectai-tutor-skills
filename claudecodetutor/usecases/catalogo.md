# Catálogo de use cases

> **Nota de uso para o tutor:**
> Este catálogo reúne 39 casos de uso organizados por tema e indexados por função de negócio e dificuldade.
> Use-o para:
> - **Montar trilhas de capacitação:** filtre pela função do aluno (ex.: `financeiro`) e escolha casos em ordem crescente de dificuldade.
> - **Puxar exemplos durante missões:** localize o caso mais próximo do problema atual do aluno e adapte o prompt-modelo.
> - **Montar a vitrine personalizada:** selecione 5-8 casos com `Recursos usados` que o aluno já domina e apresente como "o que você já pode fazer hoje".
> - **Identificar quick wins:** priorize casos com dificuldade `iniciante` e recursos `[contexto, arquivos]`.
>
> Cada caso tem um prompt-modelo com placeholders entre colchetes (ex.: `[TIPO DE RELATÓRIO]`). Instrua o aluno a substituir os placeholders antes de enviar.

---

## Índice por função

| Função | Casos (âncoras) |
|--------|----------------|
| **Financeiro** | [Revisão orçamento vs. realizado](#revisão-de-orçamento-vs-realizado), [Projeção de fluxo de caixa](#projeção-de-fluxo-de-caixa), [Modelo de valuation](#modelo-de-valuation-simplificado), [Dashboard de indicadores](#dashboard-de-indicadores-e-relatório-de-análise), [Limpeza de base de dados](#limpeza-e-padronização-de-base-de-dados) |
| **Gestão** | [Briefing de reunião](#briefing-de-preparação-para-reunião), [Atas e desdobramentos de reunião](#atas-e-desdobramentos-de-reunião), [Triagem de caixa de entrada](#triagem-de-caixa-de-entrada-com-rascunhos-na-sua-voz), [Monitoramento de metas](#monitoramento-contínuo-de-metas), [Chefe de gabinete](#chefe-de-gabinete-virtual-thread-duradoura), [Parceiro de raciocínio](#iterar-sobre-problemas-complexos-com-um-parceiro-de-raciocínio) |
| **Operações** | [Análise de exportação de dados](#análise-de-exportação-de-dados-operacionais), [Relatório vivo](#relatório-operacional-que-se-atualiza-sozinho), [Playbook de eventos](#planejamento-e-calendário-de-eventos-de-comunicação), [App interno](#construção-e-implantação-de-app-interno), [Rotinas agendadas](#automação-de-tarefas-recorrentes-via-rotinas), [Documentação de processos](#atualização-de-documentação-de-processos), [Delegação no computador](#delegação-de-tarefas-que-atravessam-aplicativos) |
| **Comercial** | [Síntese de feedbacks de clientes](#síntese-de-feedbacks-de-clientes), [Pesquisa de mercado rápida](#pesquisa-e-relatório-de-mercado-rápido), [Análise de dados de vendas](#análise-de-exportação-de-dados-operacionais), [Triagem de caixa de entrada](#triagem-de-caixa-de-entrada-com-rascunhos-na-sua-voz), [Prova de conceito](#ideia-para-prova-de-conceito-rápida) |
| **Marketing** | [Variações de conteúdo em escala](#geração-de-variações-de-conteúdo-em-escala), [Revisão de tom de marca](#revisão-e-alinhamento-de-tom-de-marca), [Playbook de eventos](#planejamento-e-calendário-de-eventos-de-comunicação), [Case study](#redação-de-case-study-em-tempo-reduzido), [Apresentação de slides](#geração-e-edição-de-apresentação-de-slides), [Melhoria iterativa de artefatos](#melhoria-iterativa-com-critério-de-qualidade-mensurável) |
| **Engenharia / TI** | [App interno](#construção-e-implantação-de-app-interno), [App móvel de campo](#aplicativo-móvel-para-equipes-de-campo), [Ferramenta de linha de comando](#ferramenta-de-linha-de-comando-para-serviços-internos), [Publicação de site](#publicação-de-site-ou-protótipo-com-link-compartilhável), [Missão de longa duração](#missão-de-longa-duração-com-critério-de-conclusão), [Skills reutilizáveis](#criação-de-rotinas-reutilizáveis-para-a-equipe) |
| **RH** | [Triagem de conflitos de interesse](#triagem-automatizada-de-conflitos-de-interesse), [Políticas internas](#redação-de-políticas-e-manuais-internos), [Monitoramento de metas](#monitoramento-contínuo-de-metas), [Tutoria de conceitos](#aprender-um-novo-conceito-com-tutoria-personalizada) |
| **Comex / Jurídico** | [Avaliação de contratos](#avaliação-e-comparação-de-contratos), [Avaliação de privacidade](#avaliação-automatizada-de-impacto-à-privacidade), [Conformidade de materiais](#triagem-de-conformidade-de-materiais-de-comunicação) |
| **Holding / Estratégia** | [Chefe de gabinete](#chefe-de-gabinete-virtual-thread-duradoura), [Monitoramento externo](#monitoramento-externo-contínuo), [Briefing de reunião](#briefing-de-preparação-para-reunião), [Modelo de valuation](#modelo-de-valuation-simplificado), [Síntese de feedbacks](#síntese-de-feedbacks-de-clientes) |
| **Aprendizado** | [Aprender um novo conceito](#aprender-um-novo-conceito-com-tutoria-personalizada), [Parceiro de raciocínio](#iterar-sobre-problemas-complexos-com-um-parceiro-de-raciocínio) |

---

## Casos

### Dados e relatórios

#### Revisão de orçamento vs. realizado

- **O que faz:** Transforma o plano orçamentário, a exportação dos valores realizados e as notas de fechamento em uma planilha de análise de variações, mapeando os lançamentos para as categorias corretas do orçamento e resumindo os maiores desvios em comentários prontos para a liderança.
- **Funções:** financeiro | gestão | holding
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma distribuidora industrial anexa o orçamento anual e o razão do mês e recebe uma planilha editável com as variações por categoria e um resumo dos três maiores desvios com possíveis causas.
- **Recursos usados:** [arquivos, dados]
- **Como pedir:**
  ```
  Atualize a revisão de orçamento vs. realizado a partir dos arquivos anexos: [@orçamento e @realizado].
  Compare o realizado com o plano, mapeie os lançamentos para as categorias corretas do orçamento,
  resuma as principais variações e prepare uma visão limpa de revisão como planilha editável (.xlsx).
  Ao final, escreva [NÚMERO] parágrafos de comentário para a reunião de diretoria.
  ```

---

#### Projeção de fluxo de caixa

- **O que faz:** Constrói uma planilha editável de previsão de fluxo de caixa (13 semanas ou mensal) integrando recebimentos, folha, fornecedores e premissas de capital de giro, com fórmulas conectadas às premissas e sinalização automática do ponto crítico de liquidez.
- **Funções:** financeiro | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma fabricante de equipamentos agrícolas anexa o histórico de entradas e saídas e recebe um modelo de 13 semanas que destaca a semana de menor caixa e alerta quando o saldo projetado fura o limite de segurança.
- **Recursos usados:** [arquivos, contexto, dados]
- **Como pedir:**
  ```
  Construa uma planilha editável de previsão de fluxo de caixa a partir dos arquivos anexos: [@arquivos].
  Inclua: caixa inicial, recebimentos esperados, folha de pagamento, pagamentos a fornecedores,
  dívidas, impostos e investimentos, com as premissas de prazos que estão nos dados.
  Preserve a cadência dos dados de origem ([semanal/mensal]).
  Inclua uma visão-resumo que destaque o ponto mais baixo de liquidez, o saldo mínimo final
  e qualquer violação do limite de segurança de [VALOR]. Use fórmulas para que eu possa testar cenários.
  ```

---

#### Modelo de valuation simplificado

- **O que faz:** Converte demonstrações financeiras históricas e premissas de avaliação em um modelo de fluxo de caixa descontado (DCF) editável em planilha, com drivers operacionais explícitos, custo de capital, valor terminal e análise de sensibilidade.
- **Funções:** financeiro | holding
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma holding que avalia a aquisição de uma empresa de logística anexa os balanços dos últimos anos e recebe um modelo DCF completo em planilha, com drivers de receita, margem e capex que pode ajustar célula a célula.
- **Recursos usados:** [arquivos, contexto, dados]
- **Como pedir:**
  ```
  Construa um modelo DCF em planilha para a empresa dos arquivos anexos: [@demonstrações financeiras].
  Inclua drivers operacionais explícitos para crescimento de receita, margens, capex e capital de giro.
  Calcule o fluxo de caixa livre desalavancado, o custo médio ponderado de capital (use [%] como base),
  o valor terminal e o valor da empresa. Adicione uma tabela de sensibilidade variando crescimento
  e taxa de desconto. Gere o resultado como planilha editável (.xlsx).
  ```

---

#### Dashboard de indicadores e relatório de análise

- **O que faz:** Transforma exportações brutas de dados (ERP, planilhas internas) em um painel de indicadores-chave com fórmulas e comentários interpretativos. Variação: empacotar a análise como relatório formal (documento ou PDF) com gráficos e conclusões para distribuição a stakeholders.
- **Funções:** financeiro | operações | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma metalúrgica exporta o relatório mensal do ERP e recebe um dashboard com margem bruta, giro de estoque e prazo médio de recebimento, mais um relatório em PDF com a análise interpretada para a diretoria.
- **Recursos usados:** [arquivos, dados, contexto]
- **Como pedir:**
  ```
  Aqui está minha exportação de dados do [SISTEMA/ERP] referente a [PERÍODO]: [cole ou @arquivo].
  Antes de analisar, inspecione as colunas e me diga o que encontrou.
  Monte um dashboard com os seguintes indicadores: [liste os KPIs desejados].
  Depois, gere um relatório de análise com gráficos e um parágrafo de interpretação
  para cada indicador, em formato [planilha/documento/PDF].
  ```

---

#### Limpeza e padronização de base de dados

- **O que faz:** Recebe uma planilha com dados sujos (datas em formatos mistos, valores monetários inconsistentes, duplicatas, apelidos de categorias, linhas de resumo misturadas) e devolve uma cópia limpa, preservando o arquivo original intacto e anexando uma nota de qualidade com tudo o que foi alterado.
- **Funções:** financeiro | operações | comercial | RH
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma fábrica de equipamentos consolida cadastros de clientes de três fontes com formatações distintas e recebe a base unificada mais uma nota listando as linhas alteradas, removidas e as que não puderam ser corrigidas com confiança.
- **Recursos usados:** [arquivos, dados]
- **Como pedir:**
  ```
  Limpe a base de dados [@arquivo]. O que está errado:
  - [ex.: datas misturadas entre DD/MM/AAAA e AAAA-MM-DD]
  - [ex.: valores monetários com R$, pontos e células em branco]
  - [ex.: linhas duplicadas vindas de exportações repetidas]
  - [ex.: nomes de categorias com vários apelidos]
  O que eu quero: gravar um arquivo limpo SEM alterar o original, usar um único formato de data,
  preservar os IDs de origem e gerar uma nota curta de qualidade de dados com as linhas
  que você alterou, removeu ou não conseguiu limpar com confiança.
  ```

---

#### Análise de exportação de dados operacionais

- **O que faz:** Responde perguntas de negócio sobre arquivos de dados (CSV, planilhas, exportações de dashboards): inspeciona as colunas, executa os cálculos e entrega a resposta acompanhada de uma visualização simples que pode ser aberta no navegador.
- **Funções:** operações | comercial | financeiro | engenharia
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um gerente comercial de uma distribuidora anexa a exportação de pedidos do trimestre, pergunta "qual segmento de clientes mais mudou em relação ao trimestre anterior?" e recebe a resposta com um gráfico interativo.
- **Recursos usados:** [arquivos, dados, contexto]
- **Como pedir:**
  ```
  Analise [@arquivo de exportação].
  Pergunta: [PERGUNTA DE NEGÓCIO, ex.: qual segmento de clientes mais mudou no último trimestre?]
  Por favor: inspecione as colunas antes de analisar, responda a pergunta a partir dos dados
  e crie uma visualização simples em HTML que eu possa abrir no navegador.
  Ao final, destaque os [NÚMERO] insights mais relevantes.
  ```

---

#### Pesquisa e relatório de mercado rápido

- **O que faz:** Pesquisa na web informações sobre um segmento ou concorrente e consolida um relatório estruturado com tendências, players relevantes e oportunidades identificadas, sempre com as fontes citadas.
- **Funções:** comercial | marketing | holding | gestão
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma empresa de purificadores industriais pede um mapeamento dos principais concorrentes nacionais com comparativo de posicionamento e faixa de preço.
- **Recursos usados:** [web, contexto]
- **Como pedir:**
  ```
  Pesquise na web sobre [TEMA/SEGMENTO/CONCORRENTE].
  Quero entender: (1) principais players e posicionamento, (2) tendências do setor em [ANO],
  (3) oportunidades ou ameaças para uma empresa como [DESCRIÇÃO DA EMPRESA].
  Consolide em um relatório de no máximo [NÚMERO] páginas com fontes citadas.
  ```

---

### Documentos e comunicação

#### Briefing de preparação para reunião

- **O que faz:** Reúne o contexto espalhado (convite da agenda, documentos, conversas da equipe, e-mails) e monta um pacote de preparação com objetivo da reunião, contexto dos participantes, fatos respaldados pelas fontes, agenda provável, perguntas em aberto e um modelo de anotações.
- **Funções:** gestão | holding | comercial
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um diretor de uma holding prepara a revisão trimestral com os gerentes das unidades e recebe um briefing que separa o que está respaldado por documentos do que é suposição, com as três perguntas que deve fazer a cada um.
- **Recursos usados:** [contexto, arquivos, e-mail]
- **Como pedir:**
  ```
  Me ajude a preparar a reunião [NOME] do dia [DATA]. Use apenas estas fontes:
  [evento da agenda, documentos/notas, conversas da equipe, threads de e-mail].
  Primeiro, faça um inventário das fontes acessíveis e aponte as lacunas.
  Devolva: objetivo da reunião, contexto dos participantes, fatos-chave respaldados pelas fontes,
  agenda provável, perguntas em aberto, decisões pendentes e um modelo de anotações.
  Mantenha afirmações sem respaldo em uma lista separada. Não atualize nem compartilhe nada sem minha aprovação.
  ```

---

#### Atas e desdobramentos de reunião

- **O que faz:** Converte a transcrição ou o resumo automático de uma reunião em todos os desdobramentos de uma vez: ata formatada, e-mail de follow-up para o cliente, atualização de registro comercial (notas, riscos, próximos passos, responsáveis) e mensagem de resumo para a equipe.
- **Funções:** gestão | operações | comercial | holding
- **Dificuldade:** iniciante
- **Exemplo setorial:** Após uma visita técnica, a gerente de contas de uma fabricante de implementos cola a transcrição da call e recebe o e-mail de follow-up para o cliente, a atualização para o CRM e o resumo para o grupo interno, tudo como rascunho para revisão.
- **Recursos usados:** [contexto, arquivos, e-mail]
- **Como pedir:**
  ```
  Use a transcrição/resumo da minha reunião com [CLIENTE/CONTA]: [cole o texto].
  Aponte qualquer informação que estiver faltando antes de redigir.
  Resuma os principais pontos, decisões, riscos, oportunidades e ações combinadas. Depois rascunhe:
  - um e-mail de follow-up para o cliente
  - uma atualização para o [CRM/sistema] com notas, riscos, próximos passos e responsáveis
  - uma mensagem para [equipe/grupo] com os pontos mais importantes
  Tudo como rascunho. Não envie nada sem minha aprovação.
  ```

---

#### Redação de case study em tempo reduzido

- **O que faz:** Estrutura e redige um estudo de caso a partir de notas brutas, entrevistas ou bullet points, reduzindo o tempo de produção de 2-3 horas para menos de 30 minutos.
- **Funções:** marketing | comercial
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um analista de marketing de uma empresa de equipamentos elevatórios tem notas de entrevista com o cliente e recebe um case completo com estrutura (desafio, solução, resultado) pronto para publicação.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Preciso redigir um case study sobre [CLIENTE/PROJETO].
  Tenho estas informações brutas: [cole notas, e-mails ou bullet points].
  Estruture em: (1) contexto e desafio, (2) solução implementada, (3) resultados mensuráveis.
  Tom: [profissional/técnico/acessível]. Extensão: [NÚMERO] palavras.
  ```

---

#### Redação de políticas e manuais internos

- **O que faz:** Transforma práticas informais ou rascunhos em documentos de política estruturados, com linguagem clara, seções padronizadas e exemplos práticos.
- **Funções:** RH | gestão | operações | jurídico
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma empresa do setor avícola precisa formalizar sua política de uso de equipamentos de proteção individual e recebe um documento estruturado com escopo, responsabilidades, procedimentos e penalidades.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Preciso criar/atualizar a política de [TEMA] da nossa empresa.
  Contexto: [descreva o setor, porte da empresa, práticas atuais].
  Rascunho ou tópicos a incluir: [liste ou cole].
  Formate como documento formal com: objetivo, escopo, responsabilidades,
  procedimento passo a passo e revisão/vigência.
  ```

---

#### Avaliação e comparação de contratos

- **O que faz:** Analisa versões de contratos, destaca alterações relevantes, identifica cláusulas de risco e sugere linguagem alternativa baseada em boas práticas comerciais.
- **Funções:** comex | jurídico | gestão | holding
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma empresa de comércio exterior recebe uma proposta de contrato de fornecedor internacional e obtém em minutos uma análise dos riscos jurídicos e comerciais com sugestões de redação para as cláusulas problemáticas.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Analise este contrato de [TIPO DE CONTRATO]: [cole o texto ou @arquivo].
  Contexto: somos [DESCRIÇÃO DA EMPRESA], e este contrato é para [FINALIDADE].
  Identifique: (1) cláusulas com risco para nós, (2) pontos omissos relevantes,
  (3) sugestões de redação alternativa para os 3 maiores riscos identificados.
  ```

---

#### Triagem de conformidade de materiais de comunicação

- **O que faz:** Avalia materiais de marketing ou comunicação antes de publicação, verificando potenciais problemas de direitos autorais, afirmações exageradas, precisão estatística e alinhamento com políticas internas, reduzindo o ciclo de revisão de dias para horas.
- **Funções:** marketing | comex | jurídico
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma empresa do setor de purificadores de água verifica automaticamente se os materiais de campanha não fazem afirmações de saúde que possam gerar problemas regulatórios antes do envio à agência.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Revise este material de comunicação antes de publicarmos: [cole o texto ou @arquivo].
  Critérios de verificação: [descreva as políticas, ex.: afirmações técnicas precisam de respaldo,
  não citar concorrentes por nome, seguir diretrizes do setor].
  Indique cada problema encontrado, o risco associado e uma sugestão de correção.
  ```

---

#### Avaliação automatizada de impacto à privacidade

- **O que faz:** Gera documentos de avaliação de impacto à privacidade (PIA/LGPD) a partir de um template e das informações sobre o processo ou sistema em análise, reduzindo a redação manual repetitiva.
- **Funções:** jurídico | operações | engenharia
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma empresa que está implantando um novo sistema de monitoramento de produção precisa documentar os impactos à privacidade dos colaboradores para conformidade com a LGPD.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Preciso de uma Avaliação de Impacto à Privacidade (PIA) para o seguinte processo/sistema:
  Nome: [NOME DO PROCESSO]
  Dados pessoais envolvidos: [liste os tipos de dados]
  Finalidade do tratamento: [descreva]
  Compartilhamento externo: [sim/não, com quem]
  Segurança aplicada: [descreva medidas existentes]
  Use o modelo padrão LGPD e preencha todas as seções.
  ```

---

### Reuniões e agenda

#### Síntese de feedbacks de clientes

- **O que faz:** Centraliza feedbacks espalhados por canais de chat, pesquisas, registros de chamados e documentos em uma planilha de revisão: agrupa os temas repetidos, inclui o link ou ID de origem de cada item, marca o nível de confiança e aponta o que exige desdobramento de produto ou operação.
- **Funções:** comercial | marketing | gestão | holding
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um gerente comercial de uma empresa de implementos rodoviários reúne feedbacks de 80 clientes vindos de pesquisa, chamados e conversas e recebe uma planilha que agrupa os temas, aponta os três problemas mais críticos e indica quem deve tratar cada um.
- **Recursos usados:** [arquivos, dados, contexto]
- **Como pedir:**
  ```
  Sintetize os feedbacks sobre [PRODUTO/ÁREA] em uma planilha de revisão. Use estas fontes:
  - [canal/threads de chat da equipe]
  - [exportação de pesquisa, planilha de chamados ou documentos]
  Na planilha: agrupe feedbacks repetidos, inclua o link ou ID de origem de cada item,
  marque o nível de confiança e destaque quais itens precisam de desdobramento
  de [produto/operação/comercial].
  ```

---

#### Planejamento e calendário de eventos de comunicação

- **O que faz:** Cria um playbook de evento ou lançamento respaldado pelas fontes de planejamento, separando claramente o material voltado ao público (textos, convites) do checklist operacional privado, com mapa de responsáveis e plano de suporte.
- **Funções:** marketing | operações | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma empresa de equipamentos para avicultura organiza o lançamento de um produto em feira setorial e recebe o playbook dividido em: textos para visitantes, checklist interno de estande, mapa de quem cuida do quê e plano de plantão.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Crie um playbook respaldado em fontes para [EVENTO/LANÇAMENTO].
  Fontes: [decisões do grupo da equipe, documentos de planejamento, agenda, planilha de tarefas].
  Divida a saída em: (1) textos voltados ao público, (2) checklist operacional privado,
  (3) mapa de responsáveis, (4) plano de suporte durante o evento.
  Não publique nada nem presuma detalhes que estiverem faltando: liste as lacunas.
  ```

---

#### Triagem automatizada de conflitos de interesse

- **O que faz:** Analisa formulários de declaração de atividades externas de colaboradores e gera recomendações sobre potenciais conflitos, eliminando a necessidade de entrevistas iniciais repetitivas.
- **Funções:** RH | jurídico | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma holding com múltiplas subsidiárias padroniza a triagem de declarações de conflito de interesse dos gerentes, recebendo um parecer inicial automático para revisão do departamento jurídico.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Analise esta declaração de atividades externas do colaborador: [cole o formulário preenchido].
  Políticas internas aplicáveis: [descreva as regras ou cole o documento de política].
  Gere: (1) avaliação de risco (baixo/médio/alto) com justificativa,
  (2) perguntas adicionais para esclarecimento, (3) recomendação de aprovação ou revisão.
  ```

---

#### Triagem de caixa de entrada com rascunhos na sua voz

- **O que faz:** Varre a caixa de entrada, identifica o que precisa de resposta e rascunha as respostas imitando o estilo de escrita do usuário, calibrado a partir de e-mails enviados anteriormente. Os rascunhos ficam salvos para revisão: nada é enviado automaticamente.
- **Funções:** gestão | comercial | holding
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um diretor comercial de uma fábrica de equipamentos volta de dois dias de viagem, pede a triagem da caixa de entrada e encontra os rascunhos das oito respostas pendentes já no seu tom de escrita, prontos para ajustar e enviar.
- **Recursos usados:** [e-mail, arquivos, contexto]
- **Como pedir:**
  ```
  Verifique meu e-mail, identifique o que preciso responder e escreva rascunhos na minha voz.
  Use minhas respostas enviadas recentes ou [exemplos de textos meus] como referência de tom.
  Priorize: [ex.: clientes externos primeiro, depois interno].
  Deixe tudo como rascunho. Liste o que você decidiu NÃO responder e por quê.
  ```

---

### Apresentações e visual

#### Geração e edição de apresentação de slides

- **O que faz:** Cria apresentações novas ou edita arquivos de slides existentes (.pptx) com regras de layout repetíveis: aplica logotipo em todas as lâminas, gera ilustrações com direção visual consistente, mantém textos editáveis e gráficos nativos e roda verificações de estouro de texto e fontes antes da entrega.
- **Funções:** gestão | marketing | comercial | holding
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um diretor de operações de uma fábrica de plásticos entrega o deck do trimestre anterior e os dados novos, e recebe a apresentação atualizada com a mesma identidade visual, gráficos editáveis e sem textos estourando as caixas.
- **Recursos usados:** [arquivos, slides, imagens]
- **Como pedir:**
  ```
  Edite esta apresentação [@arquivo.pptx] da seguinte forma:
  - Adicione [logo.png] no canto [POSIÇÃO] de todos os slides
  - [Gere ilustrações em estilo [ESTILO] para os slides [NÚMEROS]]
  - Adicione novos slides sobre [TEMA] seguindo a identidade visual existente
  Mantenha os textos editáveis e os gráficos como elementos nativos da apresentação.
  Renderize o resultado em imagens para revisão e corrija problemas de layout.
  Rode verificações de estouro de texto e de fontes antes de finalizar.
  ```

---

#### Geração de variações de conteúdo em escala

- **O que faz:** Cria múltiplas versões de textos de comunicação (anúncios, e-mails, posts) a partir de um briefing, mantendo a voz da marca e validando restrições de formato (limites de caracteres, tom).
- **Funções:** marketing | comercial
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma empresa de trailers off-road precisa de 10 variações de headline para uma campanha digital e recebe todas as variações em menos de um minuto, já validadas quanto ao limite de 90 caracteres do canal.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Crie [NÚMERO] variações de [TIPO DE CONTEÚDO: headline, e-mail, post, legenda] para [PRODUTO/CAMPANHA].
  Público-alvo: [descreva]. Tom desejado: [ex.: técnico, descontraído, urgente].
  Restrições: [limite de caracteres, palavras proibidas, formato obrigatório].
  Guia de voz da marca: [cole ou descreva].
  Entregue em tabela com numeração para facilitar a seleção.
  ```

---

#### Revisão e alinhamento de tom de marca

- **O que faz:** Revisa textos existentes e os reescreve no tom de voz definido pela marca, com explicação das alterações para que o time aprenda os padrões.
- **Funções:** marketing | RH | gestão
- **Dificuldade:** iniciante
- **Exemplo setorial:** Uma distribuidora de empilhadeiras percebe inconsistência no tom dos e-mails de pós-venda e usa a ferramenta para padronizar toda a base de templates em um único tom consultivo.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Revise e reescreva estes textos no tom de voz da nossa marca: [cole os textos ou @arquivo].
  Guia de tom: [descreva ou cole o guia de comunicação].
  Para cada texto, entregue: (1) versão reescrita, (2) lista das principais mudanças feitas
  e (3) regra de tom ilustrada por cada mudança.
  ```

---

### Automação e rotinas

#### Monitoramento contínuo de metas

- **O que faz:** Mantém uma thread persistente que acompanha metas definidas pelo usuário, compara com o progresso atual em cada sessão e gera alertas quando há desvio relevante.
- **Funções:** gestão | financeiro | RH | operações
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um gerente de vendas mantém uma conversa aberta onde registra as metas mensais da equipe e, a cada semana, cola os resultados parciais para receber um diagnóstico de quem está no caminho e quem precisa de atenção.
- **Recursos usados:** [contexto, arquivos, dados]
- **Como pedir:**
  ```
  [Na primeira mensagem da thread:]
  Vou usar esta conversa para monitorar as metas de [ÁREA] em [PERÍODO].
  Metas definidas: [liste com indicador, meta numérica e responsável].
  Cada semana trarei os resultados parciais. Avise sempre quando alguma meta estiver
  em risco (realizado abaixo de [%] do previsto) e sugira ação.

  [Nas mensagens seguintes:]
  Atualização de [DATA]: [cole os dados do período].
  ```

---

#### Missão de longa duração com critério de conclusão

- **O que faz:** Define um objetivo durável que o assistente persegue por conta própria ao longo de várias horas ou etapas, sem parar a cada passo para pedir confirmação, até atingir um estado final verificável combinado de antemão (o "contrato de pronto").
- **Funções:** engenharia | operações | gestão
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma equipe de TI de uma indústria define a missão "migrar todos os relatórios da planilha antiga para o novo padrão, validando cada um" e deixa o agente trabalhar até que a verificação automática confirme que os 40 relatórios foram convertidos.
- **Recursos usados:** [automação, arquivos, contexto]
- **Como pedir:**
  ```
  Trabalhe no seguinte objetivo sem parar até atingir o estado final verificável:
  Objetivo: [DESCREVA A MISSÃO, ex.: converter todos os arquivos da pasta X para o padrão Y].
  Estado final verificável: [COMO SABER QUE TERMINOU, ex.: todos os arquivos passam na verificação Z].
  Antes de começar: defina os pontos de checagem intermediários e o comando ou critério
  que valida o progresso. Registre o avanço a cada etapa concluída.
  ```

---

#### Automação de tarefas recorrentes via rotinas

- **O que faz:** Configura uma rotina que executa autonomamente em horário programado (diário, semanal, mensal), processa dados ou documentos e entrega um resumo pronto sem intervenção manual.
- **Funções:** operações | gestão | financeiro
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma empresa de loteamentos configura uma rotina semanal que consolida automaticamente as planilhas de obras em andamento e envia um resumo de status para os gestores todas as segundas-feiras antes das 8h.
- **Recursos usados:** [automação, arquivos, dados]
- **Como pedir:**
  ```
  Quero criar uma rotina automática que execute [FREQUÊNCIA: diariamente/semanalmente/mensalmente].
  Tarefa: [descreva o que deve ser feito, ex.: consolidar relatórios, verificar indicadores, enviar resumo].
  Fontes de dados: [descreva os arquivos ou sistemas envolvidos].
  Entregável esperado: [ex.: e-mail de resumo, arquivo atualizado, alerta se desvio > X%].
  A rotina roda sozinha, então seja explícito: defina o que é sucesso e o que fazer com o resultado.
  Configure a rotina com estas instruções e me mostre como ativá-la.
  ```

---

#### Criação de rotinas reutilizáveis para a equipe

- **O que faz:** Transforma um fluxo de trabalho que deu certo (inclusive uma conversa inteira que funcionou bem) em uma habilidade reutilizável que qualquer pessoa da equipe invoca com um comando, preservando instruções, critérios e exemplos para garantir consistência.
- **Funções:** gestão | engenharia | operações
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma metalúrgica percebe que a conversa usada para gerar o relatório mensal ficou perfeita e a converte em um comando `/relatorio-mensal` que qualquer analista executa, sempre com o mesmo formato e indicadores.
- **Recursos usados:** [automação, arquivos, contexto]
- **Como pedir:**
  ```
  Crie uma habilidade reutilizável chamada /[NOME] para o seguinte processo:
  O que faz: [descreva passo a passo, OU diga "use esta conversa como exemplo do fluxo que funcionou"].
  Entradas necessárias do usuário: [liste os dados ou arquivos que devem ser fornecidos].
  Entregável esperado: [descreva o resultado].
  Mantenha as instruções concisas, valide o resultado com um teste
  e me explique como salvar para que a equipe toda possa usar.
  ```

---

#### Atualização de documentação de processos

- **O que faz:** Compara documentos de processo com a realidade atual da operação, identifica o que ficou desatualizado, atualiza somente o necessário preservando a estrutura existente e gera a versão revisada para validação humana antes de publicar.
- **Funções:** operações | engenharia | RH | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma fábrica de componentes metálicos percebe que seus POPs não refletem as mudanças de linha dos últimos dois anos e usa a ferramenta para identificar os trechos desatualizados e propor revisões mantendo o formato padrão da empresa.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Atualize a documentação de [PROCESSO/ÁREA] com base nestas fontes:
  documento atual [@arquivo], e o que mudou: [descreva as mudanças ou cole notas].
  Identifique o que está desatualizado, atualize SOMENTE o necessário,
  preserve a estrutura e as referências cruzadas existentes
  e mantenha detalhes internos sensíveis fora de versões públicas.
  Entregue a versão revisada com um resumo das alterações para eu validar.
  ```

---

#### Delegação de tarefas que atravessam aplicativos

- **O que faz:** Controla o computador do usuário (clica, digita e navega como uma pessoa faria) para completar tarefas que atravessam vários aplicativos: ler mensagens, verificar a agenda, pesquisar opções e rascunhar respostas, sempre confirmando antes de concluir ações definitivas.
- **Funções:** gestão | operações | comercial
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um gestor de uma distribuidora pede: "veja as mensagens do cliente X, confira minha agenda, proponha dois horários de visita e rascunhe a resposta na mesma conversa", e revisa o rascunho pronto minutos depois.
- **Recursos usados:** [computador, contexto]
- **Como pedir:**
  ```
  Veja minhas mensagens de [PESSOA/CLIENTE] no [APLICATIVO].
  Verifique minha disponibilidade na agenda, [pesquise/prepare o que for necessário,
  ex.: encontre 2 opções de local, levante os dados do pedido]
  e rascunhe uma resposta na mesma conversa.
  Confirme comigo antes de concluir qualquer [envio/reserva/compra].
  ```

---

#### Melhoria iterativa com critério de qualidade mensurável

- **O que faz:** Executa um ciclo de melhoria contínua sobre um artefato (texto, planilha, página, material visual): faz uma melhoria focada por vez, reavalia com um critério de pontuação combinado, registra o que mudou e segue iterando até atingir a nota-alvo.
- **Funções:** marketing | operações | engenharia
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma equipe de marketing industrial define um checklist de qualidade para páginas de produto (clareza, completude técnica, chamada para ação) e deixa o agente iterar sobre as 15 páginas do catálogo até todas passarem com nota acima de 90%.
- **Recursos usados:** [arquivos, dados, automação]
- **Como pedir:**
  ```
  Tenho uma tarefa difícil e quero que você a execute como um ciclo de melhoria guiado por avaliação.
  Artefato: [@arquivo ou descrição]. Critério de pontuação: [descreva o checklist ou regra de nota].
  Ciclo: faça UMA melhoria focada por vez, reavalie com o critério após cada mudança,
  registre a pontuação e o que mudou, e inspecione o resultado diretamente
  (se for visual, olhe a imagem renderizada).
  Continue até a pontuação passar de [META, ex.: 90%].
  ```

---

### Construção de apps e sites

#### Ideia para prova de conceito rápida

- **O que faz:** Transforma uma ideia em protótipo funcional em duas etapas: primeiro gera um mockup visual de alta qualidade da interface para alinhar a direção, depois implementa a versão funcional e a verifica abrindo no navegador de verdade.
- **Funções:** gestão | engenharia | operações | comercial
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um gerente de operações de uma empresa de movimentação de cargas quer testar uma calculadora de capacidade por área de armazém: aprova primeiro o mockup visual e recebe o protótipo funcional verificado em menos de uma hora.
- **Recursos usados:** [contexto, imagens, automação]
- **Como pedir:**
  ```
  Gere primeiro um mockup visual de alta qualidade da interface para a seguinte ideia,
  e depois de eu aprovar, implemente a versão funcional:
  Ideia: [descreva a ferramenta, o usuário-alvo e o fluxo principal].
  Entradas: [o que o usuário fornece]. Saída esperada: [o que a ferramenta mostra ou faz].
  Ao final, abra o resultado no navegador e verifique se o fluxo principal funciona.
  ```

---

#### Construção e implantação de app interno

- **O que faz:** Constrói, testa e implanta um aplicativo web interno completo (formulários, dashboards, fluxos de aprovação) com banco de dados para informações estruturadas, armazenamento para arquivos enviados e acesso restrito aos usuários da organização.
- **Funções:** engenharia | operações | gestão
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma empresa de urbanização cria um app interno de acompanhamento de obras com formulários de vistoria, upload de fotos e painel de status, disponível para todos os colaboradores autenticados, sem montar infraestrutura própria.
- **Recursos usados:** [contexto, arquivos, automação, web]
- **Como pedir:**
  ```
  Construa e implante um app interno para [EQUIPE/PROCESSO].
  Objetivo: [o que o app deve ajudar as pessoas a fazer] | Usuários: [quem usa].
  Fontes que você deve consultar: [documentos, dados ou serviços conectados].
  Requisitos: mantenha a primeira versão focada em UM fluxo útil;
  use banco de dados para informações estruturadas e armazenamento para arquivos enviados;
  teste o fluxo principal, a persistência e o layout responsivo antes de implantar.
  Disponibilize para todos os usuários da organização.
  ```

---

#### Aplicativo móvel para equipes de campo

- **O que faz:** Cria um aplicativo móvel multiplataforma a partir da descrição da ideia, do público e do fluxo principal, permitindo testar no celular em minutos antes de investir em desenvolvimento formal.
- **Funções:** engenharia | operações
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma fabricante de equipamentos para granjas prototipa um app de checklist de instalação para os técnicos de campo registrarem fotos e medições direto do celular, testável no aparelho no mesmo dia.
- **Recursos usados:** [contexto, automação]
- **Como pedir:**
  ```
  Construa um aplicativo móvel para esta ideia:
  [descreva a ideia, os usuários-alvo e o fluxo principal de uso].
  Requisitos: comece pelas convenções padrão da plataforma de desenvolvimento móvel;
  priorize uma versão testável rapidamente no aparelho antes de qualquer build complexo.
  Funcionalidades da primeira versão: [liste 2-3 essenciais].
  ```

---

#### Ferramenta de linha de comando para serviços internos

- **O que faz:** Cria uma ferramenta de linha de comando que conecta o assistente a um serviço da empresa (sistema de chamados, API interna, fonte de logs, repositório de relatórios), permitindo que tarefas repetidas com esse serviço sejam executadas sem reexplicar a integração a cada conversa.
- **Funções:** engenharia
- **Dificuldade:** avançado
- **Exemplo setorial:** A equipe de TI de uma indústria cria uma ferramenta de linha de comando para consultar o sistema de chamados interno, e a partir daí qualquer conversa pode pesquisar, ler e classificar chamados diretamente.
- **Recursos usados:** [automação, contexto, arquivos]
- **Como pedir:**
  ```
  Crie uma ferramenta de linha de comando que você mesmo possa usar nas próximas conversas,
  e a habilidade complementar que ensina quando usá-la.
  Fonte: [URL da documentação ou especificação da API do serviço].
  Primeira tarefa que ela deve resolver: [ex.: buscar chamados abertos, baixar logs de erro].
  Nome do comando: [NOME]. Antes de programar, mostre a proposta de comandos
  e pergunte só o que estiver faltando.
  ```

---

#### Publicação de site ou protótipo com link compartilhável

- **O que faz:** Transforma um repositório, screenshot, design ou ideia em um site funcional e o publica em um ambiente de pré-visualização com URL ativa, pronto para colher feedback de colegas e clientes sem configuração manual de servidores.
- **Funções:** engenharia | marketing | comercial
- **Dificuldade:** intermediário
- **Exemplo setorial:** O time comercial de uma fabricante de purificadores precisa de uma landing page para uma feira em dois dias: descreve o conteúdo, recebe o site publicado com URL de pré-visualização e circula o link para aprovação interna.
- **Recursos usados:** [contexto, arquivos, web, automação]
- **Como pedir:**
  ```
  Transforme [repositório, screenshot, design ou ideia] em um site funcional
  e publique uma pré-visualização me entregando a URL ativa.
  Contexto: [o que o site deve fazer] | Fontes: [dados, documentos ou imagens a usar].
  Restrições: [estilo, identidade visual, o que NÃO mudar].
  Antes de me entregar, rode a build local e verifique que a publicação está no ar.
  ```

---

### Aprendizado e capacitação

#### Aprender um novo conceito com tutoria personalizada

- **O que faz:** Transforma material denso (relatório técnico, norma, artigo) em um relatório de aprendizado claro e reutilizável: resumo executivo, glossário, passo a passo guiado, mapa de conceitos com diagramas e separação explícita entre o que a fonte afirma e o que é interpretação.
- **Funções:** gestão | financeiro | RH | operações
- **Dificuldade:** iniciante
- **Exemplo setorial:** Um supervisor de produção de uma granja precisa entender uma norma técnica nova do setor e recebe um relatório de estudo com glossário, fluxograma das exigências e lista do que muda na prática da operação dele.
- **Recursos usados:** [contexto, arquivos]
- **Como pedir:**
  ```
  Me ajude a aprender [CONCEITO/TEMA] a partir deste material: [cole ou @arquivo].
  Meu perfil: [ex.: gestor de produção sem formação financeira]. Uso pretendido: [FINALIDADE].
  Produza um relatório de estudo com: resumo executivo, glossário dos termos,
  explicação passo a passo com exemplos do meu setor, diagrama dos conceitos principais
  e uma lista separando o que a fonte afirma do que é interpretação sua.
  Ao final, faça 2-3 perguntas para verificar meu entendimento.
  ```

---

#### Iterar sobre problemas complexos com um parceiro de raciocínio

- **O que faz:** Funciona como um "parceiro de pensamento" que ajuda a decompor problemas difíceis, questionar premissas, explorar alternativas e chegar a uma decisão mais robusta do que seria possível sozinho.
- **Funções:** gestão | holding | financeiro | operações
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um sócio de uma holding que enfrenta a decisão de expandir para um novo segmento usa uma sessão prolongada para mapear riscos, questionar premissas otimistas e estruturar os critérios de decisão antes de levar ao conselho.
- **Recursos usados:** [contexto]
- **Como pedir:**
  ```
  Preciso pensar junto contigo sobre [PROBLEMA/DECISÃO].
  O que está em jogo: [descreva o contexto e as alternativas disponíveis].
  Minha visão atual: [explique sua posição inicial].
  Quero que você: (1) questione minhas premissas, (2) apresente contra-argumentos relevantes,
  (3) me ajude a estruturar os critérios de decisão. Não dê a resposta diretamente:
  guie meu raciocínio com perguntas e análises.
  ```

---

## Padrões de threads duráveis

> Estes quatro padrões descrevem configurações de conversa que ganham valor ao longo do tempo, não em uma interação única. O tutor deve apresentá-los como "formas de trabalhar" antes de apresentar os casos individuais que se encaixam em cada padrão.

---

#### Chefe de gabinete virtual (thread duradoura)

- **O que faz:** Mantém uma conversa persistente que monitora as fontes de trabalho do usuário (chat da equipe, e-mail, agenda, documentos e trackers), sintetiza o que precisa de atenção, escala o que é importante ou surpreendente e rascunha as respostas. A regra fundamental: rascunha, NUNCA envia sem aprovação explícita.
- **Funções:** holding | gestão | operações
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um CEO de holding mantém uma thread aberta que toda manhã varre os canais conectados e responde "o que precisa da minha atenção hoje?", com os rascunhos das três respostas mais urgentes já preparados para revisão.
- **Recursos usados:** [contexto, arquivos, e-mail]
- **Como pedir:**
  ```
  Você será meu assistente de gestão nesta conversa de longo prazo.
  Regra fundamental: você pode rascunhar, analisar e alertar, mas NUNCA executar ações
  externas (enviar e-mails, agendar, publicar) sem minha confirmação explícita.
  Fontes que você deve verificar: [chat da equipe, e-mail, agenda, documentos/trackers].
  Comece agora: verifique as fontes e me diga o que precisa da minha atenção,
  procurando por algo importante ou surpreendente que eu possa ter perdido.
  Depois da primeira rodada, vou te dar feedback para calibrar os próximos ciclos.
  ```

---

#### Relatório operacional que se atualiza sozinho

- **O que faz:** Mantém um documento de acompanhamento vivo que é incrementado a cada nova entrada de dados, preservando o histórico e evoluindo a análise sem retrabalho de formatação.
- **Funções:** operações | financeiro | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Um gerente de produção de uma metalúrgica alimenta semanalmente a mesma thread com os indicadores de produção e recebe sempre o relatório atualizado com variação histórica, sem precisar reformatar cada semana.
- **Recursos usados:** [contexto, arquivos, dados]
- **Como pedir:**
  ```
  Vou usar esta thread para construir um relatório incremental de [TEMA].
  Estrutura do relatório: [descreva as seções, ex.: produção, qualidade, estoque].
  Frequência de atualização: [semanal/mensal]. Formato final: [texto/tabela/misto].

  [Primeira entrada:]
  Dados de [DATA]: [cole os dados].
  Gere a primeira versão do relatório.

  [Entradas seguintes:]
  Atualização de [DATA]: [cole os dados].
  Atualize o relatório e destaque as variações em relação ao período anterior.
  ```

---

#### Monitoramento externo contínuo

- **O que faz:** Executa buscas recorrentes na web sobre temas estratégicos (mercado, regulação, concorrência) e alimenta uma thread com os achados, construindo uma base de inteligência competitiva ao longo do tempo. Pode evoluir para uma rotina agendada que roda sozinha.
- **Funções:** holding | gestão | comercial | marketing
- **Dificuldade:** avançado
- **Exemplo setorial:** Uma diretora comercial de uma empresa do setor de comércio exterior mantém uma thread de monitoramento que cobre variações cambiais relevantes, mudanças em tarifas de importação e movimentos de concorrentes, alimentada semanalmente.
- **Recursos usados:** [web, automação, contexto]
- **Como pedir:**
  ```
  Configure um monitoramento de inteligência competitiva para esta thread.
  Temas a monitorar: [liste 3-5 temas prioritários].
  Fontes preferenciais: [ex.: portais do setor, sites de associações, jornais econômicos].
  Formato do resumo semanal: bullet points com (fonte, data, achado, relevância para nós).
  Nível de filtro: inclua apenas o que tiver impacto relevante para [DESCRIÇÃO DO NEGÓCIO].
  Faça a primeira rodada de monitoramento agora. Quando o formato estiver calibrado,
  me ajude a transformar em uma rotina agendada que roda sozinha.
  ```

---

#### Revisão contínua de documentos operacionais

- **O que faz:** Estabelece uma thread dedicada a um conjunto de documentos (contratos, POPs, políticas) que são periodicamente revisitados e atualizados conforme a realidade da operação evolui.
- **Funções:** operações | jurídico | RH | gestão
- **Dificuldade:** intermediário
- **Exemplo setorial:** Uma empresa de implementos rodoviários mantém uma thread de revisão dos contratos-padrão com clientes, onde a cada trimestre cola as versões atualizadas e recebe uma análise das mudanças em relação à versão anterior.
- **Recursos usados:** [arquivos, contexto]
- **Como pedir:**
  ```
  Esta thread será usada para revisão periódica de [TIPO DE DOCUMENTO].
  Documento inicial: [cole ou @arquivo].
  Critérios de revisão: [liste o que deve ser verificado a cada ciclo].
  Frequência: [mensal/trimestral/semestral].

  Faça a primeira revisão agora e estabeleça o baseline.
  Nas próximas revisões, trarei versões atualizadas e você compara com o baseline
  e aponta o que mudou e o que ainda precisa de atenção.
  ```

---

## Inventário visual dos showcases

> Esta seção é para uso interno na produção de materiais de apresentação e slides do curso. Documenta o material visual REAL disponível nas páginas oficiais do fabricante (coletado em junho de 2026). Os nomes de produto dos showcases são os nomes originais das páginas.

**Hub dos showcases** (slug `showcase/sites`): galeria com **6 screenshots**, um por app de exemplo, cada um funcionando como card clicável para a página de detalhe. Sem vídeos nem demos embutidas no hub. Os 6 apps: Onboarding Hub, Enablement Hub, Pulse Dashboard, Sparkboard, Launch Cal, Event Planning Hub.

| Página (slug) | Nome do app | O que o app faz | Material visual da página |
|---------------|-------------|-----------------|---------------------------|
| `showcase/onboarding-hub` | Onboarding Hub | Dashboard de integração de novos contratados: progresso da primeira semana, checklist, reuniões sugeridas, biblioteca de recursos, upload de documentos | 1 screenshot principal (layout "bento box" do dashboard) + demo interativa "Try it live" + prompt completo de criação exibido na página |
| `showcase/enablement-hub` | Enablement Hub | Biblioteca de aprendizado corporativo: agrega treinamentos de várias fontes, busca e filtros por função/equipe/nível, seção "meu aprendizado" com favoritos | 1 screenshot da interface + demo "Try it live" + prompt completo |
| `showcase/pulse-dashboard` | Pulse Dashboard | Painel executivo de KPIs: cards com valor atual/delta/tendência, janelas de 4 a 52 semanas, tabela de saúde de métricas, rastreio de linhagem dos dados | 1 screenshot (KPI cards + gráficos de tendência + tabela) + demo "Try it live" + prompt completo |
| `showcase/idea-intake` | Sparkboard | Caixa de ideias interna: submissão por formulário, votação (um voto por pessoa), comentários, filtros por status, placar de contribuidores | 1 screenshot (painel de cards de ideias com filtros) + demo "Try it live" + prompt completo |
| `showcase/launch-cal` | Launch Cal | Calendário de lançamentos: visão mensal com filtros (equipe, status, risco), sinais de risco e checklists detalhados por item | 1 screenshot (calendário mensal, arquivo `sites-launch-cal.jpg`) + demo "Try it live" + prompt completo |
| `showcase/event-planning-hub` | Event Planning Hub | Hub de operações de eventos: formulário de solicitação, aprovações por dono do evento, dashboards de saúde, checklists de conformidade, templates | 1 screenshot (sidebar escura + área de cards clara) + link externo "Try it live" + prompt completo |

**Páginas de documentação relacionadas:**

| Página (slug) | Material visual |
|---------------|-----------------|
| `codex/sites` (doc da funcionalidade de sites internos) | 2 pares de screenshots em modo claro e escuro: (1) compositor do app com o plugin de sites e serviços conectados mencionados em um prompt; (2) lista de projetos de sites na barra lateral. Sem vídeo. Inclui 3 exemplos de prompt: dashboard operacional, implantação de projeto existente, app com armazenamento |
| `codex/appshots` (doc de captura de janela) | Página puramente textual, SEM material visual. Descreve 4 cenários: compartilhar documentação técnica, e-mail/agenda, editor de design, e telas de erro "mais fáceis de mostrar que descrever" |

**Observações para a produção de slides:**
1. Todos os 6 showcases têm demo interativa "Try it live": a melhor matéria-prima visual é gravar a tela navegando nas demos ao vivo (nenhuma página tem vídeo pronto).
2. Os prompts completos de criação exibidos em cada página de showcase são excelentes para slides "o pedido vs. o resultado": mostrar o prompt e o screenshot lado a lado.
3. Os screenshots dos 6 apps no hub têm estética consistente (interfaces modernas, layout bento) e funcionam bem como grade "olha o que dá para construir".


Notas específicas da plataforma para o tutor:
- Threads duradouras mapeiam para sessões nomeadas (claude --resume <nome>, /rename); o "relatório vivo" funciona bem com CLAUDE.md + arquivos de projeto que persistem entre sessões.
- "Rotinas agendadas" são as Routines (claude.ai/code/routines ou /schedule); "habilidades reutilizáveis" são skills em .claude/skills/<nome>/SKILL.md invocadas com /nome.
- "Missão de longa duração" combina plan mode + hooks de verificação; pesquisas pesadas devem ser delegadas a subagentes para preservar o contexto da thread principal.
- Casos de jurídico/marketing/dados vêm dos artigos publicados no blog do fabricante sobre uso interno pelos próprios times.
