from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from board.models import DevBoardBsc
# Create your views here.

def index(request):
    boards = {'boards': DevBoardBsc.objects.all()}
    return render(request, 'board/board_list.html', boards)


def post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        board = DevBoardBsc(title=title, content=content)
        board.save()
        return HttpResponseRedirect('/board')
    else:    
        return render(request, 'board/board_post.html')
    
def detail(request, id):
    try:
        board = DevBoardBsc.objects.get(pk=id)
    except DevBoardBsc.DoesNotExist:
        raise Http404("not exists");
    return render(request, "board/board_detail.html", {'board':board})