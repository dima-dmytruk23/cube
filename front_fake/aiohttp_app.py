import aiohttp_jinja2
import jinja2
from aiohttp import web


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader("templates"))
app["static_root_url"] = "static"


@aiohttp_jinja2.template("video.html")
async def handler(request):
    return {}


app.router.add_get("/", handler)
app.router.add_static("/static/", path=str("./static/"))

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=9999)
