from django.contrib import admin

from .models import Articles
from .models import Tags
from .models import Athoder
from .models import Category
from .models import My_selected
from .models import Comments
from .models import Repaly_comments
# Register your models here.

class AdminArticles(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Articles,AdminArticles)
admin.site.register(Tags)
admin.site.register(Athoder)
admin.site.register(Category)
admin.site.register(My_selected)
admin.site.register(Repaly_comments)
admin.site.register(Comments)

