from urllib import parse
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import GenotypeSerializer
from .models import Genotype




def search_view(request):
    return render(request, 'geneplanetApi/search.html')


class SearchGenome(APIView):
    def get(self, request):

        isRs = request.GET.get("isRs")
        onlyChrom = request.GET.get("onlyChrom")
        genotypes = None
        
        if(isRs):
            query_string = request.GET.get("rsID")
            genotypes = Genotype.objects.filter(chrom_id__contains=query_string)
        elif(onlyChrom):
            query_string = request.GET.get("chrom")
            genotypes = Genotype.objects.filter(chrom__contains=query_string)
        # breakpoint()
        # query_string = request.GET.get("searchString")
        response = genotypes.values_list()
        return HttpResponse(response)
    def post(self, request):
        serializer = GenotypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)


class UpdateGenome(APIView):
    def get_objects(self, id):
        try:
            return Genotype.objects.get(id=id)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id):
        genotype = self.get_objects(id)
        serializer = GenotypeSerializer(genotype)
        return Response(serializer.data)
    def put(self, request, id):
        genotype = self.get_objects(id)
        serializer = GenotypeSerializer(genotype, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)