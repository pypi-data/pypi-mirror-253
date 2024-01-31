"""
Miscellaneous testing code
"""
from abc import ABC, abstractmethod

import numpy as np
import numpy.testing as npt
from scmdata import ScmRun

from openscm_runner import run


def _get_output_dict(  # pylint: disable=too-many-locals,too-many-branches
    res, outputs_to_get
):
    """
    Get output dictionary

    Returns a dictionary of outputs which can be used with our regression testing.

    Parameters
    ----------
    res
        Results from which to extract outputs

    outputs_to_get
        Outputs to get from the results

    Returns
    -------
        Dictionary of results which can be understood by our regression tests
    """
    output = {}
    for climate_model, checks in outputs_to_get.items():
        res_cm = res.filter(climate_model=climate_model)

        for filter_kwargs in checks:
            err_msg = f"{filter_kwargs}"
            filter_kwargs_in = {**filter_kwargs}
            check_units = filter_kwargs.pop("unit", None)
            quantile = filter_kwargs.pop("quantile")
            res_to_check = res_cm.filter(**filter_kwargs)

            if check_units is not None:
                res_to_check = res_to_check.convert_unit(check_units)

            if res_to_check.empty:
                raise AssertionError(err_msg)

            res_val = float(
                res_to_check.process_over(
                    ("climate_model", "run_id"), "quantile", q=quantile
                ).values
            )

            key = ["climate_model", climate_model]
            for k, v in filter_kwargs_in.items():
                key.append(k)
                key.append(v)

            # key = tuple(key)
            key = "_".join([str(v) for v in key])
            output[key] = np.array([res_val])

    return output


