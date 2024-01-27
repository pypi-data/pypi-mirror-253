"""The AbstractField defines an abstract baseclass for descriptor classes.
The baseclass defines how the field name and owner should be defined
automatically by the __set_name__ method. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod


class AbstractField:
  """The AbstractField defines an abstract baseclass for descriptor
  classes."""

  def __init__(self, *args, **kwargs) -> None:
    self.__field_name__ = None
    self.__field_owner__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    self.__field_owner__ = owner
    self.__field_name__ = name
    self.__prepare_owner__(owner)

  @abstractmethod
  def __prepare_owner__(self, owner: type) -> type:
    """This special abstract method must be implemented by subclasses to
    install this field into it."""
