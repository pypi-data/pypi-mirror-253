"""Taking examples from: https://docs.lammps.org/read_data.html."""
from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Optional

from dataclasses_json import DataClassJsonMixin, config

from casar_lammps_mixin.data_file_utils.section_line import (
    BasicHeaderLine,
    BoxBoundsHeaderLine,
    TiltFactorsHeaderLine,
    HEADER_LINE_PARSERS,
)


@dataclass
class HeaderSection(DataClassJsonMixin):  # type: ignore[misc]
    """Represent the header section of a LAMMPS data file."""

    atoms: BasicHeaderLine
    bonds: Optional[BasicHeaderLine]
    angles: Optional[BasicHeaderLine]
    dihedrals: Optional[BasicHeaderLine]
    impropers: Optional[BasicHeaderLine]

    atom_types: BasicHeaderLine = field(metadata=config(field_name="atom types"))
    bond_types: Optional[BasicHeaderLine] = field(
        metadata=config(field_name="bond types")
    )
    angle_types: Optional[BasicHeaderLine] = field(
        metadata=config(field_name="angle types")
    )
    dihedral_types: Optional[BasicHeaderLine] = field(
        metadata=config(field_name="dihedral types")
    )
    improper_types: Optional[BasicHeaderLine] = field(
        metadata=config(field_name="improper types")
    )

    ellipsoids: Optional[BasicHeaderLine]
    lines: Optional[BasicHeaderLine]
    triangles: Optional[BasicHeaderLine]
    bodies: Optional[BasicHeaderLine]

    x_bounds: BoxBoundsHeaderLine = field(metadata=config(field_name="xlo xhi"))
    y_bounds: BoxBoundsHeaderLine = field(metadata=config(field_name="ylo yhi"))
    z_bounds: Optional[BoxBoundsHeaderLine] = field(
        metadata=config(field_name="zlo zhi")
    )
    tilt_factors: Optional[TiltFactorsHeaderLine] = field(
        metadata=config(field_name="xy xz yz")
    )

    def __str__(self) -> str:  # noqa: D105
        contents = "# LAMMPS data file formatted by casar-lammps-mixin\n\n"
        for f in fields(self):
            value = getattr(self, f.name)
            if value:
                contents += f"{value}\n"

        return contents

    @classmethod
    def from_lines(cls, lines: list[str]) -> HeaderSection:
        """Create a header section from lines in a file.

        Args:
            lines: A list of lines from a file

        Returns:
            The header section
        """
        info = {}
        for line in lines:
            keyword = next(
                (keyword for keyword in HEADER_LINE_PARSERS.keys() if keyword in line),
                None,
            )
            if not keyword:
                continue
            info[keyword] = HEADER_LINE_PARSERS[keyword](line)

        header_section: HeaderSection = HeaderSection.from_dict(
            info, infer_missing=True
        )
        return header_section
