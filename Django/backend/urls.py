from django.contrib import admin
from django.urls import path
from api.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/suggest/', suggest_tasks,name="suggest"),  # app-level URLs include kar diye
    path('api/tasks/analyze/', analyze_tasks,name="analyze"),  # app-level URLs include kar diye
]
