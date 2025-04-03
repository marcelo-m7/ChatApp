import flet as ftimport timeimport asynciodef main(page: ft.Page):    def handler(e):      time.sleep(3)      page.add(ft.Text("Handler clicked"))    async def handler_async(e):      await asyncio.sleep(3)      page.add(ft.Text("Async handler clicked"))    page.add(        ft.ElevatedButton("Call handler", on_click=handler),        ft.ElevatedButton("Call async handler", on_click=handler_async)    )ft.app(main)

import flet as ftdef main(page: ft.Page):    page.add(ft.Text("Hello ASGI!"))app = ft.app(main, export_asgi_app=True)

import flet as ftdef main(page: ft.Page):    page.add(ft.Image(src=f"/images/my-image.png"))ft.app(main, assets_dir="assets")

import flet as ftimport flet.fastapi as flet_fastapiasync def root_main(page: ft.Page):    await page.add_async(ft.Text("This is root app!"))async def sub_main(page: ft.Page):    await page.add_async(ft.Text("This is sub app!"))app = flet_fastapi.FastAPI()app.mount("/sub-app", flet_fastapi.app(sub_main))app.mount("/", flet_fastapi.app(root_main))

from contextlib import asynccontextmanagerimport flet as ftimport flet.fastapi as flet_fastapifrom fastapi import FastAPI@asynccontextmanagerasync def lifespan(app: FastAPI):    await flet_fastapi.app_manager.start()    yield    await flet_fastapi.app_manager.shutdown()app = FastAPI(lifespan=lifespan)async def main(page: ft.Page):    await page.add_async(ft.Text("Hello, Flet!"))app.mount("/flet-app", flet_fastapi.app(main))

from flet.fastapi import FastAPI, FletStaticFilesapp = FastAPI()# mount to the root of web appapp.mount(path="/", app=FletStaticFiles())

from flet.fastapi import FletAppasync def main(page: ft.Page):    await page.add_async(ft.Text("Hello, Flet!"))@app.websocket("/app1/ws")async def flet_app(websocket: WebSocket):    await FletApp(main).handle(websocket)

from flet.fastapi import FletUpload@app.put("/upload")async def flet_uploads(request: Request):    await FletUpload("/Users/feodor/Downloads/123").handle(request)

from flet.fastapi import FletOAuth@app.get("/oauth_callback")async def flet_oauth(request: Request):    return await FletOAuth().handle(request)

