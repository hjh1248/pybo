from django.core import serializers
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['author', 'subject', 'content', 'create_date', 'modify_date', 'voter']
    author = serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    created_date = serializers.DateTimeField(input_formats=["%Y-%m-%d"])
    created_date = serializers.DateTimeField(input_formats=["%Y-%m-%d"])
    voter = serializers.CharField(max_length=100)