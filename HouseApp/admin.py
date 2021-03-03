from django.contrib import admin
from .models import House,Flat,People
from import_export import resources
from import_export.admin import ImportExportModelAdmin
import os
from django.http import HttpResponse
from docxtpl import DocxTemplate
from xlsxtpl.writerx import BookWriter

class FlatInline(admin.TabularInline):
    model = Flat
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    inlines = [FlatInline]

class PeopleResource(resources.ModelResource):
    class Meta:
        model = People

class PeopleAdmin(ImportExportModelAdmin):
    def export_to_xlsx(self, request, queryset):
        _PATH = os.path.abspath(os.path.dirname(__file__))
        XLSX_TEMP = os.path.join(_PATH, 'static', 'xlsx','example.xlsx')
        xlsx =  BookWriter(XLSX_TEMP)
        xlsx.jinja_env.globals.update(dir=dir, getattr=getattr)        
  
        person_info = {'address': u'Тестовый адрес', 'name': u'Тестовый отчет export_to_xlsx' }             
        person_info['rows'] = queryset
        payloads = [person_info]

        xlsx.render_book(payloads=payloads)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=your_template_name.xlsx'
        xlsx.save(response)
        message_bit = "Выгружен отчет в xlsx"    
        self.message_user(request, "%s успешно!" % message_bit)  
        return response        

    def export_to_docx(self, request, queryset): 
        _PATH = os.path.abspath(os.path.dirname(__file__))
        DOCX_TEMP = os.path.join(_PATH, 'static', 'docx','my_word_template.docx')
        doc = DocxTemplate(DOCX_TEMP)
        context = { 'company_name' : "Отчет export_to_docx",
              'object_list': queryset
               }
        doc.render(context)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=download.docx'
        doc.save(response)           
        message_bit = "Выгружен отчет в docx"    
        self.message_user(request, "%s успешно!" % message_bit)  
        return response      

    resource_class = PeopleResource
    list_display = ('flat','lastname','firstname','fathername','birthday','docSeries','docNumber','owner','ownerPart')
    list_display_links = ('lastname',)
    list_filter = ('owner','flat')
    ordering = ('flat','lastname','firstname')
    actions = [export_to_xlsx, export_to_docx]
    search_fields = ['lastname']

    fieldsets = (
        ('Квартира', {
            'fields': (
                'flat',
                'owner',
                'ownerPart'  
            ) 
        }),
        ('ФИО', {
            'fields': ('lastname','firstname','fathername','birthday')
        }),
        ('Документы', {
            'fields': (
                'docType',
                ('docSeries',
                'docNumber'),
                'docIssueDate',
                'docIssueOrg'
            )
        })
    )   

admin.site.register(House,HouseAdmin)
admin.site.register(Flat)
admin.site.register(People,PeopleAdmin)
