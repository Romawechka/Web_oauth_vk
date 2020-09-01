import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth import get_user_model


# Create your views here.
def login(request):
    if request.method == 'GET':
        if request.is_ajax():

            User = get_user_model()
            user_id = User.objects.filter(username=request.GET['username'])[0].id
            acc = SocialAccount.objects.filter(user_id=user_id)[0].id
            token = SocialToken.objects.filter(account_id=int(acc))[0].token

            # получаем от vk список рандомных друзей
            version = 5.92
            response = requests.get("https://api.vk.com/method/friends.get",
                                    params={
                                        'access_token': token,
                                        'v': version,
                                        'order': 'random',
                                        'count': 5
                                    })

            # список друзей
            list_friends = response.json()['response']['items']

            friends = []

            # получаем от vk информацию о каждом друге по id
            for id in list_friends:
                response = requests.get("https://api.vk.com/method/users.get",
                                         params={
                                             'access_token': token,
                                             'v': version,
                                             'user_ids': id,
                                             'fields': 'photo_50'
                                         })
                friends.append(response.json())

            return HttpResponse(json.dumps(friends, ensure_ascii=False))
        else:
            return render(request, 'me/me.html')