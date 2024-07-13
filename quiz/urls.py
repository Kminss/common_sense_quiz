from django.urls import path, include
from rest_framework.routers import DefaultRouter

from quiz.views import QuizViewSet


router = DefaultRouter()
router.register('quiz', QuizViewSet)

urlpatterns = [
    path('', include(router.urls))
]

quiz_list = QuizViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

quiz_detail = QuizViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})
