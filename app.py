import plotly.express as px
import pandas as pd

données = pd.read_csv('Ventes_Par_Produit.csv')

figure = px.pie(données, values='Total_Produit_Vendus', names='c2', title='Ventes par produit')

figure.write_html('Ventes-par-produit.html')

print('Ventes-par-produit.html généré avec succès !')
