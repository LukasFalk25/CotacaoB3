import yfinance as yf
from .models import Ativo, Cotacao
 
def obter_cotacao(codigo_ativo):    
    try:
        ativo = yf.Ticker(codigo_ativo)
        cotacao = ativo.history(period='1d')['Close'].iloc[-1]
        return cotacao
    except IndexError:
        print(f"Nenhuma cotação encontrada para o ativo {codigo_ativo}.")
        return None
    
def salvar_cotacoes():
    ativos = Ativo.objects.all() 
    for ativo in ativos:
        preco = obter_cotacao(ativo.codigo)  
        if preco:
            Cotacao.objects.create(ativo=ativo, preco=preco)