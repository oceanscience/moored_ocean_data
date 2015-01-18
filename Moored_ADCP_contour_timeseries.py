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
import Scientific.IO.NetCDF as S
import matplotlib.pyplot as plt
import numpy.ma as ma

#- Reading data from NetCDF file:

fileobj = S.NetCDFFile('MADCP_HUD2013021_1840_12556_3600_interpolated.nc', mode='r')

time = fileobj.variables['time'].getValue() #[0,:,:]
timeunits = fileobj.variables['time'].units
depth = fileobj.variables['depth'].getValue()
depthunits = fileobj.variables['depth'].units
u = fileobj.variables['u_1205'].getValue()
uunits = fileobj.variables['u_1205'].units
v = fileobj.variables['v_1206'].getValue()
vunits = fileobj.variables['v_1206'].units
fileobj.close()

#- Create Arrays:

ua=N.array(u,dtype='d')
va=N.array(v,dtype='d')
deptha=N.array(depth,dtype='d')
timea=N.array(time,dtype='d')

print N.shape(ua)
print N.shape(deptha)
print N.shape(timea)
print N.ndim(ua)
uaa=N.squeeze(ua)  
uaat=N.transpose(uaa)
vaa=N.squeeze(va)
vaat=N.transpose(vaa)

#- Remove bad bins (#22-40) and mask bad data:
uaatr=N.delete(uaat,N.arange(22, 40, 1),axis=0)
vaatr=N.delete(vaat,N.arange(22, 40, 1),axis=0)
depthar=N.delete(deptha,N.arange(22, 40, 1),axis=0)

uaatrm=ma.masked_greater_equal(uaatr, 100)
vaatrm=ma.masked_greater_equal(vaatr, 100)

print N.shape(uaatr)
print N.shape(depthar)
print depthar
 
# - Make a contour plot of U:
plt.figure()
mymapf = plt.pcolor( timea, depthar,uaatrm, cmap=plt.cm.jet, vmin=-50, vmax=50)
plt.gca().invert_yaxis()
plt.xlabel('Time [' + timeunits + ']')
plt.ylabel('Depth [' + depthunits + ']')
plt.title('ADCP, Mooring #1840 cruise Hudson2013021: July 2013 - July 2014', fontsize=14)
cbar = plt.colorbar(mymapf, orientation='horizontal') 
cbar.set_label('U [' + uunits + ']')

# - Call show and savefig:
plt.savefig('U1840-contour.png')
plt.show()

# - Make a contour plot of V:
plt.figure()
mymapf = plt.pcolor( timea, depthar,vaatrm, cmap=plt.cm.jet, vmin=-50, vmax=50)
plt.gca().invert_yaxis()
plt.xlabel('Time [' + timeunits + ']')
plt.ylabel('Depth [' + depthunits + ']')
plt.title('ADCP, Mooring #1840 cruise Hudson2013021: July 2013 - July 2014', fontsize=14)
cbar = plt.colorbar(mymapf, orientation='horizontal') 
cbar.set_label('V [' + vunits + ']')

# - Call show and savefig:
plt.savefig('V1840-contour.png')
plt.show()

# Plot Time series of U and V for certain bins
fig = plt.figure()
ax1 = fig.add_subplot(411)
plt.plot(timea,uaatrm[20,:], 'b-')
plt.plot(timea,vaatrm[20,:], 'r-') 
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
plt.legend(['U','V'], loc=3,ncol=2, fontsize=10)
plt.title("ADCP, Mooring #1840 cruise Hudson2013021: July 2013 - July 2014", fontsize=14, fontweight='bold')
ax1.axes.get_xaxis().set_visible(False)
plt.text(timea[7500],-57,'34 m', fontsize=14, fontweight='bold')

ax1 = fig.add_subplot(412)
plt.plot(timea,uaatrm[15,:], 'b-')
plt.plot(timea,vaatrm[15,:], 'r-') 
ax1.set_ylim(-80, 80)
plt.ylabel("Velocity (cm/s)")
ax1.axes.get_xaxis().set_visible(False)
plt.text(timea[7500],-57,'74 m', fontsize=14, fontweight='bold')

ax1 = fig.add_subplot(413)
plt.plot(timea,uaatrm[10,:], 'b-')
plt.plot(timea,vaatrm[10,:], 'r-') 
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
plt.text(timea[7500],-57,'114 m', fontsize=14, fontweight='bold')

ax1 = fig.add_subplot(414)
plt.plot(timea,uaatrm[5,:], 'b-')
plt.plot(timea,vaatrm[5,:], 'r-') 
ax1.set_ylim(-80, 80)
#plt.ylabel("Velocity (cm/s)")
plt.xlabel('Time [' + timeunits + ']')
plt.text(timea[7500],-57,'154 m', fontsize=14, fontweight='bold')

# - Call show and savefig:
plt.savefig('UV1840-timeseries.png')
plt.show()

