#################################################################################
# WaterTAP Copyright (c) 2020-2023, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National Laboratory,
# National Renewable Energy Laboratory, and National Energy Technology
# Laboratory (subject to receipt of any required approvals from the U.S. Dept.
# of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/watertap/"
#################################################################################

import pyomo.environ as pyo
from idaes.core import declare_process_block_class
from idaes.core.base.costing_base import FlowsheetCostingBlockData
from idaes.models.unit_models import Mixer, HeatExchanger, CSTR

from watertap.core.util.misc import is_constant_up_to_units

from watertap.costing.unit_models.mixer import cost_mixer
from watertap.costing.unit_models.heat_exchanger import cost_heat_exchanger
from watertap.costing.unit_models.cstr import cost_cstr


@declare_process_block_class("WaterTAPCostingBlock")
class WaterTAPCostingBlockData(FlowsheetCostingBlockData):
    """
    Base class for creating WaterTAP costing packages. Allows
    unit models to "self-register" their default costing methods,
    and for anonymous expressions in flow costs.
    """

    # Define default mapping of costing methods to unit models
    unit_mapping = {
        Mixer: cost_mixer,
        HeatExchanger: cost_heat_exchanger,
        CSTR: cost_cstr,
    }

    def add_LCOW(self, flow_rate, name="LCOW"):
        """
        Add Levelized Cost of Water (LCOW) to costing block.
        Args:
            flow_rate - flow rate of water (volumetric) to be used in
                        calculating LCOW
            name (optional) - name for the LCOW variable (default: LCOW)
        """

        self.add_component(
            name,
            pyo.Expression(
                expr=(
                    self.total_capital_cost * self.capital_recovery_factor
                    + self.total_operating_cost
                )
                / (
                    pyo.units.convert(
                        flow_rate, to_units=pyo.units.m**3 / self.base_period
                    )
                    * self.utilization_factor
                ),
                doc=f"Levelized Cost of Water based on flow {flow_rate.name}",
            ),
        )

    def add_specific_energy_consumption(
        self, flow_rate, name="specific_energy_consumption"
    ):
        """
        Add specific energy consumption (kWh/m**3) to costing block.
        Args:
            flow_rate - flow rate of water (volumetric) to be used in
                        calculating specific energy consumption
            name (optional) - the name of the Expression for the specific
                              energy consumption (default: specific_energy_consumption)
        """

        self.add_component(
            name,
            pyo.Expression(
                expr=self.aggregate_flow_electricity
                / pyo.units.convert(
                    flow_rate, to_units=pyo.units.m**3 / pyo.units.hr
                ),
                doc=f"Specific energy consumption based on flow {flow_rate.name}",
            ),
        )

    def add_annual_water_production(self, flow_rate, name="annual_water_production"):
        """
        Add annual water production to costing block.
        Args:
            flow_rate - flow rate of water (volumetric) to be used in
                        calculating annual water production
            name (optional) - name for the annual water productionvariable
                              Expression (default: annual_water_production)
        """
        self.add_component(
            name,
            pyo.Expression(
                expr=(
                    pyo.units.convert(
                        flow_rate, to_units=pyo.units.m**3 / self.base_period
                    )
                    * self.utilization_factor
                ),
                doc=f"Annual water production based on flow {flow_rate.name}",
            ),
        )

    def add_electricity_intensity(self, flow_rate, name="electricity_intensity"):
        """
        Add calculation of overall electricity intensity to costing block.
        Args:
            flow_rate - flow rate of water (volumetric) to be used in
                        calculating electricity intensity
            name (optional) - the name of the Expression for the specific
                              electrical intensity (default: specific_electrical_carbon_intensity)
        """
        self.add_specific_energy_consumption(flow_rate, name=name)

    def add_specific_electrical_carbon_intensity(
        self, flow_rate, name="specific_electrical_carbon_intensity"
    ):
        """
        Add specific electrical carbon intensity (kg_CO2eq/m**3) to costing block.
        Args:
            flow_rate - flow rate of water (volumetric) to be used in
                        calculating specific electrical carbon intensity
            name (optional) - the name of the Expression for the specific
                              carbon intensity (default: specific_electrical_carbon_intensity)
        """

        self.add_component(
            name,
            pyo.Expression(
                expr=self.aggregate_flow_electricity
                * self.electrical_carbon_intensity
                / pyo.units.convert(
                    flow_rate, to_units=pyo.units.m**3 / pyo.units.hr
                ),
                doc=f"Specific electrical carbon intensity based on flow {flow_rate.name}",
            ),
        )

    def _build_common_process_costs(self):
        """
        Build the common process costs to WaterTAP Costing Packages.
        The currency units should already be registered.

        The derived class should add constraints for total_capital_cost
        and total_operating_cost
        """
        self.total_capital_cost = pyo.Var(
            initialize=0,
            doc="Total capital cost of the process",
            units=self.base_currency,
        )
        self.total_operating_cost = pyo.Var(
            initialize=0,
            doc="Total operating cost of process per operating period",
            units=self.base_currency / self.base_period,
        )

    def _build_common_global_params(self):
        """
        Build the global parameters common to WaterTAP Costing Packages.
        The currency units should already be registered.

        The derived class should define the capital_recovery_factor.
        """

        self.utilization_factor = pyo.Var(
            initialize=0.9,
            doc="Plant capacity utilization [fraction of uptime]",
            units=pyo.units.dimensionless,
        )

        self.electricity_cost = pyo.Var(
            initialize=0.07,
            doc="Electricity cost",
            units=pyo.units.USD_2018 / pyo.units.kWh,
        )
        self.defined_flows["electricity"] = self.electricity_cost

        self.electrical_carbon_intensity = pyo.Var(
            initialize=0.475,
            doc="Grid carbon intensity [kgCO2_eq/kWh]",
            units=pyo.units.kg / pyo.units.kWh,
        )

        self.capital_recovery_factor = pyo.Expression(
            expr=0,
            doc="Capital annualization factor [fraction of investment cost/year]",
        )

        self.TPEC = pyo.Var(
            initialize=3.4 * (2.0 / 1.65),
            doc="Total Purchased Equipment Cost (TPEC)",
            units=pyo.units.dimensionless,
        )

        self.TIC = pyo.Var(
            initialize=2.0,
            doc="Total Installed Cost (TIC)",
            units=pyo.units.dimensionless,
        )

        self.fix_all_vars()

    @staticmethod
    def add_cost_factor(blk, factor):
        if factor == "TPEC":
            blk.cost_factor = pyo.Expression(expr=blk.costing_package.TPEC)
        elif factor == "TIC":
            blk.cost_factor = pyo.Expression(expr=blk.costing_package.TIC)
        else:
            blk.cost_factor = pyo.Expression(expr=1.0)
        blk.direct_capital_cost = pyo.Expression(
            expr=blk.capital_cost / blk.cost_factor
        )

    def _get_costing_method_for(self, unit_model):
        """
        Allow the unit model to register its default costing method,
        either through an attribute named "default_costing_method"
        or by naming the default costing method "default_costing_method"
        """
        if hasattr(unit_model, "default_costing_method"):
            return unit_model.default_costing_method
        return super()._get_costing_method_for(unit_model)

    def aggregate_costs(self):
        """
        This method aggregates costs from all the unit models and flows
        registered with this FlowsheetCostingBlock and creates aggregate
        variables for these on the FlowsheetCostingBlock that can be used for
        further process-wide costing calculations.

        The following costing variables are aggregated from all the registered
        UnitModelCostingBlocks (if they exist):

        * capital_cost,
        * direct_capital_cost,
        * fixed_operating_cost, and
        * variable_operating_cost

        Additionally, aggregate flow variables are created for all registered
        flow types along with aggregate costs associated with each of these.

        Args:
            None
        """
        super().aggregate_costs()
        c_units = self.base_currency

        @self.Expression(doc="Aggregation Expression for direct capital cost")
        def aggregate_direct_capital_cost(blk):
            e = 0
            for u in self._registered_unit_costing:
                # Allow for units that might only have a subset of cost Vars
                if hasattr(u, "direct_capital_cost"):
                    e += pyo.units.convert(u.direct_capital_cost, to_units=c_units)
                elif hasattr(u, "capital_cost"):
                    raise RuntimeError(
                        f"WaterTAP models with a capital_cost must also supply a direct_capital_cost. Found unit {u.unit_model} with `capital_cost` but no `direct_capital_cost`."
                    )

            return e

    def register_flow_type(self, flow_type, cost):
        """
        This method allows users to register new material and utility flows
        with the FlowsheetCostingBlock for use when costing flows.
        If `cost` is a constant (up to units), then this method creates a new
        `Var` on the FlowsheetCostingBlock named f`{flow_type}_cost`.
        Otherwise `cost` is a non-constant expression and this method will
        create a new `Expression` on the FlowsheetCostingBlock named
        f`{flow_type}_cost` whose value is fixed to `cost`.

        If a component named f`{flow_type}_cost` already exists on the
        FlowsheetCostingBlock, then an error is raised unless f`{flow_type}_cost`
        is `cost`. If f`{flow_type}_cost` is `cost`, no error is raised and
        the existing component f`{flow_type}_cost` is used to cost the flow.

        Args:
            flow_type: string name to represent flow type
            cost: a Pyomo expression with units representing the flow cost
        """

        flow_cost_name = flow_type + "_cost"
        current_flow_cost = self.component(flow_cost_name)
        if (current_flow_cost is None) and (not is_constant_up_to_units(cost)):
            cost_expr = pyo.Expression(expr=cost)
            self.add_component(flow_cost_name, cost_expr)
            super().register_flow_type(flow_type, cost_expr)
        else:
            # all other cases are handled in the base class
            super().register_flow_type(flow_type, cost)
