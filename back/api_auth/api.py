from ninja import NinjaAPI, File
from ninja.files import UploadedFile
from ninja import Form
from ninja import Schema
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import PermissionDenied
from ninja.security import django_auth
import vue_view.views
from api_auth.models import Picture
from back.settings import REDIRECT_BASE, DEBUG
from django.shortcuts import redirect
from back import settings

if settings.DEBUG:
    medial_url = '/' + settings.MEDIA_URL
else:
    medial_url = ''

#########


api = NinjaAPI(csrf=True, auth=django_auth, urls_namespace='api_auth')

from api_auth.models import Picture, ProfilePic

@api.get("/hi")
def hello(request):
    # user = User.objects.get(username=data.current_user_page[6:-1])
    pic = ProfilePic.objects.get(user_id=request.user.id)
    pic = medial_url+str(pic.pic)
    return api.create_response(request, {'success': True, "message": "Hii, you're still logged in!", 'username': request.user.username, "profile_pic_src": pic}, status=200)

from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
@api.get("/x-csrf-token")
def get_x_csrf_token(request, response: HttpResponse):
    response['x-csrftoken'] = get_token(request)
    return response

@api.get("/logout")
def log_out(request):
    logout(request)
    return redirect(REDIRECT_BASE)

@api.post("/change-username")
def sign(request, usern: str = Form(...)):
    user = request.user
    user.username = usern
    user.save()
    return redirect(request.headers['Referer'])

@api.post("/change-email")
def sign(request, email: str = Form(...)):
    user = request.user
    user.email = email
    user.save()
    return redirect(request.headers['Referer'])

@api.post("/change-password")
def sign(request, passw: str = Form(...)):
    user = request.user
    user.set_password(passw)
    user.save()
    return redirect(request.headers['Referer'])

from ninja import NinjaAPI, File
from ninja.files import UploadedFile

@api.post("/upload-pics")
def upload_user_pics(request, profile_pic_file: UploadedFile = File(...)): # atributo name del input tiene que ser igual a pic_file
    # user = User.objects.get(pk=request.user.id)
    Picture.objects.create(user=request.user, pic=profile_pic_file)
    return redirect(request.headers['Referer'])

@api.post("/upload-profile-pic")
def upload_profile_pic(request, page_pic_file: UploadedFile = File(...)): # atributo name del input tiene que ser igual a pic_file
    Picture.objects.update_or_create(user=request.user, pic=page_pic_file)
    return redirect(request.headers['Referer'])

