import astropy.units as u
from astroplan import Observer, FixedTarget
from astropy.coordinates import EarthLocation
from astropy.time import Time
from asterisms import vega, polaris

schoolyard_observatory_location = EarthLocation.from_geodetic(-87.8791*u.deg, 42.6499*u.deg, height=204*u.m)
schoolyard_observatory = Observer(location=schoolyard_observatory_location, name="Schoolyard Observatory",
                                  timezone="US/Central")

start_time = Time('2019-10-04 21:45:00')
end_time = Time('2019-10-04 23:45:00')

# Check sec(z) for each target and return target name with starting altitude and azimuth
def check_secz(target, start_time, end_time, secz_max=2.0):
    start_secz = schoolyard_observatory.altaz(start_time, target).secz
    end_secz = schoolyard_observatory.altaz(end_time, target).secz
    start_altaz = schoolyard_observatory.altaz(start_time, target)
    if start_secz < 2.0 or end_secz < 2.0:
        # print('{}: \tsec(z) < {} between {} and {}'.format(target.name, secz_max, start_time, end_time))
        return target.name, start_altaz.alt, start_altaz.az
    else:
        # print('\tsec(z) > {} between {} and {}'.format(secz_max, start_time, end_time))
        # return 'Too low', start_altaz.alt, start_altaz.az
        return '', '', ''


number_of_messier_objects = 110
messier_list = ('M',)*number_of_messier_objects
#  convert this tuple of numbers into the target list to check for visibility

target_list = (FixedTarget.from_name('M13'), FixedTarget.from_name('M31'), vega, polaris)

for target in target_list:
    name, altitude, azimuth = check_secz(target, start_time, end_time, secz_max=5.0)
#    if name != 'Too low':
    print('{}: Altitude, Azimuth = ({}, {}) at {}'.format(name, altitude, azimuth, start_time))

