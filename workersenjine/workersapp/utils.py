from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .model.worker import Worker
from .model.department import Department


class OblectList():
    search_query = None

    def get(self, request):

        if self.search_query == None:
            workers = Worker.objects.all()
        else:
            workers = Worker.objects.filter(**self.search_query)

        paginator = Paginator(workers, 2)  # count  in page
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''
        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''
        departments = Department.objects.all()
        workers = Worker.objects.all().count()
        context = {
            'departments': departments,
            'page_object': page,
            'is_paginated': is_paginated,
            'prev_url': prev_url,
            'next_url': next_url,
            'workers': workers,
        }
        return render(request, 'workersapp/index.html', context=context)


class ObjectDetail():
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj,
                                                       'detail': True})


class ObjectCreateMixin():
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)
        if bound_form.is_valid():
            new_object = bound_form.save()
            return redirect(new_object)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin():
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST, instance=obj)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


class ObjectDeleteMixin():
    model = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse('worker_list_url'))
