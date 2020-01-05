from django.db import models
from django.utils import timezone

# Create your models here.


class Thread(models.Model):
    class Meta:
        verbose_name = "スレッド"
        verbose_name_plural = "スレッド"

    thread_name = models.TextField()
    thread_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.thread_name


class ResPost(models.Model):
    class Meta:
        verbose_name = "ポスト"
        verbose_name_plural = "ポスト"

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    post_user = models.CharField(default="名無しさん", max_length=50)
    post_text = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_text
