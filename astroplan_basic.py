import astropy.units as u
from astroplan import Observer, FixedTarget
from astropy.coordinates import EarthLocation
from astropy.time import Time

schoolyard_observatory_location = EarthLocation.from_geodetic(-87.8791*u.deg, 42.6499*u.deg, 204*u.m)
schoolyard_observatory = Observer(location=schoolyard_observatory_location, name="Schoolyard Observatory",
                                  timezone="US/Central")

start_time = Time('2019-09-30 21:45:00')
end_time = Time('2019-09-30 23:45:00')


def check_secz(target, start_time, end_time, secz_max=2.0):
    start_secz = schoolyard_observatory.altaz(start_time, target).secz
    end_secz = schoolyard_observatory.altaz(end_time, target).secz
    if start_secz < 2.0 or end_secz < 2.0:
        print('{}: \tsec(z) < {} between {} and {}'.format(target.name, secz_max, start_time, end_time))
        return 1
    else:
        # print('\tsec(z) > {} between {} and {}'.format(secz_max, start_time, end_time))
        return 0


number_of_messier_objects = 110
messier_list = ('M',)*number_of_messier_objects
#  convert this list of numbers into the target list to check for visibility

target_list = (FixedTarget.from_name('M13'), FixedTarget.from_name('M31'))

for target in target_list:
    check_secz(target, start_time, end_time, secz_max=1.5)


