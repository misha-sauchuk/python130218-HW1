from django.test import TestCase

# Create your tests here.

from TimeTable.models import Mechanic


class MechacnicModelTest(TestCase):

    # Create an object that we'll use in tests
    @classmethod
    def setUpTestData(cls):
        Mechanic.objects.create(name='Mikhail',
                                surname='Sauchuk',
                                phone='375297287180',
                                address='Minsk',
                                timetable_number='5055')

    # Check if the field label(verbose_name)
    def test_name_label(self):
        mechainc = Mechanic.objects.get(id=1)
        field_label = mechainc._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    # Check if the field label(verbose_name)
    def test_surname_label(self):
        mechainc = Mechanic.objects.get(id=1)
        field_label = mechainc._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')

    # Check if the field label(verbose_name)
    def test_phone_label(self):
        mechainc = Mechanic.objects.get(id=1)
        field_label = mechainc._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    # Check if the field label(verbose_name)
    def test_timetable_number_label(self):
        mechainc = Mechanic.objects.get(id=1)
        field_label = mechainc._meta.get_field('timetable_number').verbose_name
        self.assertEquals(field_label, 'timetable number')

    # Check if the reload method __str__ return wright data
    def test_object_name_is_name_space_surname(self):
        mechanic = Mechanic.objects.get(id=1)
        expected_object_name = '{} {}'.format(mechanic.name, mechanic.surname)
        self.assertEquals(expected_object_name, str(mechanic))


