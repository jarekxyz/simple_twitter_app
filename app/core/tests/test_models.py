from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone

from core import models


def sample_user(email='test@example.com', password="P@ssword123"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user(self):
        """Test if creating a new user with email is successful"""
        email = 'test@example.com'
        password = 'P@ssword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalization(self):
        """Test if email for a new user is normalized"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(email, 'P@ssword123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'P@ssword123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'P@ssword123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            text="Test tag"
        )

        self.assertEqual(str(tag), tag.text)

    def test_tweet_str(self):
        """Test the tweet string representation"""
        author = sample_user()
        date_created = timezone.now()
        text = "Test tweet content"

        tweet = models.Tweet.objects.create(
            author=author,
            date_created=date_created,
            text=text
        )

        tweet_str = "{0}, {1}\n{2}\n".format(author,
                                             date_created,
                                             text)

        self.assertEqual(str(tweet), tweet_str)
