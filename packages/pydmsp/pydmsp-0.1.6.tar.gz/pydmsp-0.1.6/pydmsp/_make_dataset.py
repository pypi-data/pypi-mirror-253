import numpy as np
import xarray as xr
import os
from datetime import datetime as dt

from pydmsp._dmspexeptions import *
from pydmsp import unzip

LARGE_BLOCK_SIZE = 2640

GENERATED_BY = 'pypi package, dmsp_data_reader v.0.1.6'

def get_filepath_and_filename(filepath):
    head, tail = os.path.split(os.path.abspath(filepath))
    return head, tail


def get_data_from_filename(filename='j4f0787122'):
    num_sensor = filename[1]
    num_flight = filename[3:5]
    year = filename[5:7]
    doy = filename[7:]
    return num_sensor, num_flight, year, doy


def read_ssj(filename):
    if len(filename) != 10 or filename[0] != 'j' or filename[2] != 'f':
        raise FileNameError()

    with open(filename, 'rb') as f:
        return np.fromfile(f, dtype='>u2')


def get_ssj_data(filename='j4f0787122'):
    dmsp_ssj_data = read_ssj(filename)
    records_count, _reminder = divmod(dmsp_ssj_data.size, LARGE_BLOCK_SIZE)

    if _reminder != 0:
        raise RemiderNotZeroError()

    if records_count == 0:
        raise NumberOfBlocksIsZeroError()

    if records_count != 1440:
        raise NotEnoughBlocksInFileError()

    dmsp_ssj_data = dmsp_ssj_data.reshape((records_count, LARGE_BLOCK_SIZE))
    return dmsp_ssj_data


