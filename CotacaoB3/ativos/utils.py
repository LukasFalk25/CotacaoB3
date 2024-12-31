import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ativos.models import Ativo
from dotenv import load_dotenv
import os

load_dotenv()

server_smtp = "smtp.gmail.com"
port = 587
sender_email = os.getenv("EMAIL_HOST_USER")  
password = os.getenv("EMAIL_PASSWORD")

def enviar_email(assunto, mensagem, receiver_email):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = assunto
    message.attach(MIMEText(mensagem, "plain"))

    try:
        server = smtplib.SMTP(server_smtp, port)
        server.starttls()
        server.login(sender_email, password)
        
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"E-mail enviado com sucesso para {receiver_email}.")
    except Exception as e:
        print(f"Houve um erro ao enviar o e-mail: {e}")
    finally:
        server.quit()

def enviar_alertas():
    ativos = Ativo.objects.all()

    for ativo in ativos:
        if ativo.ultima_cotacao >= ativo.limite_superior:
            assunto = f"Alerta de Negociação"
            mensagem = (
                f"Prezado Sr. Lucas,\n\n"
                f"O ativo {ativo.nome} atingiu o valor de R${ativo.ultima_cotacao:.2f}, "
                f"baseado nos critérios do ativo recomendamos fortemente a venda.\n\n"
                f"Atenciosamente,\nLucas Lima"
            )
            receiver_email = 'falkc420@gmail.com'
        elif ativo.ultima_cotacao <= ativo.limite_inferior:
            assunto = f"Alerta de Negociação"
            mensagem = (
                f"Prezado Sr. Lucas,\n\n"
                f"O ativo {ativo.nome} atingiu o valor de R${ativo.ultima_cotacao:.2f}, "
                f"baseado nos critérios do ativo recomendamos fortemente a compra.\n\n"
                f"Atenciosamente,\nLucas Lima"
            )
            receiver_email = 'falkc420@gmail.com'
        else:
            print(f"Sem alerta para o ativo {ativo.nome}. Valor atual: R${ativo.ultima_cotacao:.2f}")
            continue

        enviar_email(assunto, mensagem, receiver_email)

