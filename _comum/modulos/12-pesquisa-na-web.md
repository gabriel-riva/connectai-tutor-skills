# Módulo: Pesquisa na web
**Nível:** eletiva · **Pré:** 01, 02 · **Tempo típico:** 25-35 min
**Resultado:** o aluno conduz uma pesquisa real de mercado, fornecedores, preços ou normas com fontes citadas e resultado em tabela, e sabe qual camada de acesso usar dependendo do que precisa acessar.

---

## Conceito em 1 minuto

Pesquisa na web sem o agente funciona como busca manual em várias abas ao mesmo tempo: você abre, lê, guarda o que importa, fecha, abre outra. O agente faz a mesma coisa, mas em paralelo e sem perder o fio. A diferença prática é que você termina com uma síntese organizada, com as fontes anotadas, em vez de vinte abas abertas que você vai fechar sem ler.

A regra de ouro de qualquer pesquisa assistida: fontes importam. Peça sempre a origem de cada afirmação. Informação sem fonte é rascunho, não pesquisa.

---

## Missão guiada

> Conduza um ato de cada vez. Só avance quando o aluno confirmar que terminou.

### Ato 1: escolher a pesquisa real

Pergunte ao aluno qual pesquisa ele precisaria fazer nos próximos dias: um fornecedor novo, um preço de referência, uma norma regulatória, um concorrente. Diga:

> "Pensa numa pesquisa de mercado ou de fornecedor que você deveria fazer esta semana e ainda não fez. Qualquer assunto da sua área: preço de insumo, alternativa de fornecedor, norma técnica, tendência de mercado."

Registre o tema. A pesquisa será feita de verdade, não como exercício fictício.

**Verificação:** aluno nomeou um tema real.

---

### Ato 2: a pesquisa com fontes citadas

Na sessão de prática, passe o modelo com o tema do aluno:

> "Pesquise [tema exato] com foco em [objetivo: preço de referência / fornecedores no mercado brasileiro / requisitos regulatórios / tendências recentes]. Para cada informação relevante que você encontrar: cite a fonte com o nome do site e a URL. Organize o resultado em uma tabela com as colunas: [Item ou Fornecedor], [Informação Principal], [Fonte]. Ao final, adicione um parágrafo com as suas conclusões principais."

Após o resultado, verifique com o aluno:

> "Tem alguma informação que surpreendeu você? Alguma fonte que você reconhece e outra que não conhecia? Vale a pena clicar em uma ou duas para confirmar?"

O objetivo é que o aluno entenda que a pesquisa é um ponto de partida para verificação, não a palavra final.

**Verificação:** tabela com fontes gerada, aluno conferiu pelo menos uma fonte.

---

### Ato 3: onde a navegação acontece (camadas de acesso)

Após a pesquisa, explique as camadas disponíveis para o aluno e quando usar cada uma. O conteúdo depende da plataforma:

<!-- @codex -->
> "Dependendo do que você precisa acessar, o agente usa camadas diferentes. Para páginas públicas sem login, ele usa o navegador integrado ($browser), acessado com `Ctrl+Shift+B`. Para sites onde você já está logado, como portais de fornecedores com senha ou ferramentas da empresa, ele usa a extensão Chrome (@chrome), que acessa com o seu perfil de usuário. Deixa eu te mostrar a diferença."

Abra o navegador integrado com `Ctrl+Shift+B` e mostre uma página pública. Então explique:

> "Para um portal de fornecedor onde você já tem conta, ou uma ferramenta interna com login, a extensão Chrome (@chrome) seria o caminho certo. Ela acessa com o seu perfil, incluindo os cookies de sessão. Para usar: no prompt, mencione '@Chrome' e o nome do site."

Confirme se o aluno tem a extensão Chrome instalada (ver `Plugins` no app). Se não tiver, marque para instalar numa próxima sessão.
<!-- @/codex -->

<!-- @claude -->
> "Dependendo do que você precisa acessar, o agente usa ferramentas diferentes. Para pesquisa de páginas públicas, ele usa a navegação pela web integrada ao app. Para sites onde você já está logado, como portais de fornecedores ou ferramentas internas com senha, a extensão 'Claude in Chrome' é o caminho: ela acessa o Chrome com o seu perfil, incluindo as sessões ativas."

