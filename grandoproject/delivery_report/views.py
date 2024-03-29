from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import DeliveryReport, EmailReportToClientSuccess
from .forms import DeliveryReportForm, EmailReportToClientForm
from django.contrib import messages
from django.core.mail import EmailMessage


@login_required
def create_delivery_report(request):
    if request.method == 'POST':
        delivery_form = DeliveryReportForm(request.POST)
        if delivery_form.is_valid():
            try:
                delivery_report = DeliveryReport(
                    direction=delivery_form.cleaned_data['direction'],
                    driver_name=delivery_form.cleaned_data['driver_name'],
                    commentary=delivery_form.cleaned_data['commentary'],
                    dispatcher=delivery_form.cleaned_data['dispatcher']
                )

                delivery_report.save()

                messages.success(request, 'Отчет успешно создан')

                return HttpResponseRedirect(reverse('delivery_report:delivery_report_history'))
            except Exception as e:
                print(f'Error saving data: {e}')
                messages.error(request, 'Произошла ошибка при сохранении отчета.')
    else:
        delivery_form = DeliveryReportForm()

    return render(request, 'delivery_report/delivery_report_create.html', {'delivery_form': delivery_form})


@login_required
def delivery_report_history(request):
    delivery_report_history_data = DeliveryReport.objects.all()

    context = {'delivery_report_history_data': delivery_report_history_data}
    return render(request, 'delivery_report/delivery_report_history.html', context)


@login_required()
def delivery_report_email(request):
    if request.method == 'POST':
        report_form = EmailReportToClientForm(request.POST)
        if report_form.is_valid():
            try:
                report_instance = EmailReportToClientSuccess(
                    direction=report_form.cleaned_data['direction'],
                    message=report_form.cleaned_data['message'],
                    date=report_form.cleaned_data['date']
                )

                report_instance.save()
                clients = report_form.cleaned_data['clients']
                report_instance.clients.set(clients)

                for client in clients:
                    client_email = client.main_email.split(',')
                    to_email = client_email[0]
                    cc_email = client_email[1:]
                    subject = f'Отчет по доставке {report_instance.direction} за {report_instance.date}'
                    message = f'{report_instance.message}'
                    email = EmailMessage(subject, message, to=[to_email], cc=cc_email)
                    email.send()

                return HttpResponseRedirect(reverse('delivery_report:delivery_report_history'))

            except Exception as e:
                print(f'Error saving data: {e}')

    else:
        report_form = EmailReportToClientForm()

    return render(request, 'delivery_report/delivery_report_email.html', {'report_form': report_form})







