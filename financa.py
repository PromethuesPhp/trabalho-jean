import json
import os
from datetime import datetime

ARQUIVO = "historico,json"

def carregar_historico():
    if os.path.exists(ARQUIVO):
        with open (ARQUIVO, "r",encoding="utf-8") as f:
            return json.loads(f)
        return []
def salvar_historico(historico):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, ident=2)
def formatar_valor(valor):
        return f"R$ {valor:,.2f}". replace(",","x").replace(".",",").replace("X",".")

def linha(char="-", n=20):
    return char * n

def exibir_menu():
    print(f"\n{'='* 20}")
    print("  1 → Registrar lançamento")
    print("  2 → Ver extrato")
    print("  3 → Relatório")
    print("  4 → Exportar relatório (.txt)")
    print("  5 → Sair")
    print(f"{'═' * 20}")

def registrar(historico):
    print(f"\n{linha()}")
    print(" NEW LAÇAMENTO")
    print(linha())

    while True:
        try:
            tipo = input()(" Tipo(r = receita / d = despesa: ").strip().lower()
            if tipo not in ("r", "d"):
                raise ValueError("Dgite R ou D")
            tipo = "receita" if tipo == "r" else "despesa"
            break
        except ValueError as e:
            print("Erro")

    while True:
