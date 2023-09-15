from django.db import models

class AvailableFunction(models.Model):
    module_name = models.CharField(max_length=255)
    function_name = models.CharField(max_length=255)
    description = models.TextField()
    source_code = models.TextField()
    docstring = models.TextField()

    def __str__(self):
        return f"{self.module_name} | {self.function_name} | {self.description}"