from .models import Header, Category, Tours, Article, Networks, Comment, Footer
from rest_framework.viewsets import ModelViewSet
from .serializers import (HeaderSerializer, CategorySerializer, ToursSerializer,
                          ArticleSerializer, NetworksSerializer, CommentSerializer,
                          FooterSerializer)

from .permissions import CustomPermission


class HeaderView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [CustomPermission]


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermission]


class ToursView(ModelViewSet):
    queryset = Tours.objects.all()
    serializer_class = ToursSerializer
    permission_classes = [CustomPermission]


class ArticleView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [CustomPermission]


class NetworksView(ModelViewSet):
    queryset = Networks.objects.all()
    serializer_class = NetworksSerializer
    permission_classes = [CustomPermission]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CustomPermission]


class FooterView(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    permission_classes = [CustomPermission]






