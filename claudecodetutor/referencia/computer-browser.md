# Referência: Navegador e Computador no Claude Code Desktop

> Destilado das docs oficiais em 10/06/2026. Cobre o app desktop Windows (aba Code). Nunca descrever fluxos exclusivos de CLI como funcionalidades do app.

---

## Claude in Chrome: automação de navegador

### O que é

A extensão **Claude in Chrome** conecta o Claude Code ao navegador Chrome ou Edge, dando ao Claude capacidades de automação web diretamente a partir de uma sessão.

Com a extensão conectada, você pode combinar ações no navegador com tarefas de código em um único fluxo de trabalho.

### Pré-requisitos

- Google Chrome ou Microsoft Edge (não suportado no Brave, Arc ou outros baseados em Chromium).
- Extensão **Claude in Chrome** versão 1.0.36 ou superior (Chrome Web Store, funciona em ambos os navegadores).
- Claude Code versão 2.0.73 ou superior.
- Plano Pro, Max, Team ou Enterprise (não disponível via provedores terceiros como Bedrock, Vertex ou Foundry).

**WSL (Windows Subsystem for Linux) não é suportado** para esta integração.

### O que você consegue fazer

- **Depuração ao vivo:** leia erros do console e estado do DOM diretamente, depois corrija o código que os causou, tudo na mesma sessão.
- **Verificação de design:** construa uma UI a partir de um mockup do Figma, abra no navegador e verifique se corresponde.
- **Testes de aplicações web:** teste validação de formulários, verifique regressões visuais, valide fluxos de usuário.
- **Apps web autenticados:** interaja com Google Docs, Gmail, Notion ou qualquer app onde você já está logado, sem precisar de conectores de API.
- **Extração de dados:** extraia informações estruturadas de páginas web e salve localmente.
- **Automação de tarefas:** automatize tarefas repetitivas como entrada de dados, preenchimento de formulários ou fluxos entre múltiplos sites.
- **Gravação de sessão:** grave interações no navegador como GIFs para documentar ou compartilhar.

### Como usar no app desktop

No app desktop, a extensão funciona a partir da aba Code da mesma forma que no CLI: Claude usa as ferramentas do navegador quando relevante para a tarefa. A extensão precisa estar instalada e conectada.

Se a extensão não estiver conectada, o Claude reportará o problema. Reinstale ou reative a extensão em `chrome://extensions` e reinicie o navegador.

### Exemplos de fluxo de trabalho

**Testar uma aplicação local:**

```
Acabei de atualizar a validação do formulário de login. Você pode abrir
localhost:3000, tentar enviar o formulário com dados inválidos e verificar
se as mensagens de erro aparecem corretamente?
```

**Depurar com logs do console:**

```
Abra a página do dashboard e verifique o console por erros quando
a página carrega.
```

**Preencher formulários automaticamente:**

```
Tenho uma planilha de contatos em contacts.csv. Para cada linha,
vá ao CRM em crm.exemplo.com, clique em "Adicionar Contato" e
preencha os campos de nome, e-mail e telefone.
```

**Gravar uma demonstração em GIF:**

```
Grave um GIF mostrando como completar o fluxo de checkout, desde
adicionar um item ao carrinho até a página de confirmação.
```

### Permissões de sites

As permissões de nível de site são herdadas das configurações da extensão Chrome. Gerencie nas configurações da extensão para controlar quais sites o Claude pode navegar, clicar e digitar.

---

## Computer use: o Claude controla sua tela

### O que é

Computer use permite ao Claude abrir aplicativos, controlar sua tela e trabalhar no computador da mesma forma que você. O Claude pode realizar tarefas que exigem uma interface gráfica (GUI), coisas que você normalmente teria que fazer manualmente.

### Disponibilidade por plataforma

| Superfície | Windows | macOS |
|-----------|---------|-------|
| App desktop | Disponível | Disponível |
| CLI (`--chrome`) | Não disponível | Disponível |

**Computer use no app desktop está disponível tanto no Windows quanto no macOS.** Requer plano Pro ou Max.

Esta é uma **prévia de pesquisa** (research preview). O comportamento pode mudar.

### Como habilitar no app desktop

1. Vá em **Settings > General** (na seção "Desktop app").
2. Ative o toggle de computer use.
3. Na primeira vez que o Claude tentar usar o computador, você verá prompts para conceder permissões do sistema operacional.

### Aprovações por sessão

