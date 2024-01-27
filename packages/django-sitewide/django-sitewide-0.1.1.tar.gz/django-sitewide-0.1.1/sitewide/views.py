from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Setting
import tomllib


class Footer:
    """Sitewide Footer"""

    def __init__(self, sitewide, **kwargs):
        """Initialize"""
        
        self.__footer = {}
        if isinstance(sitewide, Sitewide):
            self.__footer.setdefault("sitewide", sitewide)
        else:
            raise TypeError(f"Expected Sitewide Object. Got {type(sitewide)}")
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)


class Items:
    """Manage items of specified class"""

    def __init__(self, item_class):
        """initialize"""

        self.__items = {
            "class": item_class,
            "items": {},
        }

    def add(self, items):
        """Add a new item using the passed list"""

        for item in items:
            index = len(self.items) + 1
            try:
                obj = self.item_class(**item)
                if hasattr(obj, "index"):
                    # object should remember its new index too
                    obj.index = index
                self.items[index] = obj
            except AttributeError:
                pass

    @property
    def items(self):
        """return dictionary of items"""

        return self.__items.get("items")

    @property
    def item_class(self):
        """return the class of the items"""

        return self.__items.get("class")

    def list(self):
        """Override list to list items"""

        return list(self.items.values())


class MenuItem(Items):
    """A Single Sidebar Menu Entry"""

    def __init__(self, **itemdict):
        """Initialize"""

        self.__item = {}
        super().__init__(MenuItem)
        for key, value in itemdict.items():
            if key.lower() == "menu":
                self.add(value)
                continue
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def icon(self):
        """return icon of menu item"""

        return self.__item.get("icon")

    @icon.setter
    def icon(self, code):
        """set the icon of the menu item"""

        if isinstance(code, str):
            self.__item["icon"] = code

    @property
    def index(self):
        """return the index number of menu item"""

        return self.__item.get("index")

    @index.setter
    def index(self, index):
        """set the icon of the menu item"""

        if isinstance(index, int):
            self.__item["index"] = index

    @property
    def name(self):
        """return name of menu item"""

        return self.__item.get("name")

    @name.setter
    def name(self, name):
        """set the name/id of the menu item"""

        if isinstance(name, str):
            self.__item["name"] = name

    @property
    def text(self):
        """return name of menu item"""

        return self.__item.get("text")

    @text.setter
    def text(self, the_text):
        """set the text in the menu"""

        if isinstance(the_text, str):
            self.__item["text"] = the_text

    @property
    def url(self):
        """return url of menu item"""

        return self.__item.get("url")

    @url.setter
    def url(self, url):
        """set the url of the menu item"""

        if isinstance(url, str):
            self.__item["url"] = url


class Sidebar:
    """Manage Sidebar data"""

    def __init__(self, sitewide, **kwargs):
        """Initialize"""

        self.__bar = {}
        if isinstance(sitewide, Sitewide):
            self.__bar.setdefault("sitewide", sitewide)
        else:
            raise TypeError(f"Expected Sitewide Object. Got {type(sitewide)}")
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @property
    def allow(self):
        """return rank of users allowed to view sidebar"""

        return self.__bar.get("allow")

    @allow.setter
    def allow(self, userank):
        """Set the rank of users that can view Sidebar"""

        if isinstance(userank, str):
            self.__bar["allow"] = userank

    @property
    def avatar(self):
        """Link to the avatar"""

        host = self.__bar.get("sitewide")
        return (
            host.user.avatar
            if hasattr(host.user, "avatar")
            else "/static/imgs/avatar.png"
        )

    @property
    def menu(self):
        """Return menu"""

        return self.__bar.get("menu")

    @menu.setter
    def menu(self, item):
        """Set menu"""

        if isinstance(item, list):
            menu = Items(MenuItem)
            menu.add(item)
            self.__bar["menu"] = menu

    @property
    def show(self):
        """Return True if Sidebar should be visible"""

        host = self.__bar.get("sitewide")
        return (
            getattr(host.user, self.allow)
            if hasattr(host.user, self.allow)
            else False
        )


class Sitewide:
    """Manage information that shows across most pages in a Django website"""

    def __init__(self, **kwargs):
        """Initialize"""

        cfg = {}
        with open('sitewide.toml', 'rb') as file:
            cfg = tomllib.load(file)
        self.__sitewide = {
            "setting_class": Setting
        }
        for src in [kwargs, cfg]:
            for attr in src:
                if hasattr(self, attr):
                    setattr(self, attr, src.get(attr))

    @property
    def favicon(self):
        """Return sitebar object"""

        return self.__sitewide.get("favicon")

    @favicon.setter
    def favicon(self, path):
        """Set the path to the favicon"""

        if isinstance(path, str):
            self.__sitewide["favicon"] = path

    @property
    def footer(self):
        """Return footer object"""

        return self.__sitewide.get("footer")

    @footer.setter
    def footer(self, kwargs):
        """Set the contents of sitewide footers"""

        footer = Footer(self, **kwargs)
        self.__sitewide["footer"] = footer

    @property
    def settings(self):
        """Return a queryset of settings"""

        return self.settings_class.objects.all()

    @property
    def settings_class(self):
        """Return the Settings Model Class"""

        return self.__sitewide.get("setting_class")

    @property
    def sidebar(self):
        """Return sitebar object"""

        return self.__sitewide.get("sidebar")

    @sidebar.setter
    def sidebar(self, kwargs):
        """Set the sitebar object"""

        sidebar = Sidebar(self, **kwargs)
        self.__sitewide["sidebar"] = sidebar

    @property
    def sitename(self):
        """Return the name of the project"""

        return self.__sitewide.get("sitename")

    @sitename.setter
    def sitename(self, name):
        """Set the project name"""

        if isinstance(name, str):
            self.__sitewide["sitename"] = name

    @property
    def user(self):
        """Return request user"""

        return self.__sitewide.get("user")

    @user.setter
    def user(self, user):
        """Set the request user object"""

        if hasattr(user, "username"):
            self.__sitewide["user"] = user


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = {"pagetitle": "Home"}

    def get(self, request, *args, **kwargs):
        """Prepare to render view"""

        # Set sitewide request.user
        sitewide = Sitewide(user=self.request.user)
        self.extra_context["sitewide"] = sitewide
        return super().get(request, *args, **kwargs)
