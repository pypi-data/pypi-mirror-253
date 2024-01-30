[![pipeline status](https://gitlab.com/applipy/applipy_http/badges/master/pipeline.svg)](https://gitlab.com/applipy/applipy_http/-/pipelines?scope=branches&ref=master)
[![coverage report](https://gitlab.com/applipy/applipy_http/badges/master/coverage.svg)](https://gitlab.com/applipy/applipy_http/-/graphs/master/charts)
[![PyPI Status](https://img.shields.io/pypi/status/applipy-http.svg)](https://pypi.org/project/applipy-http/)
[![PyPI Version](https://img.shields.io/pypi/v/applipy-http.svg)](https://pypi.org/project/applipy-http/)
[![PyPI Python](https://img.shields.io/pypi/pyversions/applipy-http.svg)](https://pypi.org/project/applipy-http/)
[![PyPI License](https://img.shields.io/pypi/l/applipy-http.svg)](https://pypi.org/project/applipy-http/)
[![PyPI Format](https://img.shields.io/pypi/format/applipy-http.svg)](https://pypi.org/project/applipy-http/)

# Applipy HTTP

    pip install applipy_http

Applipy HTTP is a library that implements an AppHandle that starts a HTTP
server, using [`aiohttp`](https://docs.aiohttp.org/en/stable/).

## Basic Usage

Applipy HTTP is designed to be used by declaring the HTTP servers in the
application configuration file and registering APIs to those servers.

First, lets declare a couple of HTTP servers, one anonymous and one with name
`demo`:

```yaml
# dev.yaml

app:
  name: http-demo
  modules:
    - applipy_http.HttpModule

http.servers:
- host: 0.0.0.0
  port: 8080

- name: demo
  host: 0.0.0.0
  port: 8081
```

Running applipy with the configuration above will result in an application that
exposes two HTTP servers: one at `0.0.0.0:8080` and the other at `0.0.0.0:8081`.

We can now register APIs to those servers and endpoints to the APIs. We do that
by implementing them and binding them in modules.

# Example

First, lets declare an API that has an endpoint `/hello` that returns
`Hello World!` on `GET` and register that API to the anonymous HTTP server:

```python
# hello.py

from aiohttp import web
from applipy import Module
from applipy_http import Api, Context, Endpoint, HttpModule, PathFormatter
from applipy_inject import with_names


# Endpoint implementation
class HelloEndpoint(Endpoint):

    def __init__(self):
        self.name = 'World'

    # handler for HTTP method GET
    async def get(self, request: web.Request, context: Context) -> web.StreamResponse:
        return web.Response(body=f'Hello {self.name}!')

    # handler for HTTP method POST
    async def post(self, request: web.Request, context: Context) -> web.StreamResponse:
        self.name = await request.text()
        return web.Response(body='Success')

    # path of the endpoint
    def path(self) -> str:
        return '/hello'


class HelloModule(Module):

    def configure(self, bind, register):
        bind(Endpoint, HelloEndpoint, name='hello')
        # If no instance of PathFormatter (i.e. PrefixPathFormatter) is bound,
        # the API will fallback to using a PathFormatter instance
        # bind(PathFormatter, PrefixPathFormatter('v1'), name='hello')

        # here we register the API to the anonymous HTTP server
        # (name argument in bind() is not set)
        bind(with_names(Api, 'hello'))

    @classmethod
    def depends_on(cls):
        return HttpModule,
```

Next, lets declare a second API with an endpoint `/bye` that returns `Good
Bye!` on `GET` and register it to the `demo` HTTP server:

```python
# goodbye.py

from aiohttp import web
from applipy import Module
from applipy_http import Api, Context, Endpoint, HttpModule, PathFormatter
from applipy_inject import with_names


class GoodByeEndpoint(Endpoint):

    async def get(self, request: web.Request, context: Context) -> web.StreamResponse:
        return web.Response(body="Good Bye!")

    def path(self) -> str:
        return '/bye'


class GoodByeModule(Module):

    def configure(self, bind, register):
        bind(Endpoint, GoodByeEndpoint, name='bye')
        bind(PathFormatter, name='bye')

        # here we register the API to the `demo` HTTP server
        # (name argument in bind() is set to `demo`)
        bind(with_names(Api, 'bye'), name='demo')

    @classmethod
    def depends_on(cls):
        return HttpModule,
```

Finally, lets update the configuration file to include our modules:

```yaml
# dev.yaml

app:
  name: http-demo
  modules:
  - hello.HelloModule
  - goodbye.GoodByeModule

logging.level: INFO

http.servers:
- host: 0.0.0.0
  port: 8080
- name: demo
  host: 0.0.0.0
  port: 8081
```

To test it just install `applipy_http` (and `pyyaml`, because the config is in
YAML and not in JSON) and run the application:

```bash
pip install applipy_http pyyaml
applipy
```

The implemented endpoints should be available in:
 - [http://0.0.0.0:8080/hello](http://0.0.0.0:8080/hello)
 - [http://0.0.0.0:8081/bye](http://0.0.0.0:8081/bye)

## Advanced Features

Check the docs at
[`/docs`](https://gitlab.com/applipy/applipy_http/-/blob/master/docs/README.md)
for explanations on the advanced functionalities.
