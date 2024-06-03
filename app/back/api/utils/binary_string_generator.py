from abc import ABC, abstractmethod


class BinaryStringMethod(ABC):
    """
    An abstract base class defining a method for getting binary strings.

    This class is intended to be subclassed to provide implementation for
    generating binary strings.

    Attributes:
        ABC (class): ABC (Abstract Base Class) module from the Python standard library.
    """

    @abstractmethod
    def get_binary_strings(self):
        """
        Abstract method to be implemented by subclasses for generating binary strings.

        This method should be implemented to provide functionality for generating
        binary strings.

        Raises:
            NotImplementedError: If this method is not implemented by a subclass.

        Returns:
            str: Binary string generated by the implementation.
        """
        pass
