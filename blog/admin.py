from django.contrib import admin

from . models import Article, Category, Topic
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin."""
    pass

    # list_display = []

    # def __init__(self, *arg):
    #     super(ArticleAdmin, self).__init__()
    #     self.arg = arg

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin."""
    pass

    # list_display = []

    # def __init__(self, *arg):
    #     super(CategoryAdmin, self).__init__()
    #     self.arg = arg

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin."""
    pass

    # list_display = []

    # def __init__(self, *arg):
    #     super(TopicAdmin, self).__init__()
    #     self.arg = arg
