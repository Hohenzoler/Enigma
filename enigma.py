from rotors import *


class M1:
    def __init__(self, Rotors, Initial_pos, reflector):
        self.Rotors = Rotors  # [Left rotor, Middle rotor, Right rotor]
        self.pos = Initial_pos  # [Left pos, Middle pos, Right pos],
        self.reflector = reflector
        self.character_offset_factor = 65
        self.turn_3 = False
        self.ring_position = [0, 0, 0]


    def Individual_Input(self, s):
        s = s.upper()

        pos1 = self.Rotors[2][ord(s)+self.pos[2]-self.character_offset_factor]
        pos1 = chr(((ord(pos1)-self.character_offset_factor)+26-self.pos[2])%26 + self.character_offset_factor)

        # print(pos1)

        pos2 = self.Rotors[1][ord(pos1) + self.pos[1] - self.character_offset_factor]
        pos2 = chr(((ord(pos2) - self.character_offset_factor) + 26 - self.pos[1]) % 26 + self.character_offset_factor)
        # print(pos2)

        pos3 = self.Rotors[0][ord(pos2) + self.pos[0] - self.character_offset_factor]
        pos3 = chr(((ord(pos3) - self.character_offset_factor) + 26 - self.pos[0]) % 26 + self.character_offset_factor)
        # print(pos3)

        reflected = self.reflector[ord(pos3) - self.character_offset_factor]
        # print(reflected)

        pos4 = chr((ord(reflected) - self.character_offset_factor + self.pos[0] + 26) % 26 + self.character_offset_factor)
        pos4 = chr((self.Rotors[0].index(pos4) - self.pos[0] + 26) % 26 + self.character_offset_factor)
        # print(pos4)

        pos5 = chr((ord(pos4) - self.character_offset_factor + self.pos[1] + 26) % 26 + self.character_offset_factor)
        pos5 = chr((self.Rotors[1].index(pos5) - self.pos[1] + 26) % 26 + self.character_offset_factor)
        # print(pos5)

        pos6 = chr((ord(pos5) - self.character_offset_factor + self.pos[2] + 26) % 26 + self.character_offset_factor)
        pos6 = chr((self.Rotors[2].index(pos6) - self.pos[2] + 26) % 26 + self.character_offset_factor)
        print(pos6)




machine = M1([I, II, III], [1, 1, 2], UKW_B)

machine.Individual_Input('A')





