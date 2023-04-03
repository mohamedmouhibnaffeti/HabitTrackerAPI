from django.urls import path, include
from .views import PersonViewSet, UserViewSet, TasksViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
#PersonList, PersonDetails, Person_List

router = DefaultRouter()
router.register('persons', viewset = PersonViewSet, basename='persons')
router.register('users', viewset = UserViewSet)
router.register('tasks', viewset=TasksViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token),
    ]
"""

    path('persons/', PersonList.as_view()),
    path('persons/<int:id>', PersonDetails.as_view()),
path('persons', Person_List),""" 