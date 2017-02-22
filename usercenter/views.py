#!/usr/bin/env python
# coding: utf-8

from django.contrib import auth
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

from django.template import RequestContext

from usercenter.forms import LoginForm
from usercenter.models import Teacher


# 表单
# class UserForm(forms.Form):
#     username = forms.CharField(label='用户名', max_length=100)
#     password = forms.CharField(label='密码', widget=forms.PasswordInput())


# 注册
# def regist(req):
#     if req.method == 'POST':
#         uf = UserForm(req.POST)
#         if uf.is_valid():
#             # 获得表单数据
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             # 添加到数据库
#             Teacher.objects.create(username=username, password=password)
#             return HttpResponse('regist success!!')
#     else:
#         uf = UserForm()
#     return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))

# 登陆
# def login(req):
#     if req.method == 'POST':
#         uf = UserForm(req.POST)
#         if uf.is_valid():
#             # 获取表单用户密码
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             # 获取的表单数据与数据库进行比较
#             user = Teacher.objects.filter(username__exact=username, password__exact=password)
#             if user:
#                 # 比较成功，跳转index
#                 response = HttpResponseRedirect('/usercenter/index/')
#                 # 将username写入浏览器cookie,失效时间为3600
#                 response.set_cookie('username', username, 3600)
#                 return response
#             else:
#                 # 比较失败，还在login
#                 return HttpResponseRedirect('/online/login/')
#     else:
#         uf = UserForm()
#         return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))
#
#
# # 登陆成功
# def index(req):
#     username = req.COOKIES.get('username', '')
#     return render_to_response('index.html', {'username': username})
#
#
# # 退出
# def logout(req):
#     response = HttpResponse('logout !!')
#     # 清理cookie里保存username
#     response.delete_cookie('username')
#     return response

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('user/login.html', RequestContext(request, {'form': form}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                # return render_to_response('user/index.html', RequestContext(request))
                response = HttpResponseRedirect('/usercenter/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', username, 3600)
                return response
            else:
                return render_to_response('user/login.html',
                                          RequestContext(request, {'form': form, 'password_is_wrong': True}))
        else:
            return render_to_response('user/login.html', RequestContext(request, {'form': form, }))


def index(request):
    return render_to_response('user/index.html', RequestContext(request))
