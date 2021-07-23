from django.test import TestCase

class TestHomeViews(TestCase):
    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_get_contact(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    # Valid email submitted
    def test_post_contact(self):
        form = {
            "name": "Tester",
            "email": "user@email.com",
            "subject": "This is a test",
            "message":  "Some String"
        }
        response = self.client.post("/contact/", form)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/")
