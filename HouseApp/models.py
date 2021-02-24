"""
Definition of models.
"""

from django.db import models

class House(models.Model):
    name = models.CharField(max_length = 200, help_text="Укажите название дома")
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.address

class Flat(models.Model):
    house = models.ForeignKey('House',on_delete=models.SET_NULL,null=True)
    numberFlat = models.CharField(max_length=10,help_text="Укажите номер квартиры")
    entrance = models.IntegerField(verbose_name='Подъезд')
    floor = models.IntegerField(verbose_name='Этаж')
    square = models.CharField(max_length=10,help_text="Укажите площадь квартиры", verbose_name='Площадь')

    def __str__(self):
        return 'Кв. %s' % (self.numberFlat)

class People(models.Model):
    flat = models.ForeignKey('Flat',on_delete=models.SET_NULL,null=True)
    lastname = models.CharField(verbose_name = 'Фамилия',max_length = 200)
    firstname = models.CharField(verbose_name = 'Имя',max_length = 200)
    fathername = models.CharField(verbose_name = 'Отчество',max_length = 200)
    birthday = models.DateField(verbose_name = 'Дата рождения',null = False)
    TYPE_DOCUMENTS = (
        ('п','Паспорт'),
        ('св','Свидетельство о рождении'),
        ('ин','Паспорт иностранного гражданина')
    )
    docType = models.CharField(verbose_name='Тип документа', max_length=3,choices = TYPE_DOCUMENTS,blank=True,default='п', help_text='Укажите тип документа')
    docSeries = models.CharField(verbose_name='Серия документа',max_length = 5)
    docNumber = models.CharField(verbose_name='Номер документа',max_length = 8)
    docIssueDate = models.DateField(null = True,verbose_name='Дата выдачи')
    docIssueOrg = models.TextField(verbose_name='Кто выдал')
    owner = models.BooleanField(verbose_name = 'Собственник')
    PART_OWNER = (
        ('-','-'),
        ('1','целая'),
        ('1/2','одна втрорая'),
        ('1/3','одна третья'),
        ('1/4','одна четвертая')
    )
    ownerPart = models.CharField(verbose_name = 'Часть собственности',default = '-',choices = PART_OWNER,max_length = 200)

    def __str__(self):
        return '%s %s %s %s (кв. %s)' % (self.lastname,self.firstname,self.fathername,self.birthday ,self.flat.numberFlat)





