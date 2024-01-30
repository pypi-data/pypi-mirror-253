"""Line representations for each section in the Data File."""
from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Iterator, Optional


def get_section_title_index(section_title: str, lines: list[str]) -> int:
    """Get the index of a section by its title.

    Args:
        section_title: The title of the section
        lines: The lines of a file

    Returns:
        The index of the section title line

    Raises:
        ValueError: If the section title isn't found in the lines
    """
    try:
        index = next(i for i, string in enumerate(lines) if section_title in string)
        return index
    except StopIteration:
        raise ValueError(f"'{section_title}' section not found")


def collect_section_lines(
    section_title: str, n_lines: int, lines: list[str]
) -> Iterator[str]:
    """Get the lines that belong to a section.

    Args:
        section_title: The title of the section
        n_lines: The number of lines in the section, likely provided from the
                 header section
        lines: A list of lines from a file

    Yields:
        A line from the section
    """
    index = get_section_title_index(section_title, lines)

    start = index + 2  # Account for whitespaces
    end = start + n_lines

    for line in lines[start:end]:
        yield line


@dataclass
class BasicHeaderLine:
    """Represent a basic header line."""

    n: int
    keyword: str

    def __str__(self) -> str:  # noqa: D105
        return f"{self.n} {self.keyword}"

    @classmethod
    def from_line(cls, line: str) -> BasicHeaderLine:
        """Create a basic header line from a string.

        Args:
            line: The string to parse

        Returns:
            The header line
        """
        n, keyword = line.strip().split(maxsplit=1)

        return BasicHeaderLine(n=int(n), keyword=keyword)


@dataclass
class BoxBoundsHeaderLine:
    """Represent a box bound line."""

    min: float
    max: float
    keyword: str

    def __str__(self) -> str:  # noqa: D105
        return f"{self.min} {self.max} {self.keyword}"

    @classmethod
    def from_line(cls, line: str) -> BoxBoundsHeaderLine:
        """Create a box boounding header line from a string.

        Args:
            line: The string to parse

        Returns:
            The box bounding header line
        """
        min, max, keyword = line.strip().split(maxsplit=2)

        return BoxBoundsHeaderLine(min=float(min), max=float(max), keyword=keyword)


@dataclass
class TiltFactorsHeaderLine:
    """Represent tilt factors line for triclinic system."""

    xy: float
    xz: float
    yz: float

    def __str__(self) -> str:  # noqa: D105
        return f"{self.xy} {self.xz} {self.yz} xy xz yz"

    @classmethod
    def from_line(cls, line: str) -> TiltFactorsHeaderLine:
        """Create a tilt factor header line from a string.

        Args:
            line: The string to parse

        Returns:
            The tilt factor header line
        """
        xy, xz, yz, _ = line.strip().split(maxsplit=3)

        return TiltFactorsHeaderLine(xy=float(xy), xz=float(xz), yz=float(yz))


HEADER_LINE_PARSERS = {
    "atoms": BasicHeaderLine.from_line,
    "bonds": BasicHeaderLine.from_line,
    "angles": BasicHeaderLine.from_line,
    "dihedrals": BasicHeaderLine.from_line,
    "impropers": BasicHeaderLine.from_line,
    "atom types": BasicHeaderLine.from_line,
    "bond types": BasicHeaderLine.from_line,
    "angle types": BasicHeaderLine.from_line,
    "dihedral types": BasicHeaderLine.from_line,
    "improper types": BasicHeaderLine.from_line,
    "ellipsoids": BasicHeaderLine.from_line,
    "lines": BasicHeaderLine.from_line,
    "triangles": BasicHeaderLine.from_line,
    "bodies": BasicHeaderLine.from_line,
    "xlo xhi": BoxBoundsHeaderLine.from_line,
    "ylo yhi": BoxBoundsHeaderLine.from_line,
    "zlo zhi": BoxBoundsHeaderLine.from_line,
    "xy xz yz": TiltFactorsHeaderLine.from_line,
}


