from django.db import models

# Create your models here.
class Fundraiser(models.Model): #U would always need to reference Model here whenever you create another class)
    title = models.CharField(max_length=200) #This is a class attribute and this will become our column and become our database table)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) #The auto_now_add will take the date and time and add to the database)

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser', #Tell u which class it refers to
        on_delete=models.CASCADE, #in case a fundraiser is deleted the pledges linked to that fundraiser will auto be deleted, otherwise it will be bad data if the database just have pledges without frundraisers)
        related_name='pledges'
    )
