from pushbullet import Pushbullet

pb = Pushbullet("o.N9fN9fxDfWLsjqaChdWJ2SmFRbgIrY0i")

dev = pb.get_device("Galaxy S9 Plus")
push = dev.push_note("Waarschuwing!!","Je kastje is opengemaakt!!")
