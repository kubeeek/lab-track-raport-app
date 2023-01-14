import datetime

from django.test import TestCase
from django.urls import reverse

from webapp.forms import TestSampleForm
from webapp.models import TestSample, TestingFacility

class TestSampleCreateViewTestCase(TestCase):
    def setUp(self):
        self.facility = TestingFacility.objects.create(
            name='Test Facility',
            address='123 Test St'
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('test_sample_create'))
        self.assertTemplateUsed(response, 'webapp/testsample_form.html')

    def test_view_uses_correct_form(self):
        response = self.client.get(reverse('test_sample_create'))
        self.assertIsInstance(response.context['form'], TestSampleForm)

    def test_view_creates_new_test_sample(self):
        data = {
            'sample_code': '12345',
            'source_facility': self.facility.id,
            'customer_name': 'Test Customer',
            'description': 'Test description',
            'admission_date': '2022-01-01',
            'expiration_date': '2022-01-31',
            'expiration_date_optional': '',
            'test_end_date': '2022-02-01',
            'sample_size': "1 lb",
            'appeal_test': False,
            'sample_condition': 'Good',
            'sample_type': 'T1',
            'sample_method': 'T1',
        };

        self.assertTrue(TestSampleForm(data).is_valid())
        response = self.client.post(reverse('test_sample_create'), data=data)


        # Django returns the redirect to the Details page of newly created entity
        self.assertEqual(response.status_code, 302)
        self.assertEqual(TestSample.objects.count(), 1)
        test_sample = TestSample.objects.first()
        self.assertEqual(test_sample.sample_code, '12345')
        self.assertEqual(test_sample.source_facility, self.facility)
        self.assertEqual(test_sample.customer_name, 'Test Customer')
        self.assertEqual(test_sample.description, 'Test description')
        self.assertEqual(test_sample.admission_date, datetime.date(2022, 1, 1))
        self.assertEqual(test_sample.expiration_date, datetime.date(2022, 1, 31))
        self.assertEqual(test_sample.expiration_date_optional, '')
        self.assertEqual(test_sample.test_end_date, datetime.date(2022, 2, 1))
        self.assertEqual(test_sample.sample_size, '1 lb')
        self.assertEqual(test_sample.appeal_test, False)
        self.assertEqual(test_sample.sample_condition, 'Good')
        self.assertEqual(test_sample.sample_type, 'T1')
        self.assertEqual(test_sample.sample_method, 'T1')