from django.contrib import admin

from cl.favorites.models import Favorite, UserTag, DocketTag


class FavoriteInline(admin.TabularInline):
    model = Favorite
    extra = 1
    raw_id_fields = (
        "user",
        "cluster_id",
        "audio_id",
        "docket_id",
        "recap_doc_id",
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "cluster_id",
    )
    raw_id_fields = (
        "user",
        "cluster_id",
        "audio_id",
        "docket_id",
        "recap_doc_id",
    )


admin.site.register(UserTag)
admin.site.register(DocketTag)
