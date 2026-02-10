from django.db import models
from django.contrib.auth import get_user_model #We cant directly import custom function so you have to use the help function to find it for you

# Create your models here.
class Fundraiser(models.Model): #U would always need to reference Model here whenever you create another class)
    title = models.CharField(max_length=200) #This is a class attribute and this will become our column and become our database table)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True) #The auto_now_add will take the date and time and add to the database)
    is_approved = models.BooleanField(default=False) #spin
    owner = models.ForeignKey(
        get_user_model(), #Since you can always change the user models so Django has this function so that you dont have to go and change the model in your codes
        on_delete=models.CASCADE, #When the model is deleted all linked will be deleted
        related_name='owned_fundraisers'
    )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200, blank=True) #Blank=True so that comments are optional
    anonymous = models.BooleanField(default=False) #name shown unless user chooses anonymity
    fundraiser = models.ForeignKey(
        'Fundraiser', #Tell u which class it refers to
        on_delete=models.CASCADE, #in case a fundraiser is deleted the pledges linked to that fundraiser will auto be deleted, otherwise it will be bad data if the database just have pledges without frundraisers)
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )
