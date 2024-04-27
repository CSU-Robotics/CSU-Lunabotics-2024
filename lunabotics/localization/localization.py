import math
import time

P = (1, 1)
Q = (2, 9)
R = (5, 9)


# Only needs to be called a single time at the beginning of the robot operation
# calculates some specific values based on where the beacons are positioned
def setup():
    global PQ, PR, QR, aPQR
    PQ = math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
    PR = math.sqrt((P[0]-R[0])**2 + (P[1]-R[1])**2)
    QR = math.sqrt((Q[0]-R[0])**2 + (Q[1]-R[1])**2)
    aPQR = math.acos((PR**2-PQ**2-QR**2)/(-2*PQ*QR))


# function to traingulate based on angles between the light sources
def localize(theta, phi):
    ab = 2*math.pi-aPQR-theta-phi
    b = math.atan(
        1/((QR*math.sin(phi))/(PQ*math.sin(theta)*math.sin(ab)) + 1/math.tan(ab)))
    print(math.degrees(b))
    if (b < 0):
        b += math.pi
    print(math.degrees(b))
    x = QR * math.sin(math.pi-theta-b) / math.sin(theta)
    A = (R[0] + x * math.cos(math.pi - b), 0)
    A = (A[0], R[1] - x * math.sin(math.pi - b))
    return A


# main function really just used for testing at this point
if __name__ == '__main__':
    # theta = 90-63.43494882
    # phi = 90
    theta = 90-69.44395478
    phi = 90 - theta
    setup()
    # start = time.time()
    A = localize(math.radians(theta), math.radians(phi))
    # end = time.time()
    # print(str(end-start))
    print(A)
