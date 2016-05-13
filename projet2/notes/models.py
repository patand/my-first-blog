# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

frequence = (
             ('0', '-----------'),
             ('1', 'une semaine'),
             ('2', 'deux semaines'),
             ('3', 'trois semaines'),
             ('4', 'quatre semaines'),
        
     )

freqs = (
         ('NONE', _('Aucun')),
         ('JOUR', _('Jour')),
         ('SEMAINE', _('Hebdomadaire')),
         ('BIMENSUEL', _('Bimensuel')),
         ('MENSUEL', _('Mensuel')),
        
     )

COLOR = (
          ('NONE', _('Aucun')),
          ('ROUGE', _('rouge')),
          ('BLEU', _('bleu')),
          ('VERT', _('vert')),
          ('JAUNE', _('jaune')),
          ('ORANGE', _('orange')),
          ('MAGENTA', _('magenta')),
          ('CYAN', _('cyan')),
        )

WEEKEND = (
            ('NONE', _('Aucun')),
             ('EXCLUDE', _('exclus')),
             ('INCLUDE', _('inclus')),
            )


CYCLES = (
             (0, '----------'),
             (1, '1'),
             (2, '2'),
             (3, '3'),
             (4, '4'),
             (5, '5'),
             (6, '6'),
             (7, '7'),
             (8, '8'),
             (9, '9'),
             (10, '10'),
             (11, '11'),
             (12, '12'),
             (13, '13'),
             (14, '14'),
             (15, '15'),
             (16, '16'),
             (17, '17'),
             (18, '18'),
             (19, '19'),
             (20, '20'),
             (21, '21'),
             (22, '22'),
             (23, '23'),
             (24, '24'),
             (25, '25'),
                  )



CYCLES2 = (
             (0, '------'),
             (1, '1'),
             (2, '2'),
             (3, '3'),
             (4, '4'),
             (5, '5'),
                  )


class Calendar(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(_('slug'), unique=True)

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }
        
    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _('machine')
        ordering = ['name']

class Event(models.Model):
    title = models.CharField(_('titre'), max_length=100)
    start = models.DateTimeField(_(u"début de l'essai"))
    end = models.DateTimeField(_(u"Dépôt de la demande:"))#, editable=False, null=True, auto_now_add = True)
    is_cancelled = models.BooleanField(_('Annulation?'), default=False, blank=True)
    calendar = models.ForeignKey(Calendar, verbose_name=_('machine'))
    user = models.ForeignKey(User, default=None, blank= True, null = True, verbose_name=_('Utilisateur'))
    description = models.TextField(_(u"Type d'essai"), blank=True)
    frequency = models.CharField(_(u"Période :"), choices=freqs, max_length=10, default=0)
    fin = models.IntegerField(_(u"Nombre de cycles :"), choices=CYCLES, default=0)
    rep = models.IntegerField(_(u"Eprouvettes traitées:"), default=0)
    activated = models.BooleanField(verbose_name='Activation ?', default=False, blank=True)
    lundi = models.BooleanField(verbose_name='rouge', default=0, blank=True)
    mardi = models.BooleanField(verbose_name='bleu', default=0, blank=True)
    mercredi = models.BooleanField(verbose_name='vert', default=0, blank=True)
    jeudi = models.BooleanField(verbose_name='jaune', default=0, blank=True)
    vendredi = models.BooleanField(verbose_name='orange', default=0, blank=True)
    samedi = models.BooleanField(verbose_name='magenta', default=0, blank=True)
    dimanche = models.BooleanField(verbose_name='cyan', default=0, blank=True)
    lefichier = models.FileField(_(u"Pièce jointe"), upload_to='medias', null=True, blank=True)
    numero = models.CharField(_(u"Numéro de l'étude  :"), max_length=100, default = '0')
    lenombre = models.IntegerField(_(u"Nombre d'éprouvettes  :"), choices=CYCLES2, default=0)
    couleur = models.CharField(_(u"Couleur :"), choices=COLOR, max_length=10, default=0)
    weekend = models.CharField(_(u"Weekend :"), choices=WEEKEND, max_length=20, default=0)
    demandeur = models.CharField(_(u"Nom du demandeur"), max_length=100, default=0)
    rep2 = models.IntegerField(_(u"Eprouvettes à traiter:"), default=0)

    def lefichier_(self):
        if self.lefichier:
            return "<a href='%s'>download</a>" % (self.lefichier.url,)
        else:
            return "No attachment"

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        verbose_name = _('essai')
        #ordering = ['start', 'end']
