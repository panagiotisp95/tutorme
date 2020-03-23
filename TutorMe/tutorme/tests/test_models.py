from django.test import TestCase
from tutorme.models import Teacher, User, Student, Review


class TeacherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='papapolydoroup@gmail.com', password='password')

    def test_email_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        field_label = user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        field_label = user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')


class TeacherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='papapolydoroup@gmail.com', password='password')
        Teacher.objects.create(user=user, first_name='Panayiotis', last_name='Papapolydorou', description="Hello")

    def test_first_name_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        max_length = teacher._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        max_length = teacher._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_location_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_location_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        max_length = teacher._meta.get_field('location').max_length
        self.assertEquals(max_length, 30)

    def test_description_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        max_length = teacher._meta.get_field('description').max_length
        self.assertEquals(max_length, 100)

    def test_rating_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_active_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        teacher = Teacher.objects.get(user=user)
        field_label = teacher._meta.get_field('active').verbose_name
        self.assertEquals(field_label, 'active')


class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='papapolydoroup@gmail.com', password='password')
        Student.objects.create(user=user, first_name='Panayiotis', last_name='Papapolydorou', description="Hello")

    def test_first_name_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        field_label = student._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        max_length = student._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 30)

    def test_last_name_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        field_label = student._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        max_length = student._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 30)

    def test_location_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        field_label = student._meta.get_field('location').verbose_name
        self.assertEquals(field_label, 'location')

    def test_location_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        max_length = student._meta.get_field('location').max_length
        self.assertEquals(max_length, 30)

    def test_description_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        field_label = student._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        max_length = student._meta.get_field('description').max_length
        self.assertEquals(max_length, 100)

    def test_rating_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        student = Student.objects.get(user=user)
        field_label = student._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(email='papapolydoroup@gmail.com', password='password')
        user1 = User.objects.create(email='papapolydoroup1@gmail.com', password='password1')
        Review.objects.create(rating=1, reviewee=user, reviewer=user1)

    def test_rating_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        review = Review.objects.get(reviewee=user)
        field_label = review._meta.get_field('rating').verbose_name
        self.assertEquals(field_label, 'rating')

    def test_reviewee_label(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        review = Review.objects.get(reviewee=user)
        field_label = review._meta.get_field('reviewee').verbose_name
        self.assertEquals(field_label, 'reviewee')

    def test_reviewer_max_length(self):
        user = User.objects.get(email='papapolydoroup@gmail.com')
        review = Review.objects.get(reviewee=user)
        field_label = review._meta.get_field('reviewer').verbose_name
        self.assertEquals(field_label, 'reviewer')
