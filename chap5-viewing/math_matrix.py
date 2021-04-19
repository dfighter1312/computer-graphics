import numpy as np

class Proj:
    def __init__(self, load_identity=True, init_matrix=None):
        if load_identity:
            self.matr = np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        else:
            assert init_matrix != None, "Please input the initial matrix or set load_identity to True"
            self.matr = init_matrix

    def length(self, vect):
        return (vect ** 2).sum() ** (1/2)

    def normalize(self, vect):
        return vect / self.length(vect)

    def lookAt(self, eye_x, eye_y, eye_z, look_x, look_y, look_z, up_x, up_y, up_z):
        eye = np.array([eye_x, eye_y, eye_z])
        look = np.array([look_x, look_y, look_z])
        up = np.array([up_x, up_y, up_z])
        n = eye - look
        u = np.cross(up, n)
        v = np.cross(n, u)
        # Normalize vector
        n = self.normalize(n)
        u = self.normalize(u)
        v = self.normalize(v)

        d = [np.dot(-eye, u), np.dot(-eye, v), np.dot(-eye, n)]
        
        return np.array([
            [u[0], u[1], u[2], d[0]],
            [v[0], v[1], v[2], d[1]],
            [n[0], n[1], n[2], d[2]],
            [0, 0, 0, 1]
        ])

    def translate3d(self, x, y, z):
        return np.array([
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1]
        ])

    def scale3d(self, x_scale, y_scale, z_scale):
        return np.array([
            [x_scale, 0, 0, 0],
            [0, y_scale, 0, 0],
            [0, 0, z_scale, 0],
            [0, 0, 0, 1]
        ])

    def refect3d(self):
        return self.scale3d(-1, -1, -1)

    def rotate3d(self, angle, x, y, z):
        anrad = np.pi * angle / 180
        if z == 1.0 and x == 0.0 and y == 0.0:
            return np.array([
                [np.cos(anrad), -np.sin(anrad), 0, 0],
                [np.sin(anrad), np.cos(anrad), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
        elif x == 1.0 and y == 0.0 and z == 0.0:
            return np.array([
                [1,0,0,0],
                [0,np.cos(anrad), -np.sin(anrad),0],
                [0,np.sin(anrad), np.cos(anrad),0],
                [0,0,0,1]
            ])
        elif x == 0.0 and y == 1.0 and z == 0.0:
            return np.array([
                [1,0,0,0],
                []
            ])

    def shear3d(self, a=0, b=0, c=0, d=0, e=0, f=0):
        return np.array([
            [1, a, b, 0],
            [c, 1, d, 0],
            [e, f, 1, 0],
            [0, 0, 0, 1]
        ])

    def identity3d(self):
        return np.array([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])

    def transform_matr(self, *trans):
        M = trans[0]
        if len(trans) > 1:
            for i in range(1, len(trans)):
                M = M @ trans[i]
        self.matr = M
        return True
    
    def result_vect(self, vect):
        return self.matr @ vect

    def isEqualMatr(self, other):
        return np.allclose(self.matr, np.array(other).reshape(4, 4, order='F'))