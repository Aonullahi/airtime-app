import django
django.setup()


from django import forms
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings
from api.models import Product, Order, OrderedItem

############################
## Inline Formset Example ##
############################

class OrderForm(models.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderedItemForm(models.ModelForm):
    class Meta:
        model = OrderedItem
        fields = '__all__'


################################
## Plain 'ole Formset example ##
################################

CONTACT_INFO_TYPES = (
    ('MTN', 'MTN'),
    ('Airtel', 'Airtel'),
    ('Glo', 'Glo'),
    ('Etisalat', 'Etisalat'),

)

class ContactInfoForm(forms.Form):
    username = fields.CharField(max_length=150, label='Intern Name')
    phone_number = fields.CharField(max_length=150, label='Phone Number')
    amount = fields.CharField(max_length=50, label='Amount')
    network = fields.ChoiceField(choices=CONTACT_INFO_TYPES, label='Network Provider')

ContactFormset = formsets.formset_factory(ContactInfoForm)
# Define a formset, which will allow a maximum of 5 contacts, no more:
MaxFiveContactsFormset = formsets.formset_factory(ContactInfoForm, extra=5, max_num=5)
# Define the same formset, with no forms (so we can demo the form template):
EmptyContactFormset = formsets.formset_factory(ContactInfoForm, extra=0)
try:
    # Define the same formset, which will require a minimum of 2 contacts, no extra
    MinTwoContactsFormset = formsets.formset_factory(ContactInfoForm, extra=0, min_num=2)
except:
    pass # django pre 1.7

###############################################
## Plain 'ole Formset with Javascript Widget ##
###############################################
