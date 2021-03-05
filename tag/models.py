from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32,
                            verbose_name='Tag Name')

    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Registered Date/Time')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'byun_project_tags'
        verbose_name = 'byun_project_tag'
