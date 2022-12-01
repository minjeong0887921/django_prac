from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# 첫 번째 방법 : 기본 ModelAdmin으로 동작
# admin.site.register(Post)  

# 두 번째 방법 : 지정한 ModelAdmin으로 동작
# class PostAdmin(admin.ModelAdmin):
#     pass 

# admin.site.register(Post, PostAdmin)

# 세 번째 방법
@admin.register(Post) # Wrapping : 감싼 대상의 기능을 변경할 수 있음
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message'] # 링크가 아이디에 잡히던 것은 메시지로 변경
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # 서치 옵션, 메시지를 이용해 필터링

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;" />')
        return None

    def message_length(self, post):
        return f"{len(post.message)} 글자"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass