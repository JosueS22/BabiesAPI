from fuardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from babies.models import Baby
from events.models import Event
from babies.serializers import BabySerializer
from events.serializers import EventSerializer


# Create your views here.
def evaluate(user, obj, request):
    return user.username == obj.parent.username

class BabyViewSet(viewsets.ModelViewSet):
    queryset = Baby.object.all()
    serializer_class = BabySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name = 'BabyPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True
                },
                'instance': {
                    'retrieve': evaluate,
                    'destroy': evaluate,
                    'update': evaluate,
                    'partial_update': evaluate,
                    'events': evaluate,
                }
            }
        ),
    )

    def perform_create(self, serializer):
        baby = serializer.save()
        user = self.request.user
        assign_perm('babies.change_baby', user, baby)
        assign_perm('babies.view_baby', user, baby)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def events(self, request, pk=None):
        baby = self.get_object()
        response = []
        for event in Event.objects.filter(baby=baby):
            response.append(EventSerializer(event).data)
        return Response(response)

        