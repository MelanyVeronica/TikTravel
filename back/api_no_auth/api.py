


from ninja import NinjaAPI
from ninja import Form
from ninja import Schema
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.sessions.backends.db import SessionStore
from django.core.exceptions import PermissionDenied
from ninja.security import django_auth
from back.settings import REDIRECT_BASE
from django.shortcuts import redirect
from django.db.utils import IntegrityError
from back import settings
from django.core.exceptions import ObjectDoesNotExist
from back.settings import REDIRECT_BASE, DEBUG

if settings.DEBUG:
    medial_url = '/' + settings.MEDIA_URL
else:
    medial_url = settings.REDIRECT_BASE


api = NinjaAPI(csrf=False)
session = SessionStore()

# def home(request, template):
#     response = render(request, template)  # django.http.HttpResponse
#     response.set_cookie(key='id', value=1)
#     return response

@api.get("/hi")
def hello(request):
    return "Hiii (no auth) - " + repr(request)

# cada atributo name del input tiene que ser igual a lo que aparece abajo
class UserSignIn(Schema):
    usern: str = None
    passw: str = None
    email: str = None

@api.post("/sign") # 
def sign(request, user_in: UserSignIn = Form(...)):
    try:
        User.objects.create_user(username=user_in.usern, email=user_in.email, password=user_in.passw)
        return redirect(REDIRECT_BASE+'login')
    except IntegrityError:
        return api.create_response(request, {'success': False, "message": "User or email already registered"}, status=406)

# cada atributo name del input tiene que ser igual a lo que aparece abajo
class UserLogIn(Schema):
    usern: str = None
    passw: str = None
    
@api.post("/log")
def log(request, user_in: UserLogIn = Form(...)):
    try:
        user = authenticate(username=user_in.usern, password=user_in.passw)
        login(request, user)
        # return api.create_response(request, {'success': True, "message": "Logged in!"}, status=200)
        return redirect(REDIRECT_BASE)
    except PermissionDenied:
        return api.create_response(request, {'success': False, "message": "Incorrect credentials"}, status=401)
    except AttributeError:
            try:
                User.objects.get(username=user_in.usern)
            except User.DoesNotExist:
                return api.create_response(request, {'success': False, "message": "Incorrect credentials"}, status=404)
    

from api_auth.models import Picture, ProfilePic

class UserAtPage(Schema):
    current_user_page: str

# @api.post('/user-pics')
# def user_pics(request):
#     pics = Picture.objects.all()
#     # return {'pics_src': [i.url for i in pics]}

@api.post('/profile-pic')
def user_profile_pic(request, data: UserAtPage):
    try:
        user = User.objects.get(username=data.current_user_page[6:-1])
        pic = ProfilePic.objects.get(user_id=user.id)
        pic = medial_url+str(pic.pic)
        return api.create_response(request, {'success': True, "profile_pic_src": pic}, status=200)
    except User.DoesNotExist:
        try:
            user = User.objects.get(username=request.user.username)
            pic = ProfilePic.objects.get(user_id=user.id)
            pic = medial_url+str(pic.pic)
            return api.create_response(request, {'success': True, "profile_pic_src": pic}, status=200)
        except User.DoesNotExist:
            return api.create_response(request, {'success': False, "message": "User does not exist"}, status=404)

@api.post('/userpage-pics')
def userpage_pictures(request, data: UserAtPage):
    try:
        user = User.objects.get(username=data.current_user_page[6:-1])
        pics = [(medial_url+str(i.pic)) for i in Picture.objects.filter(user_id=user.id)]
        return api.create_response(request, {'success': True, "userpage_pics_srcs": pics}, status=200)
    except User.DoesNotExist:
        return api.create_response(request, {'success': False, "message": "User does not exist"}, status=404) 

import random

@api.post("/discover-pics")
def get_discover(request): # atributo name del input tiene que ser igual a pic_file
    data = []
    users_queryset = User.objects.all()
    # random.shuffle(users_queryset)
    for i in users_queryset:
        try:
            profile_pic = ProfilePic.objects.get(user_id=i.id)
            profile_pic = medial_url+str(profile_pic.pic)
            user_pics = [(medial_url+str(i.pic)) for i in Picture.objects.filter(user_id=i.id)]
            random.shuffle(user_pics)
            data.append({'user_pics': user_pics[:7], 'username': i.username, 'profile_pic': profile_pic})
        except ObjectDoesNotExist:
            continue
    return api.create_response(request, {'success': True, "discover_data": data}, status=200)
