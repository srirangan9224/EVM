from django.test import Client,TestCase
from django.db.models import Max

from.models import *

# Create your tests here.
class CandidateTestCase(TestCase):
    
    def setUp(self):
        c1 = Candidate.objects.create(
            name = "test1",
            Class = 11,
            section = "D",
            logo = None,
            description = "sample description",
            gender = "Male",
            image = None
        )
        

        c2 = Candidate.objects.create(

            name = "test2",
            Class = 14,
            section = "C",
            logo = None,
            description = "sample description",
            gender = "Female",
            image = None

        )

        c3 = Candidate.objects.create(

            name = "",
            Class = 11,
            section = "D",
            logo = None,
            description = "sample description",
            gender = "Male",
            image = None

        )


    def test_name(self):
        c1 = Candidate.objects.get(name="test1")
        self.assertEqual(c1.is_valid_candidate(),True)

        c3 = Candidate.objects.get(name="")
        self.assertEqual(c3.is_valid_candidate(),False)

    def test_class(self):
        c2 = Candidate.objects.get(Class=14)
        self.assertFalse(c2.is_valid_candidate())

        c1 = Candidate.objects.get(name="test1")
        self.assertTrue(c1.is_valid_candidate())
