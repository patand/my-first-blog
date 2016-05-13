# Create your views here.
# -*- coding: utf-8 -*-
import datetime
from django import http
from django.utils import simplejson as json
from django.utils import timezone
from notes.models import Event, Calendar
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
import warnings
import exceptions
import pytz


def main_page(request):
   
    state = " "
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
       
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/main/")
                
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Try again, username and/or password incorrect."

    return render_to_response('registration/main_page.html',{'state':state, 'username': username}, context_instance=RequestContext(request))



def eventsdrag(request):
    
    

    try:
        
        try:
            untitre = request.GET.get('title')
            macategorie = request.GET.get('categorie')
            madescription = request.GET.get('description')
            unfin= request.GET.get('lefin')
            unfrequence=request.GET.get('lefrequence')
            uncouleur=request.GET.get('couleur')
            unnumero=request.GET.get('numero')
            unweekend = request.GET.get('weekend')
            
            unlundi = request.GET.get('lundi')
            unmardi = request.GET.get('mardi')
            unmercredi = request.GET.get('mercredi')
            unjeudi = request.GET.get('jeudi')
            unvendredi = request.GET.get('vendredi')
            unsamedi = request.GET.get('samedi')
            undimanche = request.GET.get('dimanche')

            print 'categorie', macategorie
            print 'description', madescription
            print 'periode', unfrequence
            print 'Nombre de cycles', unfin      # 4
            print 'lundi', unlundi
            print 'mardi', unmardi
            print 'mercredi', unmercredi
            print 'samedi', unsamedi
            print 'fin', unfin
            print 'periode', unfrequence
            print 'couleur', uncouleur
            print 'numero', unnumero
            print 'weekend', unweekend
           
        except:
            untitre = None

        try:
            debut = float(request.GET.get('start'))
            tz = pytz.timezone("Europe/Paris")
            debut = datetime.datetime.fromtimestamp(debut, tz)

            ledebut = debut.strftime('%d')
           
        except:
            debut = None
        try:
            lafin = float(request.GET.get('end'))
            tz = pytz.timezone("Europe/Paris")
            lafin = datetime.datetime.fromtimestamp(lafin, tz)
            final = lafin.strftime('%d')

            



            if unfrequence == 'JOUR':
                delta= (lafin -debut).days
                delta = delta +1 
                if (unweekend=='EXCLUDE') and delta >=7:
                    delta=delta+2
                
                print 'final', final
                print 'ledebut', ledebut
                print 'delta', delta
               

            if unfrequence == 'SEMAINE':
                delta= (lafin -debut).days
                delta = (delta+1)/7
                print 'delta', delta
                
            if unfrequence == 'BIMENSUEL':
                delta= (lafin -debut).days
                delta = abs(delta/14)
                print 'delta', delta

            if unfrequence == 'MENSUEL':
                delta= (lafin -debut).days
                delta= abs(round(delta)/30)
      
             
        
        except:
            lafin = None
        
        
      
       
        print 'debut', debut
        print 'unefin', lafin
        ecart = (lafin -debut).days
        print 'ecart', ecart 
        untitre = untitre
        moncalendar = Calendar.objects.get(name=macategorie)
        
        print 'moncalendar', moncalendar
       
        current_user = request.user
        
        print 'utilisateur', current_user
        print 'lundi', unlundi
        print 'mardi', unmardi
        print 'mercredi', unmercredi
        print 'jeudi', unjeudi
        print 'vendredi', unvendredi
        print 'samedi', unsamedi
        print 'dimanche', undimanche

        instance = Event.objects.filter(title= untitre)
        try:
            instance.delete()
        except Exception as e:      
            print '%s (%s)' % (e.message, type(e))
      
        
        b5 = Event(title= untitre, start=debut, end=lafin, calendar= moncalendar, user=current_user, description=madescription, frequency=unfrequence, fin=delta, lundi=str(unlundi), mardi=str(unmardi),
                  mercredi=str(unmercredi), jeudi=str(unjeudi), vendredi=str(unvendredi), samedi=str(unsamedi), dimanche=str(undimanche), couleur=uncouleur, numero=unnumero, weekend=unweekend)


        try:
            b5.save()
            print 'ok'
        except Exception as e:      
            print '%s (%s)' % (e.message, type(e))
            
            
      
        print 'title', b5.title
        print 'start', b5.start
        print 'end', b5.end
        print 'categorie', b5.calendar
        print 'description', b5.description
        print 'periode', b5.frequency
        print 'fin', b5.fin
        print 'couleur', b5.couleur
       

        allDay = True
      


        
        event_list = []



         
        return http.HttpResponse(json.dumps(event_list),
                                 content_type='application/json')
    except:
        return HttpResponse("OK")



