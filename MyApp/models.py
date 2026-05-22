from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tech_stack = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title


class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    file = models.FileField(upload_to='resume/')

    def __str__(self):
        return "Resume"

        


