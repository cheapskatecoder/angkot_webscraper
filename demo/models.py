from django.db import models


class Routes(models.Model):
    class Meta:
        verbose_name_plural = "Routes"
    origin = models.CharField(max_length=255, null=True, blank=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    routes = models.CharField(max_length=255, null=True, blank=True)
    distance = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "# {} - {} - {}".format(self.id, self.origin, self.destination)
