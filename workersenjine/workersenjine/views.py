from django.shortcuts import redirect


def redirect_workers(request):
    return redirect('worker_list_url', permanent=True)
