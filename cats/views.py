from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer, CatListSerializer

from rest_framework import mixins

from django.shortcuts import get_object_or_404

from djoser.views import UserViewSet

from .serializers import CustomUserSerializer


class CustomUserViewSet(UserViewSet):
    ... 

# class CatViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Cat.objects.all()
#         serializer = CatSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Cat.objects.all()
#         cat = get_object_or_404(queryset, pk=pk)
#         serializer = CatSerializer(cat)
#         return Response(serializer.data)



class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, url_path='recent-white-cats')
    def recent_white_cats(self, request):
        cats = Cat.objects.filter(color='White')[:5]
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return CatListSerializer
        return CatSerializer






class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class CreateRetrieveViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass 

class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer









'''
from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
'''
