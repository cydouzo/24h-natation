from django.db import models

class Binet(models.Model):
	name = models.CharField(max_length=64)
	distance = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.name

class Section(models.Model):
	id = models.CharField(max_length=64,primary_key=True)
	name = models.CharField(max_length=64)
	distance = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.name

class Activity(models.Model):
	id = models.CharField(max_length=16,primary_key=True,unique=True)
	name = models.CharField(max_length=64)
	register = models.BooleanField(default=False)
	single = models.BooleanField(default=True)
	info = models.CharField(max_length=32)

	def __str__(self):
		return self.name

	def fancyid(self):
		return "activity-"+str(self.id)

from .user import User

class Nage(models.Model):
	nageur = models.ForeignKey(User,blank=True,null=True)
	pour = models.ManyToManyField(Binet,blank=True)
	backandforth = models.IntegerField("Aller-Retour",blank=True,null=True)
	remarque = models.CharField(max_length=256,blank=True)

	def distance(self):
		try :
			return int(self.backandforth)*50
		except:
			return 0
		return 0

	def __str__(self):
		return str(self.nageur)+" "+str(self.distance())+"m"+" ("+", ".join(str(binet) for binet in self.pour.all())+")" + " # "+str(self.remarque)

class Equipe(models.Model):
	nom = models.CharField(max_length=64)
	activite = models.ForeignKey(Activity)
	capitaine = models.ForeignKey(User, related_name = "capitaine")
	membres = models.ManyToManyField(User)

	def __str__(self):
		return "["+str(activite)+"] "+nom