Habilitar o computer use não concede ao Claude acesso a todos os aplicativos. Na primeira vez que o Claude precisa de um aplicativo específico em uma sessão, um prompt aparece mostrando:

- Quais aplicativos o Claude quer controlar
- Permissões extras solicitadas (como acesso à área de transferência)

Escolha **Permitir para esta sessão** ou **Negar**. Aprovações valem apenas para a sessão atual.

### Tiers de controle por categoria de app

O nível de controle do Claude varia de acordo com a categoria do aplicativo:

| Categoria | Controle disponível |
|-----------|---------------------|
| Navegadores e plataformas de trading | Somente visualização (screenshots) |
| Terminais e IDEs (VS Code, etc.) | Somente clique (sem digitar) |
| Todos os outros apps | Controle completo (clicar, digitar, rolar) |

Aplicativos com acesso amplo recebem um aviso extra no prompt de aprovação:

| Aviso | Aplica a |
|-------|---------|
| Equivalente a acesso de shell | Terminal, iTerm, VS Code, Warp |
| Pode ler ou escrever qualquer arquivo | Explorador de arquivos |
| Pode alterar configurações do sistema | Configurações do sistema |

Esses apps não são bloqueados. O aviso permite que você decida se a tarefa justifica esse nível de acesso.

### O que você pode fazer com computer use

- **Construir e validar apps nativos:** escreva código Swift/C#/etc., compile, lance o app e clique em cada controle para verificar que funciona, tudo na mesma sessão.
- **Testes de UI ponta a ponta:** abra qualquer app, clique pelo fluxo de onboarding, faça screenshots de cada etapa.
- **Depurar problemas visuais e de layout:** redimensione a janela, reproduza o bug, capture screenshot, corrija o CSS, verifique a correção.
- **Controlar ferramentas apenas com GUI:** interaja com ferramentas de design, painéis de controle de hardware, simuladores iOS/Android ou aplicativos proprietários sem CLI ou API.

### Hierarquia de ferramentas

O Claude usa a ferramenta mais precisa disponível antes de recorrer ao computer use:

1. Servidor MCP para o serviço (mais preciso).
2. Bash, se a tarefa é um comando de shell.
3. Claude in Chrome, se a tarefa é no navegador e a extensão está configurada.
4. Computer use, para apps nativos e ferramentas sem API.

### Segurança e controles

- **Aprovação por app:** o Claude só controla apps que você aprovou na sessão atual.
- **Terminal excluído de screenshots:** o Claude nunca vê sua janela de terminal.
- **Escape global:** pressione `Esc` para abortar o computer use a qualquer momento; controle retorna a você.
- **Uma sessão por vez:** apenas uma sessão pode controlar seu computador simultaneamente.
- **Lista de apps negados:** nas configurações do app desktop, você pode configurar apps que o Claude nunca pode controlar.

---

## Análise de imagens

Além do computer use, o Claude pode analisar imagens que você forneça diretamente:

- Arraste e solte uma imagem na janela de chat.
- Cole com Ctrl+V.
- Mencione um caminho de arquivo no chat.

Isso é análise de imagem (o Claude vê e descreve), não geração de imagem.

### Sem geração de imagem nativa

**O Claude Code não gera imagens nativamente.** Não há função de "gerar uma imagem" ou "criar um logo".

Para criar saída visual, o Claude pode:

- Gerar HTML/SVG/CSS para renderização no navegador.
- Criar diagramas Mermaid ou Graphviz.
- Escrever código que usa bibliotecas de visualização (matplotlib, D3.js, etc.).

Exemplo: "Crie um gráfico de barras das minhas vendas mensais" resulta em código HTML/JavaScript que você abre no navegador, não em um arquivo de imagem.

---

## Resumo: qual ferramenta usar para cada tarefa

| Tarefa | Ferramenta ideal |
|--------|------------------|
| Testar um app web no localhost | Claude in Chrome |
| Verificar Google Docs, Gmail, Notion | Claude in Chrome |
| Extrair dados de uma página pública | Claude in Chrome |
| Testar um app Windows nativo | Computer use |
| Depurar problema visual em janela redimensionada | Computer use |
| Controlar simulador iOS/Android | Computer use |
| Automatizar preenchimento de formulário web | Claude in Chrome |
| Analisar um screenshot que você tirou | Arraste a imagem no chat |
| Criar gráfico ou diagrama | Peça ao Claude para gerar HTML/SVG |
