import random
import math

ROUTE = [
    [0, 0, 0, 0, 0],
    [0, 0, 3, 4, 2],
    [0, 3, 0, 7, 5],
    [0, 4, 7, 0, 6],
    [0, 2, 5, 6, 0]
]
Z_MAX = 100
INF = 1000000000000
PENALTY = 5000
TEST = True
PARTICLE_COUNT = 1000

def rnd(lower_bound, upper_bound):
    return random.uniform(lower_bound, upper_bound - 0.0000000001)

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
        return f"ID: {self.id}\nNama: {self.nama}\nBobot Maksimal: {self.bobot_max}\nX Maksimum Umum: {self.x_max_umum}\nY Maksimum Umum: {self.y_max_umum}\nX Maksimum Khusus: {self.x_max_khusus}\nY Maksimum Khusus: {self.y_max_khusus}\nRute: {self.rute}\nJarak: {self.jarak}\nBiaya: {self.biaya}\n"


class Item:
    def __init__(self, id, nama, jenis, bobot, biaya_per_ton, tujuan):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.bobot = bobot
        self.biaya_per_ton = biaya_per_ton
        self.tujuan = tujuan

    def __str__(self):
        return f"ID: {self.id}\nNama: {self.nama}\nJenis: {self.jenis}\nBobot: {self.bobot}\nBiaya per Ton: {self.biaya_per_ton}\nTujuan: {self.tujuan}\n"


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
        self.items = items
        self.kapals = kapals
        self.positions = []
        self.velocities = []
        self.pb = INF
        self.pb_pos = []
        self.gb = INF
        self.gb_pos = []
        self.fitness = INF
        
        for i in range(len(items)):
            id_kapal = rnd(0, len(kapals) + 1)
            id_kapal_int = math.floor(id_kapal)
            
            # Tidak masuk kapal manapun
            if id_kapal_int == len(kapals):
                self.positions.append(Position(0,0,0,id_kapal))
                self.velocities.append(Velocity(0,0,0,id_kapal))
            # Jenis item umum
            elif items[i].jenis == "Umum":
                self.positions.append(Position(
                    rnd(1, kapals[id_kapal_int].x_max_umum + 1),
                    rnd(1, kapals[id_kapal_int].y_max_umum + 1),
                    rnd(1, Z_MAX + 1),
                    id_kapal
                    )
                )
                # self.velocities.append(Velocity(
                #     rnd(-kapals[id_kapal_int].x_max_umum, kapals[id_kapal_int].x_max_umum),
                #     rnd(-kapals[id_kapal_int].y_max_umum, kapals[id_kapal_int].y_max_umum),
                #     rnd(-Z_MAX, Z_MAX),
                #     id_kapal
                #     )
                # )
                self.velocities.append(Velocity(0,0,0,0))
            # Jenis item khusus
            else:
                self.positions.append(Position(
                    rnd(1, kapals[id_kapal_int].x_max_khusus + 1),
                    rnd(1, kapals[id_kapal_int].y_max_khusus + 1),
                    rnd(1, Z_MAX + 1),
                    id_kapal
                    )
                )
                # self.velocities.append(Velocity(
                #     rnd(-kapals[id_kapal_int].x_max_khusus, kapals[id_kapal_int].x_max_khusus),
                #     rnd(-kapals[id_kapal_int].y_max_khusus, kapals[id_kapal_int].y_max_khusus),
                #     rnd(-Z_MAX, Z_MAX),
                #     id_kapal
                #     )
                # )
                self.velocities.append(Velocity(0,0,0,0))
    def __str__(self):
        s = "Positions: \n"
        for pos in self.positions:
            s += str(pos)
            s += "\n"
    
        s += "\nVelocities:\n"
        for vel in self.velocities:
            s += str(vel)
            s += "\n"
        
        s += "\nFitness: " + self.fitness
        s += "\nPersonal Best: " + self.pb
        s += "\nGlobal Best: " + self.gb
        
        return s + "\n"
   
    def calculateFitness(self):
        fitness = 0
        
        
        # Biaya rute kapal
        for kapal in self.kapals:
           fitness += kapal.biaya
        
        
        # Inisialisasi barang di kapal
        kapal_weight = []
        kapal_items = []
        item_positions = []
        for i in range(len(self.kapals)):
            kapal_weight.append(0)
            kapal_items.append([])
            item_positions.append([])
        
        for i in range(len(items)):
            id_kapal_int = math.floor(self.positions[i].id_kapal)
            
            # Jika item tidak masuk manapun
            if id_kapal_int == len(self.kapals):
                total_route = 0
                for row in ROUTE:
                    for val in row:
                        total_route += val
                fitness += self.items[i].bobot * PENALTY * total_route
                
            # Masuk kapal tertentu
            else:
                if self.items[i].tujuan != self.kapals[id_kapal_int].rute[0]:  
                    kapal_weight[id_kapal_int] += self.items[i].bobot
                    kapal_items[id_kapal_int].append(self.items[i])
                    item_positions[id_kapal_int].append(self.positions[i])
                
                
        # Cek maksimal bobot
        for i in range(len(self.kapals)):
            if self.kapals[i].bobot_max < kapal_weight[i]:
                fitness = INF
                
                
        # Simulasikan pergerakan setiap kapal
        for i in range(len(self.kapals)):
            for j in range(len(self.kapals[i].rute) - 1):
                fr = self.kapals[i].rute[j]
                to = self.kapals[i].rute[j+1]
                dis = ROUTE[fr][to]
                
                # Iterasi barang
                for k in range(len(kapal_items[i]) - 1, -1, -1):
                    fitness += kapal_items[i][k].bobot * kapal_items[i][k].biaya_per_ton * dis
                    
                    # Barang sampai
                    if kapal_items[i][k].tujuan == to:
                        # Cek apakah ada barang di atasnya
                        xpop = math.floor(item_positions[i][k].x)
                        ypop = math.floor(item_positions[i][k].y)
                        zpop = item_positions[i][k].z
                        
                        for l in range(len(kapal_items[i])):
                            x = math.floor(item_positions[i][l].x)
                            y = math.floor(item_positions[i][l].y)
                            z = item_positions[i][l].z
                            
                            if x == xpop and y == ypop and z > zpop:
                                fitness += kapal_items[i][l].bobot * kapal_items[i][l].biaya_per_ton
                    
                        kapal_items[i].pop(k)
                        item_positions[i].pop(k)
                        
        return fitness

    
        
