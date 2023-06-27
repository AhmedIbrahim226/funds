from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Article, ArticleSerializers
)
from ..models import ArticleStats
from rest_framework.response import Response
from ..utils import check_can_repeat_link_on_range_time

class ArticleApiView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    http_method_names = ('get', )

    def list(self, request, *args, **kwargs):
        # print(request.data)
        # print(request.user)
        # return Response({'ff': 'ggg'})
        serial = self.get_serializer(data=request.data)

        if serial.is_valid():
            is_read = serial.validated_data.get('is_read')
            received_decimal = serial.validated_data.get('received_decimal')
            link = serial.validated_data.get('link')

            check, article = check_can_repeat_link_on_range_time(link=link, user=request.user)
            if is_read:
                if check:
                    ArticleStats.objects.create(article=article, time=10, received_decimal=received_decimal)
                    data = {
                        'id': article.id,
                        'link': link,
                        'created_at': article.created_at
                    }
                    return Response(data)

                serial.save(owner=request.user)
                ArticleStats.objects.create(article=serial.instance, time=10, received_decimal=received_decimal)
                return Response(serial.data)

            return Response({'is_read': False})
        return Response(serial.errors)

