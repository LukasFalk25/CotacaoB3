import yfinance as yf
from .models import Ativo

def obter_e_salvar_cotacao(codigo_ativo):
    try:
        # Obtém o ativo via yfinance
        ativo = yf.Ticker(codigo_ativo)
        cotacao = ativo.history(period='1d')['Close'].iloc[-1]

        if cotacao:
            # Busca o ativo no banco e atualiza a última cotação
            ativo_obj = Ativo.objects.get(codigo=codigo_ativo)
            ativo_obj.ultima_cotacao = cotacao
            ativo_obj.save()
            print(f"Última cotação atualizada para {codigo_ativo}: {cotacao}")
        else:
            print(f"Nenhuma cotação encontrada para o ativo {codigo_ativo}.")
    except IndexError:
        print(f"Erro ao buscar cotação para o ativo {codigo_ativo}.")
    except Ativo.DoesNotExist:
        print(f"Ativo com código {codigo_ativo} não encontrado no banco de dados.")
    except Exception as e:
        print(f"Erro inesperado ao processar {codigo_ativo}: {e}")

def salvar_cotacoes():  
    ativos = Ativo.objects.all()
    if not ativos.exists():
        print("Nenhum ativo cadastrado no banco de dados.")
        return

    for ativo in ativos:
        obter_e_salvar_cotacao(ativo.codigo)