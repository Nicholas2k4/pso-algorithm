import random
import math

def rnd(lower_bound, upper_bound):
    # Generate a random decimal within the specified range
    return random.uniform(lower_bound, upper_bound - 0.0000000001)  # Slightly adjust upper bound for exclusivity

class Kapal:
    def __init__(self, id, nama, bobot_max, x_max_umum, y_max_umum, x_max_khusus, y_max_khusus, rute, jarak, biaya):
        self.id = id
        self.nama = nama
        self.bobot_max = bobot_max
        self.x_max_umum = x_max_umum
        self.y_max_umum = y_max_umum
        self.x_max_khusus = x_max_khusus
        self.y_max_khusus = y_max_khusus
        self.rute = rute
        self.jarak = jarak
        self.biaya = biaya

    def __str__(self):
        return f"ID: {self.id}, Nama: {self.nama}, Bobot Maksimal: {self.bobot_max}, X Maksimum Umum: {self.x_max_umum}, Y Maksimum Umum: {self.y_max_umum}, X Maksimum Khusus: {self.x_max_khusus}, Y Maksimum Khusus: {self.y_max_khusus}, Rute: {self.rute}, Jarak: {self.jarak}, Biaya: {self.biaya}"

    # Getter untuk atribut id
    def get_id(self):
        return self.id

    # Setter untuk atribut id
    def set_id(self, id):
        self.id = id

    # Getter untuk atribut nama
    def get_nama(self):
        return self.nama

    # Setter untuk atribut nama
    def set_nama(self, nama):
        self.nama = nama

    # Getter untuk atribut bobot_max
    def get_bobot_max(self):
        return self.bobot_max

    # Setter untuk atribut bobot_max
    def set_bobot_max(self, bobot_max):
        self.bobot_max = bobot_max

    # Getter untuk atribut x_max_umum
    def get_x_max_umum(self):
        return self.x_max_umum

    # Setter untuk atribut x_max_umum
    def set_x_max_umum(self, x_max_umum):
        self.x_max_umum = x_max_umum

    # Getter untuk atribut y_max_umum
    def get_y_max_umum(self):
        return self.y_max_umum

    # Setter untuk atribut y_max_umum
    def set_y_max_umum(self, y_max_umum):
        self.y_max_umum = y_max_umum

    # Getter untuk atribut x_max_khusus
    def get_x_max_khusus(self):
        return self.x_max_khusus

    # Setter untuk atribut x_max_khusus
    def set_x_max_khusus(self, x_max_khusus):
        self.x_max_khusus = x_max_khusus

    # Getter untuk atribut y_max_khusus
    def get_y_max_khusus(self):
        return self.y_max_khusus

    # Setter untuk atribut y_max_khusus
    def set_y_max_khusus(self, y_max_khusus):
        self.y_max_khusus = y_max_khusus

    # Getter untuk atribut rute
    def get_rute(self):
        return self.rute

    # Setter untuk atribut rute
    def set_rute(self, rute):
        self.rute = rute

    # Getter untuk atribut jarak
    def get_jarak(self):
        return self.jarak

    # Setter untuk atribut jarak
    def set_jarak(self, jarak):
        self.jarak = jarak

    # Getter untuk atribut biaya
    def get_biaya(self):
        return self.biaya

    # Setter untuk atribut biaya
    def set_biaya(self, biaya):
        self.biaya = biaya



class Item:
    def __init__(self, id, nama, jenis, bobot, biaya_per_ton, tujuan):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.bobot = bobot
        self.biaya_per_ton = biaya_per_ton
        self.tujuan = tujuan

    def __str__(self):
        return f"ID: {self.id}, Nama: {self.nama}, Jenis: {self.jenis}, Bobot: {self.bobot}, Biaya per Ton: {self.biaya_per_ton}, Tujuan: {self.tujuan}"

    # Getter untuk atribut id
    def get_id(self):
        return self.id

    # Setter untuk atribut id
    def set_id(self, id):
        self.id = id

    # Getter untuk atribut nama
    def get_nama(self):
        return self.nama

    # Setter untuk atribut nama
    def set_nama(self, nama):
        self.nama = nama

    # Getter untuk atribut jenis
    def get_jenis(self):
        return self.jenis

    # Setter untuk atribut jenis
    def set_jenis(self, jenis):
        self.jenis = jenis

    # Getter untuk atribut bobot
    def get_bobot(self):
        return self.bobot

    # Setter untuk atribut bobot
    def set_bobot(self, bobot):
        self.bobot = bobot

    # Getter untuk atribut biaya_per_ton
    def get_biaya_per_ton(self):
        return self.biaya_per_ton

    # Setter untuk atribut biaya_per_ton
    def set_biaya_per_ton(self, biaya_per_ton):
        self.biaya_per_ton = biaya_per_ton

    # Getter untuk atribut tujuan
    def get_tujuan(self):
        return self.tujuan

    # Setter untuk atribut tujuan
    def set_tujuan(self, tujuan):
        self.tujuan = tujuan

