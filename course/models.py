from django.db import models
from django.utils.translation import ugettext


class Subject(models.Model):
    name = models.CharField(max_length=50)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_student = models.ManyToManyField(Subject)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        permissions = (
            ('is_teacher', ugettext('Is Teacher')),
            ('is_student', ugettext('Is Student')), 
        )
