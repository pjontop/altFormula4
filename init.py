Halt = False
myVariable = 0
BottomLeftVel = 0
BottomRightVel = 0
TopRightVel = 0
TopLeftVel = 0
BottomLeftDist = 0
TopLeftDist = 0
BottomLeftError = 0
TopLeftError = 0
TopRightError = 0
BottomRightError = 0
BottomLeftRec = 0
TopLeftRec = 0
TopRightRec = 0
BottomRightRec = 0

def when_started1():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    while True:
        BottomLeft.set_velocity(BottomLeftVel, RPM)
        BottomRight.set_velocity(BottomRightVel, RPM)
        TopRight.set_velocity(TopRightVel, RPM)
        TopLeft.set_velocity(TopLeftVel, RPM)
        wait(5, MSEC)

def when_started2():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    Halt = True
    while True:
        if Halt:
            BottomLeft.spin(FORWARD)
            BottomRight.spin(FORWARD)
            TopRight.spin(FORWARD)
            TopLeft.spin(FORWARD)
        wait(5, MSEC)

def when_started3():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    BottomLeftRot.set_position(0, DEGREES)
    TopLeftRot.set_position(0, DEGREES)
    TopRightRot.set_position(0, DEGREES)
    BottomRightRot.set_position(0, DEGREES)
    BottomLeftFree.set_position(0, DEGREES)
    TopLeftFree.set_position(0, DEGREES)
    TopRightFree.set_position(0, DEGREES)
    BottomRightFree.set_position(0, DEGREES)
    while True:
        BottomLeftError = BottomLeftRot.position(TURNS) - BottomLeftFree.position(TURNS) * myVariable
        TopLeftError = TopLeftRot.position(TURNS) - TopLeftFree.position(TURNS) * myVariable
        TopRightError = TopRightRot.position(TURNS) - TopRightFree.position(TURNS) * myVariable
        BottomRightError = BottomRightRot.position(TURNS) - BottomRightFree.position(TURNS) * myVariable
        if BottomLeftError > 0.15:
            BottomLeftRec = BottomLeftRot.position(DEGREES)
            Halt = False
            while not BottomLeftFree.position(TURNS) * myVariable == BottomLeftRec:
                BottomLeft.set_velocity(200, RPM)
                BottomLeft.spin(REVERSE)
                wait(5, MSEC)
            BottomLeftRot.set_position(BottomLeftRec, DEGREES)
        if BottomLeftError < 0.15:
            BottomLeftRec = BottomLeftRot.position(DEGREES)
            Halt = False
            while not BottomLeftFree.position(TURNS) * myVariable == BottomLeftRec:
                BottomLeft.set_velocity(200, RPM)
                BottomLeft.spin(FORWARD)
                wait(5, MSEC)
            BottomLeftRot.set_position(BottomLeftRec, DEGREES)
        if TopLeftError > 0.15:
            TopLeftRec = TopLeftRot.position(DEGREES)
            Halt = False
            while not TopLeftFree.position(TURNS) * myVariable == TopLeftRec:
                TopLeft.set_velocity(200, RPM)
                TopLeft.spin(REVERSE)
                wait(5, MSEC)
            TopLeftRot.set_position(TopLeftRec, DEGREES)
        if TopLeftError < 0.15:
            TopLeftRec = TopLeftRot.position(DEGREES)
            Halt = False
            while not TopLeftFree.position(TURNS) * myVariable == TopLeftRec:
                TopLeft.set_velocity(200, RPM)
                TopLeft.spin(FORWARD)
                wait(5, MSEC)
            TopLeftRot.set_position(TopLeftRec, DEGREES)
        if TopRightError > 0.15:
            TopRightRec = TopRightRot.position(DEGREES)
            Halt = False
            while not TopRightFree.position(TURNS) * myVariable == TopRightRec:
                TopRight.set_velocity(200, RPM)
                TopRight.spin(REVERSE)
                wait(5, MSEC)
            TopRightRot.set_position(TopRightRec, DEGREES)
        if TopRightError < 0.15:
            TopRightRec = TopRightRot.position(DEGREES)
            Halt = False
            while not TopRightFree.position(TURNS) * myVariable == TopRightRec:
                TopRight.set_velocity(200, RPM)
                TopRight.spin(FORWARD)
                wait(5, MSEC)
            TopRightRot.set_position(TopRightRec, DEGREES)
        if BottomRightError > 0.15:
            BottomRightRec = BottomRightRot.position(DEGREES)
            Halt = False
            while not BottomRightFree.position(TURNS) * myVariable == BottomRightRec:
                BottomRight.set_velocity(200, RPM)
                BottomRight.spin(REVERSE)
                wait(5, MSEC)
            BottomRightRot.set_position(BottomRightRec, DEGREES)
        if BottomRightError < 0.15:
            BottomRightRec = BottomRightRot.position(DEGREES)
            Halt = False
            while not BottomRightFree.position(TURNS) * myVariable == BottomRightRec:
                BottomRight.set_velocity(200, RPM)
                BottomRight.spin(FORWARD)
                wait(5, MSEC)
            BottomRightRot.set_position(BottomRightRec, DEGREES)
        wait(5, MSEC)

def when_started4():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    while True:
        if controller_1.buttonUp.pressing() or controller_1.buttonDown.pressing() or controller_1.buttonLeft.pressing() or controller_1.buttonRight.pressing():
            BottomLeftVel = 0
            BottomRightVel = 0
            TopRightVel = 0
            TopLeftVel = 0
            if controller_1.buttonUp.pressing():
                BottomLeftVel = BottomLeftVel + 100
                BottomRightVel = BottomRightVel + 100
                TopRightVel = TopRightVel + 100
                TopLeftVel = TopLeftVel + 100
            if controller_1.buttonDown.pressing():
                BottomLeftVel = BottomLeftVel + -100
                BottomRightVel = BottomRightVel + -100
                TopRightVel = TopRightVel + -100
                TopLeftVel = TopLeftVel + -100
            if controller_1.buttonLeft.pressing():
                BottomLeftVel = BottomLeftVel + -100
                BottomRightVel = BottomRightVel + 100
                TopRightVel = TopRightVel + 100
                TopLeftVel = TopLeftVel + -100
            if controller_1.buttonRight.pressing():
                BottomLeftVel = BottomLeftVel + 100
                BottomRightVel = BottomRightVel + -100
                TopRightVel = TopRightVel + -100
                TopLeftVel = TopLeftVel + 100
        wait(5, MSEC)

def when_started5():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    while True:
        if not (controller_1.buttonUp.pressing() or controller_1.buttonDown.pressing() or controller_1.buttonLeft.pressing() or controller_1.buttonRight.pressing()):
            BottomLeftVel = controller_1.axis3.position() - controller_1.axis4.position()
            BottomRightVel = controller_1.axis3.position() + controller_1.axis4.position()
            TopRightVel = controller_1.axis3.position() - controller_1.axis4.position()
            TopLeftVel = controller_1.axis3.position() + controller_1.axis4.position()
        wait(5, MSEC)

def when_started6():
    global Halt, myVariable, BottomLeftVel, BottomRightVel, TopRightVel, TopLeftVel, BottomLeftDist, TopLeftDist, BottomLeftError, TopLeftError, TopRightError, BottomRightError, BottomLeftRec, TopLeftRec, TopRightRec, BottomRightRec
    while True:
        myVariable = 1.6
        wait(5, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
ws4 = Thread( when_started4 )
ws5 = Thread( when_started5 )
ws6 = Thread( when_started6 )
when_started1()