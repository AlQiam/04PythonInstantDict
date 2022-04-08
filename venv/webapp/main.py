import justpy as jp
from about import About
from home import Home
from dictionary import Dictionary
from dictionary_api import Dictionary as Dict


jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.Route(Dictionary.path, Dictionary.serve)
jp.Route(Dict.path, Dict.serve)
jp.justpy(port=8001)
