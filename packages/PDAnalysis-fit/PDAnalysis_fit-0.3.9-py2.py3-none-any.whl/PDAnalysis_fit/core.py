from chipdatafit import MeasurementRetriever
from os import environ
import numpy as np
from PDAnalysis_fit.utilities import get_voltage_values, get_voltage_index

import matplotlib.pyplot as plt
import matplotlib
import boto3
import scipy 

matplotlib.rcParams['figure.figsize'] = [20, 10]

profile_name = None if environ.get('GITHUB_ACTIONS') is not None else 'hw-google'
boto3.setup_default_session(profile_name=profile_name)

# There are MeasurementRetriever config options if you need em, but the defaults are probably fine!
mr = MeasurementRetriever(query_method="ipviz")

def data_analysis_QE(filter_query,analyses_parameters):
    measurements_iv = mr.get_measurements(filter_query=filter_query, measurement_type="iv_sweep")
    measurements_alignment = mr.get_measurements(filter_query=filter_query, measurement_type="fiber_alignment")
    measurements_polarization = mr.get_measurements(filter_query=filter_query, measurement_type="polarization_maximization")
    data_array_QE = []
    count = 0
    for dut in range(int(len(measurements_iv)/2)):
        alignment_error = 0
        pol_error = 0
        data_light = measurements_iv[dut*2+1]
        data_dark = measurements_iv[dut*2]
        alignment_data = measurements_alignment[dut]
        alignment_error = alignment_data['global_percent_error'][0]
        pol_data = measurements_polarization[dut]
        current = pol_data['current']
        pol_error = np.float_((current[len(current)-1]-np.max(current))/np.max(current)*100)       
        optical_power = 10**(data_light['power_before_sweep'][0]/10)*1e-3 #to be updated 
        relative_attenuation = -measurements_iv[dut*2+1].attrs['metadata']['context']['splitting_ratios']['iv_relative_insertion_loss']['1.545e-06'] #check from the calibration file
        through_loss = analyses_parameters['through_loss']
        relative_fiber_loss = analyses_parameters['relative_fiber_loss'] # relative losses of the fibers used in the thorugh loss
        si_rib_prop_loss = analyses_parameters['si_rib_prop_loss'] #dB/cm
        si_rib_through_wg_length = analyses_parameters['si_rib_through_wg_length']
        si_rib_wg_loss = si_rib_through_wg_length* si_rib_prop_loss
        io_loss = (through_loss - si_rib_wg_loss-relative_fiber_loss)/2
        si_air_reflection_coefficient = 1/(1-0.036) # to account for the free space light detection loss
        optical_input_power_uW = optical_power * si_air_reflection_coefficient * 10**(-io_loss/10) *  10**(relative_attenuation/10)* 1e6
        voltage_value = analyses_parameters['voltage_value'] #static voltage value closest to -1 V operating point
        if data_light['voltage'][0] < 0:
            voltage_value = voltage_value*-1
        voltage_iv = get_voltage_index(data_light['voltage'],voltage_value)
        QE_1V, error_1V = [], []
        QE_1V += [
            (np.abs(data_light['current'][voltage_iv])-np.abs(data_dark['current'][voltage_iv]))*1e6/optical_input_power_uW/1.25*100
        ] 
        if count == 0:       
                data_array_QE = np.array([['device'+str(data_light.attrs['metadata']['device']),QE_1V[0], round(float(alignment_error),2), round(float(pol_error),2) ]])                 
                count +=1
        else:
            data_array_QE = np.append(data_array_QE,[['device'+str(data_light.attrs['metadata']['device']), QE_1V[0], round(float(alignment_error),2),round(float(pol_error),2)]], axis = 0)
        data_array_QE = data_array_QE[data_array_QE[:,0].argsort()] 
    return data_array_QE

