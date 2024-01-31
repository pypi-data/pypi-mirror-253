"""::

  _    _           _            __ _               
 | |  | |         | |          / _| |              
 | |__| |_   _  __| |_ __ ___ | |_| | _____      __
 |  __  | | | |/ _` | '__/ _ \|  _| |/ _ \ \ /\ / /
 | |  | | |_| | (_| | | | (_) | | | | (_) \ V  V / 
 |_|  |_|\__, |\__,_|_|  \___/|_| |_|\___/ \_/\_/  
          __/ |                                    
         |___/

This module includes functions and classes to pilot hydroflow.

Usage:
======

Insert here the description of the module


License
=======

Copyright (C) <1998 – 2024> <Université catholique de Louvain (UCLouvain), Belgique> 
	
List of the contributors to the development of Watlab: see AUTHORS file.
Description and complete License: see LICENSE file.
	
This program (Watlab) is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (see COPYING file).  If not, 
see <http://www.gnu.org/licenses/>.

"""

# Metadata
__authors__ = "Pierre-Yves Gousenbourger, Sandra Soares-Frazao, Robin Meurice, Charles Ryckmans, Nathan Delpierre"
__contact__ = "pierre-yves.gousenbourger@uclouvain.be"
__copyright__ = "MIT"
__date__ = "2022-09-05"
__version__= "0.0.1"

# internal modules

# external modules contained in requirements.txt
import numpy as np
import os
import sys
from scipy.interpolate import griddata
import rasterio
import subprocess
import shlex
import matplotlib.tri as mtri
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import contextily as ctx
import imageio
from .meshParser import MeshParser
# const
A_CONSTANT = 0.0
SVE2D_LHLLC = "SVE2D_LHLLC"
RICH2D = "Richards_Solver"
_HYDROFLOW_NAME = "hydroflow"
#%%% A name for hydroflow executable
if sys.platform == "win32":
    _HYDROFLOW_EXECUTABLE = _HYDROFLOW_NAME+".exe"
elif sys.platform == "Darwin":
    raise OSError("MacOS is not yet supported")
elif sys.platform == "linux" or sys.platform == "linux2":
    raise OSError("Linux is not yet supported")
#%%% Corresponds to the initial conditions variables
_INITIAL_WATER_LEVEL = "initial_water_level"
_INITIAL_WATER_DISCHARGE = "initial_water_discharge"
_INITIAL_SEDIMENTS_LEVEL = "initial_sediments_level"
_BEDROCK_LEVEL = "bedrock_level"
_FRICTION_COEFFICIENTS = "friction_coefficients"
_FIXED_BANKS = "fixed_banks"
#%%% Corresponds to the boundary conditions variables
_TRANSMISSIVE_BOUNDARIES = "transmissive_edges"
_BOUNDARY_WATER_LEVEL = "boundary_water_level"
_BOUNDARY_WATER_DISCHARGE = "boundary_water_discharge"
_BOUNDARY_SEDIMENTS_DISCHARGE = "boundary_sediments_discharge"
_BOUNDARY_HYDROGRAM = "boundary_hydrogram"
_BOUNDARY_LIMNIGRAM = "boundary_limnigram"
##### Default values for IO folders
_INPUT_NAME = "input"
_OUTPUT_NAME = "output"
##### Default values for generated files
_NODES_FILE = "nodes.txt"
_CELLS_FILE = "cells.txt"
_EDGES_FILE = "edges.txt"
_DATA_FILE = "data.txt"
_DATA_TEMPLATE_FILE = "data_template.txt"
_SLOPE_FILE = "slope.txt"
_INITIAL_CONDITIONS_FILE = "initial_conditions.txt"
_FIXED_BED_FILE ="fixedBed.txt"
_FRICTION_FILE = "friction_values.txt"
_SEDIMENT_LEVEL_FILE = "sediments_level.txt"
_FIXED_BANK_FILE = "fixed_banks.txt"
_PICTURE_FILE = "pictures_times.txt"
_GAUGE_FILE = "gauge.txt"
_DISCHARGE_FILE = "discharge_measurement.txt"
_DISCHARGE_OUTPUT_FILE = "discharge_measurement_output.txt"
_TEST_NAME = "tests\py"

# path to hydroflow
_dir_path_to_executable = os.path.join(os.path.dirname(__file__),"bin")
_root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def get_hydroflow_path():
    """
    Returns
    --------
    String
    Path of the hydroflow.exe folder
    """
    return _dir_path_to_executable


def _compile_code(isParallel=False):
    """
        Compiles the C++ code using g++.
    The compilation is done using the following command:
        g++ -O3 -fopenmp -pthread -o hydroflow src/cpp/*.cpp src/cpp/writer/*.cpp src/cpp/interfaces/*.cpp src/cpp/helpers/*.cpp -std=c++20
    The compilation is done in the directory where the C++ code is located.
    The compilation is done using the subprocess module.
    The subprocess module is used to run the g++ command.
    The shlex module is used to split the command into a list of strings.
    The cwd parameter of the subprocess module is used to specify the directory 
        where the compilation is done.
    The wait() method of the subprocess module is used to wait for the 
        compilation to finish.
    """
    relpath = os.path.relpath(_dir_path_to_executable,_root_path).replace('\\','/')
    src_files =  'src/cpp/*.cpp src/cpp/writer/*.cpp src/cpp/interfaces/*.cpp src/cpp/helpers/*.cpp src/cpp/physicalmodels/*.cpp'
    if isParallel:
        compiler_opt = '-O3 -fopenmp -pthread'
    else:
        compiler_opt = ''
    try:
        subprocess.call(shlex.split('g++ '+compiler_opt+' -o '+relpath+'/'+_HYDROFLOW_NAME+ ' '+src_files+' -std=c++20 -static'),
                               stdout=subprocess.PIPE,
                               shell=True,
                               cwd=_root_path,
                               text=True,
                               stderr=subprocess.PIPE)
        print("The code has been successfully compiled: the executable has been generated.")
        if isParallel: print("(Parallel version)")
    except subprocess.CalledProcessError as e:
        print("There were compiling errors, the code can not be run:")
        print("Error:", e)

class Mesh():
    """Mesh class is used to build the geometry of the simulation. \n 
    The class gives access to the informations of the mesh as \n
    nodes, cells, edges organization and regions. \n 
    Normally, the function are not needed for the user. 
    Except if there is a need for specific simulation topography imported from a tiff file.

    :param msh_mesh: The path to the .msh file representing the mesh.
        The file must comply with GMSH 4.10 file format
    :type msh_mesh: string
    :param nNodes: Number of nodes in the mesh
    :type nNodes: int
    :param nCells: Number of cells in the mesh
    :type nCells: int
    :param nEdges: Number of edges in the mesh
    :type nEdges: int
    :param tag_to_indexes: a dictionnary with key : cells_tags corresponding to values : cells_indexes
    :type tag_to_indexes: dict
    """
    def __init__(self,msh_mesh):
        """Constructs the Mesh object based on an .msh file.
        """
        self.__parser = MeshParser(msh_mesh)
        self.__nodes, self.__node_tags = self.__parser.extract_nodes()
        self.__cells, self.__cell_tags = self.__parser.extract_cells()
        self.__edge_nodes, self.__edge_cells, self.__edge_tags, self.__edgeTags_unsorted = self.__parser.extract_edges()
        self.__edges_length = self.edges_length
        self.__boundaries = self.__parser.extract_physical_groups(1)
        self.__regions = self.__parser.extract_physical_groups(2)
        self.__region_cells = self.__parser.extract_cells_by_physical_group(2)
        self.__boundary_edges = self.__parser.extract_cells_by_physical_group(1)
        self.nNodes = len(self.__node_tags)
        self.nCells = len(self.__cell_tags)
        self.nEdges = len(self.__edge_tags)
        self.__cells_barycenters = np.resize(self.__parser.extract_cells_barycenters(),(self.nCells,3))
        self.__tag_to_indexes = {tag: index for tag, index in zip(self.__cell_tags,  np.arange(0,self.nCells))}
        self.__elem_type = len(self.__cells[0]) # n_nodes for each cell 

    @property
    def nodes(self):
        """The nodes' tags and coordinates

        :getter: __nodes_tags = list of the nodes' tags
            __nodes = list of the nodes' coordinates
        :type: nDArray
        """
        
        return self.__node_tags, self.__nodes
 
    @property
    def cells(self):
        """The __cell_tags and the associated cells represented by their node_tags

        :getter: __cell_tags = list of the cells' tags
            __cells = list of the nodes describing each cell
        :type: nDArray
        """
        
        return self.__cell_tags, self.__cells

    @property
    def tag_to_indexes(self):
        """Indicates the mapping from cells' tags to cells' indexes

        :getter: __tag_to_indexes
        :type: dict{key = tag : value = index}
        """
        return self.__tag_to_indexes
    
    @property
    def edges(self):
        """The edges' tags, nodes, and cells

        :getter: __edge_tags = the tags of the edges
            __edge_nodes = the nodes n_0 and n_1 composing the edge, with n_0 < n_1
            __edge_cells: the left cell and the right cell, with respect to the edge
            where n_0 is bottom and n_1 is top.
        :type: nDArray
        """
        return self.__edge_tags, self.__edge_nodes, self.__edge_cells

    @property
    def boundaries(self):
        """The dictionnary of boundaries

        :getter: __boundaries
        :rtype: dict{tags : names}
        """
        return self.__boundaries

    def get_boundary_by_name(self,name):
        """Returns a list of boundary edges corresponding to the tag [name] 

        :param name: name of the tag to look for
        :type name: string
        :raises Exception: There is no physical boundary named after [name]
        :return: list of the boundary edges
        :rtype: list
        """

        if (name in self.__boundaries.values()):
            return list(self.__boundaries.keys())[list(self.__boundaries.values()).index(name)]
        else: 
            raise Exception("There is no physical boundary named "+name+".")

    @property
    def regions(self):
        """The dictionnary of physical groups

        :getter: __regions = the physical groups
        :type: dict{tags : names}
        """
        return self.__regions
    
    @property
    def region_cells(self):
        """The cells associated to physical group

        :getter: __region_cells
        :type: dict{Physical Group : cells }
        """
        return self.__region_cells
    
    def get_region_by_name(self,name):
        """Returns the tag of the region of name [name] : 

        :param name: name of the tag to look for
        :type name: string
        :raises Exception: There is no physical region named after [name]
        :return: returns the tag of the region corresponding to [name]
        :rtype: list
        """
        
        if (name in self.__regions.values()):
            return list(self.__regions.keys())[list(self.__regions.values()).index(name)]
        else: 
            raise Exception("There is no physical region named "+name+".")
    
    @property
    def boundary_edges(self):
        """The edges associated to physical groups as a dictionnary

        :getter: __boundary_edges
        :type: dict{physical group : edges}
        """
        return self.__boundary_edges
    
    @property
    def elem_type(self):
        """
        Returns
        -------
        Type of the elements as int 
        """
        return self.__elem_type

    def get_cells_barycenters(self):
        """Returns cells barycenters
        
        :return: __cells_barycenters
        :rtype: nDArray 
        """
        return self.__cells_barycenters
    
    @property
    def edges_length(self):
        """Returns the length of each edge composing the mesh

        :return: length of each mesh
        :rtype: ndArray
        """
        if not hasattr(self,"__edges_length"):
            x1 = np.take(self.__nodes[:,0],self.__edge_nodes[:,0].astype(np.int64)-1)
            y1 = np.take(self.__nodes[:,1],self.__edge_nodes[:,0].astype(np.int64)-1)
            x2 = np.take(self.__nodes[:,0],self.__edge_nodes[:,1].astype(np.int64)-1)
            y2 = np.take(self.__nodes[:,1],self.__edge_nodes[:,1].astype(np.int64)-1)
            self.__edges_length = np.sqrt((x2-x1)**2+(y2-y1)**2)
        return self.__edges_length
    
    def get_boundary_length(self,boundary_name) -> float:
        """Returns the length of a boundary by name

        :param boundary_name: the name of the desired boundary
        :type boundary_name: str
        :raises Exception: this boundary name does not exist
        :return: The length in [m] of the boundary
        :rtype: float
        """
        if boundary_name not in self.boundaries.values():
            raise Exception("this boundary name does not exist")
        else: 
            key = self.get_boundary_by_name(boundary_name)
            edges = self.__boundary_edges[key] - 1 
            boundary_length = np.sum(self.__edges_length[edges])
        return boundary_length
    
    def set_nodes_elevation_from_tif(self,tif_file):
        """Sets the elevation of the nodes of the mesh from a tif file.
            The z value is interpolated from the tif file and set to the corresponding nodes

        :param tif_file: path of the tif file
        :type tif_file: string
        """
       
        with rasterio.open(tif_file) as dataset:
            image_data = dataset.read()
            transform = dataset.transform
            # Get the x and y coordinates of the top-left corner of the image
            x_origin = transform.c
            y_origin = transform.f
            # Get the x and y coordinates of the bottom-right corner of the image
            x_end = x_origin + (dataset.width * transform.a) + transform.a
            y_end = y_origin + (dataset.height * transform.e) + transform.e
            x_coords, y_coords = np.meshgrid(np.linspace(x_origin, x_end, dataset.width), np.linspace(y_origin, y_end, dataset.height))
            z_values = image_data[0]
        
        def __interpolate_points(tif_points_coordinates,tif_points_elevations,desired_points):
            mesh_x = desired_points[:,0]
            mesh_y = desired_points[:,1]
            mesh_points = np.column_stack((mesh_x.flatten(), mesh_y.flatten()))
            return griddata(tif_points_coordinates, tif_points_elevations, mesh_points, method='nearest')
        
        tif_points_coordinates = np.column_stack((x_coords.flatten(), y_coords.flatten()))
        tif_points_elevations = z_values.flatten()
        self.__cells_barycenters[:,2] = __interpolate_points(tif_points_coordinates,tif_points_elevations,self.__cells_barycenters)
        self.__nodes[:,2] = __interpolate_points(tif_points_coordinates,tif_points_elevations, self.__nodes)
    
