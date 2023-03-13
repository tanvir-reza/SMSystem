from django.db import models
import uuid



class Class(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name




class Student(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    roll_number = models.IntegerField(null=False, blank=False, unique=True, default=0)
    address = models.TextField(max_length=255, blank=True, null=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


