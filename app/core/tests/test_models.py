from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_email_user_succ(self):
        """
        test creating a new user with email successfully
        """
        email = "test.email@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """
        Test the email for the new user is normalized
        """
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        """
        test creating email  with no email raise error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
    
    def test_create_new_super_user(self):
        """
        Test create new super user
        """
        user = get_user_model().objects.create_superuser('test3@gmail.com','test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)