class _AdapterTester(ABC):  # nosec
    """
    Base class for testing adapters.

    All adapters should have a test class which sub-classes this class and
    implements all abstract methods.
    """

    # pylint: disable=pointless-string-statement
    """float: relative tolerance for numeric comparisons"""
    _rtol = 1e-5

    """
    tuple[str]: variable names which are expected to be used by all adapters

    This could be replaced with the RCMIP variables in future (bigger job)
    """
    _common_variables = (
        "Surface Air Temperature Change",
        "Surface Air Ocean Blended Temperature Change",
        "Effective Radiative Forcing",
        "Effective Radiative Forcing|Anthropogenic",
        "Effective Radiative Forcing|Aerosols",
        "Effective Radiative Forcing|Aerosols|Direct Effect",
        "Effective Radiative Forcing|Aerosols|Direct Effect|BC",
        "Effective Radiative Forcing|Aerosols|Direct Effect|BC|MAGICC Fossil and Industrial",  # noqa: E501
        "Effective Radiative Forcing|Aerosols|Direct Effect|BC|MAGICC AFOLU",
        "Effective Radiative Forcing|Aerosols|Direct Effect|OC",
        "Effective Radiative Forcing|Aerosols|Direct Effect|OC|MAGICC Fossil and Industrial",  # noqa: E501
        "Effective Radiative Forcing|Aerosols|Direct Effect|OC|MAGICC AFOLU",
        "Effective Radiative Forcing|Aerosols|Direct Effect|SOx",
        "Effective Radiative Forcing|Aerosols|Direct Effect|SOx|MAGICC Fossil and Industrial",  # noqa: E501
        "Effective Radiative Forcing|Aerosols|Direct Effect|SOx|MAGICC AFOLU",
        "Effective Radiative Forcing|Aerosols|Indirect Effect",
        "Effective Radiative Forcing|Greenhouse Gases",
        "Effective Radiative Forcing|CO2",
        "Effective Radiative Forcing|CH4",
        "Effective Radiative Forcing|N2O",
        "Effective Radiative Forcing|F-Gases",
        "Effective Radiative Forcing|HFC125",
        "Effective Radiative Forcing|HFC134a",
        "Effective Radiative Forcing|HFC143a",
        "Effective Radiative Forcing|HFC227ea",
        "Effective Radiative Forcing|HFC23",
        "Effective Radiative Forcing|HFC245fa",
        "Effective Radiative Forcing|HFC32",
        "Effective Radiative Forcing|HFC4310mee",
        "Effective Radiative Forcing|CF4",
        "Effective Radiative Forcing|C6F14",
        "Effective Radiative Forcing|C2F6",
        "Effective Radiative Forcing|SF6",
        "Heat Uptake",
        "Heat Uptake|Ocean",
        "Atmospheric Concentrations|CO2",
        "Atmospheric Concentrations|CH4",
        "Atmospheric Concentrations|N2O",
        "Net Atmosphere to Land Flux|CO2",
        "Net Atmosphere to Ocean Flux|CO2",
    )

    def _check_res(self, exp, check_val, raise_error):
        try:
            npt.assert_allclose(exp, check_val, rtol=self._rtol)
        except AssertionError:
            if raise_error:
                raise

            print(f"exp: {exp}, check_val: {check_val}")

    def _get_output_dict(self, res, outputs_to_get):
        return _get_output_dict(res, outputs_to_get)

    @staticmethod
    def _check_heat_content_heat_uptake_consistency(res):
        hc_deltas = ScmRun(
            res.filter(variable="Heat Content", region="World")
            .timeseries(time_axis="year")
            .diff(axis="columns")
        )
        hc_deltas["unit"] = f"{hc_deltas.get_unique_meta('unit', True)} / yr"

        ratio = hc_deltas.divide(  # pylint: disable=no-member
            res.filter(variable="Heat Uptake", region="World"),
            op_cols={"variable": "Heat Content / Heat Uptake"},
        )

        earth_surface_area = 5.100536e14
        npt.assert_allclose(
            earth_surface_area,
            ratio.convert_unit("m^2").timeseries(drop_all_nan_times=True),
        )

    @abstractmethod
    def test_run(self, test_scenarios):
        """
        Test that the model can be run, ideally with more than one configuration
        """
        # pseudo-code
        res = run(
            climate_models_cfgs={
                "climate_model": [
                    {"para1": "value1", "para2": 1.1},
                    {"para1": "value3", "para2": 1.2},
                    {"para1": "value5", "para2": 1.3},
                ],
            },
            scenarios=test_scenarios.filter(scenario=["ssp126", "ssp245", "ssp370"]),
            output_variables=(
                "output",
                "var",
                "list",
            ),
            out_config=None,
        )

        assert isinstance(res, ScmRun)  # nosec
        assert res["run_id"].min() == 0  # pylint: disable=compare-to-zero # nosec
        assert res["run_id"].min() == 0  # pylint: disable=compare-to-zero # nosec
        assert res["run_id"].max() == 8  # nosec

        assert res.get_unique_meta("climate_model", no_duplicates=True) == "model_name"  # nosec

        assert set(res.get_unique_meta("variable")) == {
            "expected",
            "output",
            "variables",
        }  # nosec

        # output value checks e.g.
        npt.assert_allclose(
            2.31,
            res.filter(
                variable="Surface Air Temperature Change",
                region="World",
                year=2100,
                scenario="ssp126",
            ).values.max(),
            rtol=self._rtol,
        )

    @abstractmethod
    def test_variable_naming(self, test_scenarios):
        """
        Test that variable naming is implemented as expecteds
        """
        # pseudo-code

        # a model might not report all outputs
        missing_variables = (
            "Net Atmosphere to Ocean Flux|CO2",
            "Net Atmosphere to Land Flux|CO2",
        )
        common_variables = [
            c for c in self._common_variables if c not in missing_variables
        ]

        # run the model and request all common variables the model reportss
        res = run(
            climate_models_cfgs={"climate_model": ({"para1": 3.43},)},
            scenarios=test_scenarios.filter(scenario="ssp126"),
            output_variables=common_variables,
        )

        # check that all expected outputs were returned
        missing_vars = set(common_variables) - set(res["variable"])
        if missing_vars:
            raise AssertionError(missing_vars)
