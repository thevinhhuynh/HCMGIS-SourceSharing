#Copyright (C) 2020, thevinhhuynh
from django.shortcuts import render_to_response


def main(request):
    return render_to_response("online_counter.html", locals())