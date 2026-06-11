# O que faz o settings.local.json

O arquivo `settings.local.json` pré-aprova uma única permissão: leitura dos arquivos de histórico de sessões do Claude Code, guardados em `~/.claude/projects/`. Isso permite que o professor acompanhe o que o aluno praticou na janela de prática sem precisar pedir permissão a cada sessão.

A permissão é somente de **leitura**: o professor lê os históricos, nunca escreve nem altera nada fora da pasta da oficina. Nenhuma informação sai do computador do aluno.

Para remover essa permissão, basta apagar o arquivo `.claude/settings.local.json` na raiz da sua oficina ou remover a linha `"Read(~/.claude/projects/**)"` do array `allow`.
