from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


DEPARTMENT_CHOICES = [
    ('Applied Mechanics', 'Applied Mechanics'),
    ('Automobile Engineering', 'Automobile Engineering'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Computer Technology', 'Computer Technology'),
    ('Dress Desigining and Garments Manufacturing', 'Dress Desigining and Garments Manufacturing'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Exam Section', 'Exam Section'),
    ('Gymkhana', 'Gymkhana'),
    ('Hostel Boys', 'Hostel Boys'),
    ('Hostel Girls', 'Hostel Girls'),
    ('Information Technology', 'Information Technology'),
    ('Interior Desigining & Decoration', 'Interior Desigining & Decoration'),
    ('Library', 'Library'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Mechatronics engineering', 'Mechatronics engineering'),
    ('Office', 'Office'),
    ('Plastic Engineering', 'Plastic Engineering'),
    ('Science (Chemistry)' , 'Science (Chemistry)'),
    ('Science (Physics)' , 'Science (Physics)'),
    ('Workshop', 'Workshop'),

]


class DepartmentUserCreationForm(forms.ModelForm):
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'department']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
        return user