import flet as ft

def main(page: ft.Page):
    def speed_up(_):
        audio1.speed += 0.25
        audio1.update()

    def slow_down(_):
        audio1.speed -= 0.25
        audio1.update()

    audio1 = ft.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
        autoplay=True
    )
    page.overlay.append(audio1)

    page.add(
        ft.ElevatedButton("Speed Up", on_click=speed_up),
        ft.ElevatedButton("Slow Down", on_click=slow_down),
        ft.Text("Adjust the playback speed of the audio.")
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    def toggle_loop(_):
        audio1.loop = not audio1.loop
        audio1.update()
        btn_loop.text = "Disable Loop" if audio1.loop else "Enable Loop"
        btn_loop.update()

    def toggle_mute(_):
        audio1.muted = not audio1.muted
        audio1.update()
        btn_mute.text = "Unmute" if audio1.muted else "Mute"
        btn_mute.update()

    audio1 = ft.Audio(
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
        autoplay=True,
        loop=False,
        muted=False
    )
    page.overlay.append(audio1)

    btn_loop = ft.ElevatedButton("Enable Loop", on_click=toggle_loop)
    btn_mute = ft.ElevatedButton("Mute", on_click=toggle_mute)
    page.add(
        ft.Text("Control Loop and Mute"),
        btn_loop,
        btn_mute
    )

ft.app(main)

import flet as ft

def main(page: ft.Page):
    playlist = [
        "https://luan.xyz/files/audio/ambient_c_motion.mp3",
        "https://github.com/mdn/webaudio-examples/blob/main/audio-analyser/viper.mp3?raw=true",
        "https://file-examples.com/storage/fe921de743f1bba659c0e/2017/11/file_example_MP3_1MG.mp3"
    ]
    current_track = 0

    def play_next(_):
        nonlocal current_track
        current_track = (current_track + 1) % len(playlist)
        audio1.src = playlist[current_track]
        audio1.play()

    def play_previous(_):
        nonlocal current_track
        current_track = (current_track - 1) % len(playlist)
        audio1.src = playlist[current_track]
        audio1.play()

    audio1 = ft.Audio(
        src=playlist[current_track],
        autoplay=False
    )
    page.overlay.append(audio1)

    page.add(
        ft.ElevatedButton("Play Previous", on_click=play_previous),
        ft.ElevatedButton("Play Next", on_click=play_next),
        ft.Text("Use the buttons to navigate through the playlist.")
    )

ft.app(main)
