from django.db import models
from django.contrib.auth.models import User,PermissionsMixin
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class User(User,PermissionsMixin):
    def __str__(self):
        return '@{}'.format(self.username)


class Project(models.Model):
    pro_tur=models.CharField(max_length=255 ,help_text='turni tanlang fashion,event,wedding,corporate ')
    rasm=models.ImageField(upload_to='about/')
    title=models.CharField(max_length=240)
    tur=models.CharField(max_length=254)
    desc_title=models.CharField(max_length=250)
    desc=models.CharField(max_length=254)
    category=models.CharField(max_length=50,blank=True)
    cliyent=models.CharField(max_length=250)
    technology=models.CharField(max_length=100)
    date_create=models.DateField()
    visit_url=models.URLField(blank=True,null=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('my_app:project_detail',kwargs={'pk':self.pk})

class ProjectDetail(models.Model):
    project_title=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projectdetail')
    desc_title=models.CharField(max_length=250)
    desc=models.CharField(max_length=254)
    category=models.CharField(max_length=50,blank=True)
    cliyent=models.CharField(max_length=250)
    technology=models.CharField(max_length=100)
    date_create=models.DateField()
    visit_url=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.desc_title



class PostToProject(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    author_img=models.ImageField(upload_to='author/',blank=True,null=True,default='author/img3.jpg')
    title=models.CharField(max_length=254)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse('my_app:postproject_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class ProjectComment(models.Model):
    post=models.ForeignKey(PostToProject,related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=250)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)

    def approve(self):
        self.approved_comment=True
        self.save()
    
    def get_absolute_url(self):
        return reverse('my_app:postproject_list')
    
    def __str__(self):
        return self.text





