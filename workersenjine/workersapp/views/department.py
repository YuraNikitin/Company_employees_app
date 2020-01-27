from ..utils import *
from django.views.generic import View
from ..forms.department import DepartmentForm
from ..model.department import Department


class DepartmentDetail(ObjectDetail, View):
    model = Department
    template = 'workersapp/department/department_detail.html'


class DepartmentCreate(ObjectCreateMixin, View):
    form_model = DepartmentForm
    template = 'workersapp/department/department_create.html'


class DepartmentUpdate(ObjectUpdateMixin, View):
    model = Department
    form_model = DepartmentForm
    template = 'workersapp/department/department_update.html'


class DepartmentDelete(ObjectDeleteMixin, View):
    model = Department
    template = 'workersapp/department/department_delete.html'