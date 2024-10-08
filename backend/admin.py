from django.contrib import admin

from .models import Place, Path, PlaceInPath, Team, TeamPlaceAnswer, Region

admin.site.site_title = "Администрирование телеграмм-бота"
admin.site.site_header = "Администрирование телеграмм-бота"


def denied(*args, **kwargs) -> bool:
    return False


class PlaceInPathInline(admin.TabularInline):
    model = PlaceInPath
    extra = 0


class PathAdmin(admin.ModelAdmin):
    inlines = [PlaceInPathInline]


class TeamPlaceAnswerInline(admin.TabularInline):
    model = TeamPlaceAnswer
    has_add_permission = denied
    readonly_fields = ['team', 'place', 'start_datetime', 'end_datetime', 'photo', 'task_answer']
    extra = 0


class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'contacts', 'path']
    has_add_permission = denied
    inlines = [TeamPlaceAnswerInline]


admin.site.register(Place)
admin.site.register(Region)
admin.site.register(Path, PathAdmin)
admin.site.register(Team, TeamAdmin)
