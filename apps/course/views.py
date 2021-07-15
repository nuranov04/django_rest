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

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        course = self.get_object()
        return Response(course.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseHighlight(generics.GenericAPIView):
    queryset = Course.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        course = self.get_object()
        return Response(course.highlighted)


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

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        exercise = self.get_object()
        return Response(exercise.highlighted)


class ExerciseFileViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Exercise_file.objects.all()
    serializer_class = ExercisefileListSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        exercise_file = self.get_object()
        return Response(exercise_file.highlighted)


class ExerciseFileHighlight(generics.GenericAPIView):
    queryset = Exercise_file.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        exercise_file = self.get_object()
        return Response(exercise_file.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'exercise': reverse('exercise-list', request=request, format=format),
        'exercise_file': reverse('exercise_file-list', request=request, format=format)
    })


class ExerciseHighlight(generics.GenericAPIView):
    queryset = Exercise.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        exercise = self.get_object()
        return Response(exercise.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'course': reverse('course-list', request=request, format=format),
        'exercise': reverse('exercise-list', request=request, format=format)
    })


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = CourseListSerializer
