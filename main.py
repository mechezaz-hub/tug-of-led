def on_button_pressed_a():
    global Rope
    Rope += -0.1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Rope
    Rope += 0.1
input.on_button_pressed(Button.B, on_button_pressed_b)

Rope = 9
serial.write_line("A is The Winner And B Is The Loser! HAHAHAHA!")
serial.redirect_to_usb()
serial.write_buffer(serial.read_buffer(9))

def on_forever():
    basic.clear_screen()
    led.plot(Math.round(Rope), 2)
    if Rope < 0:
        basic.show_string("A is The Winner And B Is The Loser! HAHAHAHA!")
    else:
        basic.show_string("B is The Winner And A Is The Loser! HAHAHAHA!")
basic.forever(on_forever)
