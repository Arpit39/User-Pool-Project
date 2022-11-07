from celery import shared_task
from .models import Pool


@shared_task(bind=True)
def testing_func(self):
    # operation to perform
    for i in range(1, 21):
        print(i, '----------')
    return "SUCCESS"


@shared_task(bind=True)
def time_over(self, pk=None):
    print(pk)
    data = Pool.objects.get(id=pk)
    data.is_completed = True
    data.save()
    # operation to perform
    print("from scheduled celery")
    return "Pool completed-----"
