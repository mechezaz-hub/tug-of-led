input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Rope += -0.1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Rope += 0.1
})
let Rope = 9
serial.writeLine("A is The Winner And B Is The Loser! HAHAHAHA!")
serial.redirectToUSB()
serial.writeBuffer(serial.readBuffer(9))
basic.forever(function on_forever() {
    basic.clearScreen()
    led.plot(Math.round(Rope), 2)
    if (Rope < 0) {
        basic.showString("A is The Winner And B Is The Loser! HAHAHAHA!")
    } else {
        basic.showString("B is The Winner And A Is The Loser! HAHAHAHA!")
    }
    
})
