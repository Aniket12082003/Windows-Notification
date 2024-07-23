from winotify import Notification, audio

site = "https://www.youtube.com/"

toast = Notification(app_id="HP Notification", title="YouTube", msg="Error loading YouTube", duration="short", icon="E:\Projects\Python Projects\Windows Notification\icon.png")

toast.add_actions(label="Click Me", launch=site)

toast.set_audio(audio.SMS, loop=False)

toast.show()