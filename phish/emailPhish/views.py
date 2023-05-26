from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from django.template.loader import get_template
from django.http import HttpResponse 
from PIL import Image
from .serializers import GetDataSerializer


class SendTemplateMailView(APIView):

    def post(self, request, *args, **kwargs):
        email_list = ['ucw700@gmail.com','janavmakkar@gmail.com']
        for target_user_email in email_list:
            user = UserModel.objects.filter(email = target_user_email)
            
            if user is None :
                user = UserModel.create(email = target_user_email)
                user.save()
                print("Created - ",user.email)
            else:
                user = UserModel.objects.get(email = target_user_email)
                print("Already Exists - ",user.email)

            user = UserModel.get(email = target_user_email)

            print("\nSent to - ",user.email)
          
            context_data = dict()
            context_data["image_url"] = request.build_absolute_uri((f"image_load/{user.email}"))

            print("\nImage URL - ",context_data["image_url"])

            html_text = get_template("mail.html").render(context_data)

            subject, from_email, to = "innocent subject" , 'jhonnydoetest700@gmail.com',  [target_user_email]

            msg = EmailMultiAlternatives(subject, html_text, from_email, to)
            msg.content_subtype='html'
            msg.send()

        return Response({"success":True})


@api_view(['GET','POST','PUT','DELETE'])
def image_load(request, emailId):
    print("hit")
    # if request.method =='GET':
    print("\nImage Loaded\n")
    user = UserModel.objects.get(email=emailId)
    user.opened = True
    user.save()
    red = Image.new('RGB', (20, 20))
    response = HttpResponse(content_type="image/png" , status = status.HTTP_200_OK)
    red.save(response, "PNG")
    return response
       