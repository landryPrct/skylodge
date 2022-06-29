from django.contrib import admin
from django.contrib.auth.models import Group
from reservations.models import Chambre, Reservation,Categorie
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp,EmailAddress


admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)


admin.site.site_header = 'Sky Lodge Administration '
admin.site.index_title = "Welcome Sky Lodge Administration  "
admin.site.register(Chambre)
admin.site.register(Reservation)
admin.site.register(Categorie)
admin.site.unregister(Group)
