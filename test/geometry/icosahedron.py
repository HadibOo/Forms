from forms.geometry import icosahedron

reload( icosahedron )


x = icosahedron.Icosahedron().mesh()
y = icosahedron.Sierpinski().generate()

print x
print y

# Result: [nt.Transform(u'pSolid1'), nt.PolyPlatonicSolid(u'polyPlatonicSolid1')]
# Result: [nt.Transform(u'Sierpinski_Iteration_1')]