Explique os requisitos da extensão Claude in Chrome: precisa do Google Chrome ou Microsoft Edge (não funciona no Brave ou Arc), extensão versão 1.0.36 ou superior, e plano Pro, Max, Team ou Enterprise. Confirme se o aluno tem os pré-requisitos.

Se tiver, mostre como usar: "No chat, descreva o que você quer fazer no site. Por exemplo: 'Vá ao portal [nome] e me traga os preços atuais da lista de produtos.' O agente acessa o Chrome com o seu perfil logado."
<!-- @/claude -->

**Verificação:** aluno entende a diferença entre pesquisa em páginas públicas e acesso a sites autenticados.

---

### Ato 4: o comparativo em tabela

Com a pesquisa feita, finalize gerando um comparativo estruturado para uso real. Passe o modelo:

> "Com base na pesquisa que fizemos, crie uma tabela comparativa de [fornecedores / opções / normas] com as colunas mais relevantes para uma decisão. Inclua na última linha uma recomendação de qual opção você avaliaria primeiro e por quê, com base apenas nas informações encontradas."

Salve o resultado na pasta `missões/` com a data.

**Verificação:** comparativo salvo, pronto para uso em uma reunião ou decisão real.

---

## Variações por função

| Área | Pesquisa típica | Comparativo útil |
|---|---|---|
| Financeiro | Taxas de linhas de crédito ou fornecedores financeiros | Banco ou modalidade por custo efetivo |
| Comercial | Concorrentes, preços de referência do mercado | Posicionamento de preço por produto |
| Operações | Fornecedores de insumo, cotação de peça específica | Fornecedor por preço, prazo e localização |
| Marketing | Agências, plataformas de mídia, tendências de segmento | Plataforma por alcance, custo e formato |
| Engenharia | Normas técnicas, especificações de equipamento | Equipamento por especificação e custo |
| Holding | Tendências de setor, benchmarks de gestão | Práticas por segmento e resultado reportado |

---

## Aprofundamento

Para pesquisas que precisam de dados por trás de um login (portal de fornecedor, sistema de cotações, extranet de cliente), a extensão Chrome é o caminho natural para quem já tem a conta ativa. Mas há um cuidado importante: sites que exigem login têm termos de uso. Alguns permitem automação, outros não. O aluno deve verificar os termos antes de automatizar qualquer coisa em portais de terceiros.

Para pesquisas recorrentes (cotação semanal de insumos, por exemplo), o módulo 15 sobre automações mostra como transformar uma pesquisa manual em rotina agendada.

---

## Erros comuns e diagnóstico

**Resultado sem fontes ou com fontes vagas.**
O agente listou informações mas sem URL ou nome de site. Fala do tutor: "Inclui no prompt a instrução 'cite o nome do site e a URL completa para cada informação'. Pesquisa sem fonte é rascunho. Com a URL, você consegue verificar se a informação ainda é válida."

**Resultado com informações desatualizadas.**
O agente trouxe dados de anos atrás. Fala do tutor: "Adiciona no prompt: 'priorize fontes de [ano atual] e [ano anterior]; se encontrar uma fonte mais antiga, indique a data e sinalize que pode estar desatualizada'."

**Aluno quer pesquisar em site com login mas não tem a extensão.**
Fala do tutor: "Para esse site específico, vamos precisar da extensão Chrome instalada. Essa é uma configuração de alguns minutos. Quer fazer agora ou continuar com a pesquisa em páginas públicas e agendamos a instalação?"

**Tabela comparativa fica grande demais para ser útil.**
O aluno pediu muitas colunas e o resultado é difícil de ler. Fala do tutor: "Qual é a decisão que você precisa tomar com base nessa tabela? Com essa pergunta em mãos, quais colunas são realmente necessárias para a decisão? Elimina o resto."

---

## Registro

**Diário (`tutor/DIARIO.md`):** registre o tema da pesquisa real feita, se o aluno verificou alguma fonte, se teve dificuldade em formular a pesquisa com clareza e se a camada de acesso web foi compreendida.

**Cérebro:** esta missão pode alimentar:
- `empresa/contexto.md`: se a pesquisa trouxe dados sobre o segmento de atuação ou concorrentes.
- `departamento/sistemas.md`: se o aluno tem portais de fornecedores ou plataformas com login que usa regularmente.
