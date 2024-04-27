function 燈數 (num: number, 關燈: boolean) {
    if (num % 5 == 0) {
        x = 4
        y = Math.floor(num / 5) - 1
    } else {
        x = num % 5 - 1
        y = Math.floor(num / 5)
    }
    if (關燈) {
        led.unplot(x, y)
    } else {
        led.plot(x, y)
    }
}
input.onButtonPressed(Button.A, function () {
    n += 1
    燈數(n, false)
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
    n = 0
})
input.onButtonPressed(Button.B, function () {
	
})
let y = 0
let x = 0
let n = 0
n = 0
燈數(n, true)
n += -1
