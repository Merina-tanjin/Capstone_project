from django.db import models

# Create your models here.
STATE_CHOICE = (
 ('AL', 'Alabama'), 
 ('AK', 'Alaska'), 
 ('AS', 'American Samoa'),
 ('AZ', 'Arizona'), 
 ('AR', 'Arkansas'), 
 ('AA', 'Armed Forces Americas'), 
 ('AE', 'Armed Forces Europe'), 
 ('AP', 'Armed Forces Pacific'), 
 ('CA', 'California'), 
 ('CO', 'Colorado'), 
 ('CT', 'Connecticut'), 
 ('DE', 'Delaware'), 
 ('DC', 'District of Columbia'), 
 ('FL', 'Florida'), ('GA', 'Georgia'), 
 ('GU', 'Guam'), 
 ('HI', 'Hawaii'), 
 ('ID', 'Idaho'), 
 ('IL', 'Illinois'), 
 ('IN', 'Indiana'), 
 ('IA', 'Iowa'), 
 ('KS', 'Kansas'), 
 ('KY', 'Kentucky'), 
 ('LA', 'Louisiana'), 
 ('ME', 'Maine'), 
 ('MD', 'Maryland'), 
 ('MA', 'Massachusetts'), 
 ('MI', 'Michigan'), 
 ('MN', 'Minnesota'), 
 ('MS', 'Mississippi'), 
 ('MO', 'Missouri'), 
 ('MT', 'Montana'), 
 ('NE', 'Nebraska'), 
 ('NV', 'Nevada'), 
 ('NH', 'New Hampshire'), 
 ('NJ', 'New Jersey'), 
 ('NM', 'New Mexico'), 
 ('NY', 'New York'), 
 ('NC', 'North Carolina'), 
 ('ND', 'North Dakota'), 
 ('MP', 'Northern Mariana Islands'), 
 ('OH', 'Ohio'), 
 ('OK', 'Oklahoma'), 
 ('OR', 'Oregon'), 
 ('PA', 'Pennsylvania'), 
 ('PR', 'Puerto Rico'), 
 ('RI', 'Rhode Island'), 
 ('SC', 'South Carolina'), 
 ('SD', 'South Dakota'), 
 ('TN', 'Tennessee'), 
 ('TX', 'Texas'), 
 ('UT', 'Utah'), 
 ('VT', 'Vermont'), 
 ('VI', 'Virgin Islands'), 
 ('VA', 'Virginia'), 
 ('WA', 'Washington'), 
 ('WV', 'West Virginia'), 
 ('WI', 'Wisconsin'), 
 ('WY', 'Wyoming')
 
)

class Resume(models.Model):
 name = models.CharField(max_length=100)
 dob = models.DateField(auto_now=False, auto_now_add=False)
 gender = models.CharField(max_length=100)
 locality = models.CharField(max_length=100)
 city = models.CharField(max_length=100)
 pin = models.PositiveIntegerField()
 state = models.CharField(choices=STATE_CHOICE, max_length=50)
 mobile = models.PositiveIntegerField()
 email = models.EmailField()
 job_city = models.CharField(max_length=50)
 profile_image = models.ImageField(upload_to='resume/profileimg', blank=True)
 my_file = models.FileField(upload_to='resume/doc', blank=True)
 blog = models.CharField(max_length=50)