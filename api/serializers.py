from rest_framework import serializers
from firstapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    # this class helps us convert the Post data into JSON
    # also validates data passed
    # this works just like forms
    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'content',
            'date_posted',
            'author',
        ]
        read_only_fields = ['author', 'date_posted']

    def get_url(self, obj):
        return obj.get_api_url()

    def validate_title(self, value):
        qs = Post.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The title has already been created.")
        return value


