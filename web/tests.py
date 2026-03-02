from django.test import TestCase
from django.urls import reverse

from .models import GeneRecord, MultiOmicsMeasurement


class BioDbViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.gene = GeneRecord.objects.create(
            gene_id='BRCA1',
            gene_symbol='BRCA1',
            species='Homo sapiens',
            description='DNA repair gene',
            chromosome='17q21.31',
            start=43044295,
            end=43170245,
        )
        MultiOmicsMeasurement.objects.create(
            gene=cls.gene,
            omics_type='transcriptomics',
            sample_id='SAMPLE-001',
            tissue='Breast',
            condition='Tumor',
            value=10.2,
            unit='TPM',
        )

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '多组学生物信息数据库')

    def test_search_by_gene_id(self):
        response = self.client.get(reverse('gene_search'), {'q': 'BRCA1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BRCA1')

    def test_gene_detail_page(self):
        response = self.client.get(reverse('gene_detail', kwargs={'gene_id': 'BRCA1'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'SAMPLE-001')

    def test_portal_page(self):
        response = self.client.get(reverse('portal', kwargs={'portal_name': 'genomics'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '基因组学门户')
