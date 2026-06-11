# Referência: Navegador e Computador (app Codex, Windows)

> Destilado das docs oficiais em 10/06/2026

O Codex pode interagir com páginas web e aplicativos de desktop por meio de três camadas complementares. Esta referência descreve cada camada, quando usar cada uma e as restrições relevantes para o Windows.

---

## 1. As três camadas de alcance

O Codex se expande em camadas do que pode acessar:

| Camada | Símbolo | Alcance |
|---|---|---|
| Navegador integrado | `$browser` (ou "Browser") | Páginas locais e públicas sem autenticação |
| Extensão Chrome | `@chrome` (ou `@Chrome`) | Sites com login no seu perfil do Chrome |
| Controle do computador | `@computer` (ou `@Computer`) | Qualquer aplicativo de desktop com interface gráfica |

Cada camada amplia o que o Codex pode ver e fazer. Use a mais simples que resolva o problema.

---

## 2. $browser: o navegador integrado

### O que é

O navegador integrado é um painel dentro do app Codex que renderiza páginas web ao lado da conversa. Tanto você quanto o Codex podem ver a página ao mesmo tempo.

**Como abrir:** clique no ícone de browser na barra de ferramentas, clique em uma URL no chat, navegue manualmente, ou pressione `Ctrl+Shift+B` (Windows).

### O que o Codex pode fazer com $browser

Quando o plugin Browser está instalado e ativado, o Codex pode operar o navegador diretamente: clicar, digitar, inspecionar o estado renderizado, tirar screenshots, baixar arquivos e executar JavaScript de inspeção (somente leitura).

Para invocar: mencione "use o browser" no prompt ou use `@Browser`.

### Anotações visuais

No modo de anotação, você pode:

- Selecionar elementos ou áreas específicas da página
- Submeter comentários precisos sobre o que precisa mudar
- Usar `Shift+clique` para selecionar uma área
- Usar `Cmd/Ctrl+clique` para enviar o comentário imediatamente

Você pode ajustar fonte, texto, espaçamento e cor diretamente na página antes de enviar o feedback.

### Limitações importantes

O navegador integrado **não suporta:**

- Fluxos de autenticação (login)
- Páginas que exigem conta
- Cookies persistentes
- Extensões do navegador
- Abas existentes do Chrome

> Não insira senhas ou dados sensíveis no navegador integrado.

Para sites autenticados, use a extensão Chrome.

### Boas práticas

- Mantenha tarefas pequenas e revisáveis em uma passagem
- Nomeie a página, rota ou URL local
- Especifique o estado visual esperado (carregando, vazio, erro, sucesso)
- Comente elementos exatos que precisam mudar
- Peça ao Codex para verificar o servidor antes de usar o navegador

---

## 3. @chrome: a extensão Chrome

### O que é

A extensão Chrome permite que o Codex use o Chrome com o seu perfil de usuário, incluindo cookies, sessões ativas e sites autenticados. É a opção quando o site exige login.

**Quando usar:** LinkedIn, Salesforce, Gmail, ferramentas internas com autenticação, qualquer site que exija estar logado.

**Quando o navegador integrado basta:** desenvolvimento local, pré-visualizações baseadas em arquivo, páginas públicas.

### Como instalar

1. Abra o Codex e acesse **Plugins**
2. Adicione o plugin **Chrome**
3. Siga o fluxo de configuração (a extensão será instalada no Chrome)
4. Confirme no Chrome que a extensão mostra **Connected**

### Como usar

```
@Chrome abra o Salesforce e atualize o contato com estas anotações da reunião.
```

Se o Chrome não estiver aberto, o Codex pode iniciá-lo automaticamente.

### Controle de acesso a sites

Por padrão, o Codex solicita confirmação antes de interagir com novos domínios. Você pode:

- Permitir apenas para a conversa atual
- Sempre permitir o domínio (sem perguntar novamente)
- Recusar o acesso

Gerencie a lista de sites permitidos e bloqueados em **Settings > Computer Use**.

### Dados e segurança

O Codex não armazena um registro completo e separado das ações no Chrome. Os dados de navegação ficam apenas no contexto da conversa (textos lidos, screenshots, chamadas de ferramenta).

> Evite enviar senhas ou dados altamente sensíveis por tarefas de navegação, a menos que sejam estritamente necessários e você esteja presente para revisar cada prompt.

### Solução de problemas

Se o Codex não conseguir se conectar ao Chrome:

1. Verifique se a extensão mostra **Connected** na barra de ferramentas do Chrome
2. Confirme que o plugin Chrome está ativado em **Plugins**
3. Certifique-se de usar o mesmo perfil do Chrome onde a extensão foi instalada
4. Inicie uma nova thread do Codex
5. Reinicie Chrome e Codex, se necessário

---

## 4. @computer: controle de apps desktop

### O que é

Computer Use permite que o Codex veja a tela, clique, digite e navegue em qualquer aplicativo de desktop com interface gráfica. Pense nisso como o Codex "usando o computador" da mesma forma que um humano faria: vendo o que está na tela e interagindo com os controles.

**Quando usar:**

- Testar aplicativos desktop
- Reproduzir bugs que só aparecem na interface gráfica
- Realizar tarefas que exigem um app de desktop específico
- Inspecionar configurações de aplicativos
- Acessar dados em fontes sem API ou plugin

### Disponibilidade e restrição geográfica

**Disponível em:** macOS e Windows.

**Não disponível no lançamento em:** Área Econômica Europeia (AEE), Reino Unido e Suíça.

**Brasil:** sem restrição. Computer Use está disponível.

### Ativação no Windows

1. Abra as **Configurações** do Codex
2. Acesse a seção **Computer Use**
3. Clique em **Install** para instalar o plugin

No Windows, a ativação pelo toggle em Settings tem efeito imediato, sem etapa extra de permissões do sistema operacional.

(Diferente do macOS, onde é necessário conceder permissões de Gravação de Tela e Acessibilidade nas configurações do sistema.)

### Limitação específica do Windows

O aplicativo que o Codex deve controlar precisa estar **visível na área de trabalho ativa** durante a execução da tarefa. O Codex assume o controle do mouse e do teclado enquanto trabalha.

Não há execução em segundo plano: o app-alvo deve estar em primeiro plano.

### Como usar

Mencione `@Computer` ou `@NomeDoApp` no prompt:

```
Abra o app com computer use, reproduza o bug na tela de onboarding e
corrija o menor caminho de código que o causa.
```

### Limitações gerais

- Não pode automatizar terminais ou o próprio Codex
- Não pode autenticar como administrador
- Não pode aprovar prompts de segurança do sistema operacional

### Segurança

O Codex solicita permissão antes de usar cada aplicativo e pode ser interrompido a qualquer momento.

---

## 5. Resumo: qual camada usar

| Situação | Camada indicada |
|---|---|
| Verificar aparência de uma página local em desenvolvimento | `$browser` |
| Deixar comentários visuais em uma página | `$browser` (modo anotação) |
| Acessar Gmail, LinkedIn ou outro site com login | `@chrome` |
| Preencher um formulário em um site interno | `@chrome` |
| Testar um aplicativo desktop (Excel, ERP, ferramenta nativa) | `@computer` |
| Reproduzir um bug que só aparece na interface gráfica | `@computer` |
