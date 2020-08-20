from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from django.urls import get_resolver

import json
from http import HTTPStatus

from django_modelapiview import APIView, Token
from django_modelapiview.responses import APIResponse

# Create your views here.

from .models import User, Offer, BasketItem, Message, Image, Comment

class URLsView(View):
    def get(self, request, **kwargs):
        return APIResponse(HTTPStatus.OK, "URLs available", list(set(v[1] for v in get_resolver(None).reverse_dict.values())))

@method_decorator(csrf_exempt, "dispatch")
class LoginView(View):
    def post(self, request, **kwargs):
        data = request.body.decode('utf-8')
        json_data = json.loads(data)

        user = authenticate(username=json_data['username'], password=json_data['password'])
        if user is not None:
            token = Token({'uid': user.id})
            token.sign()
            return APIResponse(HTTPStatus.OK, "User logged in", {'token': str(token), 'user': user.serialize(request)})
        else:
            return APIResponse(HTTPStatus.UNAUTHORIZED, "Wrong user credentials")

class UserView(APIView):
    model = User
    route = "users"


class OfferView(APIView):
    model = Offer
    route = "offers"


class BasketItemView(APIView):
    model = BasketItem
    route = "basketitems"


class MessageView(APIView):
    model = Message
    route = "messages"


class ImageView(APIView):
    model = Image
    route = "images"

class CommentView(APIView):
    model = Comment
    route = "comments"

class Offers(TemplateView):
    template_name = "offers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offers'] = Offer.objects.all()
        return context

class Viewpost(TemplateView):
    template_name = "viewpost.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        id = self.kwargs['id']
        context['offer'] = Offer.objects.get(id=id)
        context['allmessages'] = Message.objects.all()
        return context


def LoginRequest(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/profile')
    else:
        print(username, password)
        return HttpResponseRedirect('/login')

def LogoutRequest(request):
    logout(request)
    return redirect('index')