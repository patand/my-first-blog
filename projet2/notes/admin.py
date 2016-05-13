#-*- coding: utf-8 -*- 

from django.contrib import admin
from notes.models import Calendar, Event
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models import Q
from django.http import HttpResponse
from xlrd import open_workbook, XL_CELL_TEXT
from .forms import UploadFileForm, EventForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import os


admin.site.unregister(Site)

admin.autodiscover()

def import_xls(modeladmin, request, queryset):
    form = UploadFileForm()
    return render_to_response('notes/upload01.html', {'form': form},
    context_instance=RequestContext(request))



def import_xls2(request):
    import xlrd

    try:
        value = request.GET['file']
        current_user = request.user
        
        filepath = 'C:/Users/patrice/Documents/' + str(current_user) + '/'
        print 'filepath', filepath
        if not os.path.exists(filepath):
            print 'Cannot find filepath: ' + filepath

        workbook = xlrd.open_workbook(filepath + value)
        sheet = workbook.sheet_by_index(0)
       
        resultat = []
        for row_x in range(1, sheet.nrows):
            for col_x in range(0, sheet.ncols):
                resultat.append(sheet.cell_value(row_x,col_x))

        i=0
        j=0

        print 'resu', resultat

        
        lesprop=Calendar.objects.all()
        unuser=User.objects.all()
       
        while i < sheet.nrows - 1:
    
            b=0
            theprop=[]
            while b< len(lesprop):
                print resultat[j+9]
                print lesprop[b]
                if str(lesprop[b])==str(resultat[j+7]):
                    theprop=lesprop[b]
                b+=1
             
            print 'theprop', theprop
            if theprop==[]:
                html = "<html><body>Error reading file..Check the data<br/><br/><a href=javascript:history.go(-1)>back</a></body></html>"
                return HttpResponse(html)
            else:
                utilisateur = User.objects.get(username = current_user)
                calendar,_= Calendar.objects.get_or_create(name = theprop)
               
                                                        
               

                print 'titre', resultat[j]

                print 'numero AER', resultat[j+1]
                print 'demandeur', resultat[j+2]
                print 'nb  d eprouvettes traitees', resultat[j+3]
                print 'nb  d eprouvettes a traitees', resultat[j+4]
                print 'date de depot', resultat[j+5]
                print 'type d essai', resultat[j+6]
                print 'machine', resultat[j+7]
                print 'debut', resultat[j+8]
                print 'periode', resultat[j+9]
                print 'NB cycles', resultat[j+10]
                print 'weekend', resultat[j+11]
                
                print 'Couleur', resultat[j+13]

                


                title = resultat[j]
                numero = resultat[j+1]
                demandeur=resultat[j+2]
                rep=resultat[j+3]
                rep2=resultat[j+4]
                end=resultat[j+5]
                description = resultat[j+6]
                #calendar=resultat[j+7]
                start = resultat[j+8]
                frequency= resultat[j+9]
                fin= resultat[j+10]
                weekend = resultat[j+11]
                user = utilisateur
                couleur = resultat[j+13]

                


                


                b5 = Event(title = resultat[j], numero = resultat[j+1], demandeur = resultat[j+2],  rep=resultat[j+3],  rep2=resultat[j+4], end= resultat[j+5],  description= resultat[j+6],  calendar=calendar,
                            start = resultat[j+8],  frequency =resultat[j+9],  fin =resultat[j+10], weekend=resultat[j+11], user= user,  couleur = resultat[j+13])

                try:
                    b5.save()
                except Exception as e:      
                    print '%s (%s)' % (e.message, type(e))
                    
                print 'donnees enregistrees **************************'
                print 'title', b5.title
                print 'start', b5.start
                print 'end', b5.end
                print 'categorie', b5.calendar
                print 'description', b5.description
                print 'periode', b5.frequency
                print 'fin', b5.fin
                print 'couleur', b5.couleur


                                         
            j+=14
            i+=1
    
        return HttpResponseRedirect('/admin')
    
    except IOError:
        print 'File not found !'
        html = "<html><body>please, select a file of your directory.. <br/><br/><a href=javascript:history.go(-1)>back</a></body></html>"
        return HttpResponse(html)

    
import_xls.short_description = u"Import XLS"


