from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'surveys', SurveyViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'sumbitions', SumbitionViewSet)
router.register('ratings', AddRatingViewSet)
router.register(r'likes', LikeView)
router.register(r'info_users', InfoUserViewSet)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('', include(router.urls)),
    path('reviews/', ReviewCreateView.as_view()),
]