from rest_framework import serializers
from .models import Genotype

# Work in progress
class GenotypeSerializer(serializers.Serializer):
    class Meta:
        model = Genotype
        fields = ['chrom', 'pos', 'chrom_id', 'ref', 'alt', 'ch_format']    