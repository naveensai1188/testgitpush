 np.linspace(3,5,30)
print(y)
def add(x,y):
  return np.sin(np.sqrt(x**2 + y**2))

z = add(x,y

ax = plt.axes(projection='3d')
print(ax.plot3D(x,y,z))