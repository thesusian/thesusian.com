---
date: 2024-10-12
title: FastAPI Jinja2 Translation
tags:
  - tutorial
  - python
math: false
description: How to setup translation for a Python FastAPI project with Jinja2 templates
draft: false
---
This tutorial is somewhat of a followup to [another tutorial](https://medium.com/@amirm.lavasani/how-to-add-i18n-to-your-fastapi-app-b546f7d183bb) that does the same thing, except it doesn't specify how to use it with Jinja templates.

## Setup

This tutorial assumes you already have a FastAPI project and you just want to add translation to it. For the sake of this tutorial I will be making a new minimal project.

First we need to create a virtual environment to install the packages, do this using `python -m venv .venv && source .venv/bin/activate`. Next, make a new `requirements.txt` file in the root of the project and add these packages:

```text
fastapi
jinja2          # templaes
starlette       # sessions stuff
itsdangerous    # required by starlette, I think?
babel           # translation tools
uvicorn         # running the project
```

And run `pip install -r requirements.txt`.

Now that we have our dependencies installed, we can setup our app, our templates, and the translation folders, your project should looks something like this.

```text
.
├── app
│   ├── i18n.py
│   ├── main.py
│   └── middleware.py
├── babel.cfg
├── requirements.txt
├── templates
│   └── home.html
└── translations
```

## i18n

First, let's setup the `app/i18n.py` file. Here we will define our main `TranslationWrapper` class, the `set_locale` function, and the `_` function, which wraps the `gettext` function, for convenience.

```python
import gettext
from pathlib import Path
from fastapi import Request


class TranslationWrapper:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_translation()
        return cls._instance

    def init_translation(self):
        lang = "en"  # Default language
        locales_dir = Path(__file__).parent.parent / "translations"
        self.translations = gettext.translation(
            "messages",
            localedir=locales_dir,
            languages=[lang],
            fallback=True
        )
        self.translations.install()

    def gettext(self, message: str) -> str:
        return self.translations.gettext(message)

async def set_locale(request: Request, lang: str = "en"):
    translation_wrapper = TranslationWrapper()

    locales_dir = Path(__file__).parent.parent / "translations"
    print(f"Setting language to: {lang}")
    translation_wrapper.translations = gettext.translation(
        "messages", localedir=locales_dir, languages=[lang], fallback=True
    )
    translation_wrapper.translations.install()


def _(message: str) -> str:
    translation_wrapper = TranslationWrapper()
    return translation_wrapper.gettext(message)
```

Notice how I do `locales_dir = Path(__file__).parent.parent / "translations"`, using `.parent` twice, this is because my file is inside the `app` directory, if it was in the same folder as the translations folder you would just do `.parent` once.

## The Middleware

Next is setting up our custom middleware that ensures that:

1. The appropriate language is set for each request based on session data or browser preferences.
2. The translation function (`_`) and current language are available in all Jinja2 templates.

Open your `app/middleware.py` file and add the following:

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.templating import Jinja2Templates

from .i18n import set_locale, _


class LanguageMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, templates: Jinja2Templates):
        super().__init__(app)
        self.templates = templates

    async def dispatch(self, request: Request, call_next):
        lang = request.session.get('language') or request.headers.get("Accept-Language", "en")
        await set_locale(request, lang)

        self.templates.env.globals['_'] = _
        self.templates.env.globals['lang'] = lang

        response = await call_next(request)
        return response
```

## The Main File

Obviously this will depend on your project, but here I will provide an example `app/main.py` with a home route and a `set-lang` function to set the language for the session.

```python
from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from starlette.middleware.sessions import SessionMiddleware

from .middleware import LanguageMiddleware
from .i18n import _

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.add_middleware(LanguageMiddleware, templates=templates)
app.add_middleware(SessionMiddleware, secret_key="your-totally-secret-key")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user = request.session.get('user')
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/set-lang/{lang}")
async def set_language(lang: str, request: Request, response: Response):
    supported_langs = ['en', 'ar']
    if lang not in supported_langs:
        raise HTTPException(status_code=400, detail=f"Invalid language. Only {', '.join(supported_langs)} are supported.")
    request.session['language'] = lang
    referer = request.headers.get('Referer')
    response = RedirectResponse(referer or "/")
    return response
```

Make sure you change the `supported_langs` variable.

## Example Template

We setup the middleware in a way that in all template files you have access to two things, the `_` function, in which you will wrap pieces of text you want to translate, and the `lang` variable which will tell you what language is currently set by the user, this will be changeable with our `/set-lang` route.

```html
<!doctype html>
<html>
    <head>
        <title>Test App</title>
    </head>
    <body class="p-0">
        <h1>{{ _("Hello") }}</h1>
        {% if lang == 'ar' %}
        <a href="#" onclick="setLanguage('en')">English</a>
        {% else %}
        <a href="#" onclick="setLanguage('ar')">Arabic</a>
        {% endif %}
    </body>
    <script>
        function setLanguage(lang) {
            fetch("/set-lang/" + lang, {
                method: "POST",
            }).then(() => {
                location.reload();
            });
        }
    </script>
</html>
```

## Translation

Finally, we can translate our app. First, we need to tell babel where to look for things to translate. Open `babel.cfg` and add the following: 

```cfg
[python: **.py, **/**.py]
[jinja2: **/templates/**.html]

keywords = _
```

I don't think this needs explaining.

Now, we will generate our `messages.pot`, which will hold all of our pieces of text that we want to translate, this will look in all html files in the templates folder and find anything wrapped in the `_` function. To generate it we run:

```bash
pybabel extract -F babel.cfg -o translations/messages.pot .
```

Next, we will initialize a translation folder for the languages we want, let's do Arabic for example.

**Warning**: doing this will overwrite any existing translation files for the specified language

```bash
pybabel init -i translations/messages.pot -d translations -l ar
```

You should have a file called `translations/ar/LC_MESSAGES/messages.po`, in this file you will write your translations for the language. For example, here is the translation for the `home.html` page:

```po
# metadata stuff...

#: templates/home.html:7
msgid "Hello"
msgstr "مرحبا"
```

And finally, before running your application you have to compile the `.po` file, as follows:

```bash
pybabel compile -d translations
```

## Enjoy

Everything should be done now, you can run your applications from it's root directory using:

```bash
uvicorn app.main:app --reload --host localhost --port 8000
```

And that should be it, what is suggest you do is making a `run.sh` file that compiles the translations and then runs the app to avoid having to remember doing that every time.

If you found any problem in this please contact me, info in the [about](/about) page.