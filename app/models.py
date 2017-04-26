# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class File(models.Model):
    name = models.CharField(max_length=32)
    created = models.DateTimeField('date published')