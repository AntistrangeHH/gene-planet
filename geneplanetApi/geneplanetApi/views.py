import re
from urllib import parse
from django.db.models.query import QuerySet
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GenotypeSerializer
from .models import Genotype


# View for rendering search page
def search_view(request):
    return render(request, 'geneplanetApi/search.html')


# API view for get method for search
class SearchGenome(APIView):
    def get(self, request):

        isRs = request.GET.get("isRs")
        onlyChrom = request.GET.get("onlyChrom")
        genotypes = None
        
        # queries only by rs id
        if(isRs == "true"):
            query_string = request.GET.get("rsID")
            genotypes = Genotype.objects.filter(chrom_id__startswith=query_string)[:50]

        # queries only by chrom (when user only types an integer in the input field)
        elif(onlyChrom == "true"):
            query_string = request.GET.get("chrom")
            genotypes = Genotype.objects.filter(chrom=query_string)[:50]

        # queries by chrom and pos simultaneously
        else:
            chrom = request.GET.get("chrom")
            pos = request.GET.get("pos")
            cond1 = Q(chrom=chrom)
            cond2 = Q(pos__startswith=pos)
            genotypes = Genotype.objects.filter(cond1 & cond2)[:50]
            
        response = list(genotypes.values_list())
        return JsonResponse(response, safe=False)
    def post(self, request):
        serializer = GenotypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


# This will be for the second part of the task
class UpdateGenome(APIView):
    def get_objects(self, id):
        try:
            return Genotype.objects.get(id=id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        genotype = self.get_objects(id)
        serializer = GenotypeSerializer(genotype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)