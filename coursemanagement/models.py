from django.db import models
from course.models import Course


class CourseOffer(models.Model):
	"""Only department head can offer a course"""
	def __str__(self):
		return "{}".format(self.dep_head)


class CourseSetting(models.Model):
	add_drop = models.BooleanField(default=False)
