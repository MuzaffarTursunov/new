from django.db.models import fields
from django.shortcuts import render,get_object_or_404,redirect
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views.generic import (TemplateView,CreateView, DetailView,ListView,DeleteView)
from django.views.generic.edit import UpdateView
from my_app.forms import UserCRForm,PostForm,CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from my_app.models import Project,PostToProject, ProjectComment


# Create your views here.
class IndexView(TemplateView):
    template_name='my_app/index.html'

class ThanksView(TemplateView):
    template_name='my_app/thank.html'

class BlogView(TemplateView):
    template_name='my_app/blog.html'

class SingUpView(CreateView):
    form_class=UserCRForm
    success_url =reverse_lazy('my_app:thank')
    template_name='registration/signup.html'

class SingeWorkView(TemplateView):
    template_name='my_app/single-work.html'

class ProjectListView(ListView):
    model=Project
    context_object_name='projectlar'
    
    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(DetailView):
    model=Project
    context_object_name='project_detail'
    queryset=Project.objects.all()
    template_name='my_app/project_detail.html'

#########################################################    
##############Posts and Comments#########################
#########################################################

class PostToProjectView(ListView):
    model=PostToProject

    def get_queryset(self):
        return PostToProject.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
   

class PostProjectDetail(DetailView):
    model=PostToProject
    context_object_name='post_detail'
    template_name='my_app/postproject_detail.html'
    


class PostProjectCreateView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    redirect_field_name='my_app/postproject_detail.html'
    form_class=PostForm
    model=PostToProject

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    redirect_field_name='my_app/postproject_detail.html'
    form_class=PostForm
    model=PostToProject



class PostDraftsView(LoginRequiredMixin,ListView):
    login_url='/login/'
    redirect_field_name='my_app/posttoproject_list.html'
    model=PostToProject

    def get_queryset(self):
        return PostToProject.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=PostToProject
    success_url=reverse_lazy('my_app:postproject_list')

###################################################################
######################-----functions----###########################
###################################################################
@login_required
def post_publish(request,pk):
    post=get_object_or_404(PostToProject,pk=pk)
    post.publish()
    return redirect('my_app:postproject_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(PostToProject,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('my_app:postproject_detail',pk=post.pk)
    else:
            form=CommentForm()
    return render(request,'my_app/projectcomment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(ProjectComment,pk=pk)
    comment.approve()
    return redirect('my_app:postproject_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(ProjectComment,pk=pk)
    comment.delete()
    return redirect('my_app:postproject_detail',pk=comment.post.pk)






