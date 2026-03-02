from django.db import models


class GeneRecord(models.Model):
    gene_id = models.CharField('基因ID', max_length=32, unique=True)
    gene_symbol = models.CharField('基因符号', max_length=32)
    species = models.CharField('物种', max_length=64, default='Homo sapiens')
    description = models.TextField('功能描述', blank=True)
    chromosome = models.CharField('染色体', max_length=16, blank=True)
    start = models.PositiveIntegerField('起始位点', default=0)
    end = models.PositiveIntegerField('终止位点', default=0)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        ordering = ['gene_id']

    def __str__(self) -> str:
        return f'{self.gene_id} ({self.gene_symbol})'


class MultiOmicsMeasurement(models.Model):
    OMICS_CHOICES = [
        ('genomics', 'Genomics'),
        ('transcriptomics', 'Transcriptomics'),
        ('proteomics', 'Proteomics'),
        ('metabolomics', 'Metabolomics'),
        ('epigenomics', 'Epigenomics'),
    ]

    gene = models.ForeignKey(GeneRecord, on_delete=models.CASCADE, related_name='measurements')
    omics_type = models.CharField('组学类型', max_length=32, choices=OMICS_CHOICES)
    sample_id = models.CharField('样本ID', max_length=64)
    tissue = models.CharField('组织来源', max_length=64, blank=True)
    condition = models.CharField('实验条件', max_length=64, blank=True)
    value = models.FloatField('定量值')
    unit = models.CharField('单位', max_length=32, default='a.u.')
    p_value = models.FloatField('P值', null=True, blank=True)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        ordering = ['omics_type', 'sample_id']

    def __str__(self) -> str:
        return f'{self.gene.gene_id} - {self.omics_type} - {self.sample_id}'
