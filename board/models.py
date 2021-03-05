from django.db import models


class Board(models.Model):

    title = models.CharField(max_length=128,
                             verbose_name='Title')

    contents = models.TextField(verbose_name='Contents')

    # ForeignKey: one-to-N relationship
    # eg. one user can write multiple posts
    author = models.ForeignKey('user.User',
                               on_delete=models.CASCADE,
                               verbose_name='Author')

    # ManyToManyField: many-to-many relationship
    tags = models.ManyToManyField('tag.Tag',
                                  verbose_name='Tag')

    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Registered Date/Time')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'byun_project_board'
        verbose_name = 'byun_project_board'
