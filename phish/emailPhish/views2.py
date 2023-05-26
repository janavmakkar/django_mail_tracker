from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import UserModel
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from django.template import Context
from django.template.loader import get_template

# Create your views here.

@api_view(['GET'])
def send_email(request):
    subject = "Test email"
    message = "This is a test email"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["ucw700@gmail.com"]
    try:
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False,
            # html_message=template
        )
    except Exception as e:
        print(e)
        return Response({"message": "error"})
    return Response({"message": "Email has been sent!"},status=200)

class SendTemplateMailView(APIView):
     def post(self, request, *args, **kwargs):
           subject = "Test email with very small image"
           email_from = settings.EMAIL_HOST_USER
           recipient_list = ["ucw700@gmail.com"]
           target_email = request.data.get('email')
           mail_template = get_template("mail.html")
           print(target_email)
        #    if_existing_user = UserModel.objects.filter(email=target_email)
        #    if if_existing_user:
        #        return Response({"message": "user already exists"}, status=400)  
               
           params = dict()
           params["image_url"] = request.build_absolute_uri(("render_image"))
           html_detail = mail_template.render(params)

           msg = EmailMultiAlternatives(subject, html_detail, email_from, recipient_list)
           msg.content_subtype='html'
           msg.send()
           return Response({"success":True})
     
api_view()
def render_image(request):
     if request.method =='GET':
        image= Image.new('RGB', (20, 20))
        response = HttpResponse(content_type="image/png" , status = status.HTTP_200_OK)
        user = UserModel.objects.get(id=1)
        print(user)
        user.status = True
        user.save()
        image.save(response, "PNG")
        return response