from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('漢字/',views.kanji,name='kanji'),
    path('test/',views.test,name='test'),
    path('収斂/',views.conversation,name='conversation')
]
