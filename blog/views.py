from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect
from django.views import generic
from .forms import CommentCreateForm
from .models import Post,Category,Comment

class IndexView(generic.ListView):
  model = Post
  paginate_by=10

#最新のものを上にもってくる
  def get_queryset(self):#order_by(-'フィールド名') フィールド名の降順
    queryset = Post.objects.order_by('-created_at')
    keyword = self.request.GET.get("keyword")#inputタグで指定したキーワード
    if keyword:
      queryset = queryset.filter(
        Q(title__icontains=keyword)|Q(text__icontains=keyword)#タイトルとテキストで両方検索している
      )#フィールド名__icontainsでその文字を含むものがヒットする
    return queryset

class CategoryView(generic.ListView):
  model = Post
  paginate_by = 10

  def get_queryset(self):
    category = get_object_or_404(Category,pk=self.kwargs['pk'])
    queryset = Post.objects.order_by('-created_at').filter(category=category)
    return queryset

class DetailView(generic.DetailView):
  model = Post

class CommentView(generic.CreateView):
  model = Comment
  form_class = CommentCreateForm

  def form_valid(self, form):
    post_pk = self.kwargs['post_pk']#urlにふくまれていくプライマリーキーを取得
    comment = form.save(commit=False)#データを保存する一日手前の情報を返してくれる。DBには保存されていない。
    comment.post = get_object_or_404(Post, pk=post_pk)#DBに保存する前だからデータにアクセスして書き換えができる
    comment.save()#ここでDBに保存
    return redirect('blog:detail', pk=post_pk)
