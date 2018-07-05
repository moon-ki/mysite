from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from board.models import Board

#게시판 리스트
def index(request):
    board_list = Board.objects.all().order_by('-regdate')
    context = {'board_list': board_list}
    return render(request, 'board/list.html', context)

#게시판 등록 화면
def writeform(request):
    return render(request, 'board/write.html')

#게시판 등록 TX
def write(request):
    board = Board()
    board.title = request.POST['title']
    board.content = request.POST['content']
    board.user_id = str(request.session['authuser']['id'])

    board.save()

    return HttpResponseRedirect('/board')

#게시물 detail
def view(request):
    board_view = Board.objects.filter(id=request.GET['boardid'])
    board_view = model_to_dict(board_view[0])
    context = {'board_view':board_view}
    return render(request, 'board/view.html', context)

#게시물 수정
def modifyform(request):
    board_view = Board.objects.filter(id=request.GET['boardid'])
    board_view = model_to_dict(board_view[0])
    context = {'board_view':board_view}
    return render(request, 'board/modify.html',context)

def modify(request):
    modify_data = Board.objects.get(id=request.POST['boardid'])
    modify_data.title=request.POST['title']
    modify_data.content=request.POST['content']
    modify_data.save()

    return HttpResponseRedirect('/board/view?boardid='+request.POST['boardid'])

#게시물 delete TX
def delete(request):
    Board.objects.filter(id=request.GET['boardid']).delete()
    return HttpResponseRedirect('/board')
