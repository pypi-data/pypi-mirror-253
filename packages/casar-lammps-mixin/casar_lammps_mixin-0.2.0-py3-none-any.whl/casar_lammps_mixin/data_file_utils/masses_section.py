"""Taking examples from: https://docs.lammps.org/read_data.html."""
from __future__ import annotations

from dataclasses import dataclass

from casar_lammps_mixin.data_file_utils.section_line import (
    collect_section_lines,
    MassesLine,
)


@dataclass
class MassesSection:
    """Represent the masses section of a LAMMPS data file."""

    lines: list[MassesLine]

    def __str__(self) -> str:  # noqa: D105:
        content = "Masses\n\n"
        for line in self.lines:
            content += f"{line}\n"

        return content

    @classmethod
    def from_lines(cls, n_lines: int, lines: list[str]) -> MassesSection:
        """Create a masses section from lines in a file.

        Args:
            n_lines: The number of lines in the section, likely provided from the
                     header section
            lines: A list of lines from a file

        Returns:
            The masses section
        """
        return MassesSection(
            lines=[
                MassesLine.from_line(line)
                for line in collect_section_lines("Masses", n_lines, lines)
            ]
        )
