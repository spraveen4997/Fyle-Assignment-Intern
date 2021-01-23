from django.shortcuts import render
from django.contrib.postgres.search import SearchRank
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import AppSerializer
from .models import Branches
from .models import Banks
# Create your views here.

class BankAPI(APIView):
    

    def get(self,request,ac):
        print(ac)
        q=request.GET['q']
        limit=int(request.GET['limit'])
        offset=int(request.GET['offset'])
        print(q,limit,offset)
        if ac=="autocomplete":
            op=Branches.objects.filter(branch__icontains=q).all().order_by('ifsc')[offset:offset+limit]
        elif ac=="":
            op=Branches.objects.filter(
                Q(branch__icontains=q) |
                Q(address__icontains=q) |
                Q(city__icontains=q) |
                Q(district__icontains=q) |
                Q(state__icontains=q) |
                Q(bank_name__icontains=q)).all()[offset:offset+limit]
        else:
            op=""
        serializer=AppSerializer(op,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        pass