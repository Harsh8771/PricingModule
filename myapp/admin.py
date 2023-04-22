from django.contrib import admin
from .models import PricingConfig

class PricingConfigAdmin(admin.ModelAdmin):
    list_display=('id','distance_base_price','distance_additional_price','time_multiplier_factor','enable','distance_limit','time_limit')
    list_editable=('distance_base_price','distance_additional_price','time_multiplier_factor','enable','distance_limit','time_limit')

# registering model to admin pannel
admin.site.register(PricingConfig,PricingConfigAdmin)


