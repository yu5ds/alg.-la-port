# lamport_clock.py

class LamportClock:
    def __init__(self):
        self.time = 0  # Inicializamos el reloj a 0

    def increment(self):
        """Incrementa el tiempo local del reloj."""
        self.time += 1

    def get_time(self):
        """Devuelve la marca de tiempo local."""
        return self.time

    def sync(self, other_time):
        """Sincroniza el reloj local con el de otro proceso."""
        self.time = max(self.time, other_time) + 1
