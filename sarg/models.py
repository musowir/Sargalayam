from django.db import models

# Create your models here.
class Catogory(models.Model):
    catogory_name = models.CharField(max_length=50, unique=True)
    def __str__(self):
      return self.catogory_name
class Cluster(models.Model):
   cluster_name = models.CharField(max_length=50, unique=True)
   def __str__(self):
      return self.cluster_name

class Unit(models.Model):
   unit_name = models.CharField(max_length=50, unique=True)
   cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
   def __str__(self):
      return self.unit_name
   

class Competition(models.Model):
   competition_name =models.CharField(max_length=50, unique=True)
   catogory = models.ForeignKey(Catogory, on_delete=models.CASCADE)
   is_group = models.BooleanField()

   def __str__(self):
      return self.competition_name

class Result(models.Model):
   class Places(models.IntegerChoices):
        FIRST = (1, 'first')
        SECOND = (2, 'second')
        THIRD = (3, 'third')
   competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
   name = models.CharField(max_length=500)
   unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
   position = models.IntegerField(choices=Places.choices)
   def __str__(self):
      return str(self.competition)+" "+str(self.position)