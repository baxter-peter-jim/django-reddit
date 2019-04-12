from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment
from .models import User
from .models import Profile
from .models import Save
from .models import Post_Vote
from .models import Comment_Vote
from .models import Moderator

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Save)
admin.site.register(Post_Vote)
admin.site.register(Comment_Vote)
admin.site.register(Moderator)
