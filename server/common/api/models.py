from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class User(models.Model):
	userEmail = models.CharField(max_length = 40, primary_key = True)
	userName = models.CharField(max_length = 40)
	accountType = models.CharField(max_length = 40, default = "FACEBOOK")
	isLecturer = models.BooleanField(default = False)

class Class(models.Model):
	classID = models.IntegerField(primary_key = True)
	className = models.CharField(max_length = 40)
	minGuestCount = models.IntegerField(default = 4)
	maxGuestCount = models.IntegerField(default = 8)
	price = models.FloatField()
	classRating = models.FloatField(default = 0.0,
					validators = [MaxValueValidator(5.0),
					MinValueValidator(0.0)])
	RatingCount = models.IntegerField(default=0)
	expertEmail = models.ForeignKey(User, on_delete = models.CASCADE)

class TimeTable(models.Model):
	timeTableIdx = models.AutoField(primary_key = True)
	date = models.DateField(auto_now = False)
	startTime = models.IntegerField()
	endTime = models.IntegerField()
	timezone = models.CharField(max_length = 40, 
								default = "America/Los_Angeles")
	classID = models.ForeignKey(Class, on_delete = models.CASCADE)
	isBooked = models.BooleanField(default = False)

class Reservation(models.Model):
	reservationID = models.AutoField(primary_key = True)
	guestCount = models.IntegerField()
	userEmail = models.ForeignKey(User, on_delete = models.CASCADE)
	timeTableIdx = models.ForeignKey(TimeTable, on_delete = models.CASCADE)

class Image(models.Model):
	imageIdx = models.AutoField(primary_key = True)
	coverImage = models.ImageField(blank = True, null = True)

	CLASSIMAGE = 1
	PLACEIMAGE = 2
	IMAGE_CHOICES = (
		(CLASSIMAGE, 'classImage'),
		(PLACEIMAGE, 'placeImage'),
	)

	ImageType = models.IntegerField(default=1, choices=IMAGE_CHOICES)
	classID = models.ForeignKey(Class, on_delete = models.CASCADE)
