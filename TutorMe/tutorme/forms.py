from django import forms
from tutorme.models import Category, Student, Teacher, Review, User


# Form used to register and login the user by using the user model
class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'password',)


# Form used to register a student
class StudentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'description', 'location', 'picture',)


# Form used to register a teacher
class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'description', 'location', 'picture', 'categories',)

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields["categories"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["categories"].help_text = ""
        self.fields["categories"].queryset = Category.objects.all()


# Form used to update the given teacher tuple
class TeacherUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    active = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Teacher
        fields = ('description', 'location', 'picture', 'active', 'categories',)

    # initialise categories attribute with all the categories in the db
    def __init__(self, *args, **kwargs):
        super(TeacherUpdateForm, self).__init__(*args, **kwargs)
        self.fields["categories"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["categories"].help_text = ""
        self.fields["categories"].queryset = Category.objects.all()


# Form used to update the given student tuple
class StudentUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        fields = ('description', 'location', 'picture',)
