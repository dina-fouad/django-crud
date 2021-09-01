from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="dina", email="dina_albarghouthi@yahoo.com", password="pass"
        )

        self.snack = Snack.objects.create(
            title = 'falafel',
            description  = 'delecious',
            purchaser = self.user
        )

    def test_snack_representation(self):
        self.assertEqual(str(self.snack), "falafel")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "falafel")
        self.assertEqual(f"{self.snack.purchaser}", "dina")
        self.assertEqual(f"{self.snack.description}", "delecious")

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "falafel")
        self.assertTemplateUsed(response, "snack_list.html")


    def test_snack_details_view(self):
        expected = 200
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/999/")
        self.assertEqual(response.status_code, expected)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "falafel")
        self.assertTemplateUsed(response, "snack_detail.html")



    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)

