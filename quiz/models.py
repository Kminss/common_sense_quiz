from django.db import models
from common.models import CommonModel


# Create your models here.
class Quiz(CommonModel):
    ETC = "ETC"
    HISTORY = "HIS"
    GENERAL = "GEN"
    SCIENCE = "SCI"
    CATEGORY_CHOICES = (
        ("ETC", "기타"),
        ("HIS", "역사"),
        ("GEN", "일반"),
        ("SCI", "과학"),
    )

    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, verbose_name="카테고리명", default=ETC)
    title = models.CharField("제목", max_length=300, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.title}"


class Answer(CommonModel):
    quiz = models.ForeignKey(Quiz, related_name="answers", verbose_name="질문", on_delete=models.CASCADE, null=False)
    content = models.CharField(verbose_name="내용", max_length=100, null=False, blank=False)
    is_correct = models.BooleanField("정답여부", null=False)
