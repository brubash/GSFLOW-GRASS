#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:26:24 2017

@author: gcng
modified by brubash for GSFLOW v.1.2.2
"""

# plot_gsflow_csv.m
#
# List of StatVarNames: see Table 12 of GSFLOW manual and
#  create_table_gsflowcsv.m

import sys
import platform
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import GSFLOWcsvTable as gvar  # all variable names, units, and descriptions
import time

if platform.system() == 'Linux':
    slashstr = '/'
else:
    slashstr = '\\'

# add path containing readSettings.py
sys.path.append('..' + slashstr + 'Run')

# Read in user-specified settings
from readSettings import Settings
# Set input file
if len(sys.argv) < 2:
    settings_input_file = 'settings.ini'
    print 'Using default input file: ' + settings_input_file
else:
    settings_input_file = sys.argv[1]
    print 'Using specified input file: ' + settings_input_file
Settings = Settings(settings_input_file)

#%% *** SET THE FOLLOWING *****************************************************

# GSFLOW v1.2.2 gsflow.csv variables:
# Date,StreamOut_Q,HortSroff2Stream_Q,DunnSroff2Stream_Q,Interflow2Stream_Q,
# Stream2Unsat_Q,StreamExchng2Sat_Q,Canopy_S,SnowPweqv_S,Imperv_S,Dprst_S,
# Cap_S,Grav_S,Unsat_S,Sat_S,UnsatStream_S,Lake_S,Stream_S,Precip_Q,NetBoundaryFlow2Sat_Q,
# NetWellFlow_Q,BoundaryStreamFlow_Q,CanopyEvap_Q,SnowEvap_Q,ImpervEvap_Q,DprstEvap_Q,
# CapET_Q,SwaleEvap_Q,UnsatET_Q,SatET_Q,LakeEvap_Q,DunnInterflow2Lake_Q,HortSroff2Lake_Q,
# Lake2Unsat_Q,LakeExchng2Sat_Q,SoilDrainage2Unsat_Q,Sat2Grav_Q,RechargeUnsat2Sat_Q,
# Infil2Soil_Q,KKITER

# *** enter variables to plot (see list in gsflow_csv_table.py):
PlotVar = []
PlotVar.append('StreamOut_Q')           # Previously 'basinstrmflow', Volumetric flow rate of streamflow leaving modeled region
PlotVar.append('RechargeUnsat2Sat_Q')   # Previously 'uzf_recharge', Volumetric flow rate of recharge from the unsaturated zone to the saturated zone
# In previous versions of GSFLOW the following two output variables were combined as 'basinsroff'.
PlotVar.append('DunnSroff2Stream_Q')    # Volumetric flow rate of Dunnian runoff to streams
PlotVar.append('HortSroff2Stream_Q')    # Volumetric flow rate of Hortonian runoff to streams
# not in gsflow.csv: PlotVar.append('SatDisch2Stream_Q')     # Previously 'gwflow2strms', Volumetric flow rate of ground-water discharge to streams
PlotVar.append('Interflow2Stream_Q')    # Previously 'basininterflow' slow + fast, was slow only
# not in gsflow.csv: PlotVar.append('Stream2Sat_Q')          # Previously 'streambed_loss', Volumetric flow rate of stream leakage to unsaturated and saturated zones
PlotVar.append('Precip_Q')              # Previously 'basinppt', Volumetric flow rate of precipitation on modeled region
# not in gsflow.csv: PlotVar.append('ActualET_Q')            # Previously 'basinactet', Volumetric flow rate of actual evapotranspiration from HRUs

# *** save figure to this file
savefigfile = 'fig.png'

#%% *** CHANGE FILE NAMES IF NEEDED *******************************************
# (default is to use entries from Settings File)
gsflow_csv_fil = Settings.PRMSoutput_dir + slashstr + 'gsflow.csv'  # gsflow time series data
plot_title = Settings.PROJ_CODE

#  *** CHANGE BASIN AREA AS NEEDED (SEE prms.out FILE FOR AREA IN [acres]) ***
# (default is to use entries from Settings File)
HRUfil = Settings.GISinput_dir + slashstr + 'HRUs.txt'
HRUdata = pd.read_csv(HRUfil)
HRUarea = HRUdata['hru_area']  # [acre]
basin_area = sum(HRUarea) * 4046.85642  # acre -> m2


#%%

# Create figure
fig = plt.figure(figsize=(12,6))
ax1 = plt.subplot(1,1,1)
ax2 = ax1.twinx()

while True:
    # loop over time
    #time.sleep(2) # wait 10 seconds

    # make sure basinppt and basinacet are listed last, because of twin y-axis
    PlotVar0 = PlotVar[:]
    ctr = 1
    ctr_end = len(PlotVar)
    for ii in range(len(PlotVar)):
        if (PlotVar[ii] == 'Precip_Q') or (PlotVar[ii] == 'ActualET_Q'):
            PlotVar0[ctr_end-1] = PlotVar[ii]
            ctr_end = ctr_end - 1
        else:
            PlotVar0[ctr-1] = PlotVar[ii]
            ctr = ctr + 1
    PlotVar = PlotVar0[:]

    descr = []
    unit_prev = []
    for jj in range(len(PlotVar)):
        for ii in range(len(gvar.varname)):
            if gvar.varname[ii] == PlotVar[jj]:
                unit = gvar.unit[ii]
                descr.append(gvar.descr[ii])
                if (jj > 0) and (unit != unit_prev):
                        print "Error! Plot variables do not have same units.  Exiting..."
                        sys.exit()
                unit_prev = unit
                break


    ## Read in data

    # header{1,NVars}: variable name
    # data{NVars}: all data
    data = pd.read_csv(gsflow_csv_fil);   #

    dateList = [dt.datetime.strptime(date, '%m/%d/%Y').date() for date in data['Date']]


    # - plot data

    # clear axes
    ax1.cla()
    ax2.cla()

    # convert volume units [m^3] to length [mm]
    if unit[0:2] == 'm^3':
        conv = 1. / basin_area * 1000.
        unit0 = 'mm'
        if len(unit) > 3:
            unit0 + unit[3:]
        unit = unit0[:]
    #plotunit = unit.replace('^', '$^$') # powers

    #plt.close("all")
    for ii in range(len(PlotVar)):

        if (PlotVar[ii] == 'basinppt') or (PlotVar[ii] == 'basinactet'):
            ln0 = ax2.plot(dateList, data[PlotVar[ii]], '--', color='blue')
            ax2.set_ylabel(PlotVar[ii] + ' [' + unit + ']', fontsize=16, color='blue')
        else:
            ln0 = ax1.plot(dateList, data[PlotVar[ii]], 'r-')
            ax1.set_ylabel(PlotVar[ii] + ' [' + unit + ']', fontsize=16, color='red')

        if ii == 0:
            lns = ln0
        else:
            lns = lns + ln0

    #    plt.plot(range(len(data)), data[PlotVar[ii]])
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
    #    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()

    #lns = lns1+lns2+lns3
    #labs = [l.get_label() for l in lns]
    #ax1.legend(lns, PlotVar, loc=0)

    #plt.legend(PlotVar)
    plt.title(plot_title, fontsize=16)

    plt.tight_layout()

    plt.pause(2)

    # check if run is finished
    logfile = Settings.control_dir + slashstr + 'gsflow.log'
    f = open(logfile, 'r')
    last_line = f.readlines()
    last_line = last_line[-1].rstrip()
    f.close()

    if last_line == '  Normal termination of simulation':
        plt.show()
        break

#plt.savefig(savefigfile, dpi = 300)
#
#
#print '\n-------------------'
#print 'Plotting: '
#for ii in range(len(PlotVar)):
#    print '- ' + PlotVar[ii] + ' (' + unit + '): ' + descr[ii]
#print '-------------------\n'
