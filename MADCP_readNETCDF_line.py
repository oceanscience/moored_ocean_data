#============================================================================
# Time series plots of moored ADCP U and V current data
# Reads netCDF data file using "netcdf" function from scipy.io library
# Plots using the "plot" function in Matplotlib library.  

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

# Plot Time series of U and V for certain bins
fig = plt.figure(figsize=(9, 14), dpi=100)
ax1 = fig.add_subplot(811)
dn=pltdate.julian2num(time)
dd=pltdate.num2date(dn)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[21,:], 'b-')
plt.plot(dn,vaatrm.T[21,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
plt.title("ADCP, Mooring #1840", fontsize=14, fontweight='bold')
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'18 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(812)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[18,:], 'b-')
plt.plot(dn,vaatrm.T[18,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'42 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(813)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[15,:], 'b-')
plt.plot(dn,vaatrm.T[15,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'66 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(814)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[12,:], 'b-')
plt.plot(dn,vaatrm.T[12,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
plt.ylabel("Velocity (cm/s)")
ax1.axes.get_xaxis().set_visible(False)
#plt.xlabel('dn [' + dnunits + ']')
plt.text(dn[7500],-57,'90 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(815)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[9,:], 'b-')
plt.plot(dn,vaatrm.T[9,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
#plt.xlabel('Time [' + timeunits + ']')
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'114 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(816)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[6,:], 'b-')
plt.plot(dn,vaatrm.T[6,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
#plt.xlabel('Time [' + timeunits + ']')
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'138 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(817)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[3,:], 'b-')
plt.plot(dn,vaatrm.T[3,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
#plt.xlabel('Time [' + timeunits + ']')
ax1.xaxis.set_ticklabels([])
plt.text(dn[7500],-57,'162 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_yticklabels(), fontsize=10)

ax1 = fig.add_subplot(818)
ax1.xaxis.set_major_formatter(pltdate.DateFormatter('%m/%y'))
ax1.xaxis.set_major_locator(pltdate.MonthLocator())
plt.plot(dn,uaatrm.T[0,:], 'b-')
plt.plot(dn,vaatrm.T[0,:], 'r-') 
plt.gcf().autofmt_xdate()
ax1.set_ylim(-80, 80)
plt.legend(['U','V'], loc=3,ncol=2, fontsize=10)
#plt.ylabel("Velocity (cm/s)")
plt.xlabel('Time (Month/Year)')
plt.text(dn[7500],-57,'186 m', fontsize=14, fontweight='bold')
plt.setp(ax1.get_xticklabels(), fontsize=10) #rotation='vertical'
plt.setp(ax1.get_yticklabels(), fontsize=10)
# - Call show and savefig:
plt.savefig('UV1840-Line.png')
plt.show()

