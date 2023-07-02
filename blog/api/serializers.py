from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    fields = "__all__"
    readonly = ["modified_at","created_at"]
    