from django.utils import timezone


def get_queryset(request):
    return {
        'year': timezone.now().year,
    }
