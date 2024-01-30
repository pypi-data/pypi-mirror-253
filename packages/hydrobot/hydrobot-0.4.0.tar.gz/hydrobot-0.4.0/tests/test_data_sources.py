"""Test the data_sources module."""
import pytest
from annalist.annalist import Annalist

import hydrobot.data_sources as data_sources

ann = Annalist()
ann.configure()


@pytest.mark.dependency(name="test_get_measurement_dict")
def test_get_measurement_dict():
    """Testing the measurement dictionary."""
    m_dict = data_sources.get_qc_evaluator_dict()
    assert isinstance(m_dict, dict), "not a dict somehow"
    assert (
        "Water Temperature [Dissolved Oxygen sensor]" in m_dict
    ), "Missing data source water temp"
    assert (
        m_dict["Water Temperature [Dissolved Oxygen sensor]"].qc_500_limit > 0
    ), "Water temp qc_500 limit not set up correctly"


@pytest.mark.dependency(depends=["test_get_measurement_dict"])
def test_get_measurement():
    """Testing the get_measurement method."""
    wt_meas = data_sources.get_qc_evaluator(
        "Water Temperature [Dissolved Oxygen sensor]"
    )
    assert wt_meas.qc_500_limit > 0, "Water temp qc_500 limit not set up correctly"
