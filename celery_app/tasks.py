from celery import shared_task


@shared_task(bind=True)
def test_func(*args, **kwargs):
    for i in range(5):
        print(i, " ", end="")
    return "done printing"
