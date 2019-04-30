import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from mpl_toolkits.basemap import Basemap


def print_map(m,shapefile,colored_map_dict,ax,dict_key = 'NAME'):
    """ plots using pyplot a basemap object 

    m -- the base map object
    shapefile -- a file with the coordinates of the countries
    colored_map_dict -- a dictionary that points from a legal name of a country
    in shapefile to a python color: {'Argentina':'r'}
    ax -- axis object
    """

    m.readshapefile(shapefile, 'units', drawbounds=True,linewidth=.2)    

    for info, shape in zip(m.units_info, m.units):

            unitname = info['NAME']
            try:
                color = colored_map_dict[info[dict_key]]
            except: # no color for this country
                continue

            patches = [Polygon(np.array(shape), True)]
            pc = PatchCollection(patches)
            pc.set_facecolor(color)
            ax.add_collection(pc)

    plt.show()

def color_us_map(us_color_map,shapefile = 'usa_map/st99_d00'):
    """ plots a map of USA using pyplot"""

    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
    print_map(m,shapefile,us_color_map,ax)

def color_world_map(world_color_map,shapefile='world_map/ne_10m_admin_0_countries'):
    """ plots a map of the world using pyplot """

    fig = plt.figure(figsize=(11, 6))
    ax = fig.add_subplot(111, axisbg='w', frame_on=False)
    m = Basemap(lon_0=0, projection='robin')
    m.drawmapboundary(color='w')
    print_map(m,shapefile,world_color_map,ax)


def color_map(colored_map_dict, map_type):
    """ plots a map using basemap and pyplot

    -- colored_map_dict a dictionary that points from a name of a country 
             to a python color: {'Argentina':'r'}

    -- map_type: ['world',USA']
    """

    if map_type == 'world':
        color_world_map(colored_map_dict)
    elif map_type == 'USA':
        color_us_map(colored_map_dict)


