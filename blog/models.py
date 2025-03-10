from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)  # Lien avec la table Image

    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length = 250)
    image = models.ImageField(null = True, blank = True, default = "img/default_article.png")
    introduction = models.TextField(null = True, blank = True)

    subtitle_1 = models.CharField(max_length = 250, null = True, blank = True)
    contenu_1 = models.TextField(null = True, blank = True)
    image_1 = models.ImageField(null = True, blank = True)

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    topics = models.ManyToManyField(Topic, blank = True)

    subtitle_2 = models.CharField(max_length = 250, null = True, blank = True)
    contenu_2 = models.TextField(null = True, blank = True)
    image_2 = models.ImageField(null = True, blank = True)

    subtitle_3 = models.CharField(max_length = 250, null = True, blank = True)
    contenu_3 = models.TextField(null = True, blank = True)
    image_3 = models.ImageField(null = True, blank = True)

    subtitle_4 = models.CharField(max_length = 250, null = True, blank = True)
    contenu_4 = models.TextField(null = True, blank = True)
    image_4 = models.ImageField(null = True, blank = True)

    def __str__(self):
        return f"{self.title[:50]}..." if len(self.title) > 50 else self.title


#
# class Comments(models.Model):
#     contain = models.TextField()
#     author = models.ForeignKey(User, on_delete = models.CASCADE)
#     article = models.ForeignKey(Article, on_delete = models.CASCADE)
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
#
#     date_updated = models.DateTimeField(auto_now = True)
#     date_created = models.DateTimeField(auto_now_add = True)
#
#     class Meta:
#         ordering = ['date_created']
#
#     def __str__(self):
#         return f"{self.contain[:80]}..." if len(self.contain) > 80 else self.contain
#
#
# class Reactions(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE) #, related_name='reactions')
#     type_reaction = models.CharField(
#         max_length=50,
#         choices=[
#             ("jaime", "Like"),
#             ("dislike", "Dislike"),
#         ]
#     )
#     date_reaction = models.DateTimeField(auto_now = True)
#
#     class Meta:
#         unique_together = ('author', 'article', 'type_reaction')  # Empêche plusieurs réactions du même type par utilisateur/publication
#
#     def __str__(self):
#         return f"{self.author} a réagi sur {self.article} avec {self.type_reaction}"
