from django.db import models
from django.db.models import Avg, F


class User(models.Model):
    id = models.CharField("id", max_length=100, primary_key=True)
    name = models.CharField("Username", max_length=100)
    email = models.EmailField("Email", max_length=100)
    status = models.CharField("Status", max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'


class Task(models.Model):
    id = models.CharField("id", max_length=100, primary_key=True)
    name = models.CharField("Task name", max_length=100)
    assignees = models.ManyToManyField(User)
    status = models.CharField("Status", max_length=25)
    project_name = models.CharField("Project name", max_length=200, default="None")
    start_time = models.DateTimeField("Start time")
    end_time = models.DateTimeField("End time")
    duration = models.CharField("Duration", max_length=50)
    start_date = models.DateField("Start date", default='2001-01-01')
    end_date = models.DateField("End date", default='2001-01-01')

    def __str__(self):
        return self.id

    def get_assignees(self):
        return "\n".join([i.email for i in self.assignees.all()])

    def get_duration(self):
        return self.duration

    class Meta:
        verbose_name = 'Task'


class Project(models.Model):
    id = models.CharField("id", max_length=100, primary_key=True)
    name = models.CharField('Project name', max_length=100)
    tasks = models.ManyToManyField(Task)
    archived = models.BooleanField("Archived")
    public = models.BooleanField("Public")

    def __str__(self):
        return self.name

    def get_tasks(self):
        return "\n".join([i.name for i in self.tasks.all()])

    class Meta:
        verbose_name = 'Project'


class ParsingHistory(models.Model):
    update_at = models.DateTimeField(auto_now_add=True)
