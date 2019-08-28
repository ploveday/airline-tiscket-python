from django import forms
from . import models as mpius
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

class RegForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)
    # username = forms.CharField(help_text='Must be Unique', label='User Name')
    # country = forms.ChoiceField(choices=['','--Select Country--'])
    # state = forms.ChoiceField(choices=['','State'])
    # password1 = forms.CharField(help_text='8 characters long, Uncommon, Not entirely numeric distinct from other data')
    # password2 = forms.CharField(help_text='Same password as before')
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]
# class RegForm(forms.Form):
#     email = forms.EmailField()
class DetailsForm(forms.ModelForm):
    class Meta:
        # gender = models.CharField(
        # max_length=1, choices=(('m', _('Male')), ('f', _('Female'))),
        # blank=True, null=True)
        model = mpius.Usersdetails
        fields = [
            'phone',
            'gender'
        ]
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'

class CreateTicketForm(forms.ModelForm):
    ticketName = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control'
    }), choices=([
        ('','--Select A Flight--'),
        ('pius-fly-1502','pius-fly-1502'),
        ('pius-fly-1302','pius-fly-1302'),
        ('pius-fly-1182','pius-fly-1182'),
        ('pius-fly-3152','pius-fly-3152'),
        ('pius-fly-3098','pius-fly-3098'),
    ]), required=True, label='Ticket Flight')

    ticketType = forms.ChoiceField(widget=forms.Select(attrs={
        'class':'form-control'
    }), choices=([
        ('','--Select Ticket Class--'),
        ('business','First Class'),
        ('economy','Economy Class'),
        ('promo','Promo Ticket'),
    ]), required=True, label='Class of Ticket')

    # destinationCountry = forms.ChoiceField(label='Arrival Country', choices=[('','')], widget=forms.Select(attrs={'class':'form-control text-danger'}))
    # destinationState = forms.ChoiceField(label='Arrival State', widget=forms.Select(attrs={'class':'form-control text-danger'}))
    # departureCountry = forms.ChoiceField(label='Departure Country', widget=forms.Select(attrs={'class':'form-control text-success'}))
    # departureState = forms.ChoiceField(label='Departure State', widget=forms.Select(attrs={'class':'form-control text-success'}))
    # destinationAirport = forms.CharField(label='Arrival Airport', widget=forms.TextInput(attrs={'class':'form-control text-success'}))
    # departureAirport = forms.CharField(label='Departure Airport', widget=forms.TextInput(attrs={'class':'form-control text-danger'}))
    # status = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial = 1)
    # ticketAuthor = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = mpius.Tickets
        fields = (
            'ticketName',
            'ticketType',
            'amount',
            'quantity',
            'departureDate',
            'arrivalDate',
            # 'destinationCountry',
            # 'destinationState',
            # 'destinationAirport',
            # 'departureCountry',
            # 'departureState',
            # 'departureAirport',
        )