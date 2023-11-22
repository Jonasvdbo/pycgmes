# SPDX-FileCopyrightText: 2023 Alliander
#
# SPDX-License-Identifier: Apache-2.0

from pydantic import Field
from pydantic.dataclasses import dataclass

from pycgmes.resources.Bay import Bay
from pycgmes.utils.config import cgmes_resource_config
from pycgmes.utils.profile import BaseProfile


class CustomProfile(BaseProfile):
    CUS = "Tom"
    FRO = "Mage"
    model_config = cgmes_resource_config


@dataclass
class CustomBayAttr(Bay):
    model_config = cgmes_resource_config
    colour: str = Field(
        default="Red",
        json_schema_extra={
            "in_profiles": [
                CustomProfile.CUS,
            ],
            "namespace": "custom",
        },
    )

    @classmethod
    def apparent_name(cls):
        return "Bay"


@dataclass
class CustomBayClass(Bay):
    model_config = cgmes_resource_config

    @classmethod
    def apparent_name(cls):
        return "Cheese"

    def possible_profiles(self):
        return {CustomProfile.CUS}


class TestCustom:
    def test_custom_profile_in_attrs(self):
        colour = "cheese"
        apparent = "Bay"
        cust = CustomBayAttr(colour=colour)
        mine_attrs = cust.cgmes_attributes_in_profile(CustomProfile.CUS)
        none_attrs = cust.cgmes_attributes_in_profile(CustomProfile.FRO)
        all_attrs = cust.cgmes_attributes_in_profile(None)
        assert len(mine_attrs) == 1
        assert len(all_attrs) == 6
        assert len(none_attrs) == 0

        assert f"{apparent}.colour" in mine_attrs
        assert mine_attrs[f"{apparent}.colour"]["value"] == colour
        assert mine_attrs[f"{apparent}.colour"]["namespace"] == "custom"

    def test_custom_class(self):
        cust = CustomBayClass()
        assert cust.possible_profiles() == {CustomProfile.CUS}
