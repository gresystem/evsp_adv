from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board
from evuser.models import Evuser

# Create your views here.

def boards_list(request):
  boards = Board.objects.all()

  return render(request, 'board_list.html', context={'boards': boards})

def boards_list2(request):
  boards = Board.objects.order_by('-register_dttm')

  def get_context_data(self, **kwargs):
    context = super(EvuserList, self).get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    # return context

  return render(request, 'board_list2.html', context={'boards': boards})

def boards_detail(request, board_id):
  board = get_object_or_404(Board, pk=board_id)

  return render(request, 'board_detail.html', context={'board': board})

@login_required
def board_write(request):
  errors = []
  if request.method == 'POST':
    title = request.POST.get('title', '').strip()
    content = request.POST.get('content', '').strip()
    image = request.FILES.get('image')

    if not title:
      errors.append('제목을 입력해 주세요')
    if not content:
      errors.append('내용을 입력해 주세요')
    if not errors:
      # user = get_object_or_404(Evuser, username=request.user)
      print(request.user)
      user = Evuser.objects.get(username=request.user)
      board = Board.objects.create(user=user, title=title, content=content, image=image)

      # path('board/<int:article_id>/<int:board_id>/', board_detail, name='board_detail'),
      # /board/%d/%board.id == reverse('board_detail', args=[post.id, article.id])
      return redirect(reverse('board_detail', kwargs={'board_id': board.id}))
  
  return render(request, 'board_write.html', {'user': request.user, 'errors': errors})

