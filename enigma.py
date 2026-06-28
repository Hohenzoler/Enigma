from rotors import *


class M1:
    def __init__(self, Rotors, reflector, Initial_pos=[0,0,0], ring_settings=[0,0,0]):
        self.Rotors = [Rotors[0][0], Rotors[1][0], Rotors[2][0]]  # [Left rotor, Middle rotor, Right rotor]
        self.pos = Initial_pos  # [Left pos, Middle pos, Right pos],
        self.reflector = reflector
        self.character_offset_factor = 65
        self.ring_position = [ord(Rotors[0][1]) + ring_settings[0] - self.character_offset_factor, ord(Rotors[1][1]) + ring_settings[1] - self.character_offset_factor, ord(Rotors[2][1]), + ring_settings[2] - self.character_offset_factor]


    def Individual_Input(self, s):
        s = s.upper()
        self.rotate_rotors()

        pos1 = self.Rotors[2][(ord(s) + self.pos[2] - self.character_offset_factor + 26)%26]
        pos1 = chr(((ord(pos1)-self.character_offset_factor)+26-self.pos[2])%26 + self.character_offset_factor)

        # print(pos1)

        pos2 = self.Rotors[1][(ord(pos1) + self.pos[1] - self.character_offset_factor + 26)%26]
        pos2 = chr(((ord(pos2) - self.character_offset_factor) + 26 - self.pos[1]) % 26 + self.character_offset_factor)
        # print(pos2)

        pos3 = self.Rotors[0][(ord(pos2) + self.pos[0] - self.character_offset_factor + 26)%26]
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

        return pos6


    def rotate_rotors(self):
        self.pos[2] = (self.pos[2] + 27) % 26
        if self.ring_position[2] == self.pos[2] - 1:
            self.pos[1] = (self.pos[1] + 27) % 26
            if self.ring_position[1] == self.pos[1] - 1:
                self.pos[0] = (self.pos[0] + 27) % 26

        # print(self.pos)

    def Text_Input(self, text):
        ans = ''
        text = text.replace(" ", '')
        text = text.strip()

        for i, letter in enumerate(text):
            if i % 5 == 0 and i != 0:
                ans += ' '
            ans += self.Individual_Input(letter)

        return ans


if __name__ == '__main__':
    machine = M1([I, II, III], UKW_B, [0,0,0], [0,0,0])

    print(machine.Text_Input('A'))





