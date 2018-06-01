from django.db import models


# The metadata sent with a list of raw dimensions
class RawMetaData(models.Model):
    # TODO: The following two fields should only be certain values, make new fieldtypes
    type = models.CharField(max_length=128)
    origin = models.CharField(max_length=128)


# An element of the list of the poly-vector/weight pairs submitted by a user
class RawDimensionDatum(models.Model):
    meta = models.ForeignKey(RawMetaData, on_delete=models.CASCADE)
    weight = models.FloatField()
    dimension = models.CharField(max_length=1024)

