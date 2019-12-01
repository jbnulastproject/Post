from .models import Essay
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Essay
        fields = '__all__'
        # fields = ('id', 'title', 'contents')
        write_only_fields = ('title',)