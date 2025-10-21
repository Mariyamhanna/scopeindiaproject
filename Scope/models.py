from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    reg_email = models.EmailField()
    reg_password=models.CharField(max_length=8,default='Not Provided',blank=False)
    mobile = models.CharField(max_length=15)
    course = models.CharField(max_length=100,default='Not Provided',blank=False)
    qualification = models.CharField(max_length=100)
    college = models.CharField(max_length=200)
    year = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, blank=False, default='Not Specified')
    message = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    reg_training_mode = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_training_location = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_preferred_timings = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_guardian_name = models.CharField(max_length=100,default='Not Provided')
    reg_guardian_occupation = models.CharField(max_length=100,default='Not Provided')
    reg_guardians_mobile = models.CharField(max_length=15,default='Not Provided')
    reg_address = models.CharField(max_length=255, default='Not Provided', blank=False)
    reg_country = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_state = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_city = models.CharField(max_length=100,default='Not Provided', blank=False)
    reg_zip = models.CharField(max_length=10,default='Not Provided', blank=False)
    def __str__(self):
        return self.name




