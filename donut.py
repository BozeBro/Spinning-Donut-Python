import os, math, itertools, time

"""
BASIC GUIDELINE FOR TERMINAL | Works with all terminals
os.system("cls" if os.name == "nt" else "clear")
print(*cols, sep="", end="")
"""
rows, cols = os.get_terminal_size()
R1, R2 = 1.0, 2.0
K2 = 5
offsety = 0.0
# K1 = rows * K2 * 3 / (8 * (R1 + R2)) + offsety
K1 = 200
A, B = 1.0, 1.0
theta_spacing = 10
theta_increment = math.pi / theta_spacing
phi_spacing = 31
phi_increment = math.pi / phi_spacing
"""
for i in zbuffer:
    print(cols, rows)
    print(*i, sep="", end="")
    break
quit()
"""
while True:
    A += 0.07
    B += 0.03
    sinA, cosA = math.sin(A), math.cos(A)
    sinB, cosB = math.sin(B), math.cos(B)
    output = [[" " for _ in range(rows)] for _ in range(cols)]
    zbuffer = [[0 for _ in range(rows)] for _ in range(cols)]
    for th, ph in itertools.product(range(theta_spacing), range(phi_spacing)):
        theta, phi = th * theta_increment, ph * phi_increment
        sintheta, costheta = math.sin(theta), math.cos(theta)
        sinphi, cosphi = math.sin(phi), math.cos(phi)
        # precomputations
        S, O, M, P = (
            sinA * sintheta,
            cosphi * sinB,
            R2 + R1 * costheta,
            R1 * cosA * sintheta,
        )
        x, y, z = (
            M * (cosB * cosphi + sinA * sinB * sinphi) - P * sinB,
            M * (O - cosB * sinA * sinphi) + P * cosB,
            K2 + M * cosA * sinphi + R1 * S,
        )
        ooz = 1 / z
        xp, yp = int(rows / 2 + K1 * ooz * x), int(cols / 2 - K1 * ooz * y)
        L = (
            O * costheta
            - cosA * costheta * sinphi
            - S
            + cosB * (cosA * sintheta - costheta * sinA * sinphi)
        )
        # print(xp, yp, rows, cols)
        if L > 0 and 0 <= xp < rows and 0 <= yp < cols:
            # print(xp, yp, rows, cols)
            if ooz > zbuffer[yp][xp]:
                zbuffer[yp][xp] = ooz
                output[yp][xp] = ".,-~:;=!*#$@"[int(L * 8)]
    os.system("cls" if os.name == "nt" else "clear")
    for col in output:
        print(*col, sep="")
    time.sleep(0.001)
    # print(chr(27) + "[2J")
    # print(output)