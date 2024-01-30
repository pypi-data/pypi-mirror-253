"""Generate Bond and Angle sections of a LAMMPS data file."""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Iterator, List, Optional, Tuple

import pandas as pd
from sklearn.neighbors import KDTree
from casar_lammps_mixin.data_file_utils.section_line import (
    AnglesLine,
    BoxBoundsHeaderLine,
    TiltFactorsHeaderLine,
)

from casar_lammps_mixin.data_types import (
    AnglePoints,
    EntityInfo,
    MultiTypes,
    SingleType,
)
from casar_lammps_mixin.pbc_construct import PeriodicBoundaryConditionShifts


@dataclass
class AngleGenerator:
    """Generate the Angle section of a LAMMPS data file from the provided atoms.

    Args:
        angle_dict: A dictionary summarizing the angles to be made for the system
        reference: A dataframe with atomic coordinates of the system
        info: The header info of the LAMMPS system
    """

    angle_dict: dict[AnglePoints, EntityInfo]
    atoms_reference: pd.DataFrame
    x_bounds: BoxBoundsHeaderLine
    y_bounds: BoxBoundsHeaderLine
    z_bounds: BoxBoundsHeaderLine
    tilt_factors: Optional[TiltFactorsHeaderLine]

    def subset_center_atom(self, type: SingleType) -> pd.DataFrame:
        """Subset the center type atoms.

        Args:
            type: The atom type of the center atom in the angle

        Returns:
            A dataframe of center type atoms
        """
        subset = self.atoms_reference[self.atoms_reference["atom_type"] == type]
        return subset.reset_index(drop=True)

    def subset_end_atom(self, types: SingleType | MultiTypes) -> pd.DataFrame:
        """Subset the atom2 type atoms.

        Args:
            types: The atom type of the second atom in the bond

        Returns:
            A dataframe of atom2 type atoms, including the original positions and
            the images in all dimensions.
        """
        if isinstance(types, int):
            subset = self.atoms_reference[self.atoms_reference["atom_type"] == types]
        else:
            subset = pd.concat(
                [
                    self.atoms_reference[self.atoms_reference["atom_type"] == type]
                    for type in types
                ]
            )

        pbc = PeriodicBoundaryConditionShifts(
            reference=subset,
            x_bounds=self.x_bounds,
            y_bounds=self.y_bounds,
            z_bounds=self.z_bounds,
            tilt_factors=self.tilt_factors,
        )
        return pbc.image_by_symmetry().reset_index(drop=True)

    def group_end(
        self,
        center_type: int,
        end_type: SingleType | MultiTypes,
        cutoff: float,
        group: defaultdict[int, set[int]],
    ) -> defaultdict[int, set[int]]:
        """Generate bonds between the two atoms queried from the provided cutoff.

        Args:
            center_type: The atom type of the center atom in the angle
            end_type: The atom type of the end atom in the angle
            cutoff: The cutoff radius for querying the end atoms in the angle
            group: The dictionary for collecting the queried angles

        Returns:
            The dictionary collecting the queried angles
        """
        df_center = self.subset_center_atom(type=center_type)
        df_end = self.subset_end_atom(types=end_type)

        query = df_center[["x", "y", "z"]].to_numpy()
        X = df_end[["x", "y", "z"]].to_numpy()
        tree = KDTree(X, leaf_size=2)
        indices = tree.query_radius(query, r=cutoff)
        for center_index, end_indices in enumerate(indices):
            center_atom = int(df_center.iloc[center_index]["index"])
            for end_index in end_indices:
                end_atom = int(df_end.iloc[end_index]["index"])
                group[center_atom].add(end_atom)

        return group

    def collect_end_groups(
        self,
        center_type: int,
        end1: SingleType | MultiTypes,
        cutoff1: float,
        end2: SingleType | MultiTypes,
        cutoff2: float,
    ) -> defaultdict[int, set[int]]:
        """Group the center atom to its end atoms.

        Args:
            center_type: The atom type of the center atom in the angle
            end1: The atom type of the first end atom(s) in the angle
            cutoff1: The cutoff radius for querying the first end atom(s) in the angle
            end2: The atom type of the second end atom(s) in the angle
            cutoff2: The cutoff radius for querying the second end atom(s) in the angle

        Returns:
            The dictionary of the angle groups
        """
        group: defaultdict[int, set[int]] = defaultdict(set)
        if end1 != end2:
            for end_types, cutoff in zip((end1, end2), (cutoff1, cutoff2)):
                group = self.group_end(center_type, end_types, cutoff, group)
        else:
            group = self.group_end(center_type, end1, cutoff1, group)
        return group

    @staticmethod
    def bond_group_angles(
        center_atom: int, end_atoms: List[int]
    ) -> Iterator[Tuple[int, int, int]]:
        """Generate angles from the bonded groups.

        Args:
            center_atom: Type of the center atom in the angle of interest
            end_atoms: Atom type that makes up end atoms in the angle

        Yields:
            The components of an angle as AngleData
        """
        for end1_atom in end_atoms[:-1]:
            end_atoms.pop(0)
            for end2_atom in end_atoms:
                yield center_atom, end1_atom, end2_atom

    def create_angle_data(
        self,
        center_type: int,
        end1: SingleType | MultiTypes,
        cutoff1: float,
        end2: SingleType | MultiTypes,
        cutoff2: float,
    ) -> Iterator[Tuple[int, int, int]]:
        """Create the angle data for a center atom and its end atoms.

        Args:
            center_type: The atom type of the center atom in the angle
            end1: The atom type of the first end atom(s) in the angle
            cutoff1: The cutoff radius for querying the first end atom(s) in the angle
            end2: The atom type of the second end atom(s) in the angle
            cutoff2: The cutoff radius for querying the second end atom(s) in the angle

        Yields:
            The components of an angle as AngleData
        """
        angle_group = self.collect_end_groups(center_type, end1, cutoff1, end2, cutoff2)
        for center_atom, end_atoms in angle_group.items():
            for bond_group_angle in self.bond_group_angles(
                center_atom, list(end_atoms)
            ):
                yield bond_group_angle

    def generate_angles(self) -> Iterator[AnglesLine]:
        """Generate the angles for each item in the provided angle dictionary.

        Yields:
            The components of an angle as AngleData
        """
        index = 1
        for (end1_types, center_type, end2_types), values in self.angle_dict.items():
            for center_index, end1_index, end2_index in self.create_angle_data(
                center_type=center_type,
                end1=end1_types,
                cutoff1=float(values["cutoff1"]),
                end2=end2_types,
                cutoff2=float(values["cutoff2"]),
            ):
                yield AnglesLine(
                    index=index,
                    angle_type=int(values["angle_type"]),
                    atom1=end1_index,
                    atom2=center_index,
                    atom3=end2_index,
                )
                index += 1

    # def collect_angle_section(self, checkpoint: bool) -> list[AngleData]:
    #     """Update the data info with the newly generated angles.

    #     Args:
    #         checkpoint: If true, will generate plots of generated angles.

    #     Returns:
    #         A list of angles for the Angle section.
    #     """
    #     angles = list(self.generate_angles())
    #     df_angles = pd.DataFrame(angles)
    #     self.info.angles = df_angles.shape[0]
    #     self.info.angle_types = len(df_angles["type"].unique())

    #     if checkpoint:
    #         ...

    #     return angles
