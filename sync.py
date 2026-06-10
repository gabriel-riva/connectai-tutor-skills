#!/usr/bin/env python3
"""Sincroniza _comum/ para codextutor/ e claudecodetutor/,
renderizando blocos <!-- @codex -->...<!-- @/codex --> e <!-- @claude -->...<!-- @/claude -->,
e checando pureza (nenhuma menção à outra plataforma no resultado)."""
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
PLATAFORMAS = {"codextutor": "codex", "claudecodetutor": "claude"}
BLOCO = re.compile(r"<!--\s*@(codex|claude)\s*-->\n?(.*?)<!--\s*@/\1\s*-->\n?", re.DOTALL)
PROIBIDAS = {
    "codex": [r"\bClaude Code\b", r"\bCLAUDE\.md\b", r"claudecodetutor", r"\.claude/skills"],
    "claude": [r"\bCodex\b", r"\bAGENTS\.md\b", r"codextutor", r"\.agents/skills", r"\$imagegen"],
}
TEXTUAIS = {".md", ".html", ".txt", ".css"}


def renderiza(texto: str, plataforma: str) -> str:
    return BLOCO.sub(lambda m: m.group(2) if m.group(1) == plataforma else "", texto)


def main() -> int:
    erros = []
    for destino, plataforma in PLATAFORMAS.items():
        for origem in sorted((RAIZ / "_comum").rglob("*")):
            if origem.is_dir():
                continue
            rel = origem.relative_to(RAIZ / "_comum")
            alvo = RAIZ / destino / rel
            alvo.parent.mkdir(parents=True, exist_ok=True)
            if origem.suffix in TEXTUAIS:
                texto = renderiza(origem.read_text(encoding="utf-8"), plataforma)
                alvo.write_text(texto, encoding="utf-8", newline="\n")
                for padrao in PROIBIDAS[plataforma]:
                    if re.search(padrao, texto):
                        erros.append(f"{destino}/{rel}: padrão proibido {padrao!r}")
            else:
                shutil.copy2(origem, alvo)
    if erros:
        print("FALHA DE PUREZA:")
        for e in erros:
            print(" -", e)
        return 1
    print("Sincronização OK, pureza OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
