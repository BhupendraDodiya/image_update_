from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index.as_view()),
    path('update/<int:uid>/',views.update),
    path('upd/',views.upd),
    path('table/',views.table),
    path('delete/<int:uid>/',views.delete,name='del'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