def events_json(request):
   
    try:
        start = float(request.GET.get('start'))
    except:
        start = None

    try:
        end = float(request.GET.get('end'))
    except:
        end = None

   
    if start is not None:
        start = datetime.datetime.fromtimestamp(start)
    if end is not None:
        end = datetime.datetime.fromtimestamp(end)

    events = Event.objects.all()
    events2 = Event.objects.values('calendar__name')
    
    current_user = request.user
    liste_objects = Event.objects.filter(user=current_user)

    #print 'liste :', liste_objects
    
    

    event_list = []
    event_list2 = []
    categories = []
    data2=[]
    activated = Event.objects.filter(activated=True)
   
    #for event in events:
    for event in liste_objects:
        event_start = event.start.astimezone(timezone.get_default_timezone())
        event_end = event.end.astimezone(timezone.get_default_timezone())
        
        lacat=event.calendar

        #print 'event_cancel', event.is_cancelled
       
       
        if event_start.hour == 0 and event_start.minute == 0:
            allDay = True
        else:
            allDay = False

        if not event.is_cancelled and event.weekend== 'INCLUDE':

            if event.frequency == 'JOUR':
                if event.fin !=0:
                    if not event_start.strftime('%B') != event_end.strftime('%B'): # pas de changement de mois
                        print '1'
                        var0 = event.fin
                        print 'fin', event.fin
                        if event.fin==1:
                            event.fin=event.fin
                        event_list.append({
                            'categorie': event.calendar.as_dict(),
                            'id': event.id,
                            'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                            'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin -1 )),
                            'title': event.title,
                            'description': event.description,
                            'fin':event.fin,
                            'frequency': event.frequency,
                            'allDay': allDay,
                            'lundi':  event.lundi,
                            'mardi': event.mardi,
                            'mercredi': event.mercredi,
                            'jeudi': event.jeudi,
                            'vendredi': event.vendredi,
                            'samedi': event.samedi,
                            'dimanche': event.dimanche,
                            'couleur': event.couleur,
                            'numero': event.numero,
                            'mavar': event.weekend
                            
                           
                            })
                    if event_start.strftime('%B') != event_end.strftime('%B'): # changement de mois
                        print '2'
                        event.fin = event.fin * 1
                        print 'event arrivee :', event.fin     
                        event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                
                               
                                })
                else:
                    event.fin = event.fin * 1
                    event_list.append({
                            'categorie': event.calendar.as_dict(),
                            'id': event.id,
                            'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                            'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin - 1)),
                            'title': event.title,
                            'description': event.description,
                            'fin':event.fin,
                            'frequency': event.frequency,
                            'allDay': allDay,
                            'lundi':  event.lundi,
                            'mardi': event.mardi,
                            'mercredi': event.mercredi,
                            'jeudi': event.jeudi,
                            'vendredi': event.vendredi,
                            'samedi': event.samedi,
                            'dimanche': event.dimanche,
                            'couleur': event.couleur,
                            'numero': event.numero,
                            'mavar': event.weekend
                            })
                    
            if event.frequency == 'SEMAINE':
                print 'ffff'
                if event.fin !=0:
                    if not event_start.strftime('%B') != event_end.strftime('%B'): # meme mois
                        print '1'
                        print event_start.strftime('%B')
                        print event_end.strftime('%B')
                        event.fin = event.fin * 7
                        print 'lafin', event.fin 
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                    if event_start.strftime('%B') != event_end.strftime('%B'):
                        
                        print 'pass'
                        event.fin = event.fin * 7
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin -1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                    
                   
                    
                else:
                    print 'jour dimanche', event_start.strftime('%A')
                    event_fin = event.fin * 7
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })
                    
            if event.frequency == 'BIMENSUEL':

                if event.fin !=0:
                    if not event_start.strftime('%B') != event_end.strftime('%B'):
                        var0 = event.fin
                    else:
                        event.fin= var0
                        

                    event_fin = event.fin * 14
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })
                else:
                    event_fin = event.fin * 14
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })
                    
            if event.frequency == 'MENSUEL':
                if event.fin !=0:
                    if not event_start.strftime('%B') != event_end.strftime('%B'):
                        var0 = event.fin
                    
                    event_fin = event.fin * 30
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })
                else:
                    event_fin = event.fin * 30
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })

        else:   # ********************************  traitement des weekends exclus
            
            
            if not event.is_cancelled and event.weekend== 'EXCLUDE':
                
                print ' traitement des weekends exclus'
                
                if event.frequency == 'JOUR':
                    print 'JOUR'
                    print 'jour', event_end.strftime('%A')
                    print 'cejour' 
                    print 'creneau'
                    print 'creneau jour debut', event_start.strftime('%A')
                    print 'creneau jour fin', event_end.strftime('%A')
                    print 'fin', event.fin

