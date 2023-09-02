from django.contrib import admin
from .models import *


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "gender", "name", "votes")


admin.site.register(Candidate, CandidateAdmin)
