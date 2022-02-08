from django.urls import path, re_path
from django.views.generic import UpdateView

from workdaymanagement import views
from workdaymanagement.forms import WorkdayForm
from workdaymanagement.models import Workday

app_name='Workday'
urlpatterns=[
   path('workdaylist',views.get_list.as_view(),name='workday_list'),
   path('<int:pk>',views.user_detail.as_view(),name="workday_detail"),
   path('new',views.WorkdayCreate.as_view()),
   path('<int:pk>/update',UpdateView.as_view(model=Workday,template_name='workday/workday_update.html',form_class=WorkdayForm))
]