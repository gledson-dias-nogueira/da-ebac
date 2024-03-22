import pandas as pd
import seaborn as sns

gas_price = pd.read_csv("/content/da-ebac/gasolina.csv")

gas_price['Media_Movel'] = gas_price['venda'].rolling(window=2, min_periods=1).mean()


with sns.axes_style("whitegrid"):
  grafico = sns.lineplot(data=gas_price, x="dia", y="venda")
  grafico.set(title="Variação preço de venda Gasolina", ylabel="Preço",xlabel="dia")
  grafico.set_xticks(range(1, 11))

  sns.regplot(data=gas_price, x="dia", y="Media_Movel", scatter=False, ax=grafico)

  grafico.get_figure().savefig("Preço da Gasolina.png")
