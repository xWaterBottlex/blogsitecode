# generic vies


from rest_framework import generics, mixins
# from django.db.models import Q
# from rest_framework.filters import SearchFilter
from firstapp.models import Post
from .serializers import PostSerializer
from django.utils import timezone
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):
#     # DetailView
#     lookup_field = 'pk'  # slug, id url(<int>pk)
#     serializer_class = PostSerializer
#
#     # queryset = Post.objects.all()
#
#     def get_queryset(self, *args, **kwargs):
#         qs = Post.objects.all()
#         filter_backends = [SearchFilter]
#         search_fields = ['title', 'content']
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(Q(title__icontains=query) |
#                            Q(content__icontains=query)
#                            ).distinct()
#         return qs


class BlogPostApiView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Post.objects.all()
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        elif content is not None:
            queryset = queryset.filter(content__icontains=content)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        serializer.save(date_posted=timezone.now())

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    # DetailView
    lookup_field = 'pk'  # slug, id url(<int>pk)
    serializer_class = PostSerializer

    # queryset = Post.objects.all()

    def get_queryset(self):
        return Post.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)
