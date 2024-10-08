from django.contrib import admin

from .models import Place, Path, PlaceInPath, Team, TeamPlaceAnswer

admin.site.site_title = "Администрирование телеграмм-бота"
admin.site.site_header = "Администрирование телеграмм-бота"


class PlaceInPathInline(admin.TabularInline):
    model = PlaceInPath
    extra = 1


class PathAdmin(admin.ModelAdmin):
    inlines = [PlaceInPathInline]


class TeamPlaceAnswerInline(admin.TabularInline):
    model = TeamPlaceAnswer
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamPlaceAnswerInline]


admin.site.register(Place)
admin.site.register(Path, PathAdmin)
admin.site.register(Team, TeamAdmin)
