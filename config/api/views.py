from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, filters, generics
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from api.models import preProcessedImages, newTable
from api.serializers import preProcessedImagesSerializer, newTableSerializer

from django.core.files.storage import default_storage


def mainpage(request):
    return Response("Hello, world! This is the main page")

@csrf_exempt
def preProcessImageAPI(request, id=0):
    if request.method=='GET':
        images = preProcessedImages.objects.all()
        serializer = preProcessedImagesSerializer(images, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        image_data = JSONParser().parse(request)
        serializer = preProcessedImagesSerializer(data=image_data)
        if serializer.is_valid():
            serializer.save() # Save to DB
            return JsonResponse("Successfully Added Image", safe=False)
        return JsonResponse("Failed to Add New Image", safe=False)
    elif request.method=='PUT':
        image_data = JSONParser().parse(request)
        image = preProcessedImages.objects.get(imageID=image_data['imageID'])
        serializer = preProcessedImagesSerializer(image, data=image_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Successfully Updated Image", safe=False)
        return JsonResponse("Failed to Update Image", safe=False)
    elif request.method=='DELETE':
        image = preProcessedImages.objects.get(imageID=id)
        image.delete()
        return JsonResponse("Successfully Deleted Image", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


class newTableView(viewsets.ModelViewSet):
    queryset = newTable.objects.all()
    serializer_class = newTableSerializer

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ['=image_type']
