from django.db import models

class PermissoesModelos(models.Model):

    class Meta:

        managed = False

        permissions = (
            ('modelos_permissoes', 'Permissão Global de Modelos'),
        )