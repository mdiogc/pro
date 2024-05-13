from __future__ import annotations


class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'

    def __init__(self, sequence: str):
        self.sequence = sequence.upper()


    def __str__(self): 
        return self.sequence


    @property
    def adenines(self) -> int:
        """Número de adeninas de la secuencia de ADN"""
        return self.sequence.count(self.ADENINE)


    @property
    def cytosines(self) -> int:
        """Número de citosinas de la secuencia de ADN"""
        return self.sequence.count(self.CYTOSINE)

    @property
    def guanines(self) -> int:
        """Número de guaninas de la secuencia de ADN"""
        return self.sequence.count(self.GUANINE)

    @property
    def thymines(self) -> int:
        """Número de timinas de la secuencia de ADN"""
        return self.sequence.count(self.THYMINE)

    def __add__(self, other: DNA) -> DNA:
        """Se define la suma de dos secuencias de ADN como el máximo de cada base nitrogenada
        (base a base). Por ejemplo 'T' sería mayor que 'A'.
        Si las secuencias no tienen la misma longitud, habrá que aplicar el máximo base a base
        hasta donde se pueda, y completar el resto de la secuencia con la parte que falte, bien
        de la primera o bien de la segunda secuencia, en función de cuál sea mayor.
        """
        combined_length = max(len(self.sequence), len(other.sequence))
        new_sequence = ''
        for index in range(combined_length):

            if index < len(self.sequence) and index < len(other.sequence):
                base_self = self.sequence[index]
                base_other = other.sequence[index]
                new_sequence += max(base_self, base_other)

            if index >= len(self.sequence):
                new_sequence += other.sequence[index]

            if index >= len(other.sequence):
                new_sequence += self.sequence[index]
                
        return DNA(new_sequence)

    def __len__(self):
        """Longitud de la secuencia de ADN"""
        return len(self.sequence)


    def stats(self) -> dict[str, float]:
        """Porcentaje de aparición de cada base con respecto al total.
        Se devuelve un diccionario donde la clave será la base nitrogenada
        y el valor será el porcentaje."""
        total_bases = len(self.sequence)
        PERCENT = 100
        adenine_percent = (self.adenines / total_bases) * PERCENT
        cytosine_percent = (self.cytosines / total_bases) * PERCENT
        guanine_percent = (self.guanines / total_bases) * PERCENT
        thymine_percent = (self.thymines / total_bases) * PERCENT
    
        return {
            self.ADENINE: adenine_percent,
            self.CYTOSINE: cytosine_percent,
            self.GUANINE: guanine_percent,
            self.THYMINE: thymine_percent
        }

    def __mul__(self, other: DNA) -> DNA:
        """Se define la multiplicación de dos secuencias de ADN como una nueva cadena
        de ADN donde aparecen las bases que son iguales (posición a posición)"""
        new_sequence = ''
        min_length = min(len(self.sequence), len(other.sequence))
        
        for index in range(min_length):
            base_self = self.sequence[index]
            base_other = other.sequence[index]
            if base_self == base_other:
                new_sequence += base_self
                
        return DNA(new_sequence)

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        """Construye una secuencia de ADN a partir de un fichero.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path, 'r') as file:
            sequence = file.read().strip().upper()
        return cls(sequence)

    def dump_to_file(self, path: str) -> None:
        """Vuelca una secuencia de ADN a un fichero de salida.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path, 'w') as file:
            file.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        """Devuelve la base que ocupa la posición 'index'"""
        return self.sequence[index]


    def __setitem__(self, index: int, base: str) -> None:
        """Fija la base 'base' en la posición 'index'
        NOTA: Si la base que se va a asignar no es ninguna de las 4 bases
        habituales, hay que asignar ADENINA."""
        if base not in [self.ADENINE, self.CYTOSINE, self.GUANINE, self.THYMINE]:
            base = self.ADENINE
        self.sequence = self.sequence[:index] + base + self.sequence[index + 1:]
