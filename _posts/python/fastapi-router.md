---
title: FastAPI Router for Path Operations
date: August 9, 2025
tags: python
---

The `APIRouter` class in FastAPI is used to group path operations for an app. This allows paths to be defined in multiple files which is useful for large applications. The example below defines fruits and veggies paths for the router.

```python
# routes.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/fruits")
async def get_fruits():
    return {"fruits": ["apples", "oranges", "lemons"]}


@router.get("/veggies")
async def get_veggies():
    return {"veggies": ["beans", "peas", "celery"]}
```

In the main app module shown below, the router is imported and included with the app instance. Notice a path is also defined in this file too thus paths are not all defined in the same file.

```python
# app.py

from fastapi import FastAPI
from routes import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def home():
    return {"message": "hello there"}
```

In summary, the paths for this application are `/`, `/fruits`, and `/veggies` which are defined in the `app.py` and `routes.py` files.

## Further reading

See the [APIRouter](https://fastapi.tiangolo.com/reference/apirouter/) documentation for more details about the router class. Also see the [FastAPI](https://fastapi.tiangolo.com/tutorial/bigger-applications/) tutorial about using a routers subpackage for bigger applications.
