from django.test import TestCase
from django.contrib.auth.models import User
from .models import NoteImage

class NoteImageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_note_image_creation(self):
        note = NoteImage.objects.create(
            user=self.user,
            title="Math Notes",
            subject="math",
            image="notes_images/test.jpg"  # dummy path for test
        )
        self.assertEqual(note.title, "Math Notes")
        self.assertEqual(note.subject, "math")