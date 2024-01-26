"""
Library of SPAM image correlation functions.
Copyright (C) 2020 SPAM Contributors

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy

# 2017-05-29 ER and EA
# This is spam's C++ DIC toolkit, but since we're in the tools/ directory we can import it directly
from spam.DIC.DICToolkit import pixelSearch as pixelSearchCPP


def _errorCalc(im1, im2):
    return numpy.nansum(numpy.square(numpy.subtract(im1, im2))) / numpy.nansum(im1)


def pixelSearch(
    imagette1, imagette2, imagette1mask=None, imagette2mask=None, returnError=False
):
    """
    This function performs a pixel-by-pixel search in 3D for a small reference imagette1 within a larger imagette2.

    The normalised correlation coefficient (NCC) is computed for EVERY combination of the displacements of imagette1 defined within imagette2.
    What is returned is the highest NCC value obtained and the position where it was obtained with respect to the origin in imagette2.

    Values of NCC > 0.99 can generally be trusted.

    Parameters
    ----------
        imagette1 : 3D numpy array of floats
            Imagette 1 is the smaller reference image

        imagette2 : 3D numpy array of floats
            Imagette 2 is the bigger image inside which to search

        imagette1mask : 3D numpy array of bools, optional
            A mask for imagette1 to define which pixels to include in the correlation
            (True = Correlate these pixels, False = Skip),
            Default = no mask

        imagette2mask : 3D numpy array of bools, optional
            A mask for imagette2 to define which pixels to include in the correlation
            (True = Correlate these pixels, False = Skip),
            Default = no mask

        returnError : bool, optional
            Return a normalised sum of squared differences error compatible with
            register() family of functions? If yes, it's the last returned variable
            Default = False

    Returns
    -------
        p : 3-component vector
            Z, Y, X position with respect to origin in imagette2 of imagette1 to get best NCC

        cc : float
            Normalised correlation coefficient, ~0.5 is random, >0.99 is very good correlation.
    """
    # Note
    # ----
    # It important to remember that the C code runs A BIT faster in its current incarnation when it has
    # a cut-out im2 to deal with (this is related to processor optimistaions).
    # Cutting out imagette2 to just fit around the search range might save a bit of time
    assert numpy.all(
        imagette2.shape >= imagette1.shape
    ), "spam.DIC.pixelSearch(): imagette2 should be bigger or equal to imagette1 in all dimensions"

    if imagette1mask is not None:
        assert (
            imagette1.shape == imagette1mask.shape
        ), "spam.DIC.pixelSearch: imagette1mask ({}) should have same size as imagette1 ({})".format(
            imagette1mask.shape, imagette1.shape
        )
        imagette1 = imagette1.astype("<f4")
        imagette1[imagette1mask == 0] = numpy.nan

    if imagette2mask is not None:
        assert (
            imagette2.shape == imagette2mask.shape
        ), "spam.DIC.pixelSearch: imagette2mask ({}) should have same size as imagette2 ({})".format(
            imagette2mask.shape, imagette2.shape
        )
        imagette2 = imagette2.astype("<f4")
        imagette2[imagette2mask == 0] = numpy.nan

    # Run the actual pixel search
    returns = numpy.zeros(4, dtype="<f4")
    pixelSearchCPP(imagette1.astype("<f4"), imagette2.astype("<f4"), returns)

    if returnError:
        error = _errorCalc(
            imagette1,
            imagette2[
                int(returns[0]) : int(returns[0]) + imagette1.shape[0],
                int(returns[1]) : int(returns[1]) + imagette1.shape[1],
                int(returns[2]) : int(returns[2]) + imagette1.shape[2],
            ],
        )
        return numpy.array(returns[0:3]), returns[3], error

    else:
        return numpy.array(returns[0:3]), returns[3]
