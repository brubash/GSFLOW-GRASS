# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:33:16 2017

@author: gcng
modified by brubash for GSFLOW v.1.2.2
"""

# List of gsflow-csv-file variables (and more)

# see Table 12 of GSFLOW manual and source code files 'gsflow_budget.f90' and gsflow_sum.f90'

# Create cell with descriptions
varname = []
unit = []
descr = []

#MODFLOW_len_unit = 'm'
#MODFLOW_time_unit = 'd' # day
MODFLOW_len_unit = 'L'
MODFLOW_time_unit = 'T'

# =================================== variables from gsflow_sum.f90 =============================== #
# =================================== GSFLOW v1.2.2 gsflow.csv variables ========================== #

varname.append('Date')
descr.append('Date Month, day, and year designation')
unit.append('Mon/Day/Yr')

varname.append('StreamOut_Q')
descr.append('Volumetric flow rate of streamflow leaving modeled region')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('HortSroff2Stream_Q')
descr.append('Volumetric flow rate of Hortonian runoff to streams')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('DunnSroff2Stream_Q')
descr.append('Volumetric flow rate of Dunnian runoff to streams')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Interflow2Stream_Q')
descr.append('Volumetric flow rate of slow plus fast interflow to streams')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Canopy_S')
descr.append('Volume of intercepted precipitation in plant-canopy reservoirs')
unit.append(MODFLOW_len_unit + '^3')

varname.append('SnowPweqv_S')
descr.append('Volume of water in snowpack storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Imperv_S')
descr.append('Volume of water in impervious reservoirs')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Dprst_S')
descr.append('Volume of water stored in surface-depression storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Cap_S')
descr.append('Volume of water in capillary reservoirs of the soil zone')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Grav_S')
descr.append('Volume of water in gravity reservoirs of the soil zone')
unit.append(MODFLOW_len_unit + '^3')

varname.append('UnsatStream_S')
descr.append('Volume of water in the unsaturated zone under streams')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Lake_S')
descr.append('Volume of water in lakes')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Stream_S')
descr.append('Volume of water in streams (non-zero only when '
    'transient routing option is used in SFR2)')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Precip_Q')
descr.append('Volumetric flow rate of precipitation')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('NetWellFlow_Q')
descr.append('Net volumetric flow rate of groundwater injection or removal from wells')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('BoundaryStreamFlow_Q')
descr.append('Volumetric specified streamflow into the model domain to SFR')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('CanopyEvap_Q')
descr.append('Volumetric flow rate of evaporation of intercepted precipitation')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('SnowEvap_Q')
descr.append('Volumetric flow rate of snowpack sublimation')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('ImpervEvap_Q')
descr.append('Volumetric flow rate of evaporation from impervious areas')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('DprstEvap_Q')
descr.append('Volumetric flow rate of evaporation from surface depressions')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('CapET_Q')
descr.append('Volumetric flow rate of evapotranspiration from pervious areas ')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('SwaleEvap_Q')
descr.append('Volumetric flow rate of evaporation from swale HRUs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('UnsatET_Q')
descr.append('Volumetric flow rate of evapotranspiration from the unsaturated zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('SatET_Q')
descr.append('Volumetric flow rate of evapotranspiration from the saturated zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('LakeEvap_Q')
descr.append('Volumetric flow rate of evaporation from lakes')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('DunnInterflow2Lake_Q')
descr.append('Volumetric flow rate of interflow and Dunnian surface runoff to lakes')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('HortSroff2Lake_Q')
descr.append('Volumetric flow rate of Hortonian surface runoff to lakes')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('SoilDrainage2Unsat_Q')
descr.append('Volumetric flow rate of gravity drainage to the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Sat2Grav_Q')
descr.append('Volumetric flow rate of groundwater discharge '
    'from the saturated zone to the soil zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('RechargeUnsat2Sat_Q')
descr.append('Volumetric flow rate of recharge from the unsaturated '
    'zone to the saturated zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Infil2Soil_Q')
descr.append('Volumetric flow rate of soil infiltration (including precipitation, '
    'snowmelt, and cascading Hortonian flow)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('KKITER')
descr.append('Number of iterations for each time step')
unit.append('none')

# =============================== additional gsflow_sum.f90 variables ============================= #

varname.append('CapDrainage2Sat_Q')
descr.append('Volumetric flow rate of direct gravity drainage '
    'from excess capillary water to the unsaturated zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('basinsnow')
descr.append('Volumetric flow rate of snow')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('basinrain')
descr.append('Volumetric flow rate of rain')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('LakePrecip_Q')
descr.append('Volumetric flow rate of precipitation on lakes')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('PotGravDrn2Unsat_Q')
descr.append('Potential volumetric flow rate of gravity drainage from '
    'the soil zone to the unsaturated zone (before conditions of the '
    'unsaturated and saturated zones are applied)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('basinseepout')
descr.append('Volumetric flow rate of groundwater discharge from the '
    'saturated zone to the soil zone')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Sroff2Stream_Q')
descr.append('Volumetric flow rate of surface runoff to streams')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('obs_strmflow')
descr.append('Volumetric flow rate of streamflow measured at a gaging station')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('UnsatDrainageExcess_Q')
descr.append('Volumetric flow rate of gravity drainage from the soil '
    ' zone not accepted due to conditions in the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Pref_S')
descr.append('Volume of water stored in preferential-flow reservoirs of the soil zone')
unit.append(MODFLOW_len_unit + '^3')

varname.append('uzf_et')
descr.append('Volumetric flow rate of evapotranspiration from the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Unsat_dS')
descr.append('Change in unsaturated-zone storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Stream2Sat_Q')
descr.append('Volumetric flow rate of stream leakage to the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('UnsatStream_dS')
descr.append('Change in unsaturated-zone storage under streams')
unit.append(MODFLOW_len_unit + '^3')

varname.append('SatDisch2Stream_Q')
descr.append('Volumetric flow rate of groundwater discharge to streams')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Lake2Sat_Q')
descr.append('Volumetric flow rate of lake leakage to the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Lake_dS')
descr.append('Change in lake storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('SatDisch2Lake_Q')
descr.append('Volumetric flow rate of groundwater discharge to lakes')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('basinsm2gvr')
descr.append('Volumetric flow rate of flow from capillary reservoirs to gravity reservoirs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('basingvr2sm')
descr.append('Volumetric flow rate of flow from gravity reservoirs to capillary reservoirs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Infil2CapTotal_Q')
descr.append('Volumetric flow rate of soil infiltration into capillary '
    'reservoirs including precipitation, snowmelt, and '
    'cascading Hortonian and Dunnian runoff and interflow '
    'minus infiltration to preferential-flow reservoirs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Infil2Pref_Q')
descr.append('Volumetric flow rate of soil infiltration into '
    'preferential-flow reservoirs including precipitation, '
    'snowmelt, and cascading surface runoff')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('DunnInterflow2Cap_Q')
descr.append('Volumetric flow rate of cascading Dunnian runoff and interflow to HRUs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('ActualET_Q')
descr.append('Volumetric flow rate of actual evaporation from HRUs')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('SnowMelt_Q')
descr.append('Volumetric flow rate of snowmelt')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Ave_SoilDrainage2Unsat_Q')
descr.append('Running average gravity drainage to the unsaturated and saturated zones')
unit.append(MODFLOW_len_unit + '^3')

varname.append('cum_pweqv')
descr.append('Cumulative change in snowpack storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('cum_soilstor')
descr.append('Cumulative change in soil storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('cum_uzstor')
descr.append('Cumulative change in unsaturated storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('cum_satstor')
descr.append('Cumulative change in saturated storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('rate_pweqv')
descr.append('Change in snow pack storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('rate_soilstor')
descr.append('Change in soil storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('rate_uzstor')
descr.append('Change in unsaturated storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('rate_satstor')
descr.append('Change in saturated storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('basinsoilstor')
descr.append('Volume of soil moisture storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('id_obsrunoff')
descr.append('Index of measured streamflow station corresponding to the basin outlet')
unit.append('none')

# =================================== variables from gsflow_budget.f90 ============================ #
# =================================== GSFLOW v1.2.2 gsflow.csv variables ========================== #

varname.append('Stream2Unsat_Q')
descr.append('Volumetric flow rate betweeen streams and the unsaturated '
    'zone (value is equal to Strm2UZGW minus SatDisch2Stream_Q, where a '
    'negative value indicates a net loss from streams)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('StreamExchng2Sat_Q')
descr.append('Volumetric flow rate of exchange betweeen streams and the saturated '
    'zone (value is equal to Strm2UZGW minus SatDisch2Stream_Q, where a '
    'negative value indicates a net loss from streams)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Unsat_S')
descr.append('Volume of water in the unsaturated zone')
unit.append(MODFLOW_len_unit + '^3')

varname.append('Sat_S')
descr.append('Volume of water in the saturated zone')
unit.append(MODFLOW_len_unit + '^3')

varname.append('NetBoundaryFlow2Sat_Q')
descr.append('Volumetric flow rate to the saturated zone along the external boundary '
    '(negative value is flow out of model domain)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Lake2Unsat_Q')
descr.append('Volumetric flow rate betweeen lakes and the unsaturated '
	'zone (value is equal to Strm2UZGW minus SatDisch2Stream_Q, where a '
	'negative value indicates a net loss from streams)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('LakeExchng2Sat_Q')
descr.append('Volumetric flow rate of exchange betweeen lakes and the saturated '
	'zone (value is equal to Strm2UZGW minus SatDisch2Stream_Q, where a '
	'negative value indicates a net loss from streams)')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

# ============================ additional gsflow_budget.f90 variables ============================= #

varname.append('stream_inflow')
descr.append('Specified volumetric stream inflow rate into model')
unit.append(MODFLOW_len_unit + '^3/'+ MODFLOW_time_unit)

varname.append('Sat_dS')
descr.append('Change in saturated-zone storage')
unit.append(MODFLOW_len_unit + '^3')

varname.append('total_pump')
descr.append('Total pumpage from all cells')
unit.append(MODFLOW_len_unit + '^3')

varname.append('total_pump_cfs')
descr.append('Total pumpage from all cells')
unit.append('cfs')

varname.append('reach_cfs')
descr.append('Stream flow leaving each stream reach')
unit.append('cfs')

varname.append('reach_wse')
descr.append('Water surface elevation in each stream reach')
unit.append(MODFLOW_len_unit)

varname.append('basin_gw2sm')
descr.append('Basin average water exfiltrated from unsaturated and saturated zones and added to soil zone')
unit.append('inches')

varname.append('basin_szreject')
descr.append('Basin average recharge from SZ and rejected by UZF')
unit.append('inches')

varname.append('gw2sm')
descr.append('HRU average water exfiltrated from groundwater model and added back to soil zone')
unit.append('inches')

varname.append('actet_gw')
descr.append('Actual ET from each GW cell')
unit.append('inches')

varname.append('actet_tot_gwsz')
descr.append('Total actual ET from each GW cell and PRMS soil zone')
unit.append('inches')

varname.append('streamflow_sfr')
descr.append('Streamflow as computed by SFR for each segment')
unit.append('cfs')

varname.append('gw_rejected')
descr.append('HRU average recharge rejected by UZF')
unit.append('inches')

# Note: For version 1.2.2 it is also necessary to disable the following
#   three variables in input_file_builder/printGSFLOWControlfile.py

# varname.append('uzf_infil_map')
# descr.append('HRU total gravity drainage to UZF cells')
# unit.append(MODFLOW_len_unit + '^3')

# varname.append('sat_recharge')
# descr.append('HRU total recharge to the saturated zone')
# unit.append(MODFLOW_len_unit + '^3')

# varname.append('mfoutflow_to_gvr')
# descr.append('MODFLOW total discharge and ET to each HRU')
# unit.append(MODFLOW_len_unit + '^3')
