from django.test import TestCase


class BadRequestTests(TestCase):
    def test_invalid_date(self):
        response = self.client.get('/conferences/?dateStart=somesymbols')
        self.assertEqual(response.status_code, 422)
        response = self.client.get('/conferences/?dateFinish=somesymbols')
        self.assertEqual(response.status_code, 422)

    def test_multiple_date_start_specified(self):
        response = self.client.get('/conferences/?dateStart=2002-02-02&dateStart=2002-02-02')
        self.assertEqual(response.status_code, 400)
        response = self.client.get('/conferences/?dateFinish=2002-02-02&dateFinish=2002-02-02')
        self.assertEqual(response.status_code, 400)
