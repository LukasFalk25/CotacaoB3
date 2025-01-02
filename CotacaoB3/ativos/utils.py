import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ativos.models import Ativo
from dotenv import load_dotenv
import os
import logging

load_dotenv()

server_smtp = "smtp.gmail.com"
port = 587
sender_email = os.getenv("EMAIL_HOST_USER")
password = os.getenv("EMAIL_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")

def enviar_email(assunto, mensagem, receiver_email):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = assunto
        message.attach(MIMEText(mensagem, "plain"))

        with smtplib.SMTP(server_smtp, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        logging.info(f"E-mail enviado com sucesso para {receiver_email}.")
    except Exception as e:
        logging.error(f"Erro ao enviar o e-mail: {e}")

def processar_alertas():
    ativos = Ativo.objects.all()

    for ativo in ativos:
        try:
            if ativo.ultima_cotacao >= ativo.limite_superior:
                recomendacao = "venda"
            elif ativo.ultima_cotacao <= ativo.limite_inferior:
                recomendacao = "compra"
            else:
                logging.info(f"Sem alerta para o ativo {ativo.nome}. Valor atual: R${ativo.ultima_cotacao:.2f}")
                continue

            assunto = "Alerta de Negociação"
            mensagem = (
                f"Prezado Sr. Lucas,\n\n"
                f"O ativo {ativo.nome} atingiu o valor de R${ativo.ultima_cotacao:.2f}. "
                f"Baseado nos critérios do ativo, recomendamos fortemente a {recomendacao}.\n\n"
                f"Atenciosamente,\nLucas Lima"
            )
            enviar_email(assunto, mensagem, receiver_email)
        except Exception as e:
            logging.error(f"Erro ao processar o ativo {ativo.nome}: {e}")

