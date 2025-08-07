import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Amin_celery_test.settings')
app = Celery('Amin_celery_test')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routes = {
#     'notifications.tasks.send_discount_emails': {'queue': 'queue1'},
#     'notifications.tasks.process_data_for_ml': {'queue': 'queue2'},
# }

#
# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }

app.autodiscover_tasks()
