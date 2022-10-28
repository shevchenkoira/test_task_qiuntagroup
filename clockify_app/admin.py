from django.contrib import admin

from clockify_app.models import Task, User, ParsingHistory, Project
from clockify_app.views import get_all_data


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_assignees', 'status', 'duration', 'project_name', 'start_date', 'end_date',
                    'start_time', 'end_time')
    list_filter = ('status', 'duration', 'project_name', 'start_date', 'end_date')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status')
    list_filter = ('status', )
    save_as = True
    save_on_top = True


class ParsingHistoryAdmin(admin.ModelAdmin):
    list_display = ('update_at',)
    list_filter = ('update_at', )
    readonly_fields = ('update_at',)
    save_as = True
    save_on_top = True

    def save_model(self, request, obj, form, change):
        get_all_data(request)
        super().save_model(request, obj, form, change)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_tasks', 'public', 'archived')
    list_filter = ('public', 'archived')
    save_as = True
    save_on_top = True


admin.site.register(Task, TaskAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ParsingHistory, ParsingHistoryAdmin)
