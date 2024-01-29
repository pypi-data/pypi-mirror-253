from django.contrib import admin
from Users.models.post import Post
from Users.models.comment import Comment
from Users.models.post_tags import DomainTag
from Users.models.user_details import User
from Users.models.reactions import Reaction
from Users.models.domains import Domain
from Users.models.domain_experts import DomainExpert
from Users.models.user_following_domains import UserFollowingDomain


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'profile_pic_url')


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'post_title', 'Posted_By')

    def Posted_By(self, obj):
        return obj.posted_by.username


class DomainPostsAdmin(admin.ModelAdmin):
    list_display = ('post', 'domain')


class UserPostAdmin(admin.ModelAdmin):
    list_display = ('User_ID', 'Post_ID')

    def User_ID(self, obj):
        return obj.user.user_id

    def Post_ID(self, obj):
        return obj.post_id.post_id


class UserFollowingDomainAdmin(admin.ModelAdmin):
    list_display = ('User_Name', 'DOMAIN_Name')

    def User_Name(self, obj):
        return obj.user.username

    def DOMAIN_Name(self, obj):
        return obj.domain.domain_name


class DomainsAdmin(admin.ModelAdmin):
    list_display = ('domain_id', 'domain_name')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'comment_text', 'Post_ID', 'User_ID')

    def Post_ID(self, obj):
        return obj.post_id

    def User_ID(self, obj):
        return obj.commented_by.user_id


# class ReactionAdmin(admin.ModelAdmin):
#     list_display = ('__all__',)

class DomainExpertAdmin(admin.ModelAdmin):
    list_display = ('User_ID', 'Domain_ID')

    def User_ID(self, obj):
        return obj.user.user_id

    def Domain_ID(self, obj):
        return obj.domain.domain_name


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(DomainTag)
admin.site.register(Domain, DomainsAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserFollowingDomain, UserFollowingDomainAdmin)
admin.site.register(Reaction)
admin.site.register(DomainExpert, DomainExpertAdmin)