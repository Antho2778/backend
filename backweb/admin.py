from django.contrib import admin
from .models import Prestation, Realisation, Review

class PrestationAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Register your models here.

admin.site.register(Prestation, PrestationAdmin)

class RealisationAdmin(admin.ModelAdmin):
    list_display = ('title', 'lieu', 'date', 'photo_before', 'photo_after' , 'description' )

# Register your models here.

admin.site.register(Realisation, RealisationAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'date', 'description' , 'rating')

# Register your models here.

admin.site.register(Review, ReviewAdmin)
# Register your models here.
