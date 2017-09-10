from socketIO_client import SocketIO
import ev3dev.ev3 as ev3
import time

clawMotor = ev3.MediumMotor('outA')
moveMotor1 = ev3.LargeMotor('outB')
moveMotor2 = ev3.LargeMotor('outD')

ir = ev3.InfraredSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"
ir.mode = 'IR-PROX'

ts = ev3.TouchSensor()
assert ts.connected, "Connect a touch sensor to any port"

ev3.Sound.set_volume(100)

socket = SocketIO('http://alexaev3api.azurewebsites.net')

def onDoItDudeCommand(command):
    print('DO IT DUDE')

    running = True

    while(running):
        moveForward()

        distance = ir.value()
        print('IR - DISTANCE: ' + str(distance))

        if distance < 34:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)

            stopMoving()

            openClaw()

            moveForwardTimed()

            time.sleep(1.3)

            closeClaw()

            ev3.Sound.speak('Beer Beer Beer Beer')

            time.sleep(1)

            moveBackwardForTime()

            running = False
        else:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)

    # stopMoving()
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)


def onConnect():
    print('Connected to Cloud, Dude', socket.transport_name)


def onClawCommand(command):
    print('CLAW Command: ' + command)

    if (command == 'open'):
        openClaw()
    else:
        closeClaw()


def openClaw():
    clawMotor.run_timed(time_sp=200, speed_sp=500)


def closeClaw():
    clawMotor.run_timed(time_sp=250, speed_sp=-800)


def onMoveCommand(command):
    print('MOVE Command ' + command)

    if (command == 'forward'):
        moveForward()
    elif(command == 'backward'):
        moveBackward()
    else:
        stopMoving()


def moveForward():
    print('Moving forward...')

    moveMotor1.run_forever(speed_sp=500)
    moveMotor2.run_forever(speed_sp=500)


def moveBackward():
    print('Moving backward...')

    moveMotor1.run_forever(speed_sp=-500)
    moveMotor2.run_forever(speed_sp=-500)


def moveBackwardForTime():
    moveMotor1.run_timed(time_sp=15000, speed_sp=-200)
    moveMotor2.run_timed(time_sp=15000, speed_sp=-200)


def moveForwardTimed():
    moveMotor1.run_timed(time_sp=1500, speed_sp=200)
    moveMotor2.run_timed(time_sp=1500, speed_sp=200)


def stopMoving():
    moveMotor1.stop()
    moveMotor2.stop()


socket.on('connect', onConnect)
socket.on('claw', onClawCommand)
socket.on('move', onMoveCommand)
socket.on('doItDude', onDoItDudeCommand)

socket.wait()