def get_raw_ss_min_res(data):
    res = data[:, 3].reshape(1, 1, 24, 60)
    # print(data.shape)
    metadata = {
        'short_name': 'Second',
        'long_name': 'Second of minute',
        'units': 'seconds',
        'description': 'Seconds of minute resolution',
        'Range': '0 to 59',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_geodetic_lat(data):
    res = data[:, 5].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Geodetic Lat',
        'long_name': 'Geodetic latitude',
        'units': 'unitless',
        'description': 'Geodetic latitude',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_geographic_lon(data):
    res = data[:, 6].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Geographic Lon',
        'long_name': 'Geographic longitude',
        'units': 'unitless',
        'description': 'Geographic longitude',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_altitude(data):
    res = data[:, 7].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Altitude',
        'long_name': 'Altitude',
        'units': 'nautical miles',
        'description': '-',
        'Range': '-',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_geographic_lat_110(data):
    res = data[:, 8].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Geographic Lat',
        'long_name': 'Geographic latitude',
        'units': 'unitless',
        'description': 'Geographic latitude at 110 km altitude and on the same magnetic field line as the DMSP spacecraft',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_geographic_lon_110(data):
    res = data[:, 9].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Geographic Lon',
        'long_name': 'Geographic longitude',
        'units': 'unitless',
        'description': 'Geographic longitude at 110 km altitude and on the same magnetic field line as the DMSP spacecraft',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_aacgm_lat(data):
    res = data[:, 10].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Corr Geomagnetic Lat',
        'long_name': 'Corrected geomagnetic latitude',
        'units': 'unitless',
        'description': 'Corrected geomagnetic latitude at 110 km altitude',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_aacgm_lon(data):
    res = data[:, 11].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Corr Geomagnetic Lon',
        'long_name': 'Corrected geomagnetic longitude',
        'units': 'unitless',
        'description': 'Corrected geomagnetic longitude at 110 km altitude',
        'Range': '-',
        'Kind of data': 'Minute data',
        'Note': 'Conversion to a physical quantity is required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_aacgm_mlt_hh(data):
    res = data[:, 12].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Hour',
        'long_name': 'Hour of magnetic local time',
        'units': 'hours',
        'description': 'Hour of magnetic local time in minute resolution',
        'Range': '0 to 23',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_aacgm_mlt_mm(data):
    res = data[:, 13].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Minute',
        'long_name': 'Minute of hour of magnetic local time',
        'units': 'minutes',
        'description': 'Minute of hour of magnetic local time in minute resolution',
        'Range': '0 to 59',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_aacgm_mlt_ss(data):
    res = data[:, 14].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Second',
        'long_name': 'Second of minute of magnetic local time',
        'units': 'seconds',
        'description': 'Second of minute of magnetic local time in minute resolution',
        'Range': '0 to 59',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_indic_flag_for_word_18(data):
    res = data[:, 2595].reshape(1, 1, 24, 60)

    metadata = {
        'short_name': 'Flag',
        'long_name': 'Flag for the variable "RAW_SS_SEC_RES"',
        'units': 'unitless',
        'description': 'Set to 1 to indicate that word 18 is in milliseconds',
        'Range': '0 or 1',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_zero_block(data):
    res = data[:, 2596:].reshape(1, 1, 24, 60, 44)

    metadata = {
        'short_name': 'Zeros',
        'long_name': 'Zero block',
        'units': '-',
        'description': '44 positions filled with zeros, separate data blocks with minute resolution',
        'Range': '0',
        'Kind of data': 'Minute data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


# ?неверное получение часов
def get_raw_hh_sec_res(data):
    data = data[:, 15:2595].reshape(data.shape[0], 43, 60)
    res = data[:, 0, :].reshape(1, 1, 24, 60, 60)

    metadata = {
        'short_name': 'Hour',
        'long_name': 'Hour for n-th second',
        'units': 'hours',
        'description': 'Hour of day for n-th second of data',
        'Range': '0 to 23',
        'Kind of data': 'Second data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


# ?неверное получение минут
def get_raw_mm_sec_res(data):
    data = data[:, 15:2595].reshape(data.shape[0], 43, 60)
    res = data[:, 1, :].reshape(1, 1, 24, 60, 60)

    metadata = {
        'short_name': 'Minute',
        'long_name': 'Minute for n-th second',
        'units': 'minutes',
        'description': 'Minute of hour for n-th second of data',
        'Range': '0 to 59',
        'Kind of data': 'Second data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


# ?неверное получение секунд
def get_raw_ss_sec_res(data):
    data = data[:, 15:2595].reshape(data.shape[0], 43, 60)
    res = data[:, 2, :].reshape(1, 1, 24, 60, 60)

    metadata = {
        'short_name': 'Second',
        'long_name': 'Second for n-th second',
        'units': 'seconds/milliseconds',
        'description': 'Second of minute for n-th second of data. Depending on the flag at position 2595 stores seconds or milliseconds',
        'Range': '0 to 59 or 0 to 1000',
        'Kind of data': 'Second data',
        'Note': 'Conversion to seconds may be required'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res


def get_raw_second_data(data):
    data = data[:, 15:2595].reshape(data.shape[0], 43, 60)
    res = data[:, 3:, :].reshape(1, 1, 24, 60, 60, 2, 20)

    metadata = {
        'short_name': 'Second data',
        'long_name': 'Second data for 20 channels electrons and ions',
        'units': 'unitless',
        'description': 'Second data for 20 electron channels of electrons and ions, respectively. The number of counts measured in channel i',
        'Range': '-',
        'Kind of data': 'Second data'
    }

    res = xr.DataArray(res, attrs=metadata)
    return res




def make_xr_dataset(filepath):
    '''
    Формирует dataset библиотеки xarray "сырых" данных из бинарного файла DMSP

    :param filepath: (string) путь к бинарному файлу
    :return: (xarray.core.dataset.Dataset) набор "сырых" данных
    '''
    unzip(filepath)
    path, filename = get_filepath_and_filename(filepath)
    data = get_ssj_data(filename.replace('.gz', ''))
    year = data[0][4]
    doy = data[0][0]

    iyear = np.arange(year, year+1)
    idoy = np.arange(doy, doy+1)
    ihour = np.arange(0, 24)
    iminute = np.arange(0, 60)
    isecond = np.arange(0, 60)
    ispecie = ['electrons', 'ions']
    ichannel = np.arange(1, 21)
    izeroblock = np.arange(0, 44)

    raw_ss_min_res = get_raw_ss_min_res(data)
    raw_geodetic_lat = get_raw_geodetic_lat(data)
    raw_geographic_lon = get_raw_geographic_lon(data)
    raw_altitude = get_raw_altitude(data)
    raw_geographic_lat_110 = get_raw_geographic_lat_110(data)
    raw_geographic_lon_110 = get_raw_geographic_lon_110(data)
    raw_aacgm_lat = get_raw_aacgm_lat(data)
    raw_aacgm_lon = get_raw_aacgm_lon(data)
    raw_aacgm_mlt_hh = get_raw_aacgm_mlt_hh(data)
    raw_aacgm_mlt_mm = get_raw_aacgm_mlt_mm(data)
    raw_aacgm_mlt_ss = get_raw_aacgm_mlt_ss(data)
    raw_indic_flag_for_word_18 = get_raw_indic_flag_for_word_18(data)
    raw_zero_block = get_raw_zero_block(data)

    raw_hh_sec_res = get_raw_hh_sec_res(data)
    raw_mm_sec_res = get_raw_mm_sec_res(data)
    raw_ss_sec_res = get_raw_ss_sec_res(data)
    raw_second_data = get_raw_second_data(data)

    num_sensor, num_flight, year, doy = get_data_from_filename(filename)

    join_path = os.path.join(path, filename)
    file_created = os.path.getctime(join_path)
    file_created = dt.fromtimestamp(file_created).strftime('%Y-%m-%d %I:%M:%S')

    file_modified = os.path.getmtime(join_path)
    file_modified = dt.fromtimestamp(file_modified).strftime('%Y-%m-%d %I:%M:%S')

    processed_on = dt.now()

    metadata = {
        'Program': 'DMSP',
        'Discipline': ['Space Physics->Magnetospheric Science', 'Space Physics->Ionospheric Science'],
        'Descriptor': 'SSJ/'+num_sensor,
        'Flight': num_flight,
        'Time_resolution': '1 second',
        'filename': filename,
        'filepath': path,
        'file_created': file_created,
        'file_modified': file_modified,
        'processed_on': processed_on,
        'generated by': GENERATED_BY,
        'Note': 'Dataset with raw data'
    }

    ds = xr.Dataset(
        data_vars=dict(
            RAW_SS_MIN_RES=(['iyear', 'idoy', 'ihour', 'iminute'], raw_ss_min_res.data, raw_ss_min_res.attrs),
            RAW_GEODETIC_LAT=(['iyear', 'idoy', 'ihour', 'iminute'], raw_geodetic_lat.data, raw_geodetic_lat.attrs),
            RAW_GEOGRAPHIC_LON=(['iyear', 'idoy', 'ihour', 'iminute'], raw_geographic_lon.data, raw_geographic_lon.attrs),
            RAW_ALTITUDE=(['iyear', 'idoy', 'ihour', 'iminute'], raw_altitude.data, raw_altitude.attrs),
            RAW_GEOGRAPHIC_LAT_110=(['iyear', 'idoy', 'ihour', 'iminute'], raw_geographic_lat_110.data, raw_geographic_lat_110.attrs),
            RAW_GEOGRAPHIC_LON_110=(['iyear', 'idoy', 'ihour', 'iminute'], raw_geographic_lon_110.data, raw_geographic_lon_110.attrs),
            RAW_AACGM_LAT=(['iyear', 'idoy', 'ihour', 'iminute'], raw_aacgm_lat.data, raw_aacgm_lat.attrs),
            RAW_AACGM_LON=(['iyear', 'idoy', 'ihour', 'iminute'], raw_aacgm_lon.data, raw_aacgm_lon.attrs),
            RAW_AACGM_MLT_HH=(['iyear', 'idoy', 'ihour', 'iminute'], raw_aacgm_mlt_hh.data, raw_aacgm_mlt_hh.attrs),
            RAW_AACGM_MLT_MM=(['iyear', 'idoy', 'ihour', 'iminute'], raw_aacgm_mlt_mm.data, raw_aacgm_mlt_mm.attrs),
            RAW_AACGM_MLT_SS=(['iyear', 'idoy', 'ihour', 'iminute'], raw_aacgm_mlt_ss.data, raw_aacgm_mlt_ss.attrs),
            RAW_INDIC_FLAG_FOR_WORD_18=(['iyear', 'idoy', 'ihour', 'iminute'], raw_indic_flag_for_word_18.data, raw_indic_flag_for_word_18.attrs),
            RAW_ZERO_BLOCK=(['iyear', 'idoy', 'ihour', 'iminute', 'izeroblock'], raw_zero_block.data, raw_zero_block.attrs),

            RAW_HH_SEC_RES=(['iyear', 'idoy', 'ihour', 'iminute', 'isecond'], raw_hh_sec_res.data, raw_hh_sec_res.attrs),
            RAW_MM_SEC_RES=(['iyear', 'idoy', 'ihour', 'iminute', 'isecond'], raw_mm_sec_res.data, raw_mm_sec_res.attrs),
            RAW_SS_SEC_RES=(['iyear', 'idoy', 'ihour', 'iminute', 'isecond'], raw_ss_sec_res.data, raw_ss_sec_res.attrs),
            RAW_SECOND_DATA=(['iyear', 'idoy', 'ihour', 'iminute', 'isecond', 'ispecie', 'ichannel'],
                                                                                raw_second_data.data, raw_second_data.attrs)
        ),
        coords={'iyear': iyear
            , 'idoy': idoy
            , 'ihour': ihour
            , 'iminute': iminute
            , 'isecond': isecond
            , 'ispecie': ispecie
            , 'ichannel': ichannel
            , 'izeroblock': izeroblock
        },
        attrs=metadata
    )
    return ds
