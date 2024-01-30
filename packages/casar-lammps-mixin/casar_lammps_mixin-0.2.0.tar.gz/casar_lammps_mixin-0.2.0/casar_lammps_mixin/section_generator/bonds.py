"""Generate Bond and Angle sections of a LAMMPS data file."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator, Optional, Tuple

import pandas as pd
from sklearn.neighbors import KDTree
from casar_lammps_mixin.data_file_utils.section_line import (
    BondsLine,
    BoxBoundsHeaderLine,
    TiltFactorsHeaderLine,
)

from casar_lammps_mixin.data_types import BondPair, EntityInfo
from casar_lammps_mixin.pbc_construct import PeriodicBoundaryConditionShifts


@dataclass
class BondGenerator:
    """Generate the Bond section of a LAMMPS data file from the provided atoms."""

    bond_dict: dict[BondPair, EntityInfo]
    atoms_reference: pd.DataFrame
    x_bounds: BoxBoundsHeaderLine
    y_bounds: BoxBoundsHeaderLine
    z_bounds: BoxBoundsHeaderLine
    tilt_factors: Optional[TiltFactorsHeaderLine]

    def subset_by_atom_type(self, type: int, with_images: bool) -> pd.DataFrame:
        """Subset a single atom type.

        Args:
            type: The atom type of interest
            with_images: If True, will include atom images

        Returns:
            A dataframe of subset atoms
        """
        subset = self.atoms_reference[self.atoms_reference["atom_type"] == type]
        if with_images:
            pbc = PeriodicBoundaryConditionShifts(
                reference=subset,
                x_bounds=self.x_bounds,
                y_bounds=self.y_bounds,
                z_bounds=self.z_bounds,
                tilt_factors=self.tilt_factors,
            )
            return pbc.image_by_symmetry().reset_index(drop=True)
        return subset.reset_index(drop=True)

    def create_bond_data(
        self, atom1_type: int, atom2_type: int, cutoff: float
    ) -> Iterator[Tuple[int, int]]:
        """Generate bonds between the two atoms queried from the provided cutoff.

        Args:
            atom1_type: The atom type of the first atom in the bond
            atom2_type: The atom type of the second atom in the bond
            cutoff: The cutoff radius for querying the second atoms in the bond

        Yields:
            The generated bond from the queried cutoff as BondData
        """
        df_atom1 = self.subset_by_atom_type(type=atom1_type, with_images=False)
        df_atom2 = self.subset_by_atom_type(type=atom2_type, with_images=True)

        query = df_atom1[["x", "y", "z"]].to_numpy()
        X = df_atom2[["x", "y", "z"]].to_numpy()
        tree = KDTree(X, leaf_size=2)
        indices = tree.query_radius(query, r=cutoff)
        for atom1_index, atom2_indices in enumerate(indices):
            a1 = int(df_atom1.iloc[atom1_index]["index"])
            for atom2_index in atom2_indices:
                a2 = int(df_atom2.iloc[atom2_index]["index"])
                yield a1, a2

    def generate_bonds(self) -> Iterator[BondsLine]:
        """Generate all bonds for the Bond section.

        Yields:
            The generated bond from the queried cutoff as BondData
        """
        index = 1
        for (atom1_type, atom2_type), values in self.bond_dict.items():
            for atom1_index, atom2_index in self.create_bond_data(
                atom1_type, atom2_type, cutoff=float(values["cutoff"])
            ):
                yield BondsLine(
                    index=index,
                    bond_type=int(values["bond_type"]),
                    atom1=atom1_index,
                    atom2=atom2_index,
                )
                index += 1

    # def plot_distributions(self, bonds_dataframe: pd.DataFrame) -> None:
    #     """Plot the distribution of bond distances.

    #     Args:
    #         bonds_dataframe: A dataframe with calculated bond distances
    #     """
    #     a1 = self.reference.iloc[bonds_dataframe["atom1_index"] - 1]
    #     a2 = self.reference.iloc[bonds_dataframe["atom2_index"] - 1]
    #     bonds_dataframe["distance"] = np.linalg.norm(
    #         a2[["x", "y", "z"]].values - a1[["x", "y", "z"]].values, axis=1
    #     )
    #     for bond_type in bonds_dataframe["type"].unique():
    #         subset = bonds_dataframe[bonds_dataframe["type"] == bond_type]["distance"]
    #         plt.figure()
    #         subset.hist()
    #         plt.title(f"{self.info.filepath}: Bond {bond_type}")
    #         plt.savefig(f"bond{bond_type}.png")

    # def collect_bond_section(self, checkpoint: bool) -> list[BondData]:
    #     """Update the data info with the newly generated bonds.

    #     Args:
    #         checkpoint: If true, will generate plots of generated bond distances.

    #     Returns:
    #         A list of bonds for the Bond section.
    #     """
    #     bonds = list(self.generate_bonds())
    #     df_bonds = pd.DataFrame(bonds)
    #     self.info.bonds = df_bonds.shape[0]
    #     self.info.bond_types = len(df_bonds["type"].unique())

    #     if checkpoint:
    #         self.plot_distributions(df_bonds)

    #     return bonds