class Model():
    """
    Simulation model. 
    The simulation model is made of a physical Mesh and is linked to the Export class \n
    This class must be used to design your problem by providing a solver, initial and boundary conditions. 
    The function solve() is used to launch the simulation by calling the C++ solver. 
    """
    __SIM_NAME = "Hydroflow-Simulation"
    def __init__(self,mesh: Mesh):
        """Builder of the Model class. 
        To build a Model object, only a Mesh object is needed. 

        :param mesh: the mesh object describing the physical environment of the problem
        :type mesh: Mesh
        """

        self.__current_path = os.getcwd()
        self.__mesh = mesh
        self.export = Export(self.__mesh,self)

        self.__conditions = {}
        self.__conditions_regions = {}
        self.__pic = []
        self._gauge = []
        self._gauge_time_step = 0
        #Simulation name
        self.__name = self.__SIM_NAME
        #Main parameters of the simulation
        self.__starting_time = 0.0
        self.__ending_time = 10.0
        self.__Cfl = 0.90
        #Algorithm parameters
        self.__physical_model = 1
        self.__flux_scheme = 1 # self.__FLUX_SCHEME
        self.__flux_order = 1
        self.__slope_limiter = 0
        #Hydrodynamic part: initialization
        self.__is_fixed_bed_level = 0
        #Friction parameters
        self.__is_friction = 0
        #sediment transport and height
        self.__is_sediment = 0
        self.__is_initial_sediment_level = 0
        self.__g_d50 = 0.003
        self.__g_sed_density = 2.65
        self.__g_sed_manning = 0.025
        self.__g_sed_porosity =0.4
        #bank-failure tool (only if sediments)
        self.__is_bank_failure = 0
        self.__bank_failure_method = 1 # 1 or 2
        self.__critical_emmerged_friction_angle = 87.0
        self.__critical_immerged_friction_angle = 60.0
        self.__residual_emmerged_friction_angle = 85.0
        self.__residual_immerged_friction_angle = 0.4
        #tests (only if sediments)
        self.__is_sediment_conservation = 0
        self.__dt_conservation_test = 1.0
        #Output systems
        self.__dt_enveloppe = 1.0
        self.__is_picture = 0
        self.__is_gauge = 0
        self.__is_discharge_measurement_section = 0
        self.__discharge_measurement_edges = {}
        self.__discharge_measurement_time_step = 1


    def export_data(self) -> None: 
        """ 
        Calls the export class to export the needed files in the input folder
        Please inspect the input folder to see the designed problem.
        Informations about initial conditions, nodes, edges or eventual gauges places are included
        """
        self.export.export()

    def solve(self,display=True,isParallel=False) -> None:
        """
        Calls the C++ executable and solve the current designed model
        """
        self.__launch_code(display,isParallel=isParallel)

    def resume_simulation(self,pic_file,display=True,isParallel=False,isSameMesh=True):
        """Allows the user to restart a simulation from a former pic.txt file.

        :param pic_file: pic.txt file used as initial conditions for the simulation
        :type pic_file: string
        :param display: if True shows the cpp outputed informations, defaults to True
        :type display: bool, optional
        :param isParallel: if True the parallel version of the code is used, defaults to False
        :type isParallel: bool, optional
        :param isSameMesh: if True no interpolation is performed. Initial conditions are not interpolated, defaults to True
        :type isSameMesh: bool, optional
        """
        data = np.loadtxt(pic_file,skiprows=1)
        regions = list(self.__mesh.regions.values())

        if isSameMesh : 
            h_water = data[:,3]
            qx = data[:,4]
            qy = data[:,5]
        else: 
            x_coord_pic = data[:,0]
            y_coord_pic = data[:,1]
            old_points = np.column_stack((x_coord_pic.flatten(), y_coord_pic.flatten()))  
            X_barycenters = self.__mesh.get_cells_barycenters()[:,0]
            Y_barycenters = self.__mesh.get_cells_barycenters()[:,1]
            new_points = np.column_stack((X_barycenters, Y_barycenters))
            h_pic = data[:,3]
            qx_pic = data[:,4]
            qy_pic = data[:,5]

            nearest_grid_h = griddata(old_points, h_pic, new_points, method='nearest')
            h_water = griddata(old_points, h_pic, new_points, method='linear')
            h_water[np.isnan(h_water)] = nearest_grid_h[np.isnan(h_water)]

            nearest_grid_qx = griddata(old_points, qx_pic, new_points, method='nearest')
            qx = griddata(old_points, qx_pic, new_points, method='linear')
            qx[np.isnan(qx)] = nearest_grid_qx[np.isnan(qx)] 
            nearest_grid_qy = griddata(old_points, qy_pic, new_points, method='nearest')
            qy = griddata(old_points, qy_pic, new_points, method='linear')
            qy[np.isnan(qy)] = nearest_grid_qy[np.isnan(qy)] 
            qx[h_water<10**-1] = 0
            qy[h_water<10**-1] = 0
            
        discharges = np.column_stack((qx,qy))
        for region in regions:
            region_tag = self.__mesh.get_region_by_name(region) if isinstance(region,str) else region
            indexes = [self.__mesh.tag_to_indexes.get(tag) for tag in self.__mesh.region_cells[region_tag]]
            self.set_initial_water_height(str(region),h_water[indexes].tolist())
            self.set_initial_water_discharge(str(region),discharges[indexes].tolist())
        self.export_data()
        if display: print("Input Files Generated")
        self.solve(display,isParallel=isParallel)

    def get_picture_times(self):
        """Provides the list of the times at which the results will be returned

        :return: list of picture times
        :rtype: ndArray
        """
        return self.__pic

    def set_picture_times(self,n_pic = 0, pic_array = None):
        """ 2 possibilities are given to set the output picture times
            1) User gives a number of desired pic and the list of pictures time is evaluated given the simulation time \n
            2) User directly gives a list of picture times

        :param n_pic: number of desired pictures, defaults to 0
        :type n_pic: int, optional
        :param pic_array: a list of desired picture times, defaults to None
        :type pic_array: list, optional
        """
        self.__is_picture = 1 
        if (n_pic != 0):
            self.__pic = np.linspace(0,self.ending_time,n_pic)
        else:
            self.__pic = pic_array
    
    @property
    def name(self):
        """
        The name of the simulation.

        :getter: Returns this simulation's name
        :setter: Sets this simulation's name
        :type: string
        """
        return self.__name

    @name.setter 
    def name(self,name):
        self.__name = name 

    @property
    def starting_time(self):
        """Time corresponding to the beginning of the simulation

        :getter: Returns starting time of the simulation
        :setter: Sets simulation starting time
        :type: float
        """
        return self.__starting_time

    @starting_time.setter
    def starting_time(self,starting_time):
        self.__starting_time = starting_time

    @property
    def ending_time(self):
        """Time corresponding to the end of the simulation

        :getter: Returns ending time of the simulation
        :setter: Sets simulation ending time
        :type: float
        """
        return self.__ending_time

    @ending_time.setter
    def ending_time(self,ending_time):
        self.__ending_time = ending_time

    @property
    def Cfl_number(self):
        """Convergence condition by Courant-Friedrichs-Lewy
            Must always be below 1

        :getter: Returns Courant-Friedrichs-Lewy number
        :setter: Sets Courant-Friedrichs-Lewy number
        :type: float
        """
        return self.__Cfl 

    @Cfl_number.setter    
    def Cfl_number(self,Cfl):
        self.__Cfl = Cfl

    @property
    def physical_model(self):
        """Assigns a physical model : you must decide to use only hydrodynamics or sediments...

        :getter: returns the physical model tag
        :setter: Sets Physical model tag: Hydrodynamics, sediments (1, 2,..)
        :type: int
        """
        return self.__physical_model
    
    @physical_model.setter
    def physical_model(self, physical_model_tag):
        self.__physical_model = physical_model_tag
        
    @property
    def flux_scheme(self):
        """Scheme used to compute the fluxes at the interfaces of the mesh
            FOR THE MOMENT ONLY 1 CORRESPONDING TO HLLC

        :getter: returns the flux scheme
        :setter: Sets scheme used to compute the fluxes at the interfaces of each edge (1, 2 or more)
        :type: int
        """
        return self.__flux_scheme

    @flux_scheme.setter
    def flux_scheme(self,flux_scheme):
        self.__flux_scheme = flux_scheme
    
    @property
    def flux_order(self):
        """order used to compute the fluxes

        :getter: returns the order used to compute the fluxes
        :setter: Sets the order used to compute the fluxes (1 or 2)
        :type: int (default : 1)
        """
        return self.__flux_order

    @flux_order.setter
    def flux_order(self,flux_order):
        self.__flux_order = flux_order
    
    @property
    def slope_limiter(self):
        """ This function assigns slope_limiter

        :getter: returns the slope_limiter
        :setter: 1 or 2 ???
        :type: int (default : 1)
        """
        return self.__slope_limiter

    @slope_limiter.setter
    def slope_limiter(self,slope_limiter):
        self.__slope_limiter = slope_limiter

    @property 
    def is_fixed_bed_level(self):
        """Indicates to the c++ code if there is a fixed bed level
        :return: 0 or 1 
        :rtype: Boolean of type int (0,1)
        """
        return self.__is_fixed_bed_level

    @property
    def is_friction(self):
        """Indicates to the c++ code if there is friction to be considered

        :return: 0 or 1 
        :rtype: Boolean of type int (0,1)
        """
        return self.__is_friction    
    
    @property
    def is_sediment(self):
        """Indicates to the c++ code if there is sediments must be considered

        :return: 0 or 1 
        :rtype: Boolean of type int (0,1)
        """
        return self.__is_sediment

    @property    
    def is_initial_sediment_level(self):
        """Indicates to the c++ code the initial level of the sediments

        :return: 0 or 1 
        :rtype: Boolean of type int (0,1)
        """
        return self.__is_initial_sediment_level

    @property
    def sediment_mean_grain_diameter(self):
        """Sediment mean grain diameter 

        :getter: returns mean diameter of the sediments grain
        :setter: sets the mean diameter of the sediments grain
        :type: float
        """
        return self.__g_d50

    @sediment_mean_grain_diameter.setter
    def sediment_mean_grain_diameter(self,g_d50):
        self.__g_d50 = g_d50

    @property
    def sediment_density(self):
        """Sediment grain density
        
        :getter: returns the density sediments grain
        :setter: sets the density of the sediments grain
        :type: float
        """
        return self.__g_sed_density

    @sediment_density.setter
    def sediment_density(self,sed_density):
        self.__g_sed_density = sed_density
    
    @property
    def sediment_friction_coefficient(self):
        """Sediment friction coefficient of Manning Type
        
        :getter: returns the sediments friction coefficient
        :setter: sets the sediments friction coefficient
        :type: float
        """
        return self.__g_sed_manning
    
    @sediment_friction_coefficient.setter
    def sediment_friction_coefficient(self,g_sed_manning):
        self.__g_sed_manning = g_sed_manning
    
    @property
    def sediment_porosity(self):
        """Sediment porosity
        
        :getter: returns the sediments porosity
        :setter: sets the sediments porosity : default 0.4
        :type: float
        """
        return self.__g_sed_porosity
    
    @sediment_porosity.setter
    def sediment_porosity(self,g_sed_porosity):
        self.__g_sed_porosity = g_sed_porosity
    
    @property
    def is_bank_failure(self):
        """Indicates to the c++ code if the bank failure module must be considered

        :return: 0 or 1 
        :rtype: Boolean of type int (0,1)
        """
        return self.__is_bank_failure
    
    @property
    def bank_failure_method(self):
        """ This property allows to choose for a desired bank failure method
            1: Centroid, 2: Voronoi
        
        :getter: access to the selected bank failure method tag
        :setter: impose the selected bank failure method
        :type: int
        """
        return self.__bank_failure_method
    
    @bank_failure_method.setter
    def bank_failure_method(self, bank_failure_method):
        self.__is_bank_failure = 1 
        self.__bank_failure_method = bank_failure_method
    
    @property
    def critical_emmerged_friction_angle(self):
        """ The critical emmerged friction angle has to be used with the bank failure module
            It describes the stability angle of an emmerged part of sediments
            This value has to be greater than the residual friction angle
            
        :getter: returns the value of the emmerged friction angle
        :setter: impose the emmerged friction angle
        :type: float
        """
        return self.__critical_emmerged_friction_angle
    
    @critical_emmerged_friction_angle.setter
    def critical_emmerged_friction_angle(self,phi_ce):
        self.__critical_emmerged_friction_angle = phi_ce

    @property
    def critical_immerged_friction_angle(self):
        """ The critical immerged friction angle has to be used with the bank failure module
            It describes the stability angle of an immerged part of sediments
            This value has to be greater than the residual friction angle
            
        :getter: returns the value of the immerged friction angle
        :setter: impose the immerged friction angle
        :type: float
        """
        return self.__critical_immerged_friction_angle
    
    @critical_immerged_friction_angle.setter
    def critical_immerged_friction_angle(self,phi_ci):
        self.__critical_immerged_friction_angle = phi_ci

    @property
    def residual_emmerged_friction_angle(self):
        """ The residual emmerged friction angle has to be used with the bank failure module
            It describes the residual stability angle of an emmerged part of sediments
            This value has to be lower than the critical friction angle
            
        :getter: returns the residual value of the emmerged friction angle
        :setter: impose the residual emmerged friction angle
        :type: float
        """
        return self.__residual_emmerged_friction_angle
    
    @residual_emmerged_friction_angle.setter
    def residual_emmerged_friction_angle(self,phi_re):
        self.__residual_emmerged_friction_angle = phi_re

    @property
    def residual_immerged_friction_angle(self):
        """ The residual immerged friction angle has to be used with the bank failure module
            It describes the residual stability angle of an immerged part of sediments
            This value has to be lower than the critical friction angle
            
        :getter: returns the residual value of the immerged friction angle
        :setter: impose the residual immerged friction angle
        :type: float
        """
        return self.__residual_immerged_friction_angle
    
    @residual_immerged_friction_angle.setter
    def residual_immerged_friction_angle(self,phi_ri):
        self.__residual_immerged_friction_angle = phi_ri
    
    @property
    def is_sediment_conservation(self):
        """
        1 if we check mass conservation and 0 if not
        :getter: returns a int type boolean that indicates if mass conservation has to be checked
        :setter: impose int type boolean value
        :type: int
        """
        return self.__is_sediment_conservation
    
    @is_sediment_conservation.setter
    def is_sediment_conservation(self,is_sediment_conservation):
        self.__is_sediment_conservation = is_sediment_conservation

    @property
    def time_step_enveloppe(self):
        """
        time interval dt used for the computation of the enveloppe of results 
        The enveloppe corresponds to the maximum values of height and velocities for each cell of the 
        computationnal domain  
        :getter: returns the enveloppe time step
        :setter: sets a desired enveloppe time step
        :type: float
        """
        return self.__dt_enveloppe
    
    @time_step_enveloppe.setter
    def time_step_enveloppe(self,dt_enveloppe):
        self.__dt_enveloppe = dt_enveloppe

    @property
    def is_picture(self):
        """
        Boolean of type int. 
        1 if pictures of results are needed,
        0 if not 
        :return: 0 or 1 
        :rtype: int
        """
        return self.__is_picture

    def set_gauge(self, gauge_position = [], time_step =1):
        """ The method allows to put a measurement gauge at a desired place
        A gauge file will be generated in the output folder

        :param gauge_position: list [[X1,Y1,Z1],[X2,Y2,Z2]] of the chosen gauges positions, defaults to []
        :type gauge_position: list, optional
        :param time_step: time step for measurement, defaults to 1
        :type time_step: int, optional
        """
       
        self.__is_gauge = 1 
        self._gauge = gauge_position 
        self._gauge_time_step = time_step

    def set_discharge_measurement_section(self,section_name=None,time_step=1):
        """Tool to control the discharge across a section 

        :param section_name: string or int corresponding to the tag of the desired boundary or interior line in the mesh, defaults to None
        :type section_name: string or int , optional
        :param time_step: time step used to measure the discharge accross the section, defaults to 1
        :type time_step: int, optional
        :raises Exception: throws exception if the boundary does not exist 
        """
        if isinstance(section_name, str): section_name = [section_name]
        for section in section_name: 
            boundary_tag = self.__mesh.get_boundary_by_name(section) if isinstance(section,str) else section
            if not(boundary_tag in list(self.__mesh.boundaries.keys())):
                raise Exception("There is no such boundary in boundaries. Boundary tag: "+str(section))
            self.__discharge_measurement_edges[section] = self.__mesh.boundary_edges[boundary_tag]
            self.__discharge_measurement_time_step = time_step
            self.__is_discharge_measurement_section = 1
   
    @property       
    def discharge_measurement_time_step(self):
        """ 
        :getter: The time-step used to measure the discharge accross the section
        :rtype: int
        """
        return self.__discharge_measurement_time_step

    @property
    def discharge_control_edges(self):
        """ 
        :getter: The edges corresponding to the chosen line
        :rtype: list of edges tags
        """
        return self.__discharge_measurement_edges
 
    @property
    def is_gauge(self):
        """ 
        1 if generate a gauge was placed and 0 if not
        :getter: 1 or 0
        :rtype: boolean of type int
        """
        return self.__is_gauge
    
    @property
    def is_discharge_measurement_section(self):
        """ 
        1 if generate a discharge measurement section was placed and 0 if not
        :getter: 1 or 0
        :rtype: boolean of type int
        """
        return self.__is_discharge_measurement_section 

    def __add_conditions(self,tags,values,region_tag,condition_type):
        """Adds the cell tags tags and their values values to the
        condition condition_type"""
        self.__conditions[condition_type][0].extend(tags)
        self.__conditions[condition_type][1].extend(values)
        self.__conditions_regions[condition_type].append(region_tag)

    def __replace_conditions(self,tags,values,condition_type):
        """Replace the existing initial conditions of cells (tags) with
        the values values in the condition condition_type"""
        # get
        conditions_values = np.array(self.__conditions[condition_type][1],dtype=float)
        conditions_tags = self.__conditions[condition_type][0]

        # replacement        
        conditions_values[np.isin(conditions_tags,tags)] = values
        self.__conditions[condition_type][1] = conditions_values.tolist()

    def __create_conditions(self,tags,values,region_tag,condition_type):
        """Creates the condiitons with tags, values"""
        self.__conditions[condition_type] = [tags,values]
        self.__conditions_regions[condition_type] = [region_tag]

    def __update_conditions(self,tags,values,region_tag,condition_type):
        """Updates conditions corresponding to the status (add, replace, create)"""
        if condition_type in self.__conditions:
            if region_tag in self.__conditions_regions[condition_type]:
                # Override the existing condition
                self.__replace_conditions(tags,values,condition_type)
            else:
                self.__add_conditions(tags,values,region_tag,condition_type)
        else:
            # brand new condition of this type ;-)
            self.__create_conditions(tags,values,region_tag,condition_type)

    def __set_initial_condition(self,region,value,condition_type):
        """Sets the initial condition value to the cells of a region.

        Parameters
        ----------
        region: the region name (string) or the region tag (int)
        value: the value to be given to the cells. All the cells of the region will get the same value.
        type (cst string): the type of initial condition.

        Returns
        -------
        updates the initial_conditons dictionnary with the tags of the cells and 
        the values associated to them, in the given type
        """
        region_tag = self.__mesh.get_region_by_name(region) if isinstance(region,str) else region
        if not(region_tag in list(self.__mesh.regions.keys())):
            raise Exception("There is no such region in regions. Region tag: "+str(region))

        tags = self.__mesh.region_cells[region_tag].tolist()
        if type(value)==list and len(value)==np.size(tags):
             values = value
        else: 
             values = [value]*np.size(tags)
        self.__update_conditions(tags,values,region_tag,condition_type)
    
    def __set_boundary_condition(self,boundary,value,condition_type):
        """Sets the boundary condition value to the edges of a boundary.

        Parameters
        ----------
        boundary: the boundary name (string) or the boundary tag (int)
        value: the value to be given to the edges. All the edges of the boundary will get the same value.

        Returns
        -------
        tags, values: the tags of the edges of the boundary and the values associated to them.
        """
        boundary_tag = self.__mesh.get_boundary_by_name(boundary) if isinstance(boundary,str) else boundary
        if not(boundary_tag in list(self.__mesh.boundaries.keys())):
            raise Exception("There is no such boundary in boundaries. Boundary tag: "+str(boundary))

        tags = self.__mesh.boundary_edges[boundary_tag].tolist()
        values = [value]*np.size(tags)
        
        self.__update_conditions(tags,values,boundary_tag,condition_type)

    def __set_initial_conditions(self,regions,values,condition_type):
        """Sets the initial condition values to the cells the domain.

        Parameters
        ----------
        regions (list): the regions names (string) or the regions tags (int)
        value (list): the values to be given to the cells in the correspondint region. 
                      All the cells of the region will get the same value.
        type (cst string): the type of initial condition.

        Returns
        -------
        updates the initial_conditons dictionnary with the tags of the cells and 
        the values associated to them, in the given type
        """
        if isinstance(regions,str):
            self.__set_initial_condition(regions,values,condition_type)
        else:
            for i in range(len(regions)):
                self.__set_initial_condition(regions[i],values[i],condition_type)

    def __set_boundary_conditions(self,boundaries,values,condition_type):
        """Sets the initial condition values to the edges in the domain.

        Parameters
        ----------
        boundaries (list): the boundary names (string) or the boundary tags (int)
        value (list): the values to be given to the edges in the corresponding boundary. 
                      All the edges of the boundary will get the same value.

        Returns
        -------
        tags, values: the tags of the edges and the values associated to them.
        """
        if isinstance(boundaries,str):
            self.__set_boundary_condition(boundaries,values,condition_type)
        else:
            for i in range(len(boundaries)):
                self.__set_boundary_condition(boundaries[i],values[i],condition_type)

    def set_initial_water_height(self,regions,water_heights):
        """Sets the initial water height to the cells in the domain.    
           If only one value is given, all cells will get the same value.

        :param regions: the regions names (string) or the regions tags (int)
        :type regions: string or int
        :param water_heights: the values to be given to the cells in the correspondant region. 
        :type water_heights: float or list
        """
        tags = []
        def __initial_water_height(tags,water_heights,region):
            region_indexes = [self.__mesh.tag_to_indexes.get(tag) for tag in tags]
            # get the right bedrock levels
            initial_conditions = self.get_initial_conditions()
            if _BEDROCK_LEVEL in initial_conditions.keys():
                tags_bedrock_level =  initial_conditions[_BEDROCK_LEVEL][0]
                indexes_bedrock_level =  [self.__mesh.tag_to_indexes.get(tag) for tag in tags_bedrock_level if np.isin(tag,region_indexes)] #allows to take the right indexes corresponding to the already imposed bedrock_levels
                bedrock_level = np.asarray(initial_conditions[_BEDROCK_LEVEL][1])[indexes_bedrock_level]
            else:
                bedrock_level = self.__mesh.get_cells_barycenters()[region_indexes,2]
            #evaluate water levels, since water levels are the initial condition
            if isinstance(water_heights,(int, float)) :
                water_levels = water_heights*np.ones(len(region_indexes))+bedrock_level
            else: 
                water_levels = water_heights+bedrock_level
            water_levels[np.asarray(water_heights)<10**(-2)] = 0
            self.__set_initial_conditions(region,water_levels.tolist(),_INITIAL_WATER_LEVEL)
            
        if isinstance(regions,list) or isinstance(regions,tuple):
            for index,region in enumerate(regions): 
                tags = self.__mesh.region_cells[self.__mesh.get_region_by_name(region)] 
                __initial_water_height(tags,water_heights[index],region)
        else:  
            tags = self.__mesh.region_cells[self.__mesh.get_region_by_name(regions)] 
            __initial_water_height(tags,water_heights,regions)      
        
    def set_initial_water_level(self,regions,water_levels):
        """Sets the initial water levels to the cells in the domain.
           If only one value is given, all cells will get the same value.

        :param regions: the regions names (string) or the regions tags (int)
        :type regions: string or int
        :param water_levels: the values to be given to the cells in the correspondant region. 
        :type water_levels: float or list
        """
        self.__set_initial_conditions(regions,water_levels, _INITIAL_WATER_LEVEL)

    def set_initial_water_discharge(self,regions,discharges):
        """Sets the initial water levels to the cells in the domain.
           If only one value is given, all cells will get the same value.

        :param regions: the regions names (string) or the regions tags (int)
        :type regions: string or int
        :param discharges: the values to be given to the cells in the correspondint region. 
                           Each entry must be composed of two elements (discharge x and discharge y).
        :type discharges: List
        """
        self.__set_initial_conditions(regions,discharges,_INITIAL_WATER_DISCHARGE)

    def set_initial_sediments_level(self,region,sediment_levels=0,slope=False,x_imposed=[],y_imposed=[],z_imposed=[],level_fun=None):
        """Sets the initial sediment levels for a given region.
        If only one value is given, all cells will get the same value.

        :param regions: the regions names (string) or the regions tags (int)
        :type regions: string or int
        :param sediment_levels: The initial sediment levels to be set, defaults to 0
        :type sediment_levels: int, optional
        :param slope: Flag to indicate if the sediment levels should be set according to a slope. Defaults to False.
        :type slope: bool, optional
        :param x_imposed: List of x-coordinates for the points defining the slope. Required if slope is True., defaults to []
        :type x_imposed: list, optional
        :param y_imposed: List of y-coordinates for the points defining the slope. Required if slope is True., defaults to []
        :type y_imposed: list, optional
        :param z_imposed: List of z-coordinates (sediment levels) for the points defining the slope. Required if slope is True., defaults to []
        :type z_imposed: list, optional
        :param level_fun: function to described the sediments levels, defaults to None
        :type level_fun: function, optional
        :raises Exception: If region is a string and there is no region with the given name in the regions list.
        """
        self.__is_sediment = 1 
        self.__is_initial_sediment_level = 1 
        if slope == False and level_fun is None: 
            self.__set_initial_conditions(region,sediment_levels,_INITIAL_SEDIMENTS_LEVEL)
        else:
            region_tag = self.__mesh.get_region_by_name(region) if isinstance(region,str) else region
            if not(region_tag in list(self.__mesh.regions.keys())):
                raise Exception("There is no such region in regions. Region tag: "+str(region))

            cell_tags = self.__mesh.region_cells[region_tag].tolist()
            indexes = cell_tags - self.__mesh.cells[0][0]

            X = self.__mesh.get_cells_barycenters()[indexes,0]
            Y = self.__mesh.get_cells_barycenters()[indexes,1]
            if slope == True:
                sediment_levels = griddata((x_imposed, y_imposed), z_imposed, (X, Y), method='linear').tolist()
            else:
                sediment_levels = list(map(level_fun,X,Y))
            self.__set_initial_conditions(region,sediment_levels,_INITIAL_SEDIMENTS_LEVEL)

    def set_bedrock_level(self,regions,bedrock_levels):
        """Sets the initial bedrock level to the cells in the domain.
        
        :param bedrock_levels: the values to be given to the cells in the corresponding region. 
        :type bedrock_levels: float or list
        """
        self.__is_fixed_bed_level = 1
        self.__set_initial_conditions(regions,bedrock_levels,_BEDROCK_LEVEL)
    
    def set_friction_coefficient(self,regions,friction_coefficients):
        """Sets the friction coefficients associated to each cell in the domain.
        If only one value is given, all cells will get the same value.

        :param regions: the regions names (string) or the regions tags (int)
        :type regions: string or int
        :param friction_coefficients: the values to be given to the cells in the corresponding region. 
        :type friction_coefficients: float or list
        """
        self.__is_friction = 1 
        self.__set_initial_conditions(regions,friction_coefficients,_FRICTION_COEFFICIENTS)
    
    def set_fixed_banks(self,regions):
        """
        IN CONSTRUCTION
        Defines if (True or False) the cell can be eroded or not.

        :param regions: (list) the regions names (string) or the regions tags (int)
        :param is_bank_fixed: (list) the values to be given to the cells in 
            the correspondint region. All the cells of the region will get the same value.
        :returns: (method)
        """
        # fictive value for fixed banks
        values = True if np.size(regions) == 1 else [True]*np.size(regions)
        self.__set_initial_conditions(regions,values,_FIXED_BANKS)

    def set_transmissive_boundaries(self,boundaries):
        """Defines which edges behave like a transmissive interfaces.


        :param boundaries: the boundary names (string) or the boundary tags (int)
                           where the edges behave like transmissive interfaces.
        :type boundaries: string or int
        """
        # fictive value for transmissive boundaries
        values = True if np.size(boundaries) == 1 else [True]*np.size(boundaries)
        self.__set_boundary_conditions(boundaries,values,_TRANSMISSIVE_BOUNDARIES)

    def set_boundary_water_level(self,boundaries,water_levels):
        """Defines the imposed water level at edges of the boundaries.
        
        :param boundaries: the boundary names (string) or the boundary tags (int)
        :type boundaries: string or tag
        :param water_levels: the values to be given to the edges in the corresponding boundary.
        :type water_levels: float or list
        """
        self.__set_boundary_conditions(boundaries,water_levels,_BOUNDARY_WATER_LEVEL)

    def set_boundary_water_discharge(self,boundaries,water_discharges):
        """Defines the imposed water discharge through the edges of the boundaries.
        You must introduce the total discharge. Positive value flows in the system
        
        :param boundaries: the boundary names (string) or the boundary tags (int)
        :type boundaries: string or int
        :param water_discharges: the values to be given to the edges in the corresponding boundary.
        :type water_discharges: float or list
        """
        def __corrected_water_discharge(boundary,water_discharge):
            boundary_length = self.__mesh.get_boundary_length(boundary)
            return -water_discharge/boundary_length
            
        if isinstance(boundaries,list) or isinstance(boundaries,tuple):
            for i,boundary in enumerate(boundaries):
                water_discharge = __corrected_water_discharge(boundary,water_discharges[i])
                self.__set_boundary_conditions(boundary,water_discharge,_BOUNDARY_WATER_DISCHARGE)
        else:
            self.__set_boundary_conditions(boundaries,__corrected_water_discharge(boundaries,water_discharges),_BOUNDARY_WATER_DISCHARGE)
            
    def set_boundary_sediments_discharge(self,boundaries,sediments_discharges):
        """Defines the imposed sediment discharge through the edges of the boundaries.
        You must introduce a negative flux and a flux/m of boundary
        
        :param boundaries: the boundary names (string) or the boundary tags (int)
        :type boundaries: string or int
        :param sediments_discharges: the values to be given to the edges in the corresponding boundary.
        :type sediments_discharges: float or list
        """
        self.__is_sediment = 1 
        self.__set_boundary_conditions(boundaries,sediments_discharges,_BOUNDARY_SEDIMENTS_DISCHARGE)
        
    def set_boundary_hydrogram(self,boundaries,hydrogram_paths):
        """Sets a hydrogram type of boundary condition
        Your file must be organized as follows : 
        nData : 
        t0 -Q0
        t1 -Q1
        t2 -Q3 etc....
        
        :param boundaries: the boundary names (string) or the boundary tags (int)
        :type boundaries: string or int
        :param hydrogram_paths: the paths of the hydrograms associated to the edges 
                                in the corresponding boundary.
        :type hydrogram_paths: string or list
        """
        self.__set_boundary_conditions(boundaries,hydrogram_paths,_BOUNDARY_HYDROGRAM)

    def set_boundary_limnigram(self,boundaries,limnigram_paths):
        """Sets a limnigram type of boundary condition
        
        :param boundaries: the boundary names (string) or the boundary tags (int)
        :type boundaries: string or int
        :param limnigram_paths: the paths of the limnigrams associated to the edges 
                                in the corresponding boundary.
        :type limnigram_paths: string or list
        """
        self.__set_boundary_conditions(boundaries,limnigram_paths,_BOUNDARY_LIMNIGRAM)

    def get_conditions(self,wanted_keys):
        """Returns all boundary or initial conditions imposed by the user

        :param wanted_keys: type of condition desired 
        :type wanted_keys: string
        :return: values of the conditions
        :rtype: key : value type 
        """
        # find which condition types are activated
        mask = np.isin(list(self.__conditions.keys()),wanted_keys)
        return { condition_type: self.__conditions.get(condition_type) for condition_type in np.array(list(self.__conditions.keys()))[mask] }

    def get_initial_conditions(self):
        """Returns the initial conditions in a dictionary"""
        initial_conditions_keys = [ _INITIAL_WATER_LEVEL, 
                                    _INITIAL_WATER_DISCHARGE, 
                                    _INITIAL_SEDIMENTS_LEVEL,
                                    _BEDROCK_LEVEL,
                                    _FRICTION_COEFFICIENTS,
                                    _FIXED_BANKS ]
        conditions = self.get_conditions(initial_conditions_keys)

        # remove fictive values from initial conditions
        keys = self.__conditions.keys()
        if _FIXED_BANKS in keys:
            conditions[_FIXED_BANKS] = conditions[_FIXED_BANKS][0]
        
        return conditions

    def get_boundary_conditions(self):
        """Returns the boundary conditions in a dictionary"""
        boundary_conditions_keys = [_TRANSMISSIVE_BOUNDARIES, 
                                    _BOUNDARY_WATER_LEVEL, 
                                    _BOUNDARY_WATER_DISCHARGE,
                                    _BOUNDARY_SEDIMENTS_DISCHARGE,
                                    _BOUNDARY_HYDROGRAM,
                                    _BOUNDARY_LIMNIGRAM]
        conditions = self.get_conditions(boundary_conditions_keys)

        # remove fictive value from transmissive boundaries
        keys = self.__conditions.keys()
        if _TRANSMISSIVE_BOUNDARIES in keys:
            conditions[_TRANSMISSIVE_BOUNDARIES] = conditions[_TRANSMISSIVE_BOUNDARIES][0]
        return conditions
    
    def __launch_code(self,display=True,isParallel=False):
        """
        This function launches the Hydroflow code.
        It first checks if the Hydroflow code exists in the Hydroflow folder.
        If it does not exist, it compiles the code.
        Then, it launches the Hydroflow code.
        The Hydroflow code is launched with the following input:
        - the path to the data.txt file
        """

        if os.path.exists(os.path.join(_dir_path_to_executable,_HYDROFLOW_EXECUTABLE)):
            if display: print(_HYDROFLOW_EXECUTABLE + " exists")
        else:
            if display: print("The code is being compiled...")
            _compile_code(isParallel=isParallel)
            
        if display: print("Launching the executable ...")  
        
        data_file_path = os.path.join(self.export._INPUT_FOLDER_NAME, _DATA_FILE)
        executable_cmd = os.path.join(_dir_path_to_executable, _HYDROFLOW_EXECUTABLE)

        args = [executable_cmd, '-f', data_file_path]
        
        process = subprocess.Popen(args, 
                                   stdout = subprocess.PIPE, 
                                   stderr = subprocess.STDOUT,
                                   cwd = self.__current_path,
                                   universal_newlines=True, 
                                   text = True)
        if display:
            for line in iter(process.stdout.readline, ""):
                sys.stdout.write('\r'+line[:-1])
                sys.stdout.flush()
            
        process.wait()

