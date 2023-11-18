from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post) # ba in ravesh ham mishe register kard model ro
class PostAdmin(admin.ModelAdmin):# ba sakht in class migim dar panell admin che namayesh az har object bede
    list_display = ('title', 'status','datetime_modified', )
    ordering = ('status', )# ('-status', ) : ba gozashtan "-" posht mored ordering bar aks mishe moratab kardan


#admin.site.register(Post , PostAdmin)