from rest_framework import viewsets, mixins


class UpdateDestroyViewSet(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    pass


class UpdateDestroyCreateViewSet(mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.CreateModelMixin,
                                 viewsets.GenericViewSet):
    pass


class NoListViewSet(mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass
