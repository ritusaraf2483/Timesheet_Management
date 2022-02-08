from django.urls import path

from usermanagement import views

app_name = 'Users'
urlpatterns=[
    path('userslist',views.users_list.as_view())
]