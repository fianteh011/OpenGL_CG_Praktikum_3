import numpy as np
from math import sin, cos, tan, pi


class Matrix(object):

    @staticmethod
    def Vec3(a, b, c):
        return np.array([a, b, c])

    @staticmethod
    def makeIdentity():
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeTranslation(x, y, z):
        return np.array([[1, 0, 0, x],
                         [0, 1, 0, y],
                         [0, 0, 1, z],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationX(winkel):
        c = cos(winkel)
        # print(c)
        s = sin(winkel)
        # print(s)
        return np.array([[1, 0, 0, 0],
                         [0, c, -s, 0],
                         [0, s, c, 0],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationY(winkel):
        c = cos(winkel)
        s = sin(winkel)
        return np.array([[c, 0, s, 0],
                         [0, 1, 0, 0],
                         [-s, 0, c, 0],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeRotationZ(winkel):
        c = cos(winkel)
        s = sin(winkel)
        return np.array([[c, -s, 0, 0],
                         [s, c, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makeScale(s):
        return np.array([[s, 0, 0, 0],
                         [0, s, 0, 0],
                         [0, 0, s, 0],
                         [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def makePerspective(angleOfView=60, aspectRatio=1, near=0.1, far=100):
        # Umwandlung in Bogenmass
        a = angleOfView * pi / 180  # => a = pi /3
        d = 1.0 / tan(a / 2)  # d = sqrt(3)
        r = aspectRatio
        b = (far + near) / (near - far)  # (100.1/-0.99)
        c = 2 * far * near / (near - far)  # -20.20200...
        return np.array([[d / r, 0, 0, 0],
                         [0, d, 0, 0],
                         [0, 0, b, c],
                         [0, 0, -1, 0]]).astype(float)

    @staticmethod
    def makeLook_at(eye, target, up):
        z = (eye - target) / (np.sqrt((eye - target).dot(eye - target)))
        x = np.cross(up, z)
        y = np.cross(z, x)
        a = -x.dot(eye)
        b = -y.dot(eye)
        c = -z.dot(eye)
        return np.array([[x[0], y[0], z[0], 0],
                         [x[1], y[1], z[1], 0],
                         [x[2], y[2], z[2], 0],
                         [a, b, c, 1]]).astype(float)

    @staticmethod
    def makeTranspose(matrix):
        t_matrix = matrix
        return np.transpose(t_matrix)

    @staticmethod
    def multiply(matrix1, matrix2):
        return np.dot(matrix1, matrix2, )

    @staticmethod
    def m_inverse(matrix):
        return np.linalg.inv(matrix)
