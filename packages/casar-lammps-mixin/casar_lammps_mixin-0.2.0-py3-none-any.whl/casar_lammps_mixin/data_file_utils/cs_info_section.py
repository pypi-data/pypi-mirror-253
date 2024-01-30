"""Taking examples from: https://docs.lammps.org/read_data.html."""
from __future__ import annotations

from dataclasses import dataclass

from casar_lammps_mixin.data_file_utils.section_line import (
    AtomsLine,
    CSInfoLine,
)


@dataclass
class CSInfoSection:
    """Represent the CS-Info section of a LAMMPS data file."""

    lines: list[CSInfoLine]

    def __str__(self) -> str:  # noqa: D105:
        content = "CS-Info\n\n"
        for line in self.lines:
            content += f"{line}\n"

        return content

    @classmethod
    def from_atoms_lines(cls, atoms_lines: list[AtomsLine]) -> CSInfoSection:
        """Create a CS-Info section from atom lines.

        Args:
            atoms_lines: A list of atoms lines

        Returns:
            The CS-Info section
        """
        return CSInfoSection(
            lines=[CSInfoLine.from_atoms_line(atom_line) for atom_line in atoms_lines]
        )
