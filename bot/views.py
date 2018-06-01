from django.shortcuts import render
from .models import RawMetaData, RawDimensionDatum


# Receives from the webhook
def update(request):
    # Get a list of messages
    if request.method == "POST":
        msgs = request.body

    # Parse each message, get the response and then add datum to database


# Takes a polyvector, compares it to eigenideologies, returns info to the user
def makeResponse(v):
    # Compare vector v to ideologies, get different metrics
    cosd = v # TODO: Get the cosine difference for each ideology
    euclid = v # TODO: Get the euclidean distance (2-norm)

    pass


if __name__ == "__main__":
    main()