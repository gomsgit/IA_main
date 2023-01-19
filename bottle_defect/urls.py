from django.urls import path
from . import views as bottle_views
# from ..capsule import views as capsule_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', bottle_views.login_user, name='login'),
    path('select', bottle_views.select, name='select'),
    path('image_upload', bottle_views.image_upload, name='image_upload'),
    path('category_list', bottle_views.category_list, name='category_list'),
    path('batch_detail', bottle_views.batch_detail, name='batch_detail'),
    path('introduction', bottle_views.introduction, name='introduction'),
    path('upload_file', bottle_views.upload_file, name='upload_file'),
    path('result', bottle_views.result, name='result'),
    path('detail', bottle_views.detail, name='detail'),
    path('prac', bottle_views.prac, name='prac'),
    path('test', bottle_views.test, name='test'),
    # path('upload_transistor', transistor_view.upload_transistor, name='upload_transistor'),
    path('logout', bottle_views.logout_user, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print("urlllllllll",static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))