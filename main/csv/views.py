from django.shortcuts import render, redirect, get_object_or_404, Http404
from .forms import CSVDataForm
from .models import CSVData
from .tasks import generate_data_to_csv_celery_task


def csvList(request):
    csv = CSVData.objects.filter(user=request.user)
    return render(request, 'csv_list.html', {'csv': csv})


def addCsvData(request):
    form = CSVDataForm(request.POST or None)
    if form.is_valid():
        csv = form.save(commit=False)
        csv.user = request.user
        csv.save()
        return redirect('csv:cvs-list')
    return render(request, 'add_csv_data.html', {'form': form})


def editCsvData(request, id):
    try:
        csv = get_object_or_404(CSVData, id=id)
    except:
        raise Http404
    form = CSVDataForm(request.POST or None, instance=csv)

    if csv.user == request.user:
        if form.is_valid():
            form.save()
            return redirect('csv:cvs-list')
    else:
        return redirect('user:login')
    return render(request, 'edit_csv_data.html', {'form': form})


def deleteCsvData(request, id):
    try:
        csv = get_object_or_404(CSVData, id=id)
    except:
        raise Http404

    if request.user == csv.user:
        csv.delete()
        return redirect('csv:cvs-list')
    else:
        return redirect('user:login')


def generateDataToCsv(request, id):
    print('dasdsadas')
    generate_data_to_csv_celery_task.delay(id)
    return redirect('csv:cvs-list')
