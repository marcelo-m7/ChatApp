import flet as ftdef main(page: ft.Page):    def pick_files_result(e: ft.FilePickerResultEvent):        selected_files.value = (            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"        )        selected_files.update()    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)    selected_files = ft.Text()    page.overlay.append(pick_files_dialog)    page.add(        ft.Row(            [                ft.ElevatedButton(                    "Pick files",                    icon=ft.Icons.UPLOAD_FILE,                    on_click=lambda _: pick_files_dialog.pick_files(                        allow_multiple=True                    ),                ),                selected_files,            ]        )    )ft.app(main)

from fastapi import FastAPI, Responsefrom fastapi.responses import FileResponseapp = flet_fastapi.app(main)@app.get("/download/{filename}")def download(filename: str):    path = prepare_file(filename)    return FileResponse(path)

ft.ElevatedButton("Download myfile", on_click=lambda _: page.launch_url("/download/myfile.txt"))

upload_url = page.get_upload_url("dir/filename.ext", 60)

ft.app(main, upload_dir="uploads")

