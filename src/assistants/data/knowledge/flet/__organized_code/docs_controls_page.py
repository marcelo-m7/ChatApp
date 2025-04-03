page.controls.append(ft.Text("Hello!"))page.update()

page.controls.pop()page.update()

page.padding = 0page.update()

def main(page: ft.Page):    if page.platform == ft.PagePlatform.MACOS:        page.add(ft.CupertinoDialogAction("Cupertino Button"))    else:        page.add(ft.TextButton("Material Button"))

import flet as ftdef main(page):    def set_android(e):        page.platform = ft.PagePlatform.ANDROID        page.update()        print("New platform:", page.platform)    def set_ios(e):        page.platform = "ios"        page.update()        print("New platform:", page.platform)    page.add(        ft.Switch(label="Switch A", adaptive=True),        ft.ElevatedButton("Set Android", on_click=set_android),        ft.ElevatedButton("Set iOS", on_click=set_ios),    )    print("Default platform:", page.platform)ft.app(main)

def main(page: ft.Page):    def on_broadcast_message(message):        print(message)    page.pubsub.subscribe(on_broadcast_message)

def main(page: ft.Page):    def on_message(topic, message):        print(topic, message)    page.pubsub.subscribe_topic("general", on_message)

@dataclassclass Message:    user: str    text: strdef main(page: ft.Page):    def on_broadcast_message(message):        page.add(ft.Text(f"{message.user}: {message.text}"))    page.pubsub.subscribe(on_broadcast_message)    def on_send_click(e):        page.pubsub.send_all(Message("John", "Hello, all!"))    page.add(ft.ElevatedButton(text="Send message", on_click=on_send_click))

@dataclassclass Message:    user: str    text: strdef main(page: ft.Page):    def on_leave_click(e):        page.pubsub.unsubscribe()    page.add(ft.ElevatedButton(text="Leave chat", on_click=on_leave_click))

def main(page: ft.Page):    def client_exited(e):        page.pubsub.unsubscribe_all()    page.on_close = client_exited

page.title = "My awesome app"page.update()

page.add(ft.Text("Hello!"), ft.FilledButton("Button"))

import flet as ftdef main(page: ft.Page):    x = ft.IconButton(ft.Icons.ADD)    page.add(x)    print(type(page.get_control(x.uid)))ft.app(main)

upload_url = page.get_upload_url("dir/filename.ext", 60)

ft.app(main, upload_dir="uploads")

page.set_clipboard("This value comes from Flet app")

def page_resized(e):    print("New page size:", page.window.width, page.window_height)page.on_resized = page_resized

import flet as ftdef main(page: ft.Page):    hello = ft.Text("Hello, World!")    page.add(hello)    print(hello in page)  # True        ft.app(main)

