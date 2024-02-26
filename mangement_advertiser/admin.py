from django.contrib import admin

from .models import Ad, Advertiser, Click, View

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'advertiser', 'approve')
    list_filter = ('approve', 'advertiser__name')  
    search_fields = ('title', 'advertiser__name') 


admin.site.register(Advertiser)
admin.site.register(Click)
admin.site.register(View)