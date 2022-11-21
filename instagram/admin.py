from django.contrib import admin
from .models import Post


# 첫 번째 방법 : 기본 ModelAdmin으로 동작
# admin.site.register(Post)  

# 두 번째 방법 : 지정한 ModelAdmin으로 동작
# class PostAdmin(admin.ModelAdmin):
#     pass 

# admin.site.register(Post, PostAdmin)

# 세 번째 방법
@admin.register(Post) # Wrapping : 감싼 대상의 기능을 변경할 수 있음
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length', 'is_public','created_at', 'updated_at']
    list_display_links = ['message'] # 링크가 아이디에 잡히던 것은 메시지로 변경
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # 서치 옵션, 메시지를 이용해 필터링

    def message_length(self, post):
        return f"{len(post.message)} 글자"