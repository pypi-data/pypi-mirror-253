
import numpy
from dataclasses import dataclass


@dataclass
class CylindricalCoordinates:
    rho: numpy.ndarray
    phi: numpy.ndarray
    z: numpy.ndarray

    def to_cartesian(self) -> object:
        x = self.rho * numpy.cos(self.phi)
        y = self.rho * numpy.sin(self.phi)
        z = self.z

        cartesian_coordinate = CartesianCoordinates(x=x, y=y, z=z)

        return cartesian_coordinate

    def to_cylindrical(self):
        return self


@dataclass
class CartesianCoordinates:
    x: numpy.ndarray
    """ Must be 1D-vector """
    y: numpy.ndarray
    """ Must be 1D-vector """
    z: numpy.ndarray
    """ Must be 1D-vector """

    @classmethod
    def generate_from_boundaries(cls,
            x_limits: list = [-1, 1],
            y_limits: list = [-1, 1],
            z_limits: list = [-1, 1],
            x_points: int = 100,
            y_points: int = 100,
            z_points: int = 100):

        x = numpy.linspace(x_limits[0], x_limits[1], x_points)
        y = numpy.linspace(y_limits[0], y_limits[1], y_points)
        z = numpy.linspace(z_limits[0], z_limits[1], z_points)

        instance = CartesianCoordinates(
            x=x,
            y=y,
            z=z
        )

        return instance

    @classmethod
    def generate_from_cube(cls, size: float, center: tuple = (0, 0, 0), n_points: int = 100):
        x0, y0, z0 = center

        x = numpy.linspace(-size / 2, size / 2, n_points) + x0
        y = numpy.linspace(-size / 2, size / 2, n_points) + y0
        z = numpy.linspace(-size / 2, size / 2, n_points) + z0

        instance = CartesianCoordinates(
            x=x,
            y=y,
            z=z
        )

        instance.dx = abs(x[1] - x[0])
        instance.dy = abs(y[1] - y[0])
        instance.dz = abs(z[1] - z[0])

        return instance

    @classmethod
    def generate_from_square(cls, size: float, center: tuple = (0, 0), n_points: int = 100):
        x0, y0 = center

        x = numpy.linspace(-size / 2, size / 2, n_points) + x0
        y = numpy.linspace(-size / 2, size / 2, n_points) + y0

        x_mesh, y_mesh = numpy.meshgrid(y, x)

        instance = CartesianCoordinates(
            x=x_mesh.T,
            y=y_mesh.T,
            z=0
        )

        instance.dx = abs(x[1] - x[0])
        instance.dy = abs(y[1] - y[0])

        return instance

    def to_cylindrical(self) -> object:
        rho = numpy.sqrt(self.x**2 + self.y**2)
        phi = numpy.arctan2(self.y, self.x)

        cylindrical_coordinate = CylindricalCoordinates(
            rho=rho,
            phi=phi,
            z=self.z
        )
        return cylindrical_coordinate

    def to_cartesian(self):
        return self


def vector_cyl2cart(cylindrical_vector: numpy.ndarray, vector_position: CartesianCoordinates | CylindricalCoordinates) -> tuple:
    """
    Takes a cylindrical vector as inputs as well as its cartesian position and returns
    the cartesian vector.

    :param      cylindrical_vector:  The cylindrical vector
    :type       cylindrical_vector:  { type_description }
    :param      vector_position:     The vector position
    :type       vector_position:     { type_description }

    :returns:   The vector in the cartesian basis
    :rtype:     CartesianCoordinates
    """
    vrho, vphi, vz = cylindrical_vector

    cylindrical_position = vector_position.to_cylindrical()

    vx = vrho * numpy.cos(cylindrical_position.phi) - vphi * numpy.sin(cylindrical_position.phi)
    vy = vrho * numpy.sin(cylindrical_position.phi) + vphi * numpy.cos(cylindrical_position.phi)
    vz = vz

    vector = CartesianCoordinates(x=vx, y=vy, z=vz)

    return vector


# -
