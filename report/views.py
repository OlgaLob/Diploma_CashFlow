import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.core.files.storage import FileSystemStorage

from .models import BankStatementsRes


def Import_Excel_acc_pandas(request):
    if request.method == 'POST' and request.FILES['*']:
        myfile = request.FILES['*']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        empexceldata = pd.read_excel(filename)
        dbframe = empexceldata
        for dbframe in dbframe.itertuples():
            obj = BankStatementsRes.objects.create(date=dbframe.Дата,
                                                   revenue=dbframe.Поступление,
                                                   write_off=dbframe.Списание,
                                                   purpose_of_payment=dbframe.Назначение_платежа,
                                                   contractor=dbframe.Контрагент,
                                                   doc_number=dbframe.Вх_номер,
                                                   transaction_type=dbframe.Вид_операции,
                                                   division=dbframe.Подразделение,
                                                   article_revenue=dbframe.Статья_доходов
                                                   )
            obj.save()
        return render(request, 'Import_excel_acc_db.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'Import_excel_acc_db.html', {})


def export_to_excel(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.dds_report")
        data = cursor.fetchall()

    df = pd.DataFrame(data, columns=['month', 'article_revenue', 'division',
                                     'total_revenue', 'total_write_off'])

    df['month'] = pd.to_datetime(df['month'])
    df = df.pivot_table(index=['article_revenue', 'division'], columns='month',
                        values=['total_revenue', 'total_write_off'], aggfunc=sum)
    df.columns = [f'{level[0]}-{level[1]}' for level in df.columns]
    df.to_excel('report.xlsx')

    with open('report.xlsx', 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=report.xlsx'
        return response
