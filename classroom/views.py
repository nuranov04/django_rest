from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'teacher': reverse('teachers-list', request=request, format=format),
        'student': reverse('students-list', request=request, format=format),
        'courses': reverse('courses-list', request=request, format=format),
        'exercise': reverse('exercise-list', request=request, format=format),
        'exercise_file': reverse('exercise_file-list', request=request, format=format),
    })