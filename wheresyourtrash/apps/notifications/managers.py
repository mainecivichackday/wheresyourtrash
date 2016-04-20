from django.db import models

class TrashManager(models.Manager):
    """
    Trash Manager for Trash model
    """
    def __init__(self):
        super(TrashManager, self).__init__()

    def get_queryset(self):
        return super(TrashManager, self).get_queryset().filter(trashed=False)
