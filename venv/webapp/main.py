import justpy as jp
from about import About
from home import Home


jp.Route(About.path, About.serve)
jp.Route(Home.path, Home.serve)
jp.justpy(port=8001)
