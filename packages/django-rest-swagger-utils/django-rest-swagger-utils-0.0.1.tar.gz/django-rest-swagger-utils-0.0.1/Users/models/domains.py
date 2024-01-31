from django.db import models


class Domain(models.Model):
    domain_id = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=63)
    description = models.CharField(max_length=1024, blank=True)
    is_requested = models.BooleanField(default=False)

    def __int__(self):
        return self.domain_name