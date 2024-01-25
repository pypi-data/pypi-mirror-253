# En __init__.py del paquete que contiene AtomPositionManager
try:
    from sage_lib.partition.PartitionManager import PartitionManager
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing PartitionManager: {str(e)}\n")
    del syss

try:
    from sage_lib.IO.structure_handling_tools.AtomPosition import AtomPosition
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing AtomPosition: {str(e)}\n")
    del sys
    
try:
    import numpy as np
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing numpy: {str(e)}\n")
    del sys

try:
    import copy
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing copy: {str(e)}\n")
    del sys

try:
    import os
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing os: {str(e)}\n")
    del sys

try:
    import imageio
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing imageio: {str(e)}\n")
    del sys

try:
    from concurrent.futures import ProcessPoolExecutor
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing imageio: {str(e)}\n")
    del sys
    
try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing matplotlib.pyplot: {str(e)}\n")
    del sys

class MolecularDynamic_builder(PartitionManager):
    """
    Class for building and managing molecular dynamic simulations.
    
    Inherits from PartitionManager and integrates additional functionalities
    specific to molecular dynamics, such as calculating displacement and plotting.

    Attributes:
        _molecule_template (dict): A template for the molecule structure.
        _density (float): Density value of the molecule.
        _cluster_lattice_vectors (numpy.ndarray): Lattice vectors of the cluster.
    """

    def __init__(self, file_location:str=None, name:str=None, **kwargs):
        """
        Initialize the MolecularDynamicBuilder object.

        Args:
            file_location (str, optional): File location of the input data.
            name (str, optional): Name of the simulation.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(name=name, file_location=file_location)

        self._molecule_template = {}
        self._density = None
        self._cluster_lattice_vectors = None

    def get_displacement(self, reference:str=None):
        """
        Calculate the displacement of atoms based on a reference point.

        Args:
            reference (str, optional): Reference axis or lattice vector ('a', 'b', 'c', 'x', 'y', 'z').

        Returns:
            numpy.ndarray: Array of displacement values for each atom.
        """

        data_displacement = []
        for container_i, container in enumerate(self.containers):

            if container_i == 0:
                displacement_reference_values = container.AtomPositionManager.atomPositions
                reference_values = self._calculate_reference_values(container, reference)

            displacement = np.linalg.norm(displacement_reference_values - container.AtomPositionManager.atomPositions, axis=1)
            data_displacement.append(displacement + reference_values)

        return np.array(data_displacement, dtype=np.float64 )

    def _plot_RBF_for_container(self, container, container_i, output_path):
        """
        Función para trazar RBF para un contenedor específico.
        """
        print(container_i)
        output_path_container = os.path.join(output_path, f'MD_RBF/{container_i}')
        self.create_directories_for_path(output_path_container)
        container.AtomPositionManager.plot_RBF(output_path=output_path_container, save=True)

    def plot_RBF(self, output_path:str=None):
        """

        """
        output_path = output_path if output_path is not None else '.' 
        data_displacement = []

        # Usar ProcessPoolExecutor para paralelizar
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(self._plot_RBF_for_container, container, container_i, output_path)
                       for container_i, container in enumerate(self.containers)]

            for future in futures:
                # Aquí puedes manejar los resultados o excepciones si es necesario
                result = future.result()

        return data_displacement
        '''
        output_path = output_path if output_path is not None else '.' 
        data_displacement = []
        for container_i, container in enumerate(self.containers):
            self.create_directories_for_path(output_path+f'/MD_RBF/{container_i}')
            container.AtomPositionManager.plot_RBF(output_path=output_path+f'/MD_RBF/{container_i}', save=True)

        return data_displacement
        '''

    def _calculate_reference_values(self, container, reference):
        """
        Calculate reference values based on the specified reference type.

        Args:
            container: The container holding atom positions and lattice vectors.
            reference (str): The reference type ('a', 'b', 'c', 'x', 'y', 'z').

        Returns:
            numpy.ndarray: Calculated reference values.
        """
        if type(reference) is str and reference.upper() in ['A', 'B', 'C']:
            lv_index = {'A': 0, 'B': 1, 'C': 2}[reference.upper()]
            lv = container.AtomPositionManager.latticeVectors[:, lv_index]
            return np.dot(container.AtomPositionManager.atomPositions, lv / np.linalg.norm(lv))
        
        if type(reference) is str and reference.upper() in ['X', 'Y', 'Z']:
            return container.AtomPositionManager.atomPositions[:, {'X': 0, 'Y': 1, 'Z': 2}[reference.upper()]]
    
        return np.zeros(container.AtomPositionManager.atomCount)

    def plot_displacement(self, data_displacement, save:bool=True, verbose:bool=True):
        """
        Plot the displacement of atoms.

        Args:
            data_displacement (numpy.ndarray): Displacement data to plot.
            save (bool, optional): Whether to save the plot as an image. Defaults to True.
            verbose (bool, optional): Enable verbose output. Defaults to True.
        """
        for u in self.containers[0].AtomPositionManager.uniqueAtomLabels:
            mask = self.containers[0].AtomPositionManager.atomLabelsList == u

            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
            color = self.containers[0].AtomPositionManager.element_colors[u]

            ax1.plot(data_displacement[:, mask], color=color, alpha=0.3, lw=0.5)
            self.setup_subplot(ax1, 'Time', 'Displacements', f'Displacements for {u}')

            avg_displacement = np.mean(data_displacement[:, mask], axis=0)
            var_displacement = np.var(data_displacement[:, mask], axis=0)
            avg_displacement = self._calculate_reference_values(self.containers[0], 'c')[mask]
            ax2.plot(var_displacement, avg_displacement, 'o', label='Average', color=color)
            self.setup_subplot(ax2, 'Variance', 'Average', f'Average and Variance for {u}')

            plt.tight_layout()
            if save:
                plt.savefig(f'displacements_{u}.png', dpi=100)
            plt.clf()

            if verbose:
                print(f' >> Plot :: displacements ({u}) - data shape {data_displacement.shape}')

    def animated_RBF(self, output_path:str=None, duration:float=0.1, save:bool=True, verbose:bool=True):
        """

        """

        for u in self.containers[0].AtomPositionManager.uniqueAtomLabels:
            images = []
            #for file_name in sorted(os.listdir(file_location)):
                #if file_name.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            for container_i, container in enumerate(self.containers):
                file_path = f'MD_RBF/{container_i}/RBF_{u}.png'
                images.append(imageio.imread(file_path))
        
            if save:
                imageio.mimsave( f'MD_RBF{u}.gif', images, duration=duration)

    @staticmethod
    def setup_subplot(ax, xlabel, ylabel, title):
        """
        Set up the subplot with labels and title.

        Args:
            ax (matplotlib.axes.Axes): The axes object to setup.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
            title (str): Title of the subplot.
        """
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        #ax.legend(loc='upper right')

    def handleMDAnalysis(self, values:list, file_location:str=None):
        """
        Handle molecular dynamics analysis based on specified values.

        Args:
            values (list): List of analysis types to perform.
            file_location (str, optional): File location for output data.
        """

        MDA_data = {}

        for plot in values:
            if plot.upper() == 'displacements':
                MDA_data['displacement'] = self.get_displacement(reference=values[plot].get('reference', None))
                self.plot_displacement( MDA_data['displacement'], verbose=values[plot].get('verbose', False) )

            if plot.upper() == 'RBF':
                MDA_data['RBF'] = self.plot_RBF()
                self.animated_RBF( output_path=values[plot].get('output_path', '.'), duration=0.1, save=True, verbose=values[plot].get('verbose', False) )


