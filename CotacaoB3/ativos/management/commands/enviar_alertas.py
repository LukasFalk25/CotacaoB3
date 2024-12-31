from django.core.management.base import BaseCommand
from ativos.utils import enviar_alertas

class Command(BaseCommand):
    help = "Envia alertas de e-mail com base nas cotações dos ativos"

    def handle(self, *args, **kwargs):
        enviar_alertas()