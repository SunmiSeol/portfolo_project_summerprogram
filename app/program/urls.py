from django.urls import path
from program import views as program_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', tutorials_views.index, name='home'),
    path('', program_views.index.as_view(), name='home'),
    path('api/programs/', program_views.program_list),
    path('api/programs/<int:pk>/', program_views.program_detail),
    path('api/programs/open/', program_views.registration_open_list)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)