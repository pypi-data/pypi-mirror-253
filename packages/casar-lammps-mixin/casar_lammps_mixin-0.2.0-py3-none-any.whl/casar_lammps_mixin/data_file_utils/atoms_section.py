"""Taking examples from: https://docs.lammps.org/read_data.html."""
from __future__ import annotations

from dataclasses import dataclass

from casar_lammps_mixin.data_file_utils.section_line import (
    collect_section_lines,
    AtomsLine,
)


@dataclass
class AtomsSection:
    """Represent the atoms section of a LAMMPS data file."""

    lines: list[AtomsLine]

    def __str__(self) -> str:  # noqa: D105
        content = "Atoms  # full\n\n"
        for line in self.lines:
            content += f"{line}\n"

        return content

    @classmethod
    def from_lines(cls, n_lines: int, lines: list[str]) -> AtomsSection:
        """Create a atoms section from lines in a file.

        Args:
            n_lines: The number of lines in the section, likely provided from the
                     header section
            lines: A list of lines from a file

        Returns:
            The atoms section
        """
        return AtomsSection(
            lines=[
                AtomsLine.from_line(line)
                for line in collect_section_lines("Atoms", n_lines, lines)
            ]
        )
