from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview')  # Убраны 'slug' и 'created_at'
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')  # Убраны 'slug' и 'created_at'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.pk])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        return super().get(request, *args, **kwargs)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('materials:list')