def export_xls(modeladmin, request, queryset):
    import xlwt
    try:
        response = HttpResponse(mimetype='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet("MyModel")
        
        row_num = 0
        
        columns = [
            #(u"ID", 4000),
            (u"Titre", 6000),
            (u"Numéro de l'étude", 4000),
            (u"Nom du demandeur", 4000),
            (u"Nombre d'éprouvettes traitées", 6000),
            (u"Nombre d'éprouvettes à traitées", 6000),
            (u" Date de dépôt de la demande", 4000),
            (u"Type d'essai", 12000),
            (u"Machine", 4000),
            (u" Date de début", 4000),
            (u"Période", 4000),
            (u"Nombre de cycles", 5000),
            
        ]
        
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
            

        for col_num in xrange(len(columns)):
            ws.write(row_num, col_num, columns[col_num][0], font_style)
            # set column width
            ws.col(col_num).width = columns[col_num][1]

        font_style = xlwt.XFStyle()
        font_style.alignment.wrap = 1
        
        for obj in queryset:
            row_num += 1
            row = [
                #obj.pk,
                obj.title,
                obj.numero,
                obj.demandeur,
                obj.rep,
                obj.rep2,
                obj.end,
                obj.description,
                obj.calendar,
                obj.start,
                obj.frequency,
                obj.fin,
                
            ]
            for col_num in xrange(len(columns)):
                ws.write(row_num, col_num, str(row[col_num]), font_style)
                   
        wb.save(response)
        return response

    except IOError:
        print 'file not found'
        html = "<html><body>please, select a line.. <br/><br/><a href=javascript:history.go(-1)>back</a></body></html>"
        return HttpResponse(html)
    
export_xls.short_description = u"Export XLS"


class CalendarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class EventAdmin(admin.ModelAdmin):
    

    actions = [export_xls, import_xls]

    class Media:
        print 'pass_media'
      
        css = {
            "all" : ('/static/css/width.css',)
            }

    
    list_display = ('title', 'demandeur', 'numero', 'rep', 'rep2', 'end', 'description',  'calendar', 'start',  'fin', 'frequency', 'weekend', 'user', 'couleur',)
    
    fieldsets = (
        (None, {
            'fields': ('title', 'demandeur', 'numero', 'rep', 'rep2', 'end', 'description', 'calendar',  'start', 'weekend',  'is_cancelled', 'user', )
        }),

         (u"Durée", {
                'fields': ( 'fin', 'frequency',)
            }),


         (None, {
                'fields': ( 'lefichier',)
            }),

    (u"couleur de l' évenement", {
                'fields': ( ('couleur'),)
            }),
    )
    #readonly_fields = ("end",)
    list_filter = ('calendar', 'user')
    search_fields = ['title']
    date_hierarchy = 'start'

    def get_actions(self, request):
        if request.user.is_superuser == True:
            actions = super(EventAdmin, self).get_actions(request)
            return actions
        else:   
            actions = super(EventAdmin, self).get_actions(request)
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def queryset(self, request):
        qs = super(EventAdmin, self).queryset(request)
        current_user = request.user
        if request.user.is_superuser:
            return qs
        else:
             BelongToMe = Event.objects.get(user=current_user)
             return qs.filter(Q(user=request.user))
             
    
##    def get_readonly_fields(self, request, obj=None):
##        current_user = request.user
##        #print current_user 
##        if request.user.is_superuser == False:
##            #print 'passage'
##            notBelongToMe = Event.objects.exclude(user=current_user)
##            BelongToMe = Event.objects.get(user=current_user)
##            # evennements non crees par l'utilisateur courant 
##            jj=0
##            if obj:
##                while jj < len(notBelongToMe):
##                    if notBelongToMe[jj] == obj:
##                        return self.readonly_fields + (
##                    'title',
##                    'start',
##                    'end',
##                    'calendar',
##                    'is_cancelled',
##                    'user',
##                    
##                    )
##                    jj+=1
##                    
##        return self.readonly_fields
    
    def has_delete_permission(self, request, obj=None):
        current_user = request.user
        notBelongToMe = Event.objects.exclude(user=current_user)
        jj=0
        var1= False
        if request.user.is_superuser:
            return True
        
        if obj: # nom du materiau en cours
            while jj < len(notBelongToMe):
                if notBelongToMe[jj] == obj:
                    var1= True  
                jj+=1

        print 'var1', var1
        if var1==True:
            return False
        else:
            return True
        

admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Event, EventAdmin)
