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
MARCADOR = re.compile(r"<!--\s*@/?(?:codex|claude)\s*-->")
PROIBIDAS = {
    "codex": [r"\bClaude Code\b", r"\bCLAUDE\.md\b", r"claudecodetutor", r"\.claude/skills"],
    "claude": [r"\bCodex\b", r"\bAGENTS\.md\b", r"codextutor", r"\.agents/skills", r"\$imagegen"],
}
TEXTUAIS = {".md", ".html", ".txt", ".css"}


def renderiza(texto: str, plataforma: str) -> str:
    return BLOCO.sub(lambda m: m.group(2) if m.group(1) == plataforma else "", texto)


def main() -> int:
    erros = []
    comum = RAIZ / "_comum"
    gerenciados = {p.relative_to(comum) for p in comum.rglob("*") if p.is_file()}
    pastas_comum = {p.name for p in comum.iterdir() if p.is_dir()}
    for destino, plataforma in PLATAFORMAS.items():
        for origem in sorted(comum.rglob("*")):
            if origem.is_dir():
                continue
            rel = origem.relative_to(comum)
            alvo = RAIZ / destino / rel
            alvo.parent.mkdir(parents=True, exist_ok=True)
            if origem.suffix in TEXTUAIS:
                texto = renderiza(origem.read_text(encoding="utf-8"), plataforma)
                alvo.write_text(texto, encoding="utf-8", newline="\n")
                for padrao in PROIBIDAS[plataforma]:
                    if re.search(padrao, texto):
                        erros.append(f"{destino}/{rel}: padrão proibido {padrao!r}")
                if MARCADOR.search(texto):
                    erros.append(
                        f"{destino}/{rel}: marcador de plataforma vazado "
                        "(abertura/fechamento desbalanceado)"
                    )
            else:
                shutil.copy2(origem, alvo)
        # Remoção de órfãos: apaga do destino apenas o que é espelho de _comum.
        # Regra: um arquivo do destino só é removido se (a) seu caminho relativo
        # NÃO existe mais em _comum (não é gerenciado) E (b) seu primeiro
        # segmento é uma pasta que existe em _comum (zona espelhada). Arquivos
        # próprios da skill (SKILL.md, referencia/, assets/, oficina/) não vêm
        # de _comum, ficam fora da zona espelhada e nunca são tocados; na raiz
        # do destino nada é removido (zona mista com arquivos próprios).
        for arquivo in sorted((RAIZ / destino).rglob("*")):
            if arquivo.is_dir():
                continue
            rel = arquivo.relative_to(RAIZ / destino)
            if rel in gerenciados:
                continue
            if len(rel.parts) > 1 and rel.parts[0] in pastas_comum:
                arquivo.unlink()
                print(f"Removido órfão: {destino}/{rel}")
    if erros:
        print("FALHA DE PUREZA:")
        for e in erros:
            print(" -", e)
        return 1
    print("Sincronização OK, pureza OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
