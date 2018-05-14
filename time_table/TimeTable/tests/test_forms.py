from django.test import TestCase

# Create your tests here.

from TimeTable.forms import AddMechanic


class AddMechanicFormTest(TestCase):
    # Check if the help_text is correct
    def test_add_mech_form_phone_field_help_text(self):
        form = AddMechanic()
        self.assertEqual(form.fields['phone'].help_text,'Use only numbres without space, example: 375291234567')

    # Check if the form is valid with right input data
    def test_phone_form_correct(self):
        name = 'Mike'
        surname = 'Jordan'
        address = 'Chicago'
        timetable_number = 5011
        phone_start_with = 375
        form_data = {'phone': phone_start_with,
                     'name': name,
                     'surname':surname,
                     'address':address,
                     'timetable_number':timetable_number}
        form = AddMechanic(data=form_data)
        self.assertTrue(form.is_valid())

    # Check if the form is not valid with incorrect data (number of code is less than right code)
    def test_phone_form_incorrect_less(self):
        name = 'Mike'
        surname = 'Jordan'
        address = 'Chicago'
        timetable_number = 5011
        phone_start_with = 374
        form_data = {'phone': phone_start_with,
                     'name': name,
                     'surname':surname,
                     'address':address,
                     'timetable_number':timetable_number}
        form = AddMechanic(data=form_data)
        self.assertFalse(form.is_valid())

    # Check if the form is not valid with incorrect data (number of code is more than right code)
    def test_phone_form_incorrect_more(self):
        name = 'Mike'
        surname = 'Jordan'
        address = 'Chicago'
        timetable_number = 5011
        phone_start_with = 376
        form_data = {'phone': phone_start_with,
                     'name': name,
                     'surname':surname,
                     'address':address,
                     'timetable_number':timetable_number}
        form = AddMechanic(data=form_data)
        self.assertFalse(form.is_valid())

    # Check if the form is not valid with incorrect data (number of code is 0)
    def test_phone_form_incorrect_zero(self):
        name = 'Mike'
        surname = 'Jordan'
        address = 'Chicago'
        timetable_number = 5011
        phone_start_with = 0
        form_data = {'phone': phone_start_with,
                     'name': name,
                     'surname':surname,
                     'address':address,
                     'timetable_number':timetable_number}
        form = AddMechanic(data=form_data)
        self.assertFalse(form.is_valid())