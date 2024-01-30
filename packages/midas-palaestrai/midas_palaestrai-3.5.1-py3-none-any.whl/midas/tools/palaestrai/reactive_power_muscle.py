from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Optional, Dict, Any

import numpy as np

from palaestrai.agent import Muscle
from palaestrai.types import Box

if TYPE_CHECKING:
    from palaestrai.agent import SensorInformation, ActuatorInformation

LOG = logging.getLogger("palaestrai.agent.Muscle.ReactivePowerMuscle")


class ReactivePowerMuscle(Muscle):
    # This mapping echoes the mapping in the MIDAS config. The MIDAS config
    # is authoritative. This happens to be here because we need to map
    # sensor-actuator (bus voltage - q value), but can't peek at the MIDAS
    # config.
    SENSOR_ACTUATOR_MAPPING = {
        # Sensor ID : Actuator ID
        "0-bus-3.vm_pu": "Photovoltaic-0.q_set_mvar",
        "0-bus-4.vm_pu": "Photovoltaic-1.q_set_mvar",
        "0-bus-5.vm_pu": "Photovoltaic-2.q_set_mvar",
        "0-bus-6.vm_pu": "Photovoltaic-3.q_set_mvar",
        "0-bus-7.vm_pu": "Photovoltaic-4.q_set_mvar",
        "0-bus-8.vm_pu": "Photovoltaic-5.q_set_mvar",
        "0-bus-9.vm_pu": "Photovoltaic-6.q_set_mvar",
        "0-bus-11.vm_pu": "Photovoltaic-7.q_set_mvar",
        "0-bus-13.vm_pu": "Photovoltaic-8.q_set_mvar",
    }

    STEP_SIZE = 5.0

    def __init__(
        self, sensor_actuator_mapping: Optional[Dict] = None, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self._sensor_actuator_mapping = (
            sensor_actuator_mapping
            if sensor_actuator_mapping
            else ReactivePowerMuscle.SENSOR_ACTUATOR_MAPPING
        )
        self._setpoints = {}

    def setup(self):
        pass

    def propose_actions(
        self, sensors, actuators_available, is_terminal=False
    ) -> tuple:
        LOG.debug(
            "%s: sensors: %s, actuators available: %s",
            self,
            sensors,
            actuators_available,
        )

        relevant_sensors = {
            short_sid: sensor
            for short_sid in self._sensor_actuator_mapping.keys()
            for sensor in sensors
            if short_sid in sensor.sensor_id
        }
        relevant_actuators = {
            short_aid: actuator
            for short_aid in self._sensor_actuator_mapping.values()
            for actuator in actuators_available
            if short_aid in actuator.actuator_id
        }

        LOG.debug("%s => %s", relevant_sensors, relevant_actuators)

        def _clip_reshape_value(
            setpoint: Any, actuator: ActuatorInformation
        ) -> np.array:
            assert isinstance(actuator.space, Box)
            actuator_box: Box = actuator.space
            _clipped_reshaped_value = actuator_box.reshape_to_space(
                np.clip(
                    setpoint,
                    a_min=actuator_box.low,
                    a_max=actuator_box.high,
                )
            )
            return _clipped_reshaped_value

        def _set_actuator_for_sensor(short_id, sensor: SensorInformation):
            sensor_reading = sensor()
            aid = self._sensor_actuator_mapping[short_id]
            prev_setpoint = self._setpoints.get(aid, None)
            actuator: ActuatorInformation = relevant_actuators[aid]
            setpoint = _clip_reshape_value(
                ReactivePowerMuscle._setpoint(sensor_reading, prev_setpoint),
                actuator,
            )
            self._setpoints[aid] = setpoint

            actuator(setpoint)
            return actuator

        new_setpoints = [
            _set_actuator_for_sensor(ssid, sensor)
            for ssid, sensor in relevant_sensors.items()
            if self._sensor_actuator_mapping[ssid] in relevant_actuators
        ]

        for a in [a for a in actuators_available if a not in new_setpoints]:
            clipped_reshaped_value = _clip_reshape_value(0.0, a)
            a(clipped_reshaped_value)
            new_setpoints.append(a)

        LOG.debug("%s: new setpoints: %s", self, new_setpoints)
        return new_setpoints

    @staticmethod
    def _setpoint(sensor_value, prev_setpoint):
        """Make sure the voltage actually fluctuates around V=1 pu! Otherwise
        the setpoint will simply converge to -1 or 1."""
        if prev_setpoint is None:
            return 0.0

        return float(
            prev_setpoint - ReactivePowerMuscle.STEP_SIZE * (sensor_value - 1)
        )

    def update(self, update):
        pass

    def prepare_model(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return f"{self.__class__}(id=0x{id(self):x})"
