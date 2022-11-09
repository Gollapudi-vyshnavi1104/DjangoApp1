from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
# from django.db import models


# # Create your views here.
# from rest_framework import viewsets
# from myapp.serializers import AssetSerializer
# from myapp.models import Asset

# class AssetViewSet(viewsets.ModelViewSet):
#     id = Asset.objects.all()
#     asset_id = Asset.objects.all()
#     asset_name = Asset.objects.all()
#     asset_stat = Asset.objects.all()
#     segment_id = Asset.objects.all()
#     route_id = Asset.objects.all()
#     route_name = Asset.objects.all()
#     route_class = Asset.objects.all()
#     county_id = Asset.objects.all()
#     division_id = Asset.objects.all()
#     serializer_class = AssetSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AssetSerializer
from .models import Asset
'''
class Assetviews(APIView):
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, id=None):
    #     if id:
    #         item = Asset.objects.get(id=id)
    #         serializer = AssetSerializer(item)
    #         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    #     items = Asset.objects.all()
    #     serializer = AssetSerializer(items, many=True)
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):  
        result = Asset.objects.all()  
        serializers = AssetSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  

    
    # def patch(self, request, id=None):
    #     item = Asset.objects.get(id=id)
    #     serializer = AssetSerializer(item, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status": "success", "data": serializer.data})
    #     else:
    #        return Response({"status": "error", "data": serializer.errors})
    '''


from .serializers import AssetSerializer
from .models import Asset

class Assetviews(APIView):
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	
	
    def get(self, request, id=None):
        if id:
            item = Asset.objects.get(id=id)
            serializer = AssetSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Asset.objects.all()
        serializer = AssetSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    
    def patch(self, request, id=None):
        item = Asset.objects.get(id=id)
        serializer = AssetSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

