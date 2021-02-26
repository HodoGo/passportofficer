from django.shortcuts import render
from docxtpl import DocxTemplate
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





