# Create your models here.
from django.db import models
from django.utils import timezone

class MkPro(models.Model):
    UNIVERSITY = (
            ('UFRN','Universidade Federal do Rio Grande do Norte'),
            ('UERN','Universidade Estadual do Rio Grande do Norte'),
            ('IFRN','Instituto Federal de Educação Ciência e Tecnologia do Rio Grande do Norte'),
    )
    STARS = (
        ('1','1 ESTRELA'),
        ('2','2 ESTRELAS'),
        ('3','3 ESTRELAS'),
        ('4','4 ESTRELAS'),
        ('5','5 ESTRELAS'),
    )
    name = models.CharField(max_length=144)
    institution  = models.CharField(
            max_length = 4,
            choices = UNIVERSITY,
    )
    stars = models.CharField(
            max_length = 1,
            choices = STARS,
    )
    published_date = timezone.now()
