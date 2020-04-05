from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Post(models.Model):   # models는 POST가 장고 모델임을 의미. 이 코드때문에 장고는 POST가 DB에 저장되어야 한다고 알게 됨.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ForeignKey() : 다른모델에 대한 링크를 의미
    title = models.CharField(max_length = 200)  # CharField() : 글자수가 제한된 텍스트. 즉 제목같은 제한된 텍스트에서 사용 됨
    text = models.TextField()                   # TextField() : 글자수 제한이 없는 텍스트
    created_date = models.DateTimeField(default=timezone.now)   # DateTimeField() : 날짜와 시간을 의미
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title