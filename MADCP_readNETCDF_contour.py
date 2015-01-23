#============================================================================
# Contour and time series plots of moored ADCP U and V current data
# Reads netCDF data file using "NetCDFFile" function from Scientific.IO.NetCDF library
# Plots using the "pcolor" and "plot" plot functions in Matplotlib library.  

#  Created By:   Diana Cardoso, Bedford Institute of Oceangraphy
#                Diana.Cardoso@dfo-mpo.gc.ca
#		  
#============================================================================
#- Module imports:
import numpy as N
#import Scientific.IO.NetCDF as S
import matplotlib.pyplot as plt
import matplotlib.dates as pltdate
import numpy.ma as ma
from scipy.io import netcdf

#- Reading data from NetCDF file:

fileobj = netcdf.netcdf_file('MADCP_HUD2013021_1840_12556_3600_interpolated.nc', mode='r')
# print fileobj.history
# print fileobj.variables
t = fileobj.variables['time']
timeunits = fileobj.variables['time'].units
time = t[:].copy()

d= fileobj.variables['depth']
depthunits = fileobj.variables['depth'].units
depth = d[:].copy()

u = N.squeeze((fileobj.variables['u_1205'].data).astype(N.float64))
uunits = fileobj.variables['u_1205'].units

v = N.squeeze((fileobj.variables['v_1206'].data).astype(N.float64))
vunits = fileobj.variables['v_1206'].units

pgd= N.squeeze((fileobj.variables['PGd_1203'].data).astype(N.float64))
pgdunits = fileobj.variables['PGd_1203'].units

#- Close NetCDF file:
fileobj.close()

#- Remove bad bins (#22-40) and mask bad data:
uaatr=N.delete(u,N.arange(22, 40, 1),axis=1)
vaatr=N.delete(v,N.arange(22, 40, 1),axis=1)
depthar=N.delete(depth,N.arange(22, 40, 1))
pgdaatr=N.delete(pgd,N.arange(22, 40, 1),axis=1)

uaatrm=ma.masked_greater_equal(uaatr, 100)
vaatrm=ma.masked_greater_equal(vaatr, 100)

## - Make a contour plot of U:
plt.figure(figsize=(8, 11), dpi=100)
plt.subplot(3,1,1)
dn=pltdate.julian2num(time)
dd=pltdate.num2date(dn)
plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
plt.gca().xaxis.set_major_locator(pltdate.MonthLocator())
mymapf = plt.pcolor( dn, depthar,uaatrm.T, cmap=plt.cm.jet, vmin=-50, vmax=50)
plt.gcf().autofmt_xdate()
#print dd[0]
plt.gca().invert_yaxis()
plt.gca().xaxis.set_ticklabels([])
#plt.xlabel('Time [Month/Year]')
#plt.ylabel('Depth [' + depthunits + ']')
plt.setp(plt.gca().get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(plt.gca().get_yticklabels(), fontsize=10)
plt.title('ADCP Mooring #1840', fontsize=14)
cbar = plt.colorbar(mymapf, orientation='vertical') 
cbar.set_label('U [' + uunits + ']')

plt.subplot(3,1,2)
dn=pltdate.julian2num(time)
dd=pltdate.num2date(dn)
plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
plt.gca().xaxis.set_major_locator(pltdate.MonthLocator())
mymapf = plt.pcolor( dn, depthar,vaatrm.T, cmap=plt.cm.jet, vmin=-50, vmax=50)
plt.gcf().autofmt_xdate()
plt.gca().invert_yaxis()
plt.gca().xaxis.set_ticklabels([])
#plt.xlabel('Time [Month/Year]')
plt.ylabel('Depth [' + depthunits + ']')
plt.setp(plt.gca().get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(plt.gca().get_yticklabels(), fontsize=10)
cbar = plt.colorbar(mymapf, orientation='vertical') 
cbar.set_label('V [' + vunits + ']')

plt.subplot(3,1,3)
dn=pltdate.julian2num(time)
dd=pltdate.num2date(dn)
plt.gca().xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
plt.gca().xaxis.set_major_locator(pltdate.MonthLocator())
mymapf = plt.pcolor( dn, depthar,pgdaatr.T, cmap=plt.cm.jet, vmin=40, vmax=100)
plt.gcf().autofmt_xdate()
plt.gca().invert_yaxis()
plt.xlabel('Time [Month/Year]')
#plt.ylabel('Depth [' + depthunits + ']')
plt.setp(plt.gca().get_xticklabels(), fontsize=10,rotation=70) #rotation='vertical'
plt.setp(plt.gca().get_yticklabels(), fontsize=10)
cbar = plt.colorbar(mymapf, orientation='vertical') 
cbar.set_label('Percent Good [' + pgdunits + ']')

# - Call show and savefig:
plt.savefig('UVPGD1840-contour_test.png', orientation = 'tall')
plt.show()



