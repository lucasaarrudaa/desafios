import pandas as pd

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

# funcao para calcular o percentual que cada estado possui no valor total de vendas na empresa.
def calculo_perc(estado, comp):
    resul = str(abs(round(((comp - estado)*100/comp) -100 , 2)))
    return resul + '%'

sp_perc = calculo_perc(sp, total)
rj_perc = calculo_perc(rj, total)
mg_perc = calculo_perc(mg, total)
es_perc = calculo_perc(es, total)
otrs_perc = calculo_perc(outros, total)

# montando dataframe para representar. 

dic = {'Estados': ['SP','RJ','MG','ES','Outros'],
'Faturamento por estado':[sp_perc,rj_perc,mg_perc,es_perc,otrs_perc]}

df = pd.DataFrame(dic, index=['1','2','3','4','5'])
print(df)




