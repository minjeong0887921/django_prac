from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from .models import Post


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
post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)