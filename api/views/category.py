from django.utils.functional import cached_property
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from core.models import Category
from core.serializers import CategorySerializer




class CategoryListView(APIView):
    serializer_class = CategorySerializer
    
    
    def get(self, request):
        #-interaction with database-
        categories = Category.objects.all()
        #-interaction with serializer
        serializer = self.serializer_class(categories, many=True) 
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class CategoryDetailView(APIView):
    serializer_class = CategorySerializer
    
    
    #Django Classic  
    # def setup(self, request: HttpRequest, *args: Any, **kwargs: Any) -> None:
    #     self.category = get_object_or_404(Category, pk=kwargs['pk'])
    #     return super().setup(request, *args, **kwargs)
    
    #REST FRAMEWORK
    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs['pk'])
    
    # @cached_property
    # def category(self):
    #     return get_object_or_404(Category, pk=self.kwargs['pk'])
    
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()            
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()
        return Response({'detail': 'Category deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)