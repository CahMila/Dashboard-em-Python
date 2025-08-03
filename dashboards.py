from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# iniciando o app
app = Dash(__name__)

# leitura da base de dados
df = pd.read_excel("vendas.xlsx")

# grafico inicial
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group", template="plotly_dark")

# lista de opções para o dropdown
opcoes = list (df ['ID Loja'].unique())
opcoes.append("Todas as Lojas")

# Layout do app
app.layout = html.Div(
    style={'backgroundColor': '#2c3e50',
        'color': '#f2f2f2',
        'fontFamily': 'Arial, sans-serif',
        'padding': '40px',
        'minHeight': '100vh'
           },
    children=[
        html.H1(
            "📊 Faturamento das lojas",
            style = {'textAlign': 'center', 'color': '#1abc9c'}
        ),
        html.H2(
            children=  "Gráfico com Produtos Vendidos por Loja",
            style={'textAlign': 'center', 'color': '#ecf0f1'}
        ),
        html.P(
    "🔎 Obs: Esse gráfico mostra a quantidade de produtos vendidos.",
            style={'textAlign': 'center', 'fontStyle': 'italic', 'color': '#bdc3c7'}
        ),

        html.Div(
            style={ 'width': '50%',
                'margin': '30px auto',
                'backgroundColor': '#2c2c2c',
                'padding': '20px',
                'borderRadius': '10px',
                'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.4)'
                   },
            children=[
                html.Label("Selecione uma loja:", style={'marginBottom': '10px', 'display': 'block'}),
                dcc.Dropdown(
                     options=[{'label': loja, 'value': loja} for loja in opcoes],
                     value='Todas as Lojas',
                     id='lista_lojas',
                     clearable=False,
                     className='meu-dropdown'
                )
            ]
        ),

        dcc.Graph(
            id='grafico_quantidade_vendas',
            figure=fig,
            style={'marginTop': '40px'}


        )
    ]
)

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group", template="plotly_dark")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group", template="plotly_dark")
    return fig


if __name__ == '__main__':
    app.run(debug=True)