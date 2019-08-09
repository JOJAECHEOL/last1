from django.db import models

class Member(models.Model):
    title = models.CharField(max_length=200)
    pw = models.CharField(max_length=200)
    LEVEL=(
        ('n', 'Newbie Hacker'),
        ('j', 'Junior Hacker'),
        ('s', 'Senior Hacker'),
        ('p', 'Professional Hacker'),
        ('w', 'World Class Hacker'),
    )
    level=models.CharField(
        max_length=1,
        choices=LEVEL,
        blank=True,
        default='n',
        help_text='Class Level',
    )
    
    jjim = models.TextField()
    choose = models.CharField(max_length=200)


    def __str__(self):
        return self.title
       