class Position:
    def __init__(self, x, y, z, id_kapal):
        self.x = x
        self.y = y
        self.z = z
        self.id_kapal = id_kapal
        
    def __str__(self):
        return "x: " + str(self.x) + "\n" + "y: " + str(self.y) + "\n" + "z: " + str(self.z) + "\n" + "id_kapal: " + str(self.id_kapal) + "\n"
        
class Velocity:
    def __init__(self, x, y, z, id_kapal):
        self.x = x
        self.y = y
        self.z = z
        self.id_kapal = id_kapal
        
    def __str__(self):
        return "x: " + str(self.x) + "\n" + "y: " + str(self.y) + "\n" + "z: " + str(self.z) + "\n" + "id_kapal: " + str(self.id_kapal) + "\n"

class Particle:
    def __init__(self, items, kapals):
        self.positions = []
        self.velocities = []
        
        idx = 0
        for i in range(len(items)):
            id_kapal = rnd(1, len(kapals) + 1)
            
            if items[idx].jenis == "Umum":
                self.positions.append(Position(
                    rnd(1, kapals[math.floor(id_kapal) - 1].x_max_umum + 1),
                    rnd(1, kapals[math.floor(id_kapal) - 1].y_max_umum + 1),
                    rnd(1, 6),
                    id_kapal))
                self.velocities.append(Velocity(
                    rnd(-kapals[math.floor(id_kapal) - 1].x_max_umum, kapals[math.floor(id_kapal) - 1].x_max_umum + 1),
                    rnd(-kapals[math.floor(id_kapal) - 1].y_max_umum, kapals[math.floor(id_kapal) - 1].y_max_umum + 1),
                    rnd(-5, 6),
                    id_kapal))
            else:
                self.positions.append(Position(
                    rnd(1, kapals[math.floor(id_kapal) - 1].x_max_khusus + 1),
                    rnd(1, kapals[math.floor(id_kapal) - 1].y_max_khusus + 1),
                    rnd(-5, 6),
                    id_kapal))
                self.velocities.append(Velocity(
                    rnd(-kapals[math.floor(id_kapal) - 1].x_max_khusus, kapals[math.floor(id_kapal) - 1].x_max_khusus + 1),
                    rnd(-kapals[math.floor(id_kapal) - 1].y_max_khusus, kapals[math.floor(id_kapal) - 1].y_max_khusus + 1),
                    rnd(-5, 6),
                    id_kapal))
            idx+=1
        
    def __str__(self):
        s = "Pos: \n"
        
        for pos in self.positions:
            s += str(pos)
            s += "\n"
    
        s += "\nVel:\n"
        
        for vel in self.velocities:
            s += str(vel)
            s += "\n"
        
        s += "\n"
        
        return s
        
# main
items_data = [
    [1, "xxx1", "Umum", 10, 1000, 1],
    [2, "xxx2", "Umum", 20, 1000, 2],
    [3, "xxx3", "Khusus", 15, 1500, 3],
    [4, "xxx4", "Umum", 10, 1000, 1],
    [5, "xxx5", "Khusus", 20, 1500, 2],
    [6, "xxx6", "Umum", 15, 1000, 3]
]

items = []

for data in items_data:
    item = Item(*data)
    items.append(item)

# Mencetak informasi setiap item dalam array
for item in items:
    print(item)
    
    
kapals_data = [
    [1, "Kapal 1", 50, 5, 10, 3, 4, [1, 3, 4, 2], 15, 15000],
    [2, "Kapal 2", 60, 7, 20, 1, 5, [1, 2, 4, 3], 14, 14000],
    [3, "Kapal 3", 60, 6, 10, 3, 4, [1, 4, 3, 2], 15, 15000]
]

kapals = []

for data in kapals_data:
    kapal = Kapal(*data)
    kapals.append(kapal)

# Mencetak informasi setiap kapal dalam array
for kapal in kapals:
    print(kapal)


# Generate particle
particles = []
for i in range(6):
    particles.append(Particle(items, kapals))

for par in particles:
    print(par)
