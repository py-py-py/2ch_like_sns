from django.shortcuts import render
from .models import Thread, ResPost
from django.views import generic
from .forms import CreateThread, CreateResPost
from django.urls import reverse_lazy


def thread_index_view(request):
    threads = Thread.objects.all()
    context = {"threads": threads}
    return render(request, template_name="sns_app/thread_index.html", context=context)


def thread_view(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    response_posts = ResPost.objects.filter(thread=thread.id)[:5]
    context = {
        "thread": thread,
        "response_posts": response_posts,
    }
    return render(request, "sns_app/thread.html", context=context)


def res_detail_view(request, thread_id, respost_id):
    thread = Thread.objects.get(id=thread_id)
    respost = ResPost.objects.filter(thread=thread.id).get(id=respost_id)
    respost_text = respost.post_text
    context = {"respost_text": respost_text}
    return render(request, "sns_app/post.html", context=context)


class CreateThreadView(generic.CreateView):
    template_name = "sns_app/create_thread.html"
    model = Thread
    form_class = CreateThread
    success_url = reverse_lazy("sns_app:index")


class CreateResPost(generic.CreateView):
    template_name = "sns_app/create_respost.html"
    model = ResPost
    form_class = CreateResPost
    success_url = reverse_lazy("sns_app:thread")


def create_respost_ver2(request, thread_id):
    from .forms import CreateRespost2

    form = CreateRespost2(request.GET)
    context = {"form": form, "thread_id": thread_id}
    return render(request, template_name="sns_app/create_response_ver2.html", context=context)