import justpy as jp
from about import About
from home import Home
from dictionary import Dictionary


jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.justpy(port=8001)
