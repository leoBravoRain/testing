# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Templates
indexTemplate = "index/index.html"

# Create your views here.

def index_view(request):

	template = indexTemplate

	context = {}

	return render(request, template, context)