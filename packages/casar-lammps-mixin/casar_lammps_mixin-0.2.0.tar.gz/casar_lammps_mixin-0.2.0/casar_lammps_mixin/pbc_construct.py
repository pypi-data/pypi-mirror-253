"""Assist with creating an expanded system using periodic boundary conditions."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

import pandas as pd

from casar_lammps_mixin.data_file_utils.section_line import (
    BoxBoundsHeaderLine,
    TiltFactorsHeaderLine,
)


class PBCShiftMixin:
    """A namespace for assisting with periodic boundary conditions."""

    @staticmethod
    def update_df(
        reference: pd.DataFrame,
        dx: pd.Series | None = None,
        dy: pd.Series | None = None,
        dz: pd.Series | None = None,
    ) -> pd.DataFrame:
        """Shift the positions of a given dimension.

        Args:
            reference: The dataframe from which positions are referenced
            dx: The shifted positions in the x-direction
            dy: The shifted positions in the y-direction
            dz: The shifted positions in the z-direction

        Returns:
            A dataframe with shifted positions
        """
        updated = reference.copy()
        if isinstance(dx, pd.Series):
            updated["x"] = dx
        if isinstance(dy, pd.Series):
            updated["y"] = dy
        if isinstance(dz, pd.Series):
            updated["z"] = dz
        return updated

    @classmethod
    def translate_x(cls, df: pd.DataFrame, shift: float) -> pd.DataFrame:
        """Translate in the x-dimension.

        Args:
            df: A dataframe with an "x"-column
            shift: Quantity to shift in the x-direction

        Returns:
            A dataframe that is shifted in the x-direction
        """
        shift = df["x"] + shift
        return cls.update_df(reference=df, dx=shift)

    @classmethod
    def translate_y(cls, df: pd.DataFrame, shift: float) -> pd.DataFrame:
        """Translate in the y-dimension.

        Args:
            df: A dataframe with a "y"-column
            shift: Quantity to shift in the y-direction

        Returns:
            A dataframe that is shifted in the y-direction
        """
        shift = df["y"] + shift
        return cls.update_df(reference=df, dy=shift)

    @classmethod
    def translate_z(cls, df: pd.DataFrame, shift: float) -> pd.DataFrame:
        """Translate in the z-dimension.

        Args:
            df: A dataframe with a "z"-column
            shift: Quantity to shift in the z-direction

        Returns:
            A dataframe that is shifted in the z-direction
        """
        shift = df["z"] + shift
        return cls.update_df(reference=df, dz=shift)

    @classmethod
    def translate_tilty(
        cls, df: pd.DataFrame, shift_y: float, shift_xy: float
    ) -> pd.DataFrame:
        """Translate along the xy-tilt.

        Args:
            df: A dataframe with an "x"- and "y"-column
            shift_y: Quantity to shift in the y-direction
            shift_xy: Quantity to shift the x-direction

        Returns:
            A dataframe that is shifted in the z-direction
        """
        col_shifty = df["y"] + shift_y
        col_shiftx = df["x"] + shift_xy
        return cls.update_df(reference=df, dx=col_shiftx, dy=col_shifty)

    @classmethod
    def translate_tiltz(
        cls, df: pd.DataFrame, shift_z: float, shift_xz: float, shift_yz: float
    ) -> pd.DataFrame:
        """Translate along the xz-tilt.

        Args:
            df: A dataframe with an "x", "y", and "z"-column
            shift_z: Quantity to shift in the z-direction
            shift_xz: Quantity to shift the x-direction
            shift_yz: Quantity to shift the y-direction

        Returns:
            A dataframe that is shifted in the z-direction
        """
        col_shiftz = df["z"] + shift_z
        col_shifty = df["y"] + shift_yz
        col_shiftx = df["x"] + shift_xz
        return cls.update_df(reference=df, dx=col_shiftx, dy=col_shifty, dz=col_shiftz)


@dataclass
class PeriodicBoundaryConditionShifts(PBCShiftMixin):
    """Apply periodic boundary shifts to atomic coordinates."""

    reference: pd.DataFrame
    x_bounds: BoxBoundsHeaderLine
    y_bounds: BoxBoundsHeaderLine
    z_bounds: BoxBoundsHeaderLine
    tilt_factors: Optional[TiltFactorsHeaderLine]

    def image_by_symmetry(self) -> pd.DataFrame:
        """Determine if the simulation box is orthogonal or orthoclinic.

        Returns:
            A dataframe with the reference and its images in all dimensions
        """
        if self.tilt_factors:
            # This means there is a tilt factor transforming an orthogonal system to a
            # parallelipiped. So, create images according to orthoclinic shifts.
            return self.combine_triclinic_shifts()
        else:
            # There are no tilt factors in the system. So, create images according to
            # orthogonal shfits.
            return self.combine_ortho_shifts()

    def combine_ortho_shifts(self) -> pd.DataFrame:
        """Combine all orthogonal shifts.

        Returns:
            A dataframe with the reference and its images in all dimensions
        """
        assert self.z_bounds is not None
        lx = self.x_bounds.max - self.x_bounds.min
        ly = self.y_bounds.max - self.y_bounds.min
        lz = self.z_bounds.max - self.z_bounds.min

        comb1 = pd.concat(
            [
                self.reference,
                self.translate_x(df=self.reference, shift=lx),
                self.translate_x(df=self.reference, shift=-lx),
            ]
        )
        comb2 = pd.concat(
            [
                comb1,
                self.translate_y(df=comb1, shift=ly),
                self.translate_y(df=comb1, shift=-ly),
            ]
        )
        comb3 = pd.concat(
            [
                comb2,
                self.translate_z(df=comb2, shift=lz),
                self.translate_z(df=comb2, shift=-lz),
            ]
        )
        return comb3

    def combine_triclinic_shifts(self) -> pd.DataFrame:
        """Combine all orthogonal shifts.

        Returns:
            A dataframe with the reference and its images in all dimensions
        """
        assert self.z_bounds is not None
        assert self.tilt_factors is not None
        lx = self.x_bounds.max - self.x_bounds.min
        ly = self.y_bounds.max - self.y_bounds.min
        lz = self.z_bounds.max - self.z_bounds.min

        comb1 = pd.concat(
            [
                self.reference,
                self.translate_x(df=self.reference, shift=lx),
                self.translate_x(df=self.reference, shift=-lx),
            ]
        )
        comb2 = pd.concat(
            [
                comb1,
                self.translate_tilty(
                    df=comb1, shift_y=ly, shift_xy=self.tilt_factors.xy
                ),
                self.translate_tilty(
                    df=comb1, shift_y=-ly, shift_xy=-self.tilt_factors.xy
                ),
            ]
        )
        comb3 = pd.concat(
            [
                comb2,
                self.translate_tiltz(
                    df=comb2,
                    shift_z=lz,
                    shift_xz=self.tilt_factors.xz,
                    shift_yz=self.tilt_factors.yz,
                ),
                self.translate_tiltz(
                    df=comb2,
                    shift_z=-lz,
                    shift_xz=-self.tilt_factors.xz,
                    shift_yz=-self.tilt_factors.yz,
                ),
            ]
        )
        return comb3
