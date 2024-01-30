"""Represent the contents of a LAMMPS data file."""
from __future__ import annotations

from dataclasses import dataclass, fields
from pathlib import Path
from typing import Optional

import pandas as pd

from casar_lammps_mixin.data_file_utils.angles_section import AnglesSection
from casar_lammps_mixin.data_file_utils.atoms_section import AtomsSection
from casar_lammps_mixin.data_file_utils.bonds_section import BondsSection
from casar_lammps_mixin.data_file_utils.cs_info_section import CSInfoSection
from casar_lammps_mixin.data_file_utils.header_section import HeaderSection
from casar_lammps_mixin.data_file_utils.masses_section import MassesSection
from casar_lammps_mixin.data_file_utils.section_line import BasicHeaderLine
from casar_lammps_mixin.data_types import AnglePoints, BondPair, EntityInfo


@dataclass
class LAMMPSData:
    """Access the information of a LAMMPS data file."""

    header: HeaderSection
    masses: MassesSection
    atoms: AtomsSection
    bonds: Optional[BondsSection] = None
    angles: Optional[AnglesSection] = None
    cs_info: Optional[CSInfoSection] = None

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return str.join("\n", values)

    @property
    def has_3d_box(self) -> bool:
        """Flag if the the system has 3D box information defined.

        Returns:
            True, if the system has defined 3D box information
        """
        return self.header.z_bounds is not None

    @property
    def has_3d_tilt(self) -> bool:
        """Flag if the the system has 3D tilt information defined.

        Returns:
            True, if the system has defined 3D tilt information
        """
        return self.header.tilt_factors is not None

    @classmethod
    def load_from_local_lammps_data_file(
        cls, filepath: Path, include_cs_info_section: bool = True
    ) -> LAMMPSData:
        """Construct LAMMPSData from a local file LAMMPS data file.

        Args:
            filepath: Local path to a .lammps file
            include_cs_info_section: Bool flag to include a CS-Info section

        Returns:
            The LAMMPSData for the given file

        Raises:
            ValueError: If the provided file doesn't have a .data extension
        """
        if filepath.suffix != ".data":
            raise ValueError(
                "File provided is not a LAMMPS data file with '.data' extension."
            )

        with open(filepath, "r") as file:
            lines = file.readlines()

        header = HeaderSection.from_lines(lines)
        lammps_data_file = LAMMPSData(
            header=header,
            masses=MassesSection.from_lines(header.atom_types.n, lines),
            atoms=AtomsSection.from_lines(header.atoms.n, lines),
        )

        if header.bonds and header.bonds.n:
            lammps_data_file.bonds = BondsSection.from_lines(header.bonds.n, lines)
        if header.angles and header.angles.n:
            lammps_data_file.angles = AnglesSection.from_lines(header.angles.n, lines)
        if include_cs_info_section:
            lammps_data_file.cs_info = CSInfoSection.from_atoms_lines(
                lammps_data_file.atoms.lines
            )

        return lammps_data_file

    def define_new_bond_section(self, bond_dict: dict[BondPair, EntityInfo]) -> None:
        """Define a new bond section from the defined bonds.

        Args:
            bond_dict: A dictionary summarizing the bonds to be made for the system

        Raises:
            NotImplementedError: If the system isn't 3D
        """
        if not self.header.z_bounds:
            raise NotImplementedError(
                "Section generation only supported for 3D systems."
            )
        atoms_reference = pd.DataFrame(self.atoms.lines)

        self.bonds = BondsSection.generate_from_atoms(
            bond_dict, atoms_reference, self.header
        )
        self.header.bonds = BasicHeaderLine(n=len(self.bonds.lines), keyword="bonds")
        self.header.bond_types = BasicHeaderLine(
            n=len(set(v["bond_type"] for v in bond_dict.values())), keyword="bond types"
        )

    def define_new_angle_section(
        self, angle_dict: dict[AnglePoints, EntityInfo]
    ) -> None:
        """Define a new angle section from the defined bonds.

        Args:
            angle_dict: A dictionary summarizing the angle to be made for the system

        Raises:
            NotImplementedError: If the system isn't 3D
        """
        if not self.header.z_bounds:
            raise NotImplementedError(
                "Section generation only supported for 3D systems."
            )
        atoms_reference = pd.DataFrame(self.atoms.lines)

        self.angles = AnglesSection.generate_from_atoms(
            angle_dict, atoms_reference, self.header
        )
        self.header.angles = BasicHeaderLine(n=len(self.angles.lines), keyword="angles")
        self.header.angle_types = BasicHeaderLine(
            n=len(set(v["angle_type"] for v in angle_dict.values())),
            keyword="angle types",
        )

    def write_to_file(self, dst_path: Path) -> None:
        """Write the LAMMPS data to a local file.

        Args:
            dst_path: The path to write the file to
        """
        with open(dst_path.with_suffix(".FINAL.data"), "w") as file:
            file.write(str(self))
