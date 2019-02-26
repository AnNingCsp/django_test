from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article
def index(request):
    sitename = 'Django中文网'
    url = 'www.django.cn'
    # 新加一个列表
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    mydict = {
        'name': '陈森鹏',
        'qq': '111',
        'wx': 'AnNingcsp',
        'email': '1064241235@qq.com',
        'Q群': '1120',
    }
    context = {
        'sitename': sitename,
        'url': url,
        'list': list,  # 把list封装到context
        'mydict': mydict,
    }
    return render(request, 'index1.html', context)

def find_all(request):
    all_article = Article.objects.all()
    context = {'all_article': all_article}
    return render(request,'all_title.html',context=context)