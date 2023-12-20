from django.db import models
from django.contrib.auth.models import User as auth_user


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    auth_user = models.OneToOneField(auth_user, on_delete=models.CASCADE, null=True)
    grad_year = models.IntegerField(default=9999)
    is_port = models.BooleanField(default=False)
    is_starboard = models.BooleanField(default=False)
    is_rookie = models.BooleanField(default=True)
    total_minutes = models.IntegerField(default=0)
    total_absences = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} ({self.email})'

class Absence(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField(blank=True)
    reason = models.CharField(max_length=200)

class Extra_Workout(models.Model):
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='extra_workouts')
    date = models.DateField(blank=True)
    minutes = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

class Shell(models.Model):
    name = models.CharField(max_length=50)
    is_coxed = models.BooleanField(default=True)
    n_rowers = models.IntegerField(default=8)
    is_port_stroke = models.BooleanField(default=True)
    is_scull = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.n_rowers}{"+" if self.is_coxed else "x" if self.is_scull else "-"} {"PORT" if self.is_port_stroke else "STBD"})'

class Lineup(models.Model):
    shell = models.ForeignKey(Shell, on_delete=models.CASCADE, related_name='lineups')
    oars = models.CharField(max_length=50)
    coxswain = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='boats_coxed', null=True)
    rowers = models.ManyToManyField(User, blank=True, related_name='boats_rowed')
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='boats_coached', null=True)
    launch = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='boats_launched', null=True)
    is_port_stroke = models.BooleanField(default=True)
    date = models.DateField(blank=True)
    workout = models.CharField(max_length=300, default='')
