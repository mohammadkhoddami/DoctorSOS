from rest_framework import serializers
from core.models import Comment, Patient
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.user.username')
    class Meta:
        model = Comment
        fields = ['body', 'author']
        
        
    def create(self, validated_data):
        user = self.context.get('request').user #type: ignore
        patient = Patient.objects.get(user=user)
        doctor = self.context.get('doctor_id')
        
        # if not user.is_authenticated:
        #     raise serializers.ValidationError('You must auth first')
        
        return Comment.objects.create(author=patient, doctor_id=doctor, **validated_data)