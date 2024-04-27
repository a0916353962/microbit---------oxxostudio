def on_pin_pressed_p0():
    pass
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def 燈數(num: number, 關燈: bool):
    global x, y
    if num % 5 == 0:
        x = 4
        y = Math.floor(num / 5) - 1
        led.unplot(x, y)
    else:
        x = num % 5 - 1
        y = Math.floor(num / 5)

def on_button_pressed_a():
    global n
    n += 1
    燈數(n, False)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_melody_note_played():
    pass
music.on_event(MusicEvent.MELODY_NOTE_PLAYED, on_melody_note_played)

def on_button_pressed_ab():
    global n
    basic.clear_screen()
    n = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

y = 0
x = 0
n = 0
n = 0
燈數(n, True)
n += -1