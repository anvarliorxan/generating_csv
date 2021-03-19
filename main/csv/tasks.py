from celery import shared_task
from django.http import JsonResponse

from main.csv.models import CSVFiles, CSVData
import csv
from io import StringIO
from django.core.files.base import ContentFile


@shared_task
def generate_data_to_csv_celery_task(id):
    csv_data = CSVData.objects.filter(id=int(id))
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(['full_name', 'job', 'email', 'domain_name', 'phone_number',
                     'company_name', 'text', 'integer', 'address', 'date'])

    for c in csv_data:
        writer.writerow([c.full_name, c.job, c.email, c.domain_name, c.phone_number,
                         c.company_name, c.text, c.integer, c.address, c.date])

    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))

    file = CSVFiles()
    file.user = c.user
    file.csv_data_id = c.id
    file.save()
    file.file.save('output.csv', csv_file)

    return 'success'
