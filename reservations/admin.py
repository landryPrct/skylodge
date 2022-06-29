from django.contrib import admin
from django.contrib.auth.models import Group
from reservations.models import Chambre, Reservation,Categorie
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp,EmailAddress



class cha(admin.ModelAdmin):
    list_display = ['chambre_status','categorie',"chambre_numero"]

class res(admin.ModelAdmin):
    list_display = ['debut_sejour','fin_sejour','client','chambre','status',"date_operation"]

class cat(admin.ModelAdmin):
    list_display = ['type',"prix"]



admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(EmailAddress)


admin.site.site_header = 'Sky Lodge Administration '
admin.site.index_title = "Welcome Sky Lodge Administration  "
admin.site.register(Chambre,cha)
admin.site.register(Reservation,res)
admin.site.register(Categorie,cat)
admin.site.unregister(Group)


