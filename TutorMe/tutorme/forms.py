from django import forms
from tutorme.models import Category, Student, Teacher, Review, User

RATING = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

CATEGORY_CHOICES = [
    ('none', 'None'),
    ('algebra', 'Algebra'),
    ('mathematics', 'Mathematics'),
]


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.NAME_MAX_LENGTH,help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password',)


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'description', 'location', 'picture',)


class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    categories_list = forms.CharField(label='Choose any category to add to your list', widget=forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-control categories'}))
    categories = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control teacherCategories', 'readonly': 'readonly', 'id': 'teacherCategories', 'rows': 2}))

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'description', 'location', 'categories_list', 'categories', 'picture',)


class ReviewForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    rating = forms.CharField(label='What is your rating?', widget=forms.Select(choices=RATING))

    class Meta:
        model = Review
        fields = ('title', 'description', 'rating',)
