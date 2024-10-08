from django.contrib import admin

from .models import Place, Path, PlaceInPath, Team, TeamPlaceAnswer, Region

admin.site.site_title = "Администрирование телеграмм-бота"
admin.site.site_header = "Администрирование телеграмм-бота"


class PlaceInPathInline(admin.TabularInline):
    model = PlaceInPath
    extra = 0


class PathAdmin(admin.ModelAdmin):
    inlines = [PlaceInPathInline]


class TeamPlaceAnswerInline(admin.TabularInline):
    model = TeamPlaceAnswer
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamPlaceAnswerInline]


admin.site.register(Place)
admin.site.register(Region)
admin.site.register(Path, PathAdmin)
admin.site.register(Team, TeamAdmin)
