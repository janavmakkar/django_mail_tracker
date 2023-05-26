from django.urls import path
from .views import SendTemplateMailView , image_load 

urlpatterns = [
    # path('send_text/', send_email, name='index'),
    # path('send/render_image/',render_image, name='render_image'),

    path('send_html/', SendTemplateMailView.as_view(), name='send_template'),
    path('send_html/image_load/<str:emailId>/',image_load, name='image_load'),
]