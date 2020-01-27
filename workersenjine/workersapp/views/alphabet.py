from django.shortcuts import render
from django.views.generic import View
from itertools import groupby
from operator import itemgetter
from django.db.models import Func, F, Value
from ..model.worker import Worker


class AlphabetList(View):

    # make groups on surnames. Key - first letter in surname.
    def group(self, items):
        for letter, names in groupby(sorted(items), key=itemgetter(0)):
            yield list(names)

    def union_group(self, items, min_len, max_len):
        buffer = []
        for item in items:
            if len(buffer) >= max_len:
                yield sorted(buffer)
                buffer = []
            if len(item) <= min_len:
                buffer += item
            else:
                yield item
        yield sorted(buffer)

    def get(self, request, group=None):
        surnames = sorted(Worker.objects.all().values_list('surname', flat=True))
        groups_list = self.union_group(self.group(surnames), 50, 100)
        aplhabet = {'{}-{}'.format(item[0][0], item[-1][0]): item for item in groups_list}

        a = []
        for i in range(ord(group[0:1].upper()), ord(group[-1:].upper()) + 1):
            a.append(chr(i))
        query = Worker.objects.annotate(
            surname_letter=Func(F('surname'), Value(1), Value(1), function='substring')).filter(surname_letter__in=a)

        return render(request, 'workersapp/alphabet/alphabet.html', context={'names': aplhabet, 'query': query})
