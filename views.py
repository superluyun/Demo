from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from collections import Counter
import json
from django.core import serializers
import os
# Create your views here.
def index_view(request):
    return render(request,'bar-simple.html')
def server_view(request):
    # uname = request.POST['uname']
    return HttpResponse("<script type='text/javascript' src='../static/js/bar.js'></script>")

def test_views(request):
    prov = IndexCtable.objects.filter(pid=0)
    i = 0
    j = 0
    citys = []
    couns = []

    for p in prov:
        i += 1

    for c in range(i):
        cityss = IndexCtable.objects.filter(pid = prov[c].id)
        for i in cityss:
            citys.append(i)

    for city in citys:
        counss = IndexCtable.objects.filter(pid = citys[j].id)
        j += 1
        for co in counss:
            couns.append(co)

    #-----------------------------------------------------------------------------------------------
    Clist = []
    c_num = []
    f = IndexFlaut.objects.values_list("local").annotate(Count("id"))
    #>>[(5, 2), (6, 2), (8, 1), (11, 1)]
    for i in f:
        a = IndexCtable.objects.filter(id=i[0])
        for x in range(i[1]):
            Clist.append(IndexCtable.objects.filter(id=a[0].pid)[0].cname)
            #>>Counter({'济南市': 3, '杭州市': 2, '青岛市': 1})
    c = Counter(Clist).most_common(len(Clist))
    for x in c:
        c_num.append({x[0]:x[1]})
    print(c_num)
    return render(request,'test.html',locals())

def show_line(request):
    return render(request,"lines.html")
def show_lines(request):
    Llist = []
    city = IndexCtable.objects.filter(cname="济南市")
    pid = city[0].id
    lines = IndexCtable.objects.filter(pid = pid)
    for line in lines:
        Llist.append({"value":len(IndexFlaut.objects.filter(local_id=line.id)),"name":line.cname})
    print(Llist)
    jsonstr = json.dumps(Llist)

    return HttpResponse(jsonstr)

def show_lines2(request):
    Llist = []
    city = IndexCtable.objects.filter(cname="杭州市")
    pid = city[0].id
    lines = IndexCtable.objects.filter(pid = pid)
    for line in lines:
        Llist.append({"value":len(IndexFlaut.objects.filter(local_id=line.id)),"name":line.cname})
    print(Llist)
    jsonstr = json.dumps(Llist)

    return HttpResponse(jsonstr)

def page(request):

    return render(request,"page.html")
def page_server(request):
    page = request.GET["page"]
    start = 15*(int(page)-1)
    end = 15*int(page)
    c  = Citys.objects.all()[start:end] #0:2 2:4 4:6
    jsonStr = serializers.serialize('json',c)
    print(jsonStr)
    return  HttpResponse(jsonStr)
def file(request):
    return  render(request,"file.html")

def file_server(request):

    myFile = request.FILES.get("myfile") # 获取上传的文件，如果没有文件，则默认为None
    print(myFile)
    destination = open(os.path.join("E:", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    return HttpResponse("upload over!")

def city(request):
    page = request.GET["page"]
    start = 15 * (int(page) - 1)
    end = 15 * int(page)

    c = Citys.objects.all()[start:end]
    jsonStr = serializers.serialize('json', c)
    print(jsonStr)
    return HttpResponse(jsonStr)