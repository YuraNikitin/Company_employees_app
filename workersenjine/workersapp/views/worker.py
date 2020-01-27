from ..utils import *
from django.views.generic import View
from ..forms.worker import WorkerForm
from ..model.worker import Worker


class WorkerList(OblectList, View):
    search_query = None


class WorkerFilter(OblectList, View):
    search_query = {'endDate': None}


class WorkerListDetail(ObjectDetail, View):
    model = Worker
    template = 'workersapp/worker/worker_detail.html'


class WorkerCreate(ObjectCreateMixin, View):
    form_model = WorkerForm
    template = 'workersapp/worker/worker_create.html'


class WorkerUpdate(ObjectUpdateMixin, View):
    model = Worker
    form_model = WorkerForm
    template = 'workersapp/worker/worker_update.html'


class WorkerDelete(ObjectDeleteMixin, View):
    model = Worker
    template = 'workersapp/worker/worker_delete.html'
