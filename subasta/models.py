from django.db import models
from users.models import Pasaje, CustomUser
# Create your models here.

class Subasta(models.Model):
    ValorSubastaActualizado = models.IntegerField(default='0')
    Puja = models.IntegerField(default='0')
    HoraI_Subasta = models.TimeField()
    HoraF_Subasta = models.TimeField()
    Fecha_Subasta = models.DateField()
    Estado_Subasta = models.BooleanField(default=False)
    Estado_Puja = models.BooleanField(default=False)
    Pasaje_A_Sub = models.ForeignKey(Pasaje, on_delete=models.CASCADE)
    Ultima_Puja = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def Pujar(self):
        self.ValorSubastaActualizado = self.ValorSubastaActualizado + self.Puja
        self.Estado_Puja = True
        self.save()

    def Cancelar(self):
        self.Estado_Subasta = True
        self.save()

    def ReactivarSub(self):
        self.Estado_Subasta = False
        self.save()
