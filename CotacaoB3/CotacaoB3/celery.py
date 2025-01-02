#Estático 

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CotacaoB3.settings')

app = Celery('CotacaoB3')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega tarefas registradas
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'salvar-cotacoes-tarefa': {
        'task': 'ativos.tasks.tarefa_salvar_cotacoes', 
        'schedule': crontab(minute='*/1'),  
    },
        'enviar-alertas-tarefa': {
        'task': 'ativos.tasks.tarefa_enviar_alertas',  
        'schedule': crontab(minute='*/5'),  
    },
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