##                    for x in range(event.fin):
##                        if x > 0:
##                            if event_start.strftime('%A')== 'Monday':
##                                if x==6:
##                                    event.fin=event.fin + 1
##                                if x>=7 and x<=11:
##                                    event.fin=event.fin + 2
##                            if event_start.strftime('%A')== 'Tuesday':
##                                if x==5:
##                                     event.fin=event.fin + 1
##                                if x>=6 and x<=10:
##                                    event.fin=event.fin + 2
##                            if event_start.strftime('%A')== 'Wednesday':
##                                print 'pass4', x
##                                if event.fin==4:
##                                    print 'x=4'
##                                    event.fin=event.fin + 1
##                                if x>=5 and x<=9:
##                                    event.fin=event.fin + 2
##                            if event_start.strftime('%A')== 'Thursday':
##                                if x==3:
##                                    event.fin=event.fin + 1
##                                if x>=4 and x<=9:
##                                    event.fin=event.fin + 2
##                            if event_start.strftime('%A')== 'Friday':
##                                if x==2:
##                                    event.fin=event.fin + 1
##                                if x>=3 and x<=8:
##                                    event.fin=event.fin + 2



                    if event_start.strftime('%A')== 'Monday':
                        print 'pass1'
                        if event.fin >= 7 and  event.fin <= 11:
                            event.fin=event.fin + 2
                        if event.fin == 6:
                            event.fin=event.fin + 1
                    if event_start.strftime('%A')== 'Tuesday':
                        print 'pass2', event.fin
                        if event.fin == 5:
                            event.fin=event.fin + 1
                        if event.fin >= 6 and  event.fin <= 10:
                            event.fin=event.fin + 2
                    if event_start.strftime('%A')== 'Wednesday':
                        print 'pass3', event.fin
                        if event.fin == 4:
                             event.fin=event.fin + 1
                        if event.fin >= 5 and event.fin<=9:
                            print '>5'
                            event.fin=event.fin + 2
                    if event_start.strftime('%A')== 'Thursday':
                        if event.fin == 3:
                             event.fin=event.fin + 1
                        if event.fin >= 4 and event.fin <= 9:
                            event.fin=event.fin + 2
                    if event_start.strftime('%A')== 'Friday':
                        if event.fin == 2:
                            event.fin=event.fin + 1
                        if event.fin >= 3 and event.fin <=8:
                            event.fin=event.fin + 2
                        
                        
                        
                    
                    #event.fin=event.fin + 2
                    event_list.append({
                            'categorie': event.calendar.as_dict(),
                            'id': event.id,
                            'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                            'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event.fin - 1)),
                            'title': event.title,
                            'description': event.description,
                            'fin':event.fin,
                            'frequency': event.frequency,
                            'allDay': allDay,
                            'lundi':  event.lundi,
                            'mardi': event.mardi,
                            'mercredi': event.mercredi,
                            'jeudi': event.jeudi,
                            'vendredi': event.vendredi,
                            'samedi': event.samedi,
                            'dimanche': event.dimanche,
                            'couleur': event.couleur,
                            'numero': event.numero,
                            'mavar': event.weekend
                        
                       
                        })
                    
                 
                        
                       
                       
                           
        
                                        
                if event.frequency == 'SEMAINE':
                    print 'SEMAINE'
                    print 'jour semaine', event_start.strftime('%A')
                    print 'depart',  event_start.strftime('%A')
                    print 'arrivee', event_end.strftime('%A')
                    print 'unefin', event.fin

                    tab1= event.fin
                    event_fin = event.fin * 7
                    event_fin = event_fin + 2 * tab1
                    print event_fin
                    
                    event_list.append({
                                'categorie': event.calendar.as_dict(),
                                'id': event.id,
                                'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                'title': event.title,
                                'description': event.description,
                                'fin':event.fin,
                                'frequency': event.frequency,
                                'allDay': allDay,
                                'lundi':  event.lundi,
                                'mardi': event.mardi,
                                'mercredi': event.mercredi,
                                'jeudi': event.jeudi,
                                'vendredi': event.vendredi,
                                'samedi': event.samedi,
                                'dimanche': event.dimanche,
                                'couleur': event.couleur,
                                'numero': event.numero,
                                'mavar': event.weekend
                                })

                      
               
                    
                if event.frequency == 'BIMENSUEL':
                    if event_end.strftime('%A')=='Saturday':
                        event_fin = event.fin * 14
                        event.fin=event.fin+2
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })

                    if event_end.strftime('%A')=='Sunday':
                        event_fin = event.fin * 14
                        event.fin=event.fin+1
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                    if event_end.strftime('%A') !='Saturday' and event_end.strftime('%A') !='Sunday':
                        event_fin = event.fin * 14
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
               
                    
                if event.frequency == 'MENSUEL':
                     if event_end.strftime('%A')=='Saturday':
                         event_fin = event.fin * 30
                         event.fin=event.fin+2
                         event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                         
                     if event_end.strftime('%A')=='Sunday':
                         event_fin = event.fin * 30
                         event.fin=event.fin+1
                         event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                     if event_end.strftime('%A') !='Saturday' and event_end.strftime('%A') !='Sunday':
                        event_fin = event.fin * 30
                        event_list.append({
                                    'categorie': event.calendar.as_dict(),
                                    'id': event.id,
                                    'start': event_start.strftime('%Y-%m-%d %H:%M:%S'),
                                    'end': str(datetime.datetime.strptime(event_start.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  + datetime.timedelta(days=event_fin - 1)),
                                    'title': event.title,
                                    'description': event.description,
                                    'fin':event.fin,
                                    'frequency': event.frequency,
                                    'allDay': allDay,
                                    'lundi':  event.lundi,
                                    'mardi': event.mardi,
                                    'mercredi': event.mercredi,
                                    'jeudi': event.jeudi,
                                    'vendredi': event.vendredi,
                                    'samedi': event.samedi,
                                    'dimanche': event.dimanche,
                                    'couleur': event.couleur,
                                    'numero': event.numero,
                                    'mavar': event.weekend
                                    })
                

            

        

    
    if len(event_list) == 0:
        raise http.Http404
    else:
        return http.HttpResponse(json.dumps(event_list),
                                 content_type='application/json')
    
                

      
           


           














    
