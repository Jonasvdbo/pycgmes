# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass

from ..utils.profile import BaseProfile, Profile
from .GeneratingUnit import GeneratingUnit


@dataclass
class ThermalGeneratingUnit(GeneratingUnit):
    """
    A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.

    CAESPlant: A thermal generating unit may be a member of a compressed air energy storage plant.
    CogenerationPlant: A thermal generating unit may be a member of a cogeneration plant.
    CombinedCyclePlant: A thermal generating unit may be a member of a combined cycle plant.
    FossilFuels: A thermal generating unit may have one or more fossil fuels.
    """

    CAESPlant: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    CogenerationPlant: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    CombinedCyclePlant: Optional[str] = Field(
        default=None,
        json_schema_extra={
            "in_profiles": [
                Profile.EQ,
            ]
        },
    )

    # *Association not used*
    # Type M:0..n in CIM
    # FossilFuels : list = Field(default_factory=list, json_schema_extra={"in_profiles":[Profile.EQ, ]})

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
            Profile.SSH,
        }
