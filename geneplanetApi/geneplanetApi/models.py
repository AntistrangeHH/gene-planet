from django.db import models

class Genotype(models.Model):
    chrom = models.CharField(max_length=2)
    pos = models.IntegerField()
    chrom_id = models.CharField(max_length=25, primary_key=True)
    ref = models.CharField(max_length=128)
    alt = models.CharField(max_length=128)
    ch_format = models.CharField(max_length=256)
