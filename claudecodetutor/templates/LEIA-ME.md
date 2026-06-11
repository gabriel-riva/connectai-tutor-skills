# Templates de Artefatos do Tutor

Manual de uso dos templates HTML desta pasta.

---

## O que são estes templates

Cada arquivo `.html` é um artefato visual que o tutor gera e entrega ao aluno durante a jornada. Todos os textos visíveis estão em português com acentos. O tema é neutro e sem marcas: nenhum logo de plataforma, ferramenta ou empresa aparece nos templates.

A identidade visual da empresa do aluno entra apenas nos artefatos produzidos dentro do módulo construtor, que usa seus próprios arquivos de brand.

---

## Quando gerar cada artefato

| Template | Quando usar |
|---|---|
| `trilha.html` | Ao montar a trilha personalizada do aluno no início da jornada, e novamente toda vez que a trilha for atualizada (módulo concluído, ritmo ajustado, eletiva escolhida). |
| `cheatsheet.html` | Ao final do primeiro dia de aprendizado, com os prompts que o aluno já praticou. Atualizar progressivamente a cada módulo concluído. |
| `vitrine.html` | No momento em que o aluno escolhe as eletivas ou quando o tutor apresenta os casos de uso disponíveis para o perfil. |
| `mapa-pessoal.html` | No fechamento do primeiro ciclo completo, após o diagnóstico de rotina do aluno. Revisar junto com o aluno antes de entregar. |

---

## Como usar

1. Copie o template desejado para a pasta `missões/` do aluno (ou subpasta equivalente do encontro).
2. Renomeie o arquivo com um nome descritivo em português com acentos. Exemplos:
   - `trilha-maria-junho.html`
   - `cheatsheet-análise-de-dados.html`
   - `mapa-pessoal-financeiro.html`
3. Abra o arquivo copiado em qualquer editor de texto.
4. Substitua **todos** os `{{PLACEHOLDERS}}` por valores reais. Nenhum placeholder pode aparecer no arquivo entregue ao aluno.
5. Preencha também os blocos de exemplo (ou apague-os): os comentários `<!-- exemplo: ... -->` são guias para o tutor e não devem aparecer na versão final.
6. Salve e abra no painel de preview para conferir visualmente antes de compartilhar.

---

## Regras obrigatórias

**Nenhum placeholder pode sobrar.** Antes de entregar, faça uma busca por `{{` no arquivo. Se encontrar algum, preencha-o.

**Tema neutro é intencional.** Não adicione logos de plataformas, ferramentas de IA, marcas de empresas ou identidade visual de qualquer programa. Estes templates são do tutor, não de uma ferramenta específica.

**Português com acentos sempre.** Nunca remova acentos, cedilhas ou caracteres especiais por conveniência técnica. Se um nome próprio tem acento, mantenha.

**Datas reais, nunca inventadas.** Use a data em que o artefato está sendo gerado ou a data do encontro. Em caso de dúvida, pergunte ao aluno ou ao coordenador antes de preencher.

**Tamanho dos textos.** Cada campo tem uma indicação de tamanho esperado no próprio template (ex.: "2 linhas", "1 linha"). Respeite esses limites para não quebrar o layout.

---

## Estrutura dos placeholders

Todos os placeholders seguem o padrão `{{NOME_EM_MAIUSCULAS}}`. Os mais comuns:

| Placeholder | O que preencher |
|---|---|
| `{{NOME_DO_ALUNO}}` | Nome completo ou primeiro nome do aluno |
| `{{FUNCAO}}` | Cargo ou função atual do aluno |
| `{{DATA}}` | Data de geração no formato DD/MM/AAAA |
| `{{PCT}}` | Percentual de progresso (0 a 100, sem o símbolo %) |
| `{{NOME_MODULO}}` | Nome exato do módulo conforme a trilha oficial |
| `{{RESULTADO_1_LINHA}}` | Uma frase descrevendo o resultado alcançado no módulo |
| `{{TEMPO_MIN}}` | Duração estimada do módulo em minutos |
| `{{CATEGORIA}}` | Categoria de prompts no cheatsheet (ex.: "Análise de Dados") |
| `{{PERIODO_OU_AREA}}` | Período, área ou recorte analisado no prompt de exemplo |
| `{{SETOR_DA_EMPRESA}}` | Setor ou contexto de trabalho do aluno |
| `{{NOME_DA_AREA_OU_RELATORIO}}` | Nome da área, processo ou relatório analisado |
| `{{NOME_DO_CASO}}` | Nome do caso de uso na vitrine |
| `{{COMO_FICARIA_NA_EMPRESA_DO_ALUNO}}` | Descrição concreta de como o caso se aplica à realidade do aluno |
| `{{ATIVIDADE}}` | Nome de uma atividade da rotina do aluno |
| `{{COMO}}` | Como o agente auxilia nessa atividade |
| `{{GANHO}}` | Ganho estimado (ex.: "~30 min/semana") |
| `{{MODULO}}` | Módulo da trilha que cobre essa atividade |

---

## Sobre o arquivo `base.html`

O `base.html` é a fundação visual dos demais templates. Ele define os tokens de cor (variáveis CSS `:root`) e a estrutura tipográfica básica. Não é entregue diretamente ao aluno: serve de referência para o tutor criar novos artefatos que sigam o mesmo padrão visual.

Se precisar criar um novo tipo de artefato, copie o `base.html`, adicione os estilos específicos dentro do bloco `<style>` existente e substitua `{{CONTEUDO}}` pelo corpo do novo artefato.
