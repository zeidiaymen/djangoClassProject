from .models import *
from django.contrib import admin

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def setToValid(self,request,queryset):
        queryset.update(est_valide=True)
    setToValid.short_description="Valider"
    actions = ['setToValid']
    list_per_page = 2
    search_fields = ['nom','duree_projet']
    list_display = ('nom','duree_projet','temps_alloue_par_createur','descriptions','besoins','est_valide')

@admin.register(Etudiant)
class ProjectEtd(admin.ModelAdmin):
    def tester(self,request,queryset):
        queryset.update(nom="aymen")
    tester.short_description="ChangeName"
    actions=['tester']
    search_fields = ['nom']
    list_display =('nom','prenom','email')
#admin.site.register(Etudiant)
#admin.site.register(Project,ProjectAdmin)
admin.site.register(Coach)
admin.site.register(MemberShipInProject)