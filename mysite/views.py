from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect

from backend.models import *

class Index(View):
    def get(self, request):
        return render(request,'index.html')

class MakePost(View):
    def post(self, request):
        text = request.POST.get("post")
        new_post = Post(text=text)
        new_post.save()
        newDict = []
        newDict.append(new_post)
        return render(request,'view.html')