def spectral_IV_analyses(filter_query, analyses_parameters):
    measurements = mr.get_measurements(filter_query=filter_query, measurement_type="spectral_iv")
    measurements_iv = mr.get_measurements(filter_query=filter_query, measurement_type="iv_sweep")
    devicename_array =[]
    devicefield_array =[]
    for dut in range(len(measurements)):       
        calibration_frequency = np.array(list(measurements_iv[0].attrs['metadata']['context']['splitting_ratios']['spectral_relative_insertionloss'])[4:-2])
        calibration_insertion_loss  = np.array(list(measurements_iv[0].attrs['metadata']['context']['splitting_ratios']['spectral_relative_insertionloss'].values())[4:-2])
        spectral = measurements[dut]
        data_dark = measurements_iv[2*dut] #for now, the light and dark IVs should seperate eventually
        relative_attenuation = -calibration_insertion_loss #check from the calibration file
        through_loss = analyses_parameters['through_loss']
        relative_fiber_loss = analyses_parameters['relative_fiber_loss'] # relative losses of the fibers used in the thorugh loss
        
        si_rib_prop_loss = analyses_parameters['si_rib_prop_loss'] #dB/cm
        si_rib_through_wg_length = analyses_parameters['si_rib_through_wg_length']
        si_rib_wg_loss = si_rib_through_wg_length* si_rib_prop_loss
        io_loss = (through_loss - si_rib_wg_loss-relative_fiber_loss)/2
        si_air_reflection_coefficient = 1/(1-0.036) # to account for the free space light detection loss
        Res_1V_array = []
        if analyses_parameters['plot'] == True:
            plt.figure()
        index1 = 0
        index2 = 0
        for v in range(len(analyses_parameters['voltage_values'])):
            voltage_value_for_spectral = analyses_parameters['voltage_values'][v] #static voltage value closest to -1 V operating point
            index1 = get_voltage_index(spectral['voltage'],analyses_parameters['voltage_values'][v]) 
            if v < len(analyses_parameters['voltage_values'])-1:
                index2 = get_voltage_index(spectral['voltage'],analyses_parameters['voltage_values'][v+1]) 
            else:
                index2 = len(spectral['voltage'])
            optical_power = 10**(-spectral['power'][index1:index2]/10)*1e-3
            optical_input_power_uW = np.multiply(optical_power, si_air_reflection_coefficient * 10**(-io_loss/10) *  10**(relative_attenuation/10)* 1e6)
            dark_index = get_voltage_index(data_dark['voltage'],voltage_value_for_spectral)
            Res_1V = (np.abs(spectral["current"][index1:index2])-np.abs(data_dark["current"][dark_index]))*1e6/optical_input_power_uW
            Res_1V_array.append(Res_1V)
            if analyses_parameters['plot'] == True:
                plt.plot(spectral['wavelength'][index1:index2].values*1e9,Res_1V, label = 'Voltage = ' + str(analyses_parameters['voltage_values'][v]))
                plt.ylabel('Responsivity (A/W)')
                plt.xlabel('Wavelength (nm)')
                plt.title('Spectral Response of ' + measurements[dut].attrs['metadata']['foundry']\
                + str(measurements[dut].attrs['metadata']['run']) + ' ' + 'Field' +\
                str(measurements[dut].attrs['metadata']['field']) + ' Device'+\
                str(measurements[dut].attrs['metadata']['device']))
                plt.grid()
                plt.legend()
        devicename_array.append( 'device'+str(measurements[dut].attrs['metadata']['device']))
        devicefield_array.append('field'+ str(measurements[dut].attrs['metadata']['field']))
    return np.float_(Res_1V_array),spectral['wavelength'][index1:index2], devicename_array, devicefield_array


def attenuation_sweep_data_analyses(filter_query):
    measurements = mr.get_measurements(filter_query=filter_query, measurement_type="attenuation_sweep")
    measurements_iv = mr.get_measurements(filter_query=filter_query, measurement_type="iv_sweep")
    data_array_aim6_automated_attenuation = []
    Ids_array = []
    max_clearance_array = []
    devicename_array =[]
    count = 0
    for dut in range(len(measurements)):
        index_array = []
        data = measurements[dut]
        atten = data['attenuation']
        curs = data['current']
        power = data['power']
        voltages, change_indexes = get_voltage_values(data['voltage'])
        device_name = 'device'+str(measurements[dut].attrs['metadata']['device'])
        data_dark = measurements_iv[2*dut]
        for v in voltages:
            index_array.append(get_voltage_index(data_dark['voltage'],v))
        idark =  np.array(data_dark['current'][index_array])
        transmission1dbs=[]
        i1dbs=[]
        for i in range(len(voltages)):
            x=np.array(10**(-atten[change_indexes[i]:change_indexes[i+1]]/10))
            y=-curs[change_indexes[i]:change_indexes[i+1]]+idark[i]
            # find roughly the saturation point, in order to fit linear region
            grad=np.diff(y)/np.diff(x)
            lingrad=np.max(grad)
            linear_region=np.where(grad>lingrad*0.90)[0] #region where gradient within 10% of linear
            lim2=linear_region[-1]-2
            lim=np.clip(lim2-10,0,lim2) # 10 points before lim2 or 0

            fit=np.polyfit(x[lim:lim2],y[lim:lim2],1)
            compression=10*np.log10((np.diff(y)/np.diff(x))/fit[0])
            interp=scipy.interpolate.InterpolatedUnivariateSpline(x[1:], compression+1)
            roots=interp.roots()
            roots=roots[roots>x[lim2]] #ignore any roots below lim2
            if roots.size>0:
                transmission1dbs.append(roots[0])
            else:
                transmission1dbs.append(0)
            interp2=scipy.interpolate.InterpolatedUnivariateSpline(x, y)
            i1dbs.append(interp2(transmission1dbs[-1]))
            
        plt.plot(-np.array(voltages),10*np.log10(-np.array(i1dbs)/idark),'.', label = device_name)
        plt.ylabel('Detector dark-current-limited clearance (dB)')
        plt.xlabel('Reverse Bias (V)')
        plt.legend()  
        Ids_array= np.append(Ids_array,i1dbs)
        max_clearance_array= np.append(max_clearance_array,np.max(10*np.log10(-np.array(i1dbs)/idark)))
        devicename_array = np.append(devicename_array,device_name )
    plt.figure()
    plt.plot(devicename_array[np.argsort(devicename_array)],max_clearance_array[np.argsort(devicename_array)],'o')
    plt.xticks(rotation=45, fontsize='11', horizontalalignment='right')
    plt.ylabel('Maximum Detector dark-current-limited clearance (dB)')
    return Ids_array, max_clearance_array,devicename_array