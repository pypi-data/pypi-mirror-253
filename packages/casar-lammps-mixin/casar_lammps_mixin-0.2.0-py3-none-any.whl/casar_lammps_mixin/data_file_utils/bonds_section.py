"""Taking examples from: https://docs.lammps.org/read_data.html."""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from casar_lammps_mixin.data_file_utils.header_section import HeaderSection

from casar_lammps_mixin.data_file_utils.section_line import (
    collect_section_lines,
    BondsLine,
)
from casar_lammps_mixin.data_types import BondPair, EntityInfo
from casar_lammps_mixin.section_generator.bonds import BondGenerator


@dataclass
class BondsSection:
    """Represent the bonds section of a LAMMPS data file."""

    lines: list[BondsLine]

    def __str__(self) -> str:  # noqa: D105:
        content = "Bonds\n\n"
        for line in self.lines:
            content += f"{line}\n"

        return content

    @classmethod
    def from_lines(cls, n_lines: int, lines: list[str]) -> BondsSection:
        """Create a bonds section from lines in a file.

        Args:
            n_lines: The number of lines in the section, likely provided from the
                     header section
            lines: A list of lines from a file

        Returns:
            The bonds section
        """
        return BondsSection(
            lines=[
                BondsLine.from_line(line)
                for line in collect_section_lines("Bonds", n_lines, lines)
            ]
        )

    @classmethod
    def generate_from_atoms(
        cls,
        bond_dict: dict[BondPair, EntityInfo],
        atoms_reference: pd.DataFrame,
        header_section: HeaderSection,
    ) -> BondsSection:
        """Generate bonds for given atoms and simulation box description.

        Args:
            bond_dict: A dictionary summarizing the bonds to be made for the system
            atoms_reference: A dataframe of atomic coordinates with columns -
                             'atom_type', 'x', 'y', 'z'
            header_section: The header section associated with the given atoms

        Returns:
            The bond section generated from the given atoms and simulation box

        Raises:
            NotImplementedError: If the simulation box isn't 3-dimensional
        """
        if not header_section.z_bounds:
            raise NotImplementedError(
                "Bonds section generation only supported for 3D systems"
            )

        bond_generator = BondGenerator(
            bond_dict,
            atoms_reference,
            header_section.x_bounds,
            header_section.y_bounds,
            header_section.z_bounds,
            header_section.tilt_factors,
        )

        return BondsSection(lines=[line for line in bond_generator.generate_bonds()])
