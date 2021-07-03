"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
import math
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # [DONE] TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    # - The arguments to the constructor should be changed for clarity. As when instantiating
    #   an instance of this class, it would otherwise give you no indication of the expected
    #   parameters.
    def __init__(self, designation: str, hazardous: bool, name: str = None, diameter: float = "nan"):
        """Create a new `NearEarthObject`.

        :param designation: Primary designation of the NEO.
        :param hazardous: NEO marked as potentially hazardous to Earth.
        :param name: NEO's IAU name.
        :param diameter: NEO's diameter in kilometers.
        """
        # [DONE] TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        self.designation = str(designation)
        self.name = str(name) if name else None
        self.diameter = float(diameter)
        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # [DONE] TODO: Use self.designation and self.name to build a fullname for this object.
        return f"{self.designation} ({self.name})" if self.name else f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        # [DONE] TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        is_hazardous = "is" if self.hazardous else "is not"
        if not math.isnan(self.diameter):
            return (f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km"
                    f" and {is_hazardous} potentially hazardous.")

        return f"NEO {self.fullname} {is_hazardous} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # [DONE] TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.

    def __init__(self, designation: str, dt: str, distance: float, velocity: float):
        """Create a new `CloseApproach`.

        :param designation: Primary designation of the NEO.
        :param dt: NASA-formatted calendar date/time in UTC of the closest approach.
        :param distance: The nominal approach distance in astronomical units.
        :param velocity: The relative approach velocity in kilometers per second.
        """
        # [DONE] TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = str(designation)
        # [DONE] TODO: Use the cd_to_datetime function for this attribute.
        self.time = cd_to_datetime(dt)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # [DONE] TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        # STUDENT NOTE: This class does not have a self.name attribute, unclear what is being
        # asked in the second TODO.
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        # [DONE] TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return (f"At {self.time_str}, '{self.neo.fullname}' approaches Earth"
                f" at a distance of {self.distance:.2f} au and a velocity of"
                f" {self.velocity:.2f} km/s.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
