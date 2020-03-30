from __future__ import unicode_literals

from django.template.defaultfilters import slugify
from .manager import UserManager
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


# Category model used to store a tutor category
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# User model used to store a user but overrides the default user in django by inheriting from
# AbstractBaseUser and PermissionsMixin to create a user that the unique attribute is the
# email and not the username
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=False, unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


# Abstract model used to store the student and teacher common attributes
class CommonInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30, blank=False, default='')
    last_name = models.CharField(max_length=30, blank=False, default='')
    picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    location = models.CharField(_('location'), max_length=30, blank=False)
    description = models.CharField(_('description'), max_length=100, blank=False)
    rating = models.IntegerField(_('rating'), default=0)

    class Meta:
        abstract = True

    # function used to calculate the rating of the current teacher
    def calculate_rating(self, **kwargs):
        my_reviews = Review.objects.filter(reviewee=self.user)
        mean_rating = 0
        for review in my_reviews:
            mean_rating = mean_rating + review.rating
        mean_rating = mean_rating/len(my_reviews)
        self.rating = mean_rating
        self.save()

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.user.email], **kwargs)


# Student model that inherits from the commonInfo above
class Student(CommonInfo):

    class Meta(CommonInfo.Meta):
        db_table = 'students'
        verbose_name = _('student')
        verbose_name_plural = _('students')


# Student model that inherits from the commonInfo above nad adds more attributes unique to the teacher
class Teacher(CommonInfo):
    categories = models.ManyToManyField(Category, related_name="teachers", blank=True)
    active = models.BooleanField(default=True)
    students = models.ManyToManyField(Student, related_name="teachers")
    notify = models.BooleanField(default=False)

    class Meta(CommonInfo.Meta):
        db_table = 'teachers'
        verbose_name = _('teacher')
        verbose_name_plural = _('teachers')


# Review model used to enable students add rating to the teachers
# this will later include more attributes upon user request
class Review(models.Model):
    rating = models.IntegerField(_('rating'), blank=False)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    reviewee = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reviewee')
    reviewer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reviewer')

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')
