# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

class IndexView(TemplateView):
   template_name = "fest/index.html"

class ContentView(TemplateView):
   template_name = "fest/content.html"   

class Post1View(TemplateView):
   template_name = "fest/post1.html"

class Post2View(TemplateView):
   template_name = "fest/post2.html"

class YouView(TemplateView):
   template_name = "fest/you.html"