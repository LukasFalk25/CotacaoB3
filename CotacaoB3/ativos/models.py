from django.db import models

class Ativo(models.Model):
    nome = models.CharField(max_length=20)
    codigo = models.CharField(max_length=10, unique=True)
    limite_inferior = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    limite_superior = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    periodicidade = models.PositiveIntegerField(help_text="Periodicidade em minutos")
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"
    
class Cotacao(models.Model):
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE, related_name="cotacoes")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.ativo.codigo} - {self.preco} ({self.data_hora})"