from django.shortcuts import render, redirect
from django.http import Http404
from django.core.paginator import Paginator
from user.models import User
from tag.models import Tag
from .models import Board
from .forms import BoardForm


def board_list(request):
    all_boards = Board.objects.all().order_by("-id")

    # Use paginator to get page information
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 5)
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # Get current user info
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            # Create board
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.author = user
            board.save()

            # Add tags
            tags = form.cleaned_data['tags'].split(',')
            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_detail(request, pk):
    # Check if board exists in DB
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404("The post you're looking for does not exist.")

    return render(request, 'board_detail.html', {'board': board})
