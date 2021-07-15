from apps.course.models import *
from apps.course.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User
from apps.course.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'courses': reverse('course-list', request=request, format=format),
    })


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseListSerializer


class ExerciseFileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Exercise_file.objects.all()
    serializer_class = ExercisefileListSerializer


class ExerciseFileHighlight(generics.GenericAPIView):
    queryset = Exercise_file.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        exercise_file = self.get_object()
        return Response(exercise_file.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'course': reverse('course-list', request=request, format=format),
        'exercise': reverse('exercise-list', request=request, format=format),
        'exercise_file': reverse('exercise_file-list', request=request, format=format)
    })

