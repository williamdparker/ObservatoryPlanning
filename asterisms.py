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

# Little Dipper
polaris = FixedTarget.from_name('Polaris')
kochab = FixedTarget.from_name('Kochab')
pherkad = FixedTarget.from_name('Pherkad')
yildun = FixedTarget.from_name('Yildun')
epsilon_UMi = FixedTarget.from_name('eps UMi')
zeta_UMi = FixedTarget.from_name('zet UMi')
eta_UMi = FixedTarget.from_name('eta UMi')
little_dipper = (polaris, yildun, epsilon_UMi, zeta_UMi, eta_UMi, pherkad, kochab)



