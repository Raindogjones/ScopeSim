"""
Tests for Effect AutoExposure
"""
import pytest

from scopesim import rc
from scopesim import UserCommands
from scopesim.optics.image_plane import ImagePlane
from scopesim.effects.electronic import AutoExposure
from scopesim.utils import from_currsys

from scopesim.tests.mocks.py_objects.imagehdu_objects import _image_hdu_square

# pylint: disable=no-self-use, missing-class-docstring
# pylint: disable=missing-function-docstring

@pytest.fixture(name="imageplane", scope="class")
def fixture_imageplane():
    """Instantiate an ImagePlane object"""
    implane = ImagePlane(_image_hdu_square().header)
    implane.hdu.data += 1.e5
    return implane

@pytest.fixture(name="autoexposure", scope="class")
def fixture_autoexposure():
    """Instantiate an AutoExposure object"""
    return AutoExposure(fill_frac=0.75, full_well=1.e5, exptime=None,
                        mindit=0.011)

class TestAutoExposure:
    def test_initialises_correctly(self):
        autoexposure = AutoExposure(fill_frac=0.75,
                                    full_well=1.e5,
                                    exptime=None,
                                    mindit=0.011)
        assert isinstance(autoexposure, AutoExposure)

    def test_returns_imageplane(self, autoexposure, imageplane):
        rc.__currsys__ = UserCommands(properties={"!OBS.dit": 60,
                                                  "!OBS.ndit": 2})
        outimpl = autoexposure.apply_to(imageplane)
        assert isinstance(outimpl, ImagePlane)

    def test_produces_correct_values(self, autoexposure, imageplane):
        in_dit = 50
        in_ndit = 2
        exptime = in_dit * in_ndit
        rc.__currsys__ = UserCommands(properties={"!OBS.dit": in_dit,
                                                  "!OBS.ndit": in_ndit})

        # imageplane has 1e5 e/s, full_well is 1e5 e. To fill to 75% need:
        ref_dit = 0.75

        autoexposure.apply_to(imageplane)

        out_dit = from_currsys("!OBS.dit")
        out_ndit = from_currsys("!OBS.ndit")
        assert out_dit == ref_dit
        assert out_dit * out_ndit >= exptime
        assert out_dit * (out_ndit - 1) < exptime

    def test_detects_saturation(self, imageplane):
        mindit = 0.011
        autoexposure = AutoExposure(fill_frac=0.75,
                                    full_well=10.,
                                    exptime=None,
                                    mindit=mindit)
        autoexposure.apply_to(imageplane)

        out_dit = from_currsys("!OBS.dit")
        assert out_dit == mindit

    def test_exptime_overrides_dit_ndit(self, imageplane):
        rc.__currsys__ = UserCommands(properties={"!OBS.dit": 1,
                                                  "!OBS.ndit": 1})
        exptime = 100.
        autoexposure = AutoExposure(fill_frac=0.75,
                                    full_well=1e5,
                                    exptime=exptime,
                                    mindit=0.011)
        autoexposure.apply_to(imageplane)

        out_dit = from_currsys("!OBS.dit")
        out_ndit = from_currsys("!OBS.ndit")

        assert out_dit * out_ndit >=exptime
        assert out_dit * (out_ndit - 1) < exptime

    def test_fill_frac_acts_correctly(self, imageplane):
        fill_1 = 1.
        fill_2 = 0.5
        autoexp_1 = AutoExposure(fill_frac = fill_1,
                                 full_well = 1e5,
                                 exptime=None,
                                 mindit=0.011)
        rc.__currsys__ = UserCommands(properties={"!OBS.dit": 1,
                                                  "!OBS.ndit": 1})
        autoexp_1.apply_to(imageplane)
        out_dit_1 = from_currsys("!OBS.dit")
        out_ndit_1 = from_currsys("!OBS.ndit")

        autoexp_2 = AutoExposure(fill_frac = fill_2,
                                 full_well = 1e5,
                                 exptime=None,
                                 mindit=0.011)
        rc.__currsys__ = UserCommands(properties={"!OBS.dit": 1,
                                                  "!OBS.ndit": 1})
        autoexp_2.apply_to(imageplane)
        out_dit_2 = from_currsys("!OBS.dit")
        out_ndit_2 = from_currsys("!OBS.ndit")

        assert out_dit_1 == fill_1 / fill_2 * out_dit_2
        assert out_ndit_1 == fill_2 / fill_1 * out_ndit_2
