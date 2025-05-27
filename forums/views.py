from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Topic, Post
from .forms import ForumForm, TopicForm, PostForm

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    topics = Topic.objects.filter(forum=forum)
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    posts = Post.objects.filter(topic=topic)
    return render(request, 'forum/topic_detail.html', {'topic': topic, 'posts': posts})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save()
            return redirect('forum_detail', forum_id=forum.id)
    else:
        form = ForumForm()
    return render(request, 'forum/create_forum.html', {'form': form})

@login_required
def create_topic(request, forum_id):
    forum = get_object_or_404(Forum, pk=forum_id)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.forum = forum
            topic.author = request.user
            topic.save()
            return redirect('topic_detail', topic_id=topic.id)