class Plotter():
    def __init__(self,msh_mesh: Mesh):
        """
        
        """
        self.__mesh = msh_mesh
        self.__cells_nodes = self.__mesh.cells[1]-1
        self.__nodes_coord = self.__mesh.nodes[1]
        self.__triangle_organization =  mtri.Triangulation(self.__nodes_coord[:,0],self.__nodes_coord[:,1],self.__cells_nodes)
        self.__value_at_node = None
    
    @property
    def values_at_nodes(self):
        """
        Returns
        -------
        Values at nodes of the variable
        """
        return self.__value_at_node
        
    def __set_value_at_node(self,values):
        """
        Since the solver is a FV solver, the unknowns are at the cell's centers. 
        --------
        This function interpolates values of the desired plotted infos at nodes
        --------- 
        In : values np array : size nCells
        """ 
        X_barycenters, Y_barycenters = self.__mesh.get_cells_barycenters()[:,0], self.__mesh.get_cells_barycenters()[:,1]
        points = np.column_stack((X_barycenters.flatten(), Y_barycenters.flatten()))
        values = values.flatten()
        mesh_x, mesh_y = self.__mesh.nodes[1][:,0], self.__mesh.nodes[1][:,1]
        mesh_points = np.column_stack((mesh_x.flatten(), mesh_y.flatten()))
        nearest_grid = griddata(points, values, mesh_points, method='nearest')
        self.__value_at_node = griddata(points, values, mesh_points, method='linear')
        self.__value_at_node[np.isnan(self.__value_at_node)] = nearest_grid[np.isnan(self.__value_at_node)] 
    
    def __extract_data_from_picture_file(self,file):
        data = np.loadtxt(file,skiprows=1)
        bedrock_level,water_height,q_x,q_y = data[:,2],data[:,3],data[:,4],data[:,5]
        return bedrock_level,water_height,q_x,q_y
    
    def plot_profile_along_line(self, picture_file_path:str, x_coordinate = None , y_coordinate = None , new_fig = False, variable_name = "Water level", n_points = 50, label="")-> None:
        """ 
        Plot the profile of the selected variable along a line between given coordinates points.
    
        :param picture_file_path: the path to the selected pic file to plot
        :type picture_file_path: string      
        :param x_coordinate: x_coordinate = [x_P1 x_P2]
        :type x_coordinate: list or ndArray
        :param y_coordinate: y_coordinate = [y_P1 y_P2]
        :type y_coordinate: list or ndArray
        :param new_fig: True: create a new figure
                    False: plot on the current figure , defaults to False
        :type new_fig: bool, optional
        :param variable_name: Name the plotted variable, defaults to "Water height"
                               Other options : q_x, q_y 
        :type variable_name: str, optional
        :param n_points: number of interpolation points, defaults to 50
        :type n_points: int, optional
        :param label: string corresponding to the label of the figure, defaults to ""
        :type label: str, optional
        """
        if new_fig:
            plt.figure()
        bedrock_level,water_height,q_x,q_y = self.__extract_data_from_picture_file(picture_file_path)
        data = {"bedrock level": bedrock_level,"Water height": water_height, "Water level" : water_height+bedrock_level,
                                                                    "q_x":q_x,"q_y":q_y}[variable_name]
        self.__set_value_at_node(data)
        interpolated_plane_value = mtri.LinearTriInterpolator(self.__triangle_organization,self.__value_at_node)
        self.__set_value_at_node(bedrock_level)
        interpolated_plane_zb = mtri.LinearTriInterpolator(self.__triangle_organization,self.__value_at_node)
        x, y = np.linspace(x_coordinate[0],x_coordinate[1],n_points), np.linspace(y_coordinate[0],y_coordinate[1],n_points)
        profile_values, profile_zb = interpolated_plane_value(x,y), interpolated_plane_zb(x,y) 
        abscisses = np.linspace(0,np.sqrt((x_coordinate[1]-x_coordinate[0])**2+(y_coordinate[1]-y_coordinate[0])**2),n_points)        
        plt.plot(abscisses,profile_values,label=label)
        plt.plot(abscisses,profile_zb,label="Bedrock")
        plt.legend()
        plt.show()
        
    def plot(self, picture_file_path, variable_name = "Water level", velocities = False, velocity_ds =1, scale = 1,opacity=1,vmax=0,show=True):
        """ This is a basic plot function with a series of args
            Press m will show the mesh on the plot
            Press d and left click on two different locations will pop up a cut in your plot
         
        :param pic_path: the path to the selected pic file to plot
        :type pic_path: string      
        :param variable_name: Name the plotted variable, defaults to "Water level"
                               Other options : q_x, q_y 
        :type variable_name: str, optional
        :param velocities: If true, the velocities will be plotted as a quiver, defaults to False
        :type velocities: bool, optional
        :param velocity_ds: velocity downsampling : a value [0,1]
                            corresponding to the percentage of arrows to be seen on the map, defaults to 1
        :type velocity_ds: int, optional
        :param scale: value to modify the length of arrows (quiver), defaults to 1
        :type scale: int, optional
        :param opacity: A value [0,1] to change the opacity of the plot, defaults to 1
        :type opacity: int, optional
        :param vmax: maximum value of the colorbar, defaults to 0
        :type vmax: int, optional
        :param show: if true plt.show is activated, defaults to True
        :type show: boolean
        """        
        plt.figure()
        
        def __on_clicked(event):
            global coords_x
            global coords_y
            ix, iy = event.xdata, event.ydata
            coords_x.append(ix)
            coords_y.append(iy)
            if len(coords_x)==2:
                plt.plot(coords_x,coords_y,color='red')
                plt.draw()
                print(coords_x,coords_y)
                self.plot_profile_along_line(picture_file_path, coords_x, coords_y,new_fig=True, variable_name="Water level", n_points = 50, label="water level [m]")
                plt.gcf().canvas.mpl_disconnect(__on_clicked)
                plt.gcf().canvas.mpl_connect('key_press_event', __on_press)

        def __on_press(event):
            global coords_x
            global coords_y
            print('press', event.key)
            sys.stdout.flush()
            if event.key == 'd':
                plt.gcf().canvas.mpl_disconnect(__on_press)
                coords_x = []
                coords_y = []
                plt.gcf().canvas.mpl_connect('button_press_event', __on_clicked)
            if event.key == 'm':
                plt.triplot(self.__triangle_organization,lw=0.1)
                self.__triangle_visible = True

        bedrock_level,water_height,q_x,q_y = self.__extract_data_from_picture_file(picture_file_path)
        data = {"bedrock level": bedrock_level,"Water height": water_height, "Water level" : water_height+bedrock_level,
                                                                    "q_x":q_x,"q_y":q_y}[variable_name]
        plt.gcf().canvas.mpl_connect('key_press_event', __on_press)
        
        if vmax==0:
            levels = np.linspace(0.001,max(data), 100)
        else: 
            levels = np.linspace(0.001,vmax,100)
            
        self.__set_value_at_node(data)
        try : 
            TC = plt.tricontourf(self.__triangle_organization,self.__value_at_node,alpha=opacity,cmap=cm.turbo,levels=levels,antialiased=True,extend="max")
            plt.gca().set_aspect('equal', adjustable='box')
            cbar= plt.colorbar(TC)
            cbar.set_label(variable_name)
        except ValueError:
            print("Contour lines must be increasing, error has been catched") 
        
        if velocities:
            X, Y = self.__mesh.get_cells_barycenters()[:,0], self.__mesh.get_cells_barycenters()[:,1]
            v_x = q_x/water_height
            v_y = q_y/water_height
            N = int(1/velocity_ds)
            plt.quiver(X[::N],Y[::N],v_x[::N],v_y[::N],scale = scale)
        if show:
          plt.show()

    def plot_on_map(self, pic_path, variable_name = "Water level", velocities = False,velocity_ds=1, scale = 1,opacity=0.5,vmax=0, csr=31370,show=True):
        """ The function plots on a specified coordinate system map 

        :param pic_path: the path to the selected pic file to plot
        :type pic_path: string
        :param variable_name: Name the plotted variable, defaults to "Water level"
                               Other options : q_x, q_y 
        :type variable_name: str, optional
        :param velocities: If true, the velocities will be plotted as a quiver, defaults to False
        :type velocities: bool, optional
        :param velocity_ds: velocity downsampling : a value [0,1]
                            corresponding to the percentage of arrows to be seen on the map, defaults to 1
        :type velocity_ds: int, optional
        :param scale: value to modify the length of arrows (quiver), defaults to 1
        :type scale: int, optional
        :param opacity: A value [0,1] to change the opacity of the plot, defaults to 1
        :type opacity: int, optional
        :param vmax: maximum value of the colorbar, defaults to 0
        :type vmax: int, optional
        :param csr: user specified coordinate reference system, defaults to 31370 for belgium
        :type csr: int, optional
        :param show: if true plt.show is activated, defaults to True
        :type show: boolean
        """
        self.plot(pic_path, variable_name = variable_name, velocities = velocities,velocity_ds = velocity_ds, scale = scale,opacity=opacity,vmax=vmax,show=show)
        ax = plt.gca()
        ctx.add_basemap(ax, crs=csr,source=ctx.providers.OpenStreetMap.Mapnik)
    
    def create_video(self, pic_path_template, video_filename, time_step, variable_name="Water level", velocities=False, velocity_ds=1, scale=1, opacity=1, vmax=0, csr=31370, fps=5,on_map=False):
        """ The function creates a video from a folder of pic file given a certain time step. 

        :param pic_path_template: the template of the pic file. Example : "PathToFiles\pic_{:d}_{:02d}.txt" 
        :type pic_path_template: string
        :param video_filename: user-defined name for the simulation
        :type video_filename: string
        :param time_step: time between the chosen pic files
        :type time_step: int
        :param variable_name: Name the plotted variable, defaults to "Water level"
                               Other options : q_x, q_y 
        :type variable_name: str, optional
        :param velocities: If true, the velocities will be plotted as a quiver, defaults to False
        :type velocities: bool, optional
        :param velocity_ds: velocity downsampling : a value [0,1]
                            corresponding to the percentage of arrows to be seen on the map, defaults to 1
        :type velocity_ds: int, optional
        :param scale: value to modify the length of arrows (quiver), defaults to 1
        :type scale: int, optional
        :param opacity: A value [0,1] to change the opacity of the plot, defaults to 1
        :type opacity: int, optional
        :param vmax: maximum value of the colorbar, defaults to 0
        :type vmax: int, optional
        :param csr: user specified coordinate reference system, defaults to 31370 for belgium
        :type csr: int, optional
        :param fps: frame per seconds for the video, defaults to 5
        :type fps: int, optional
        :param on_map: if true will be plotted on a map, defaults to False
        :type on_map: bool, optional
        """
        file_list = []
        time_second = 0
        time_hundreds = 00

        while os.path.exists(pic_path_template.format(time_second,time_hundreds)):
            file_list.append(pic_path_template.format(time_second,time_hundreds))
            time_second += time_step

        frame_list = []
        n_files = len(file_list)
        print("Building Video frames")

        for i, file in enumerate(file_list):
            if on_map:
                    self.plot_on_map(file, variable_name=variable_name, velocities=velocities, velocity_ds=velocity_ds, scale=scale,vmax=vmax, opacity=opacity, csr=csr,show=False)
            else:
                self.plot(file, variable_name=variable_name, velocities=velocities, velocity_ds=velocity_ds, scale=scale,vmax=vmax, opacity=opacity,show=False)
            plt.savefig("frame_{:d}.png".format(i),dpi=300)
            plt.close()
            frame_list.append("frame_{:d}.png".format(i))
            print("Proceeding:" + str(np.around(i/n_files*100,2))+"%")

        images = []
        for filename in frame_list:
            images.append(imageio.imread(filename))

        imageio.mimsave("{}.mp4".format(video_filename), images, fps=fps)
        print("Your video is ready")
        for frame in frame_list:
            os.remove(frame)


