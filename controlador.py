import pandas as pd
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


class Controlador:
    def __init__(self):
        self.gastos = pd.read_excel("Dados.xlsx")

    def registrar_gasto(self, dia, tipo, recorrencia, valor):
        novo = pd.DataFrame(
            [[dia, tipo, recorrencia, valor]],
            columns=["Data", "Tipo", "Recorrencia", "Valor"],
        )
        self.gastos = pd.concat([self.gastos, novo])

    def mostrar_tabela(self):
        display(self.gastos)

    def salvar_tabela(self):
        self.gastos.to_excel("Dados.xlsx", index=False)

    def grafico_ano(self, ano):
        dados = self.gastos[self.gastos["Data"].dt.strftime("%Y") == f"{ano}"]
        meses = {
            "01": "Jan",
            "02": "Fev",
            "03": "Mar",
            "04": "Abr",
            "05": "Mai",
            "06": "Jun",
            "07": "Jul",
            "08": "Ago",
            "09": "Set",
            "10": "Out",
            "11": "Nov",
            "12": "Dez",
        }
        dados["Mês"] = pd.DatetimeIndex(dados["Data"]).month
        # [meses[i.dt.strftime("%m")] for i in dados["Data"]]

        f, ax = plt.subplots(figsize=(15, 6))

        p = sns.barplot(
            x="Mês", y="Valor", data=dados, hue="Tipo", legend=True, errorbar=None
        )
        for i in range(0, len(p.containers)):
            ax.bar_label(p.containers[i], label_type="center")

        plt.show()

    def grafico_mes(self, mes, ano):
        if mes < 10:
            mes_tratado = f"0{mes}"
        else:
            mes_tratado = f"{mes}"
        dados = self.gastos[
            self.gastos["Data"].dt.strftime("%Y-%m") == f"{ano}-{mes_tratado}"
        ]
        f, ax = plt.subplots(figsize=(15, 6))

        ax = sns.barplot(
            x="Tipo",
            y="Valor",
            data=dados,
            hue="Tipo",
            legend=True,
            errorbar=None,
        )
        for i in range(0, len(dados["Tipo"].unique())):
            ax.bar_label(ax.containers[i], fontsize=10)
        # ax.legend(self.gastos["Tipo"].unique(), loc="upper right")
        meses = {
            1: "Jan",
            2: "Fev",
            3: "Mar",
            4: "Abr",
            5: "Mai",
            6: "Jun",
            7: "Jul",
            8: "Ago",
            9: "Set",
            10: "Out",
            11: "Nov",
            12: "Dez",
        }
        plt.title(f"Gastos do mês {meses[mes]}/{ano}")
        sns.despine(left=True, right=True, bottom=True, top=True)
        plt.show()
