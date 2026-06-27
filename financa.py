import json
import os
from datetime import datetime

ARQUIVO = "historico.json"


def carregar_historico():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)  # era json.loads(f)
    return []  # era indentação errada, estava dentro do with


def salvar_historico(historico):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)  # era ident=2


def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")  # era "x" minúsculo


def linha(char="-", n=20):
    return char * n


def exibir_menu():
    print(f"\n{'=' * 20}")
    print("  1 - Registrar lancamento")
    print("  2 - Ver extrato")
    print("  3 - Relatorio")
    print("  4 - Exportar relatorio (.txt)")
    print("  5 - Sair")
    print(f"{'=' * 20}")


def registrar(historico):
    print(f"\n{linha()}")
    print("  NOVO LANCAMENTO")
    print(linha())

    tipo = ""
    valor = 0.0
    categoria = ""
    descricao = ""

    while True:
        tipo = input("  Tipo (r = receita / d = despesa): ").strip().lower()
        if tipo in ("r", "d"):
            tipo = "receita" if tipo == "r" else "despesa"
            break
        print("  Erro: Digite r ou d")

    while True:
        try:
            valor = float(input("  Valor (ex: 32.50): ").strip().replace(",", "."))
            if valor > 0:
                break
            print("  Erro")
        except ValueError:
            print("  Erro")

    while True:
        categoria = input("  Categoria (Alimentacao/Salario): ").strip()
        if categoria:
            break
        print("  Erro")

    while True:
        descricao = input("  Descricao: ").strip()
        if descricao:
            break
        print("  Erro")

    lancamento = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "tipo": tipo,
        "categoria": categoria.lower(),
        "descricao": descricao,
        "valor": valor,
    }

    historico.append(lancamento)
    salvar_historico(historico)

    sinal = "+" if tipo == "receita" else "-"
    print(f"\n  Lancamento salvo! ({sinal}{formatar_valor(valor)})")


def ver_extrato(historico):
    print(f"\n{linha()}")
    print("  EXTRATO")
    print(linha())

    if not historico:
        print("  Nenhum lancamento encontrado.")
        return

    for i, l in enumerate(historico, 1):
        sinal = "+" if l["tipo"] == "receita" else "-"
        print(f"  #{i:>3}  {l['data']}")
        print(f"        {l['tipo'].capitalize()} - {l['categoria'].capitalize()}")
        print(f"        {l['descricao']}")
        print(f"        {sinal}{formatar_valor(l['valor'])}")
        print(f"        {linha('-', 20)}")  # era faltando o ) final


def calcular_relatorio(historico):
    receitas = sum(l["valor"] for l in historico if l["tipo"] == "receita")
    despesas = sum(l["valor"] for l in historico if l["tipo"] == "despesa")
    saldo = receitas - despesas

    categorias = {}
    for l in historico:
        cat = l["categoria"]
        categorias.setdefault(cat, {"receita": 0.0, "despesa": 0.0})
        categorias[cat][l["tipo"]] += l["valor"]

    return receitas, despesas, saldo, categorias


def exibir_relatorio(historico):
    print(f"\n{linha()}")
    print("  RELATORIO")
    print(linha())

    if not historico:
        print("  Nenhum dado para exibir.")
        return

    receitas, despesas, saldo, categorias = calcular_relatorio(historico)

    saldo_status = "positivo" if saldo >= 0 else "negativo"
    print(f"  Total de receitas : {formatar_valor(receitas)}")
    print(f"  Total de despesas : {formatar_valor(despesas)}")
    print(f"  Saldo atual ({saldo_status}) : {formatar_valor(saldo)}")
    print(f"\n  {linha('-', 44)}")
    print("  POR CATEGORIA")
    print(f"  {linha('-', 44)}")

    for cat, vals in sorted(categorias.items()):
        print(f"  {cat.capitalize()}")
        if vals["receita"]:
            print(f"       Receitas : {formatar_valor(vals['receita'])}")
        if vals["despesa"]:
            print(f"       Despesas : {formatar_valor(vals['despesa'])}")


def exportar_relatorio(historico):
    if not historico:
        print("\n  Nenhum dado para exportar.")
        return

    receitas, despesas, saldo, categorias = calcular_relatorio(historico)
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    linhas = []
    linhas.append("=" * 52)
    linhas.append("       CONTROLE FINANCEIRO PESSOAL")
    linhas.append(f"       Gerado em: {agora}")
    linhas.append("=" * 52)
    linhas.append("")
    linhas.append("RESUMO GERAL")
    linhas.append("-" * 52)
    linhas.append(f"  Total de receitas : {formatar_valor(receitas)}")
    linhas.append(f"  Total de despesas : {formatar_valor(despesas)}")
    linhas.append(f"  Saldo atual       : {formatar_valor(saldo)}")
    linhas.append("")
    linhas.append("POR CATEGORIA")
    linhas.append("-" * 52)

    for cat, vals in sorted(categorias.items()):
        linhas.append(f"  {cat.capitalize()}")
        if vals["receita"]:
            linhas.append(f"    Receitas : {formatar_valor(vals['receita'])}")
        if vals["despesa"]:
            linhas.append(f"    Despesas : {formatar_valor(vals['despesa'])}")

    linhas.append("")
    linhas.append("EXTRATO COMPLETO")
    linhas.append("-" * 52)

    for i, l in enumerate(historico, 1):
        sinal = "+" if l["tipo"] == "receita" else "-"
        linhas.append(
            f"  #{i:>3} | {l['data']} | {l['tipo'].capitalize():<8} | "
            f"{l['categoria'].capitalize():<15} | "
            f"{sinal}{formatar_valor(l['valor']):<14} | {l['descricao']}"
        )

    linhas.append("")
    linhas.append("=" * 52)

    conteudo = "\n".join(linhas)

    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write(conteudo)

    print("\n  Arquivo relatorio.txt gerado com sucesso!")


def main():
    historico = carregar_historico()
    print("\n  Historico carregado:", len(historico), "lancamento(s).")

    while True:
        exibir_menu()
        try:
            opcao = input("  Escolha uma opcao: ").strip()
        except (KeyboardInterrupt, EOFError):
            opcao = "5"

        if opcao == "1":
            registrar(historico)
        elif opcao == "2":
            ver_extrato(historico)
        elif opcao == "3":
            exibir_relatorio(historico)
        elif opcao == "4":
            exportar_relatorio(historico)
        elif opcao == "5":
            print("\n  Ate logo! Todos os dados estao salvos.\n")
            break
        else:
            print("  Opcao invalida. Digite um numero de 1 a 5.")


if __name__ == "__main__":
    main()
