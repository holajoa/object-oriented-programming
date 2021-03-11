def test_ufl():
    import ufl
    argyris = ufl.FiniteElement("Argyris", degree=6, cell=ufl.triangle)
