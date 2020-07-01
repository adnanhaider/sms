from django.test import TestCase
from .models import User

class UserProfileTest(TestCase):
    
    def test_user_model_has_profile(self):
        user = User(
            email = "adnan@gmail.com",
            password="admin"
        )
        user.save()
        self.assertTrue(
            hasattr(user, 'principal')
        )