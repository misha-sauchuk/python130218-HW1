from django.test import TestCase

# Create your tests here.

from TimeTable.models import Mechanic


class MechacnicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Mechanic.objects.create(name='Mikhail',
                                surname='Sauchuk',
                                phone='375297287180',
                                address='Minsk',
                                timetable_number='5055')

    def test_name_label(self):
        mechainc = Mechanic.objects.get(id=1)
        field_label = mechainc._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')




