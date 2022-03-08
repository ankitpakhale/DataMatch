from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, serializers,status
from rest_framework.response import Response
from .serializer import *
from rest_framework.views import APIView
import io
import csv

# Create your views here.

def index(request):
    return HttpResponse("Working Properly")   

class UploadCSVView(APIView):
    serializer_class =Uploadcsvserializer

    def post(self, request, *args, **kwargs):
        # login_user=request.user
        # serializer_class = self.get_serializer(data=request.data)
        serializer = Uploadcsvserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        print(file)
        decoded_file = file.read().decode()
        # upload_products_csv.delay(decoded_file, request.user.pk)
        io_string = io.StringIO(decoded_file)
        # reader = csv.reader(io_string)
        reader=csv.DictReader(io_string)
        a = 'ankit'
        for row in reader:
            print(row)
            try:
                m=Uploadcsv.objects.get(Hsn_code=row.get('HSN/SAC Code'),user=a)
                m.Rate=row.get('Rate/Unit')
                m.Hsn_code=row.get('HSN/SAC Code')
                m.Description=row.get('Description')
                m.CGst_rate=row.get('CGST Rate')
                m.SGst_rate=row.get('SGST Rate')
                m.IGst_rate=row.get('IGST Rate')
                m.Per=row.get('Per')
                m.save()
            except Uploadcsv.DoesNotExist:
                user = Uploadcsv(Hsn_code=row.get('HSN/SAC Code'),Description=row.get('Description'),Rate=row.get('Rate/Unit'),CGst_rate=row.get('CGST Rate'),SGst_rate=row.get('SGST Rate'),IGst_rate=row.get('IGST Rate'),Per=row.get('Per'),user=a)
                user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        query= Uploadcsv.objects.all()
        serializer=Uploadcsvserializer1(query,many=True)
        return Response(serializer.data)