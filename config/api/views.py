from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from api.models import preProcessedImages
from api.serializers import preProcessedImagesSerializer

from django.core.files.storage import default_storage

import cv2
import numpy as np
from tensorflow import keras
from keras.layers import Dense
from skimage.feature import hog
from keras.models import Sequential, load_model




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


# Define the function to calculate the siamese features of an image
def get_siamese_features(img):
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(image, (256, 256))
    return resized


class ImageUploadView(APIView):
    """ API to recieve images from UI and conduct machine learning tasks """
    parser_classes = [MultiPartParser]


    def post(self, request, format = None):
        # file1 = request.data['file1']
        # file2 = request.data['file2']

        # print("FILE 1: ", file1)
        # print("FILE 2: ", file2)

        file = request.data['file']
        print("FILE: ", file)
        
        # siamese_model = '../SeniorExperience/API/config/api/backend/siamese_model.h5'
        # # Load the trained Siamese network model (saved in previous code)
        # model = load_model(siamese_model)

        # # Compute the Siamese features of the images
        # siamese1 = get_siamese_features(file1)
        # siamese2 = get_siamese_features(file2)

        # # Create a numpy array with the input data
        # X1 = np.array([siamese1])
        # X2 = np.array([siamese2])

        # # Use the trained Siamese network to predict the similarity score between the two images
        # similarity_score = model.predict([X1, X2])[0][0]

        # # Output the percent similarity score
        # print("The percent similarity between the two images is " + str(similarity_score*100))

        return Response({'status': 'success'})
