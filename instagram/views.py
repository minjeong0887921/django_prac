from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import ArchiveIndexView, DayArchiveView, DetailView, ListView, MonthArchiveView, YearArchiveView
from .models import Post


# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q :
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list' : qs,
#         'q' : q,
#     })


# def post_detail(request:HttpRequest, pk:int) -> HttpRequest:
#     # post = Post.objects.get(pk=pk)  # 없을 때는 DoesNotExist 예외
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'instagram/post_detail.html', {
#         'post': post,
#     })


# 장고 기본 제공 CBV 활용
# post_list = login_required(ListView.as_view(model=Post, paginate_by=3))
# post_detail = DetailView.as_view(
#     model=Post,
#     queryset=Post.objects.filter(is_public=True))


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post 
    paginate_by = 3 

class PostDetailView(DetailView):
    model = Post 

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs 

post_list = PostListView.as_view()
post_detail = PostDetailView.as_view()
post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at')
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)
# post_archive_month = MonthArchiveView.as_view(model=Post, date_field='created_at')
# post_archive_day = DayArchiveView.as_view(model=Post, date_field='created_at', month_format = '%m')