@dataclass
class MassesLine:
    """Represent a line in the 'Masses' section."""

    index: int
    mass: float

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return f"\t{str.join('  ', values)}"

    @classmethod
    def from_line(cls, line: str) -> MassesLine:
        """Create a masses line from a string.

        Args:
            line: The string to parse

        Returns:
            The masses line
        """
        split = line.strip().split()

        return MassesLine(index=int(split[0]), mass=float(split[1]))


@dataclass
class CoefficientLine:
    """Represent a line for coeffecients."""

    index: int
    coeffs: list[float]


@dataclass
class AtomsLine:
    """Represent a line in the 'Atoms  # full' section.

    A line can optionally have 3 flags (nx,ny,nz) appended to it, which indicate which
    image of a periodic simulation box the atom is in.
    """

    index: int
    molecule_tag: int
    atom_type: int
    charge: float
    x: float
    y: float
    z: float
    nx: Optional[float] = None
    ny: Optional[float] = None
    nz: Optional[float] = None

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return f"\t{str.join('  ', values)}"

    @classmethod
    def from_line(cls, line: str) -> AtomsLine:
        """Create an atoms line from a string.

        Args:
            line: The string to parse

        Returns:
            The atoms line
        """
        split = line.strip().split()

        atoms_line = AtomsLine(
            index=int(split[0]),
            molecule_tag=int(split[1]),
            atom_type=int(split[2]),
            charge=float(split[3]),
            x=float(split[4]),
            y=float(split[5]),
            z=float(split[6]),
        )

        if len(split) == 10:
            atoms_line.nx = float(split[7])
            atoms_line.ny = float(split[8])
            atoms_line.nz = float(split[9])

        return atoms_line


@dataclass
class VelocitiesLine:
    """Represent a line in the 'Velocities' section."""

    index: int
    vx: float
    vy: float
    vz: float


@dataclass
class BondsLine:
    """Represent a line in the 'Bonds' section."""

    index: int
    bond_type: int
    atom1: int
    atom2: int

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return f"\t{str.join('  ', values)}"

    @classmethod
    def from_line(cls, line: str) -> BondsLine:
        """Create a bonds line from a string.

        Args:
            line: The string to parse

        Returns:
            The bonds line
        """
        split = [int(value) for value in line.strip().split()]

        return BondsLine(
            index=split[0],
            bond_type=split[1],
            atom1=split[2],
            atom2=split[3],
        )


@dataclass
class AnglesLine:
    """Represent a line in the 'Angles' section.

    Atom 2 is the center of the angle.
    """

    index: int
    angle_type: int
    atom1: int
    atom2: int
    atom3: int

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return f"\t{str.join('  ', values)}"

    @classmethod
    def from_line(cls, line: str) -> AnglesLine:
        """Create an angles line from a string.

        Args:
            line: The string to parse

        Returns:
            The angles line
        """
        split = [int(value) for value in line.strip().split()]

        return AnglesLine(
            index=split[0],
            angle_type=split[1],
            atom1=split[2],
            atom2=split[3],
            atom3=split[4],
        )


@dataclass
class DihedralsLine:
    """Represent a line in the 'Dihedrals' section.

    Atoms 2,3 form central bond.
    """

    index: int
    dihedral_type: int
    atom1: int
    atom2: int
    atom3: int
    atom4: int


@dataclass
class ImpropersLine:
    """Represent a line in the 'Impropers' section.

    Atom 2 is central atom.
    """

    index: int
    improper_type: int
    atom1: int
    atom2: int
    atom3: int
    atom4: int


@dataclass
class CSInfoLine:
    """Represent a line in the 'CS-Info' section."""

    index: int
    molecule_tag: int

    def __str__(self) -> str:  # noqa: D105
        values = [
            str(getattr(self, f.name)) for f in fields(self) if getattr(self, f.name)
        ]
        return f"\t{str.join('  ', values)}"

    @classmethod
    def from_atoms_line(cls, atoms_line: AtomsLine) -> CSInfoLine:
        """Create a CS-Info line from an atoms line.

        Args:
            atoms_line: An atoms line of interest

        Returns:
            A CSInfoLine
        """
        return CSInfoLine(index=atoms_line.index, molecule_tag=atoms_line.molecule_tag)
