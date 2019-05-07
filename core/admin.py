from django.contrib import admin
from core.models import Content, Attach


class AttachInline(admin.TabularInline):
    model = Attach


class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_id',
        'writer_id',
        'sliced_title',
        'sliced_content',
        'created_date',
        'modified_date'
    )
    inlines = [
        AttachInline
    ]

    @staticmethod
    def sliced_title(obj):
        title = obj.title
        if len(title) < 50:
            return title
        else:
            return title[:50]

    @staticmethod
    def sliced_content(obj):
        content = obj.content
        if len(content) < 70:
            return content
        else:
            return content[:70]


class AttachAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file_name',
        'file_ext',
        'file_path',
        'created_date',
        'modified_date'
    )


admin.site.register(Content, ContentAdmin)
admin.site.register(Attach, AttachAdmin)
