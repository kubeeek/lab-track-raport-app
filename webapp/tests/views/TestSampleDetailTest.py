from django.test import RequestFactory, TestCase
from django.urls import reverse

from webapp.models import TestSample, TestingFacility
from webapp.views import TestSampleDetailView


class TestSampleDetailViewTestCase(TestCase):
    def setUp(self):
        self.testing_facility = TestingFacility.objects.create(
            name="Test Facility 1",
            address="Test St 123"
        )

        self.test_sample = TestSample.objects.create(
            sample_code='TEST123',
            customer_name='Test Customer',
            source_facility=self.testing_facility,
            description='Test Description',
            admission_date='2022-01-01',
            expiration_date='2022-12-31',
            expiration_date_optional="",
            test_end_date='2022-12-31',
            sample_size='100g',
            appeal_test=False,
            sample_condition='Bez zastrzezeń',
            sample_type='T1',
            sample_method='T1',
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('test_sample_detail', args=[self.test_sample.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webapp/testsample_detail.html')

    def test_view_passes_correct_data_to_template(self):
        response = self.client.get(reverse('test_sample_detail', args=[self.test_sample.id]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['testsample'], self.test_sample)

    def test_view_404_for_invalid_test_sample(self):
        response = self.client.get(reverse('test_sample_detail', args=[9999]))

        self.assertEqual(response.status_code, 404)
