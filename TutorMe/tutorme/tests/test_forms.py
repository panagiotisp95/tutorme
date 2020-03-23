from django.test import TestCase
from tutorme.forms import TeacherForm, StudentForm, TeacherUpdateForm, StudentUpdateForm, UserForm


class UserFormTest(TestCase):
    def test_user_form_email_field_label(self):
        form = UserForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Email')

    def test_user_form_password_field_label(self):
        form = UserForm()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')


class TeacherFormTest(TestCase):
    def test_teacher_form_first_name_field_label(self):
        form = TeacherForm()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')

    def test_teacher_form_last_name_field_label(self):
        form = TeacherForm()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Last name')

    def test_teacher_form_description_field_label(self):
        form = TeacherForm()
        self.assertTrue(form.fields['description'].label == None or form.fields['description'].label == 'Description')

    def test_teacher_form_location_field_label(self):
        form = TeacherForm()
        self.assertTrue(form.fields['location'].label == None or form.fields['location'].label == 'Location')


class StudentFormTest(TestCase):
    def test_student_form_first_name_field_label(self):
        form = StudentForm()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')

    def test_student_form_last_name_field_label(self):
        form = StudentForm()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Last name')

    def test_student_form_description_field_label(self):
        form = StudentForm()
        self.assertTrue(form.fields['description'].label == None or form.fields['description'].label == 'Description')

    def test_student_form_location_field_label(self):
        form = StudentForm()
        self.assertTrue(form.fields['location'].label == None or form.fields['location'].label == 'Location')


class TeacherUpdateFormTest(TestCase):
    def test_teacher_update_form_description_field_label(self):
        form = TeacherUpdateForm()
        self.assertTrue(form.fields['description'].label == None or form.fields['description'].label == 'Description')

    def test_teacher_update_form_location_field_label(self):
        form = TeacherUpdateForm()
        self.assertTrue(form.fields['location'].label == None or form.fields['location'].label == 'Location')

    def test_teacher_update_form_active_field_label(self):
        form = TeacherUpdateForm()
        self.assertTrue(form.fields['active'].label == None or form.fields['active'].label == 'Active')


class StudentUpdateFormTest(TestCase):
    def test_student_update_form_description_field_label(self):
        form = StudentUpdateForm()
        self.assertTrue(form.fields['description'].label == None or form.fields['description'].label == 'Description')

    def test_student_update_form_location_field_label(self):
        form = StudentUpdateForm()
        self.assertTrue(form.fields['location'].label == None or form.fields['location'].label == 'Location')
