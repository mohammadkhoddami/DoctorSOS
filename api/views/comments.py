from rest_framework.viewsets import ModelViewSet
from core.serializers import CommentSerializer
from core.models import Comment


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        doctor = self.kwargs['doctor_pk']
        return Comment.objects.filter(doctor=doctor).select_related('author')
    
    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['doctor_id'] = self.kwargs['doctor_pk']
        return response