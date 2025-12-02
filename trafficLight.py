from gpiozero import TrafficLights, LED, Button
from time import sleep

auto_ampel = TrafficLights(25, 8, 7)

fussg_rot = LED(21)
fussg_gruen = LED(20)

# Der Knopf
knopf = Button(16)


def ampel_zyklus():
    print("Knopf gedrückt! Ampelphasen starten...")

    sleep(2)
    auto_ampel.green.off()
    auto_ampel.amber.on()
    sleep(3)

    auto_ampel.amber.off()
    auto_ampel.red.on()

    sleep(2)

    fussg_rot.off()
    fussg_gruen.on()
    print("Fussgänger können gehen.")

    sleep(5)

    fussg_gruen.off()
    fussg_rot.on()

    sleep(2)

    auto_ampel.amber.on()
    sleep(1)

    auto_ampel.red.off()
    auto_ampel.amber.off()
    auto_ampel.green.on()
    print("Autos haben wieder Grün.")


print("Ampel-System gestartet. Drücke STRG+C zum Beenden.")

auto_ampel.green.on()
fussg_rot.on()

try:
    while True:
        knopf.wait_for_press()

        ampel_zyklus()

except KeyboardInterrupt:
    print("\nProgramm beendet.")