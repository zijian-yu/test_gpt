from django.db import models


class Post(models.Model):
    title = models.CharField('标题', max_length=120)
    content = models.TextField('内容')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
