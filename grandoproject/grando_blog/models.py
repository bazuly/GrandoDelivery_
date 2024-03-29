from django.db import models

# сделать приложение с возможными претензиями
class Category(models.Model):
    CATEGORIES_CHOICES = [
        ('Претензии', 'Претензии')
    ]
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return f'{self.title} успешно добавлен'


class Comment(models.Model):
    author = models.CharField(max_length=128)  # сделать чтобы тут был залогиненый юзер
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} успешно добавил комментарий в {self.post}'
