from __future__ import unicode_literals

from django.db import models
from md5 import md5

class Problem(models.Model):
	title = models.CharField(max_length=100)
	problem_content = models.TextField()
	problem_id = models.CharField(max_length=100)

	def save(self):
		super(Problem, self).save()
		self.problem_id = md5(str(self.id)).hexdigest()
		super(Problem, self).save()

	def __str__(self):
		return self.title