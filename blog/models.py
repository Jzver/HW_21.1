from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="заголовок")
    slug = models.CharField(max_length=150, verbose_name='URL', **NULLABLE)
    content = models.TextField(verbose_name="содержимое", **NULLABLE)
    preview = models.ImageField(upload_to="media/photo", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    published = models.BooleanField(default=True, verbose_name='опубликован')
    views = models.PositiveIntegerField(default=0, verbose_name='просмотры')

    def save(self, *args, **kwargs):
        if self.views is not None and self.views < 0:
            self.views = 0
        super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"