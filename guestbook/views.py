from django.shortcuts import render
from guestbook.models import Guestbook
from django.http import HttpResponseRedirect

def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list':guestbook_list}
    return render(request, 'guestbook/list.html',context)

def add(reqeust):
    guestbook = Guestbook()
    guestbook.name = reqeust.POST['name']
    guestbook.password = reqeust.POST['pass']
    guestbook.message = reqeust.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook')

def deleteform(request):
    context = {'guestbook_id':request.GET['guestbookid']}

    return render(request, 'guestbook/deleteform.html',context)

def delete(request):
    Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST['password']).delete()
    return HttpResponseRedirect('/guestbook')