class Plane:
    def __init__(normal, point):
        self.normal = normal
        self.point = point
        self.normalLength = (normal[1]**2 + normal[2]**2 + normal[3]**2) ** (1/2)
        self.d = -dot(normal, point)
        self.distance = -self.d / self.normalLength

    def intersect(line):
        """
        Fine the intersect point.
        Parameters:
            line: (p, v) In parametric form.
        Return the intersection point.
        """
        p, v = line
        dot1 = dot(self.normal, p)
        dot2 = dot(self.normal, v)
        
        # If denominator=0, no intersect
        if(dot2 == 0):
            return (None, None, None)
        t = -(dot1 + self.d) / dot2

        res = list()
        res.append(p[0] + v[0]*t)
        res.append(p[1] + v[1]*t)
        res.append(p[2] + v[2]*t)
        return res

def dot(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

def length(vector):
    return (vector[1]**2 + vector[2]**2 + vector[3]**2) ** (1/2)