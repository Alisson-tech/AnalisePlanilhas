import pandas as pd
from twilio.rest import Client

#   SID Conta twilio (twilio.com/console)
account_sid = "AC91f3bb1b9268f48ad4aaa57bf1300a34"
#Token conta twilio (twilio.com/console)
auth_token  = "2c800cc1702a59698684312a42078c46"

client = Client(account_sid, auth_token)

#nome dos arquivos
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#abrir planilhas
for mes in lista_meses:
    tabelas_vendas = pd.read_excel(f'Planilhas/{mes}.xlsx')

    #verificar se algum valor (any) é maior que 55000
    if(tabelas_vendas['Vendas']>55000).any():
        #obter vendedor
        vendedor = tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000,'Vendedor'].values[0]

        #obter valor de vendas
        vendas=tabelas_vendas.loc[tabelas_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        #enviar sms
        message = client.messages.create(
            to="+5519989989910",
            from_="+13218788103",
            body=f'no mês de {mes} alguem bateu a meta. O vendedor {vendedor} vendeu R$ {vendas}')





