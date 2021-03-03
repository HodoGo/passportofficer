from django.shortcuts import render
from docxtpl import DocxTemplate
from xlsxtpl.writerx import BookWriter
from django.http import HttpResponse
import os

from HouseApp.models import House,People,Flat

def people_list(request,template_name='reportapp/people_list.html'):
  p = People.objects.select_related().order_by('flat').all()
  data = {}
  data['object_list'] = p
  return render(request,template_name,data)

def export_word(request):
  _PATH = os.path.abspath(os.path.dirname(__file__))
  DOCX_TEMP = os.path.join(_PATH, 'static', 'docx','my_word_template.docx')
  doc = DocxTemplate(DOCX_TEMP)
  p = People.objects.select_related().order_by('flat').all()
  context = { 'company_name' : "World company(Test)",
              'object_list': p
               }
  doc.render(context)
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
  response['Content-Disposition'] = 'attachment; filename=download.docx'
  doc.save(response)
  return response

def export_excel(request):
  _PATH = os.path.abspath(os.path.dirname(__file__))
  XLSX_TEMP = os.path.join(_PATH, 'static', 'xlsx','example.xlsx')
  xlsx =  BookWriter(XLSX_TEMP)
  xlsx.jinja_env.globals.update(dir=dir, getattr=getattr)

  p = People.objects.select_related().order_by('flat').all()
  
  person_info = {'address': u'Test', 'name': u'rwe', 'fm': 178 }             
  person_info['rows'] = p
  person_info['tpl_idx'] = 0
  payloads = [person_info]

  xlsx.render_book(payloads=payloads)
  response = HttpResponse(content_type='application/vnd.ms-excel')
  response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
  xlsx.save(response)

  return response