# main

# Kapals
kapals_data = [
    # [1, "Kapal 1", 50, 5, 10, 3, 4, [1, 3, 4, 2], 15, 15000],
    # [2, "Kapal 2", 60, 7, 20, 1, 5, [1, 2, 4, 3], 14, 14000],
    # [3, "Kapal 3", 60, 6, 10, 3, 4, [1, 4, 3, 2], 15, 15000]
    [1, "Kapal 1", 50000, 1, 1, 1, 1, [1, 3, 4, 2], 15, 15000],
    [2, "Kapal 2", 60000, 1, 1, 1, 1, [1, 2, 4, 3], 14, 14000],
    [3, "Kapal 3", 60000, 1, 1, 1, 1, [1, 4, 3, 2], 15, 15000]
]

kapals = []

for data in kapals_data:
    kapal = Kapal(*data)
    kapals.append(kapal)

# Mencetak informasi setiap kapal dalam array
for kapal in kapals:
    print(kapal)
print()



# Items
items_data = [
    [1, "xx1", "Umum", 10, 1000, 1],
    [2, "xx2", "Umum", 20, 1000, 2],
    [3, "xx3", "Khusus", 15, 1500, 3],
    [4, "xx4", "Umum", 10, 1000, 1],
    [5, "xx5", "Khusus", 20, 1500, 2],
    [6, "xx6", "Umum", 10, 1000, 1],
    [7, "xx7", "Umum", 15, 1000, 2],
    [8, "xx8", "Umum", 8, 1000, 3],
    [9, "xx9", "Umum", 5, 1000, 2],
    [10, "xx10", "Umum", 7, 1000, 1],
    [11, "xx11", "Umum", 8, 1000, 2],
    [12, "xx12", "Umum", 10, 1000, 1],
    [13, "xx13", "Umum", 20, 1000, 2],
    [14, "xx14", "Khusus", 15, 1500, 3],
    [15, "xx15", "Umum", 10, 1000, 1],
    [16, "xx16", "Khusus", 20, 1500, 2],
    [17, "xx17", "Umum", 10, 1000, 1],
    [18, "xx18", "Umum", 15, 1000, 2],
    [19, "xx19", "Umum", 8, 1000, 3],
    [20, "xx20", "Umum", 5, 1000, 2],
    [21, "xx21", "Umum", 7, 1000, 1],
    [22, "xx22", "Umum", 8, 1000, 2],
    [23, "xx23", "Umum", 10, 1000, 1],
    [24, "xx24", "Umum", 20, 1000, 2],
    [25, "xx25", "Khusus", 15, 1500, 3],
    [26, "xx26", "Umum", 10, 1000, 1],
    [27, "xx27", "Khusus", 20, 1500, 2],
    [28, "xx28", "Umum", 10, 1000, 1],
    [29, "xx29", "Umum", 15, 1000, 2],
    [30, "xx30", "Umum", 8, 1000, 3],
    [31, "xx31", "Umum", 5, 1000, 2],
    [32, "xx32", "Umum", 7, 1000, 1],
    [33, "xx33", "Umum", 8, 1000, 2],
    [34, "xx34", "Umum", 10, 1000, 1],
    [35, "xx35", "Umum", 20, 1000, 2],
    [36, "xx36", "Khusus", 15, 1500, 3],
    [37, "xx37", "Umum", 10, 1000, 1],
    [38, "xx38", "Khusus", 20, 1500, 2],
    [39, "xx39", "Umum", 10, 1000, 1],
    [40, "xx40", "Umum", 15, 1000, 2]
]

