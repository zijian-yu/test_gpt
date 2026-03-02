from django.contrib import admin

from .models import GeneRecord, MultiOmicsMeasurement


@admin.register(GeneRecord)
class GeneRecordAdmin(admin.ModelAdmin):
    list_display = ('gene_id', 'gene_symbol', 'species', 'chromosome', 'updated_at')
    search_fields = ('gene_id', 'gene_symbol', 'species')


@admin.register(MultiOmicsMeasurement)
class MultiOmicsMeasurementAdmin(admin.ModelAdmin):
    list_display = ('gene', 'omics_type', 'sample_id', 'tissue', 'value', 'p_value')
    list_filter = ('omics_type', 'tissue', 'condition')
    search_fields = ('gene__gene_id', 'gene__gene_symbol', 'sample_id')