class Export():
    """Exports the input files
    
    :param mesh: a mesh object from the hydroflow lib
    :type mesh: mesh
    :param model: a model object
    :type model: model
    """
    # Class variables 
    _INPUT_FOLDER_NAME = _INPUT_NAME
    _OUTPUT_FOLDER_NAME = _OUTPUT_NAME
    _INPUT_FOLDER_PATH = os.path.join(os.getcwd(), _INPUT_FOLDER_NAME)
    _OUTPUT_FOLDER_PATH = os.path.join(os.getcwd(), _OUTPUT_FOLDER_NAME)

    def __init__(self, mesh: Mesh, model: Model, test = False):
        """Constructs the Mesh object based on an .msh file.
        """
        
        self.__mesh = mesh
        self.__model = model
        self.__folder_path = os.getcwd()
        #create the two input and output folders 
        # if (test):
        #     self.__set_folder_path(os.path.join(os.getcwd(), _TEST_NAME))
        # else:
        
    @property
    def output_folder_path(self):
        """The path of the output folder

        :getter: Returns the path of the output folder
        :type: string
        """
        return self._OUTPUT_FOLDER_PATH

    @property
    def output_folder_name(self):
        """The name of the output folder

        :getter: Returns the name of the output folder
        :setter: Sets the name of the output folder
        :type: string
        """
        return self._OUTPUT_FOLDER_NAME

    @output_folder_name.setter
    def output_folder_name(self,name):
        self._OUTPUT_FOLDER_NAME = name
        self._OUTPUT_FOLDER_PATH = os.path.join(os.getcwd(), self._OUTPUT_FOLDER_NAME)

    @property
    def input_folder_path(self):
        """The path of the input folder

        :getter: Returns the path of the input folder
        :type: string
        """
        return self._INPUT_FOLDER_PATH

    @property
    def input_folder_name(self):
        """The name of the input folder

        :getter: Returns the name of the input folder
        :setter: Sets the name of the input folder
        :type: string
        """
        return self._INPUT_FOLDER_NAME

    @input_folder_name.setter
    def input_folder_name(self,name):
        self._INPUT_FOLDER_NAME = name
        self._INPUT_FOLDER_PATH = os.path.join(os.getcwd(), self._INPUT_FOLDER_NAME)

    def export(self):
        """Export all .txt files in the input folder:
        
        :return: self.__NODES_NAME, self.__CELLS_NAME, self.__EDGES_NAME, self.__INITIAL_CONDITIONS_NAME, self.__FRICTION_NAME
            self.__BOUNDARY_NAME, self.__PICTURE_NAME, self.__DATA_NAME, self.__SEDIMENT_LEVEL_NAME
        :rtype: .txt    
        """
        self.__set_folder_path()
        os.makedirs(self._INPUT_FOLDER_PATH,exist_ok=True)
        os.makedirs(self._OUTPUT_FOLDER_PATH,exist_ok=True)
        self.__export_nodes()
        self.__export_cells()
        self.__export_edges()

        self.__export_initial_conditions()
        self.__export_friction()
        self.__export_sediment_level()
        self.__export_bedrock_level()
        self.__export_fixed_bank()
        self.__export_pic()
        self.__export_gauge()
        self.__export_discharge_measurement_section()
        self.__export_data()

    def get_folder_path(self):
        """Returns the path of the concerned folder

        :return: Path of the working folder
        :rtype: string
        """
        return self.__folder_path
    
    def __set_folder_path(self,folder_path=os.getcwd()):
        """This function assigns a new folder_path and adapts all the paths

        :param folder_path: path of the work folder, default os.getcwd()
        :type folder_path: string
        """
        self.__data_file_path = os.path.join(self._INPUT_FOLDER_NAME,_DATA_FILE)
        self.__nodes_path = os.path.join(self._INPUT_FOLDER_NAME,_NODES_FILE)
        self.__cells_path = os.path.join(self._INPUT_FOLDER_NAME,_CELLS_FILE)
        self.__edges_path = os.path.join(self._INPUT_FOLDER_NAME,_EDGES_FILE)
        self.__slope_limiter_path = os.path.join(self._INPUT_FOLDER_NAME,_SLOPE_FILE)
        self.__initial_condition_path = os.path.join(self._INPUT_FOLDER_NAME,_INITIAL_CONDITIONS_FILE)
        self.__fixed_bed_level_path = os.path.join(self._INPUT_FOLDER_NAME,_FIXED_BED_FILE)
        self.__friction_path = os.path.join(self._INPUT_FOLDER_NAME,_FRICTION_FILE)
        self.__initial_sediment_level_path = os.path.join(self._INPUT_FOLDER_NAME,_SEDIMENT_LEVEL_FILE)
        self.__fixed_bank_path = os.path.join(self._INPUT_FOLDER_NAME,_FIXED_BANK_FILE)
        self.__picture_path = os.path.join(self._INPUT_FOLDER_NAME,_PICTURE_FILE)
        self.__gauge_path = os.path.join(self._INPUT_FOLDER_NAME,_GAUGE_FILE)
        self.__discharge_path = os.path.join(self._INPUT_FOLDER_NAME,_DISCHARGE_FILE)

    def __export_nodes(self):
        """Exports the nodes from the GSMH mesh to a file.

        :return: A text file containing the number of nodes and their coordinates.
            First line: n_nodes
            Each following line is formatted as [x_n, y_n, z_n].
        :rtype: .txt
        """
        fmt = '%1.9f', '%1.9f', '%1.9f'

        myfile = self.__nodes_path
        f = open(myfile,'w')        
        f.write(str(self.__mesh.nNodes) + '\n')
        f.close()

        tags_nodes,nodes = self.__mesh.nodes
        with open(myfile,'ab') as f:
           np.savetxt(f,nodes, delimiter=" ", fmt=fmt)

    def __export_cells(self):
        """Exports the cells from the GSMH mesh to a file.

        :return: A text file containing the number of cells, the number of nodes for each cell and the tags of the corresponding nodes.
            First line: n_cells
            Each following line is formatted as [n_node_of_cell, node_1, node_2, node_3].
        :rtype: .txt
        """
        myfile = self.__cells_path
        
        f = open(myfile ,'w')
        f.write(str(self.__mesh.nCells)+'\n')
        f.close()

        fmt = '%d', '%d', '%d','%d'
        dim = self.__mesh.elem_type*np.ones((self.__mesh.nCells,1)) 
        tags_cells,cells = self.__mesh.cells

        with open(myfile,'ab') as f:
            np.savetxt(f,np.hstack((dim,cells-1)), delimiter=" ", fmt=fmt) 
    
    def __export_edges(self):
        """Exports the edges from the GSMH mesh to a file.

        :return: A text file containing the number of edges, the corresponding nodes and if requested, 
            the left and right adjacent cells.
            First line: n_edges
            Each following line is formatted as [left_cell_tag, right_cell_tag, node_tag_1, node_tag_2].
        :rtype: .txt
        """

        myfile = self.__edges_path
        
        # preparing file
        f = open(myfile,'w')
        f.write(str(self.__mesh.nEdges)+'\n')
        f.close()

        # preparing output
        fmt = '%d', '%d', '%d', '%d', '%s'
        tags,edge_nodes,edge_cells = self.__mesh.edges
        cell_tags, cells = self.__mesh.cells
        edge_cells[edge_cells != -1] = [self.__mesh.tag_to_indexes.get(tag) for tag in edge_cells[edge_cells != -1]]

        output = np.hstack((edge_cells,edge_nodes-1))

        boundary_conditions_code =  {
            _TRANSMISSIVE_BOUNDARIES : -2,
            _BOUNDARY_WATER_LEVEL : -4, 
            _BOUNDARY_WATER_DISCHARGE : -3,
            _BOUNDARY_SEDIMENTS_DISCHARGE : -3,
            _BOUNDARY_HYDROGRAM : -33,
            _BOUNDARY_LIMNIGRAM : -44 }

        used_boundary_conditions = self.__model.get_boundary_conditions().keys()
        bc_value =  np.empty(len(tags),dtype=object)
        bc_value[:] = np.nan

        for condition in used_boundary_conditions: 
            if condition == _TRANSMISSIVE_BOUNDARIES:
                condition_edge = np.asarray(self.__model.get_boundary_conditions()[condition])
                output[condition_edge-1,1] = boundary_conditions_code[condition]
            else:   
                condition_edge = np.asarray(self.__model.get_boundary_conditions()[condition][0])
                condition_value = np.asarray(self.__model.get_boundary_conditions()[condition][1])
                output[condition_edge-1,1] = boundary_conditions_code[condition]
                bc_value[condition_edge-1] = condition_value
        output = pd.DataFrame(output)
        output['new_col'] = bc_value
        output.fillna(value='', inplace=True)

        with open(myfile,'ab') as f:
            np.savetxt(f,output.values, delimiter=" ", fmt=fmt)

    def __export_initial_conditions(self,tag=-1):
        """Exports the water and discharge initial conditions to a file

        :param tag: Negative (default): returns the initial conditions for the cells corresponding to the given data
            Positive: returns all initial conditions
        :type: int
        :return: A text file named after OUTPUT_NAME containing the initial water depth and water discharges for each cells
            Each line is formatted as [h_w, p, q].
        :rtype: .txt
        """
        fmt = '%1.6f','%1.6f','%1.6f'
        initial_conditions = self.__model.get_initial_conditions()
        initial_export_conditions = np.zeros((self.__mesh.nCells,3))

        if _INITIAL_WATER_LEVEL not in initial_conditions:
            pass 
        else:
            water_level = np.array([initial_conditions[_INITIAL_WATER_LEVEL][1]]).T
            water_level_cells_tags = initial_conditions[_INITIAL_WATER_LEVEL][0]
            water_level_cells_index = [self.__mesh.tag_to_indexes.get(tag) for tag in water_level_cells_tags]
            initial_export_conditions[water_level_cells_index,0] = water_level.reshape(len(water_level),)

        if _INITIAL_WATER_DISCHARGE not in initial_conditions:
            pass 
        else:
            discharge = np.array(initial_conditions[_INITIAL_WATER_DISCHARGE][1])
            discharge_cells_tags = initial_conditions[_INITIAL_WATER_DISCHARGE][0]
            discharge_cells_index  = [self.__mesh.tag_to_indexes.get(tag) for tag in discharge_cells_tags]
            initial_export_conditions[discharge_cells_index,1:3] = discharge.reshape(len(discharge),2)

        myfile = self.__initial_condition_path
        np.savetxt(myfile,initial_export_conditions, delimiter=" ", fmt=fmt)

    def __export_sediment_level(self):
        """Exports the initial sediment level to a file.
            The initial sediment level is retrieved from the `initial_conditions` dictionary using the key specified in `self.__model_variables_dic["INITIAL_SEDIMENTS_LEVEL"]`. 
            If this key is not present in the dictionary, the function does nothing.
    
        :return: The resulting array is saved to a file with the filename being the concatenation of the folder path, INPUT_NAME, and SEDIMENT_LEVEL_NAME.
            The output format is specified using the `fmt` variable.
        :rtype: .txt
        """
        initial_sediment_level_export = np.zeros(self.__mesh.nCells)
        initial_conditions = self.__model.get_initial_conditions()

        if _INITIAL_SEDIMENTS_LEVEL not in initial_conditions:
            return
       
        sediment_level = np.array(initial_conditions[_INITIAL_SEDIMENTS_LEVEL][1]).T
        sediment_level_cells_tags = initial_conditions[_INITIAL_SEDIMENTS_LEVEL][0]
        sediment_level_cells_index  = [self.__mesh.tag_to_indexes.get(tag) for tag in sediment_level_cells_tags]
        initial_sediment_level_export[sediment_level_cells_index] = sediment_level
        fmt = '%1.6f'
        myfile = self.__initial_sediment_level_path
        np.savetxt(myfile,initial_sediment_level_export, delimiter=" ", fmt=fmt)

    def __export_bedrock_level(self):
        """Exports the initial bedrock level to a file.
            The initial bedrock level is retrieved from the `initial_conditions` dictionary using the key specified in `self.__model_variables_dic["BEDROCK_LEVEL"]`. 
            If this key is not present in the dictionary, the function does nothing.

        :return: an array is saved to a file with the filename being the concatenation of the folder path, INPUT_NAME, and BEDROCK_NAME. 
            The output format is specified using the `fmt` variable.
        :rtype: .txt
        """
        initial_bedrock_level_export = np.zeros(self.__mesh.nCells)
        initial_conditions = self.__model.get_initial_conditions()

        if _BEDROCK_LEVEL not in initial_conditions:
            return
       
        bedrock_level = np.array(initial_conditions[_BEDROCK_LEVEL][1]).T
        bedrock_level_cells_tags = initial_conditions[_BEDROCK_LEVEL][0]
        bedrock_level_cells_index  = [self.__mesh.tag_to_indexes.get(tag) for tag in bedrock_level_cells_tags]
        initial_bedrock_level_export[bedrock_level_cells_index] = bedrock_level
        fmt = '%1.6f'
        myfile = self.__fixed_bed_level_path
        np.savetxt(myfile,initial_bedrock_level_export, delimiter=" ", fmt=fmt)
    
    def __export_fixed_bank(self):
        """Exports the fixed bank array to a file. 
            IN DEVELOPMENT: FOR THE MOMENT 0 EVERYWHERE : TO PRECISE ?? VERIFY
        """
        initial_conditions = self.__model.get_initial_conditions()
        if _FIXED_BANKS not in initial_conditions:
            return
        np.savetxt(self.__fixed_bank_path,np.zeros(self.__mesh.nCells))

    def __export_friction(self):
        """Exports the friction coefficients to a file.
            Those coefficients are retrieved from the `initial_conditions` dictionary using the key specified in `self.__model_variables_dic["FRICTION_COEFFICIENTS"]`. 
            If this key is not present in the dictionary, the function does nothing.
        
        :return: an array is saved to a file with the filename being the concatenation of the folder path, INPUT_NAME, and get_FRICTION_NAME. The output format is specified using the `fmt` variable.
        :rtype: .txt
        """

        friction_coefficients_export = np.zeros(self.__mesh.nCells)
        initial_conditions = self.__model.get_initial_conditions()

        if _FRICTION_COEFFICIENTS not in initial_conditions:
            return
        
        friction_coefficients = np.array(initial_conditions[_FRICTION_COEFFICIENTS][1]).T
        friction_coefficients_cells_tags = initial_conditions[_FRICTION_COEFFICIENTS][0]
        friction_coefficients_cells_index  = [self.__mesh.tag_to_indexes.get(tag) for tag in friction_coefficients_cells_tags]
        friction_coefficients_export[friction_coefficients_cells_index] = friction_coefficients
    
        fmt = '%1.6f'
        myfile = self.__friction_path 
        np.savetxt(myfile,friction_coefficients_export, delimiter=" ", fmt=fmt)

    def __export_pic(self):        
        """This functions create the pic.txt file and write the following information:
            n_pic
            t_pic,1
            t_pic,2
            ...
            t_pic,n_pic
        :return: a pic file
        :rtype: .txt        
        """

        myfile = self.__picture_path
        #write n_pic
        f = open(myfile, 'w')
        f.write(str(len(self.__model.get_picture_times()))+'\n')
        f.close()
        #write picture times
        fmt = '%1.2f'
        with open(myfile,'ab') as f:
           np.savetxt(f,self.__model.get_picture_times(), delimiter=" ", fmt=fmt)
    
    def __export_gauge(self):
        """Exports the gauge position and time step

        :return: a file composed by
            nGauges
            OutputGaugeName : default : gauge.txt
            time step of measurement
            gauge positions : [[X1,Y1,Z1],[X1,Y1,Z1]] of the chosen gauges
        :rtype: .txt
        """
        
        if not self.__model.is_gauge:
            return
        
        myfile = self.__gauge_path
        f = open(myfile, 'w')
        f.write(str(len(self.__model._gauge))+'\n')
        f.write(_GAUGE_FILE+'\n')  #same name is used for input gauge than for output gauges
        f.write(str(self.__model._gauge_time_step)+'\n')
        f.close()
        fmt = '%1.2f'
        with open(myfile,'ab') as f:
           np.savetxt(f,self.__model._gauge, delimiter=" ", fmt=fmt)

    def __export_discharge_measurement_section(self):
        """Exports a file containing the discharges

        :return: a file composed by 
            Number of sections : for the moment only 1
            time step of measurement
            OutputDischargeName : default : discharge.txt
            The number of edges concerned
            the edges tags
        :rtype: .txt
        """
        if not self.__model.is_discharge_measurement_section:
            return
        edges_data = []
        for elements in self.__model.discharge_control_edges.values():
            edges_data.extend([len(elements), *elements.tolist()])
        myfile = self.__discharge_path
        with open(myfile, 'w') as f:
            f.write(f"{len(self.__model.discharge_control_edges)} {self.__model.discharge_measurement_time_step}\n")
            f.write(_DISCHARGE_OUTPUT_FILE + '\n')
        fmt = '%i'
        with open(myfile, 'ab') as f:
            np.savetxt(f, np.asarray(edges_data), delimiter=" ", fmt=fmt)
           
    def __export_data(self):
        """Generates a txt file based on a template where the informations about the model and the mesh are summarized
            This function will delete the EDGES_NAME file if existing and clean all the pics in the Output folder.

        :return: A text file containing the parameters of the simulation
        :rtype: .txt
        """

        this_dir = os.path.join(os.path.dirname(__file__),"data")
        myfile_template = os.path.join(this_dir,_DATA_TEMPLATE_FILE)

        myfile = self.__data_file_path
        
        with open(myfile_template, 'r') as f:
            template = f.read()
        
        input_data = {'Simulation Name': self.__model.name,
                    't0': str(self.__model.starting_time),'tend':  str(self.__model.ending_time),'CFL': str(self.__model.Cfl_number),
                    'output_folder': self._OUTPUT_FOLDER_NAME+"\\\\",
                    'nodes_file': self.__nodes_path,
                    'cells_file': self.__cells_path,
                    'interfaces_file': self.__edges_path,
                    'physical_model': self.__model.physical_model, 
                    'flux_scheme': self.__model.flux_scheme,
                    'reconstruction_order': self.__model.flux_order,
                    'slope_limiter': self.__model.slope_limiter 
                                                if self.__model.flux_order == 2 
                                                else ' '.join(["!", str(self.__model.slope_limiter)]),
                    'hydrodynamic_initial_conditions':  self.__initial_condition_path,
                    'fixed_bed_level': self.__model.is_fixed_bed_level,
                    'fixed_bed_level_file': self.__fixed_bed_level_path 
                                                if self.__model.is_fixed_bed_level 
                                                else ' '.join(["!", str(self.__fixed_bed_level_path)]),
                    'isFriction': self.__model.is_friction,
                    'isFrictionFile': self.__friction_path 
                                                if self.__model.is_friction 
                                                else ' '.join(["!",str(self.__friction_path)]),
                    'is_sediment_transport': self.__model.is_sediment 
                                                if self.__model.is_sediment 
                                                else ' '.join(['!',str(self.__model.is_sediment)]),
                    'is_initial_sediment_level': self.__model.is_initial_sediment_level 
                                                if (self.__model.is_sediment and self.__model.is_initial_sediment_level == 1) 
                                                else ' '.join(['!',str(self.__model.is_initial_sediment_level)]), 
                    'initial_sediment_level_file':  self.__initial_sediment_level_path 
                                                if (self.__model.is_sediment and self.__model.is_initial_sediment_level == 1) 
                                                else  ' '.join(['!',str(self.__initial_sediment_level_path)]),
                    'sedimentological_parameters':' '.join([str(self.__model.sediment_mean_grain_diameter), 
                                                            str(self.__model.sediment_density), 
                                                            str(self.__model.sediment_friction_coefficient), 
                                                            str(self.__model.sediment_porosity)]) 
                                                if self.__model.is_sediment==1 
                                                else  ' '.join(["!",str(self.__model.sediment_mean_grain_diameter), 
                                                                str(self.__model.sediment_density), 
                                                                str(self.__model.sediment_friction_coefficient), 
                                                                str(self.__model.sediment_porosity)]),
                    'is_bank_failure': self.__model.is_bank_failure 
                                                if self.__model.is_sediment 
                                                else ' '.join(['!',str(self.__model.is_bank_failure)]),
                    'bank_failure_tool':  self.__model.bank_failure_method 
                                                if self.__model.is_sediment 
                                                else ' '.join(["!",str(self.__model.bank_failure_method)]),
                    'bank_failure_parameters': ' '.join([str(self.__model.critical_emmerged_friction_angle), 
                                                         str(self.__model.critical_immerged_friction_angle), 
                                                         str(self.__model.residual_emmerged_friction_angle), 
                                                         str(self.__model.residual_immerged_friction_angle)])  
                                                if self.__model.is_sediment==1 
                                                else  ' '.join(["!", str(self.__model.critical_emmerged_friction_angle), 
                                                                str(self.__model.critical_immerged_friction_angle), 
                                                                str(self.__model.residual_emmerged_friction_angle), 
                                                                str(self.__model.residual_immerged_friction_angle)]),
                    'fixed_bank_file':  self.__fixed_bank_path  
                                                if self.__model.is_sediment 
                                                else ' '.join(["!", str(self.__fixed_bank_path )]),
                    'mass_conservation_check': self.__model.is_sediment_conservation 
                                                if self.__model.is_sediment 
                                                else ' '.join(["!", str(self.__model.is_sediment_conservation)]),
                    'enveloppe_of_results': self.__model.time_step_enveloppe,
                    'is_picture': self.__model.is_picture,
                    'snapshots_of_flow': self.__picture_path 
                                                if self.__model.is_picture 
                                                else ' '.join(["!", str(self.__picture_path)]),
                    'is_gauges': self.__model.is_gauge,
                    'gauges':  self.__gauge_path if self.__model.is_gauge 
                                                else ' '.join(["!",str(self.__gauge_path)])    ,
                    'is_discharge_measured': self.__model.is_discharge_measurement_section,
                    'discharge_measured':  self.__discharge_path 
                                                if self.__model.is_discharge_measurement_section 
                                                else ' '.join(["!",str(self.__discharge_path)])
                    }
        
        data_file = template.format(**input_data)
        
        with open(myfile, 'w') as f:
            f.write(data_file)

if __name__ == "__main__":
    print("Hydroflow isn't a script. Try again later.")