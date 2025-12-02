from gpiozero import TrafficLights, LED, Button
from time import sleep

ampel_1 = TrafficLights(25, 8, 7)
ampel_2 = TrafficLights(26, 19, 13)

fussg_rot = LED(21)
fussg_gruen = LED(20)
knopf = Button(16)

anforderung_fussgaenger = False


def knopf_gedrueckt():
    global anforderung_fussgaenger
    anforderung_fussgaenger = True
    print("Knopf wurde gedrückt! Anforderung gespeichert.")


knopf.when_pressed = knopf_gedrueckt


def intelligentes_warten(sekunden):
    global anforderung_fussgaenger

    schritte = int(sekunden * 10)

    for _ in range(schritte):
        if anforderung_fussgaenger:
            return True
        sleep(0.1)
    return False


def alles_auf_rot():
    if ampel_1.green.value == 1:
        ampel_1.green.off()
        ampel_1.amber.on()
        sleep(2)
        ampel_1.amber.off()
        ampel_1.red.on()

    if ampel_2.green.value == 1:
        ampel_2.green.off()
        ampel_2.amber.on()
        sleep(2)
        ampel_2.amber.off()
        ampel_2.red.on()

    sleep(1)


def fussgaenger_zyklus():
    """Der Ablauf für die Fußgänger"""
    global anforderung_fussgaenger
    print("Fußgängerphase startet...")

    alles_auf_rot()

    # Fußgänger Grün
    fussg_rot.off()
    fussg_gruen.on()
    sleep(5)

    fussg_gruen.off()
    fussg_rot.on()
    sleep(2)

    anforderung_fussgaenger = False
    print("Fußgängerphase beendet.")



print("Kreuzungs-Steuerung aktiv.")
print("Drücke den Knopf für Fußgänger.")

ampel_1.green.on()
ampel_2.red.on()
fussg_rot.on()

try:
    while True:
        abbruch = intelligentes_warten(5)

        if abbruch:
            fussgaenger_zyklus()
            ampel_1.red.off()
            ampel_1.amber.on()
            sleep(1)
            ampel_1.amber.off()
            ampel_1.green.on()
            continue

        ampel_1.green.off()
        ampel_1.amber.on()
        sleep(2)
        ampel_1.amber.off()
        ampel_1.red.on()

        sleep(1)

        ampel_2.red.off()
        ampel_2.amber.on()  # Rot-Gelb
        sleep(1)
        ampel_2.amber.off()
        ampel_2.green.on()

        abbruch = intelligentes_warten(5)

        if abbruch:
            fussgaenger_zyklus()
            continue

        ampel_2.green.off()
        ampel_2.amber.on()
        sleep(2)
        ampel_2.amber.off()
        ampel_2.red.on()

        sleep(1)

        ampel_1.red.off()
        ampel_1.amber.on()
        sleep(1)
        ampel_1.amber.off()
        ampel_1.green.on()

except KeyboardInterrupt:
    print("Beendet")