from django.db.models import Q
from django.shortcuts import render

from .models import GeneRecord


def home(request):
    featured_genes = GeneRecord.objects.all()[:6]
    return render(request, 'web/home.html', {'featured_genes': featured_genes})


def gene_search(request):
    keyword = request.GET.get('q', '').strip()
    records = GeneRecord.objects.none()
    if keyword:
        records = GeneRecord.objects.filter(
            Q(gene_id__icontains=keyword) | Q(gene_symbol__icontains=keyword)
        )
    return render(
        request,
        'web/gene_search.html',
        {
            'keyword': keyword,
            'records': records,
        },
    )


def gene_detail(request, gene_id):
    gene = GeneRecord.objects.filter(gene_id__iexact=gene_id).prefetch_related('measurements').first()
    return render(request, 'web/gene_detail.html', {'gene': gene, 'query_id': gene_id})


def portal(request, portal_name):
    portal_map = {
        'genomics': '基因组学门户',
        'transcriptomics': '转录组学门户',
        'proteomics': '蛋白组学门户',
        'metabolomics': '代谢组学门户',
        'epigenomics': '表观组学门户',
        'downloads': '数据下载门户',
        'docs': '文档与API门户',
    }
    return render(
        request,
        'web/portal.html',
        {
            'portal_name': portal_name,
            'portal_title': portal_map.get(portal_name, '综合门户'),
        },
    )
from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.all()[:10]
    return render(request, 'web/home.html', {'posts': posts})


def about(request):
    return render(request, 'web/about.html')
