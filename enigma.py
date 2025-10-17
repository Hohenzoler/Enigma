from rotors import *


class M1:
    def __init__(self, Rotors, Initial_pos, reflector):
        self.Rotors = Rotors  # [Left rotor, Middle rotor, Right rotor]
        self.pos = Initial_pos  # [Left pos, Middle pos, Right pos],
        self.reflector = reflector
        self.character_offset_factor = 65
        self.turn_3 = False


    def Individual_Input(self, s):
        s = s.capitalize()

        if self.pos[2] == ord(self.Rotors[2][-1]) - self.character_offset_factor:
            self.pos[1] += 1
            self.turn_3 = True
            if self.pos[1] == 27:
                self.pos[1] = 1




        if self.pos[1] == ord(self.Rotors[1][-1]) - self.character_offset_factor and self.turn_3:
            self.pos[0] += 1
            self.turn_3 = False
            if self.pos[0] == 27:
                self.pos[0] = 1




        self.pos[2] += 1
        if self.pos[2] == 27:
            self.pos[2] = 1







        value = ord(s) - self.character_offset_factor + self.pos[2] - 1
        if value > 25:
            value %= 26
        elif value < 0:
            value += 26

        s = self.Rotors[2][value]
        # print(s)


        value = ord(s) - self.character_offset_factor - self.pos[2] + 1
        if value > 25:
            value %= 26
        elif value < 0:
            value += 26
        s = self.Rotors[1][value]
        # print(s)

        value = ord(s) - self.character_offset_factor
        if value > 25:
            value %= 26
        elif value < 0:
            value += 26
        s = self.Rotors[0][value]
        # print(s)

        value = ord(s) - self.character_offset_factor
        if value > 25:
            value %= 26
        elif value < 0:
            value += 26
        s = self.reflector[value]
        # print(s)

        reflected_value = self.Rotors[0].index(s) + self.character_offset_factor
        if reflected_value > 90:
            reflected_value = reflected_value%90 + self.character_offset_factor-1
        elif reflected_value < 65:
            reflected_value += 26

        s = chr(reflected_value)
        # print(s)

        reflected_value = self.Rotors[1].index(s) + self.character_offset_factor + self.pos[2] - 1
        if reflected_value > 90:
            reflected_value = reflected_value%90 + self.character_offset_factor-1
        elif reflected_value < 65:
            reflected_value += 26

        s = chr(reflected_value)
        # print(s)

        reflected_value = self.Rotors[2].index(s) + self.character_offset_factor - self.pos[2] + 1
        if reflected_value > 90:
            reflected_value = reflected_value%90 + self.character_offset_factor-1
        elif reflected_value < 65:
            reflected_value += 26

        s = chr(reflected_value)

        print(s)

machine = M1([III, II, I], [1, 1, 1], UKW_B)

for _ in range(20):
    machine.Individual_Input('A')

print(machine.pos)



