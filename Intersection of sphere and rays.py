
# coding: utf-8

# In[81]:


import math
class Vector:
    def __init__(self,x = None,y = None,z =None):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return "({}, {}, {})".format(self.x,self.y,self.z)
    def module(self):
        return math.sqrt(self.x**2+self.y**2+self.y**2)
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y+self.z*other.z
    def __sub__(self, other):
        x = self.x - other.x
        y = self.x - other.y
        z  = self.z - other.z
        return Vector(x,y,z)



class SphereRayIntersection:
    def __init__(self, ray_start : [int, int, int],ray_direction : [int, int, int],sphere_center : [int, int, int],sphere_r: int):
        self.ray_start = Vector(ray_start[0],  ray_start[1], ray_start[2])
        self.ray_direction = Vector(ray_direction[0], ray_direction[1], ray_direction[2]) 
        self.sphere_center = Vector(sphere_center[0], sphere_center[1], sphere_center[2] )
        self.r = sphere_r

    def Intersect_long(self):
        vray = self.ray_direction - self.ray_start
        v02c = self.sphere_center - self.ray_start
        
        projection = v02c*vray/vray.module()
        d = math.sqrt(v02c.module()**2-projection**2)
        if d >self.r:
            return []
        elif d == self.r:
            return [projection]
        else:
            intersect = math.sqrt(self.r**2-d**2)
            return [projection+intersect,projection-intersect, ]
    def intersect_coordinate(self):
        vray = self.ray_direction - self.ray_start
        v02c = self.sphere_center - self.ray_start

        projection = v02c*vray/vray.module()
        d = math.sqrt(v02c.module()**2-projection**2)
        if d >self.r:
            return []
        elif d == self.r:
            ratio = projection/vray.module()
            return [(vray.x*ratio, vray.y*ratio, vray.y*ratio)] 
        else:
            intersect = math.sqrt(self.r**2-d**2)
            ratio1 = (projection+intersect)/vray.module()
            ratio2 = (projection-intersect)/vray.module()
            return [(vray.x*ratio1, vray.y*ratio1, vray.y*ratio1,),(vray.x*ratio2, vray.y*ratio2, vray.y*ratio2,)] 
if __name__ == "__main__":     
    center = [1,1,1]
    origin = [0,0,0]
    direction = [1,0,0]
    R = 3
    print(SphereRayIntersection(origin,direction,center,R).Intersect_long())
    print(SphereRayIntersection(origin,direction,center,R).intersect_coordinate())

