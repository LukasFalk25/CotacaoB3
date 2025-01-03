#Estático 

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .services import salvar_cotacoes
import logging 
from ativos.utils import processar_alertas
import logging

@shared_task
def tarefa_salvar_cotacoes():
    try:
        resultado = salvar_cotacoes()
        logging.info("Tarefa salvar_cotacoes concluída com sucesso.")
        return resultado
    except Exception as e:
        logging.error(f"Erro ao salvar cotações: {e}")
        raise
    
@shared_task
def tarefa_enviar_alertas():
    try:
        processar_alertas()
        logging.info("Tarefa enviar_alertas concluída com sucesso.")
    except Exception as e:
        logging.error(f"Erro ao enviar alertas: {e}")
        raise
