from django.urls import re_path
from api import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^pre-processed-images$', views.preProcessImageAPI),
    re_path(r'^pre-processed-images/([0-9]+)$', views.preProcessImageAPI),
    # re_path(r"^pre-processed-images/savefile", views.SaveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)