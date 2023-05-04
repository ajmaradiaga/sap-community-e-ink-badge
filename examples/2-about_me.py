import badger2040
from badger2040 import WIDTH

TEXT_SIZE = 1
LINE_HEIGHT = 15
EMPTY_LINE_HEIGHT = 10

display = badger2040.Badger2040()
display.led(128)

ABOUT_ME_PATH = "/about-me.txt"

# Open the badge file
try:
    about_me = open(ABOUT_ME_PATH, "r")
except OSError:
    with open(ABOUT_ME_PATH, "w") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
    about_me = open(ABOUT_ME_PATH, "r")

# Clear to white
display.set_pen(15)
display.clear()

# Retrieve name from about me file
my_name = about_me.readline()

display.set_font("bitmap8")
display.set_pen(0)
display.rectangle(0, 0, WIDTH, 16)
display.set_pen(15)
display.text(my_name, 3, 4, WIDTH, 1)
display.text("about me", WIDTH - display.measure_text("about me", 0.4) - 4, 4, WIDTH, 1)

display.set_pen(0)

y = 16 + int(LINE_HEIGHT / 2)

lines = about_me.read().strip().split("\n")

for line in lines:
    display.text(line, 5, y, WIDTH, TEXT_SIZE)
    
    y += EMPTY_LINE_HEIGHT if len(line) == 0 else LINE_HEIGHT

display.update()


# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    display.keepalive()
    display.halt()

