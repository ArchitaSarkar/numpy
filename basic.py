import numpy as np
a=np.array([1,2,3])
print(a)
print(type(a))

#2d and 3d
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(type(c))

# float type
d=np.array([1,2,3],dtype=float)
print(d)

# bool type
e=np.array([0,2,3],dtype=bool)
print(e)

f=np.array([1,2,3],dtype=int)
print(f)
print(e)

# complex type
g=np.array([1,2,3],dtype=complex)
print(g)

# np.arrange
h=np.arange(10)
print(h)

# reshape
i=np.arange(1,11).reshape(2,5)
print(i)

print(np.ones((3,4)))
print(np.zeros((3,4)))


print(np.linspace(-10,10,11))
print(np.identity(3))


# ndim

print(a.ndim) 
print(b.ndim)
print(c.ndim)

print(a.shape)
print(b.shape)
print(c.shape)

print(a.size)
print(b.size)
print(c.size)

print(a.itemsize)
print(b.itemsize)
print(c.itemsize)
print(d.itemsize)
print(e.itemsize)
print(f.itemsize)

print(a.astype(np.int32))
print(b.astype(np.int32))
print(c.astype(np.int32))
print(d.astype(np.int32))
print(e.astype(np.int32))
print(f.astype(np.int32))


print("\n")
#Array operation 

a1=[[2,4,6],
    [4,6,8],
    [6,8,10]]

print("a1",a1)
# arithmetic
print(a1*2)
print("\n")
