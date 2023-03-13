from django.db import models
from academic.models import Student, Subject, Class
import uuid


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    score = models.IntegerField(default=0)
    

    class Meta:
        unique_together = ['student','subject']
                           

    def __str__(self):
        return self.student.first_name