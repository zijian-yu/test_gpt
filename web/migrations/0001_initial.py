from django.db import migrations, models
import django.db.models.deletion


def seed_demo_data(apps, schema_editor):
    GeneRecord = apps.get_model('web', 'GeneRecord')
    MultiOmicsMeasurement = apps.get_model('web', 'MultiOmicsMeasurement')

    genes = [
        {
            'gene_id': 'BRCA1',
            'gene_symbol': 'BRCA1',
            'species': 'Homo sapiens',
            'description': 'DNA损伤修复相关抑癌基因。',
            'chromosome': '17q21.31',
            'start': 43044295,
            'end': 43170245,
        },
        {
            'gene_id': 'TP53',
            'gene_symbol': 'TP53',
            'species': 'Homo sapiens',
            'description': '经典肿瘤抑制因子，调控细胞周期与凋亡。',
            'chromosome': '17p13.1',
            'start': 7661779,
            'end': 7687550,
        },
        {
            'gene_id': 'EGFR',
            'gene_symbol': 'EGFR',
            'species': 'Homo sapiens',
            'description': '表皮生长因子受体，常见肿瘤驱动基因。',
            'chromosome': '7p11.2',
            'start': 55086714,
            'end': 55275885,
        },
    ]

    for item in genes:
        gene = GeneRecord.objects.create(**item)
        MultiOmicsMeasurement.objects.create(
            gene=gene,
            omics_type='transcriptomics',
            sample_id='TCGA-DEMO-001',
            tissue='Breast',
            condition='Tumor',
            value=12.8,
            unit='TPM',
            p_value=0.003,
        )
        MultiOmicsMeasurement.objects.create(
            gene=gene,
            omics_type='proteomics',
            sample_id='CPTAC-DEMO-001',
            tissue='Breast',
            condition='Tumor',
            value=2.31,
            unit='log2FC',
            p_value=0.017,
        )


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='GeneRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_id', models.CharField(max_length=32, unique=True, verbose_name='基因ID')),
                ('gene_symbol', models.CharField(max_length=32, verbose_name='基因符号')),
                ('species', models.CharField(default='Homo sapiens', max_length=64, verbose_name='物种')),
                ('description', models.TextField(blank=True, verbose_name='功能描述')),
                ('chromosome', models.CharField(blank=True, max_length=16, verbose_name='染色体')),
                ('start', models.PositiveIntegerField(default=0, verbose_name='起始位点')),
                ('end', models.PositiveIntegerField(default=0, verbose_name='终止位点')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={'ordering': ['gene_id']},
        ),
        migrations.CreateModel(
            name='MultiOmicsMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omics_type', models.CharField(choices=[('genomics', 'Genomics'), ('transcriptomics', 'Transcriptomics'), ('proteomics', 'Proteomics'), ('metabolomics', 'Metabolomics'), ('epigenomics', 'Epigenomics')], max_length=32, verbose_name='组学类型')),
                ('sample_id', models.CharField(max_length=64, verbose_name='样本ID')),
                ('tissue', models.CharField(blank=True, max_length=64, verbose_name='组织来源')),
                ('condition', models.CharField(blank=True, max_length=64, verbose_name='实验条件')),
                ('value', models.FloatField(verbose_name='定量值')),
                ('unit', models.CharField(default='a.u.', max_length=32, verbose_name='单位')),
                ('p_value', models.FloatField(blank=True, null=True, verbose_name='P值')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='web.generecord')),
            ],
            options={'ordering': ['omics_type', 'sample_id']},
        ),
        migrations.RunPython(seed_demo_data, migrations.RunPython.noop),
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={'ordering': ['-created_at']},
        ),
    ]
