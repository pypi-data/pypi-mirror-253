from http import HTTPMethod

from http_api_lambda import App, Router

# @app.get("/")
# def a():
#     pass

# equals

# def a():
#     pass
# app.get("/")(a)

# apply decorator in this way, so that we can compare the un-decorated functions in the lookup test


## Tests
def test_lookup_handler():
    app = App()
    def a():
        pass
    app.get("/")(a)

    def b():
        pass
    app.post("/")(b)
    
    assert app._lookup_handler("/", HTTPMethod.GET).handler_fn == a
    assert app._lookup_handler("/", HTTPMethod.POST).handler_fn == b
    

def test_lookup_handler_with_path_param():
    app = App()
    def a():
        pass
    app.put("/{id}")(a)
    
    assert app._lookup_handler("/1", HTTPMethod.PUT).handler_fn == a


def test_handler_lookup_with_routers():
    app = App()
    router1 = Router(route_prefix="/a")
    def a():
        pass
    router1.get("/b")(a)

    router2 = Router(route_prefix="/c")
    def b():
        pass
    router2.post("/d")(b)

    app.include_router(router1)
    app.include_router(router2)

    assert app._lookup_handler("/a/b", HTTPMethod.GET).handler_fn == a
    assert app._lookup_handler("/c/d", HTTPMethod.POST).handler_fn == b