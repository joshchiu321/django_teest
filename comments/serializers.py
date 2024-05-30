from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['comment_id', 'user', 'station_no', 'create_time', 'updated_time', 'comment']
        read_only_fields = ['create_time', 'updated_time', 'user']