items = []

for data in items_data:
    item = Item(*data)
    items.append(item)

# Mencetak informasi setiap item dalam array
for item in items:
    print(item)
print()



# Generate particle
particles = []
for i in range(PARTICLE_COUNT):
    particles.append(Particle(items, kapals))

w = 0.9
w_step = -0.005
same_gb_limit = 5
gb_list = []
iter = 0

# Iteration
while True:
    # Hitung fitness
    for i in range(len(particles)):
        particles[i].fitness = particles[i].calculateFitness()
        # print(f"Particle {i}: {particles[i].fitness}")
        
        if iter == 0:
            particles[i].pb = particles[i].fitness
            particles[i].pb_pos = particles[i].positions
            particles[i].gb = particles[i].fitness
            particles[i].gb_pos = particles[i].positions
        elif particles[i].pb > particles[i].fitness:
            particles[i].pb = particles[i].fitness
            particles[i].pb_pos = particles[i].positions

    
    # Tentukan global best baru
    max_gb = particles[0].gb
    max_gb_pos = particles[0].gb_pos
    
    for i in range(len(particles)):
        if particles[i].fitness < max_gb:
            max_gb = particles[i].fitness
            max_gb_pos = particles[i].positions
            
    for i in range(len(particles)):
        particles[i].gb = max_gb
        particles[i].gb_pos = max_gb_pos
        
        
    # Update velocity
    for i in range(len(particles)):
        for j in range(len(particles[i].velocities)):        
            vx = particles[i].velocities[j].x
            vy = particles[i].velocities[j].y
            vz = particles[i].velocities[j].z
            vid = particles[i].velocities[j].id_kapal
            
            c1 = 2
            c2 = 2
            
            vx = w * rnd(0,1) * vx + c1 * rnd(0,1) * (particles[i].pb_pos[j].x - particles[i].positions[j].x) + c2 * rnd(0, 1) * (particles[i].gb_pos[j].x - particles[i].positions[j].x)
            vy = w * rnd(0,1) * vy + c1 * rnd(0,1) * (particles[i].pb_pos[j].y - particles[i].positions[j].y) + c2 * rnd(0, 1) * (particles[i].gb_pos[j].y - particles[i].positions[j].y)
            vz = w * rnd(0,1) * vz + c1 * rnd(0,1) * (particles[i].pb_pos[j].z - particles[i].positions[j].z) + c2 * rnd(0, 1) * (particles[i].gb_pos[j].z - particles[i].positions[j].z)
            vid = w * rnd(0,1) * vid + c1 * rnd(0,1) * (particles[i].pb_pos[j].id_kapal - particles[i].positions[j].id_kapal) + c2 * rnd(0, 1) * (particles[i].gb_pos[j].id_kapal - particles[i].positions[j].id_kapal)
            
            particles[i].velocities[j].x = vx
            particles[i].velocities[j].y = vy
            particles[i].velocities[j].z = vz
            particles[i].velocities[j].id_kapal = vid
            
            
    # Update position
    for i in range(len(particles)):
        for j in range(len(particles[i].positions)):
            px = particles[i].positions[j].x
            py = particles[i].positions[j].y
            pz = particles[i].positions[j].z
            pid = particles[i].positions[j].id_kapal
            
            px += particles[i].velocities[j].x
            py += particles[i].velocities[j].y
            pz += particles[i].velocities[j].z
            pid += particles[i].velocities[j].id_kapal
            
            pid = max(0, min(pid, len(kapals)))
            pid_int = math.floor(pid)
            
            if pid_int != len(kapals):
                if particles[i].items[j].jenis == "Umum":
                    px = max(1, min(px, kapals[pid_int].x_max_umum))
                    py = max(1, min(py, kapals[pid_int].y_max_umum))
                else:
                    px = max(1, min(px, kapals[pid_int].x_max_khusus))
                    py = max(1, min(py, kapals[pid_int].y_max_khusus))
            
            particles[i].positions[j].x = px
            particles[i].positions[j].y = py
            particles[i].positions[j].z = pz
            particles[i].positions[j].id_kapal = pid
    
    print("Iteration " + str(iter) + ": " + str(max_gb))
    gb_list.append(max_gb)
    
    if iter >= same_gb_limit - 1:
        if gb_list[iter-same_gb_limit + 1] == gb_list[iter]:
            break

    w = w - w_step
    iter += 1
        
