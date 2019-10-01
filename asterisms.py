from astroplan import FixedTarget

# Summer Triangle
altair = FixedTarget.from_name('Altair')
vega = FixedTarget.from_name('Vega')
deneb = FixedTarget.from_name('Deneb')
summer_triangle = (altair, vega, deneb)

# Big Dipper
alioth = FixedTarget.from_name('Alioth')
mizar = FixedTarget.from_name('Mizar')
alkaid = FixedTarget.from_name('Alkaid')
megrez = FixedTarget.from_name('Megrez')
phecda = FixedTarget.from_name('Phecda')
merak = FixedTarget.from_name('Merak')
dubhe = FixedTarget.from_name('Dubhe')
big_dipper = (alioth, mizar, alkaid, megrez, phecda, merak, dubhe)
