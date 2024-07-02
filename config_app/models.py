from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.DateField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    experience = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
class Students(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    parents_phone_number = models.IntegerField()
    telegram_link = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
