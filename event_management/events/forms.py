
from django import forms
from django.contrib.auth.models import User

from .models import (
    Event,
    Booking
)


# =====================================
# USER REGISTRATION FORM
# =====================================

class RegisterForm(forms.ModelForm):

    password = forms.CharField(

        widget=forms.PasswordInput(

            attrs={

                'class': 'form-control',

                'placeholder': 'Enter Password'

            }

        )

    )

    username = forms.CharField(

        widget=forms.TextInput(

            attrs={

                'class': 'form-control',

                'placeholder': 'Enter Username'

            }

        )

    )

    email = forms.EmailField(

        widget=forms.EmailInput(

            attrs={

                'class': 'form-control',

                'placeholder': 'Enter Email'

            }

        )

    )

    class Meta:

        model = User

        fields = [

            'username',

            'email',

            'password'

        ]

    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.filter(

            email=email

        ).exists():

            raise forms.ValidationError(

                "Email already exists."

            )

        return email


# =====================================
# EVENT FORM
# =====================================

class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = [

            'title',

            'description',

            'venue',
            'location',
            'date',

            'time',

            'total_tickets',

            'available_tickets',

            'image'

        ]

        widgets = {

            'title': forms.TextInput(

                attrs={

                    'class': 'form-control',

                    'placeholder': 'Event Title'

                }

            ),
            
            'location': forms.TextInput(
    attrs={
        'class': 'form-control',
        'placeholder': 'Enter Location (e.g. Madurai)'
    }
),

            'description': forms.Textarea(

                attrs={

                    'class': 'form-control',

                    'rows': 5,

                    'placeholder': 'Event Description'

                }

            ),

            'venue': forms.TextInput(

                attrs={

                    'class': 'form-control',

                    'placeholder': 'Venue'

                }

            ),

            'date': forms.DateInput(

                attrs={

                    'class': 'form-control',

                    'type': 'date'

                }

            ),

            'time': forms.TimeInput(

                attrs={

                    'class': 'form-control',

                    'type': 'time'

                }

            ),

            'total_tickets': forms.NumberInput(

                attrs={

                    'class': 'form-control',

                    'placeholder': 'Total Tickets'

                }

            ),

            'available_tickets': forms.NumberInput(

                attrs={

                    'class': 'form-control',

                    'placeholder': 'Available Tickets'

                }

            ),

            'image': forms.ClearableFileInput(

                attrs={

                    'class': 'form-control'

                }

            )

        }

    def clean(self):

        cleaned_data = super().clean()

        total = cleaned_data.get(

            'total_tickets'

        )

        available = cleaned_data.get(

            'available_tickets'

        )

        if total and available:

            if available > total:

                raise forms.ValidationError(

                    "Available tickets cannot be greater than total tickets."

                )

        return cleaned_data


# =====================================
# BOOKING FORM
# =====================================

class BookingForm(forms.ModelForm):

    quantity = forms.IntegerField(

        min_value=1,

        widget=forms.NumberInput(

            attrs={

                'class': 'form-control',

                'placeholder': 'Number of Tickets'

            }

        )

    )

    class Meta:

        model = Booking

        fields = [

            'quantity'

        ]

    def clean_quantity(self):

        quantity = self.cleaned_data[

            'quantity'

        ]

        if quantity <= 0:

            raise forms.ValidationError(

                "Quantity must be greater than 0"

            )

        return quantity

