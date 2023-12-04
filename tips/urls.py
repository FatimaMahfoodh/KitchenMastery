from django.urls import path
from .views import AddTipView
from .views import TipsView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'tips'
urlpatterns = [
    path('',TipsView.as_view(),name='tips'),
    path('add_tip/',AddTipView.as_view(), name='add_tip'),
]+ static (settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
