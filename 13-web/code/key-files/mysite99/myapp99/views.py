from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# 接收用户的请求，采用标准的httpreponse返回数据
def index(request):
    # 这里处理模型
    return HttpResponse("Hello Django") # 模版