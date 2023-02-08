"""Test PurpleAir diagnostics."""
from homeassistant.components.diagnostics import REDACTED

from tests.components.diagnostics import get_diagnostics_for_config_entry


async def test_entry_diagnostics(hass, config_entry, hass_client, setup_config_entry):
    """Test config entry diagnostics."""
    assert await get_diagnostics_for_config_entry(hass, hass_client, config_entry) == {
        "entry": {
            "entry_id": config_entry.entry_id,
            "version": 1,
            "domain": "purpleair",
            "title": REDACTED,
            "data": {
                "api_key": REDACTED,
            },
            "options": {
                "sensor_indices": [
                    123456,
                ],
            },
            "pref_disable_new_entities": False,
            "pref_disable_polling": False,
            "source": "user",
            "unique_id": REDACTED,
            "disabled_by": None,
        },
        "data": {
            "fields": [
                "sensor_index",
                "name",
                "location_type",
                "model",
                "hardware",
                "firmware_version",
                "rssi",
                "uptime",
                "latitude",
                "longitude",
                "altitude",
                "humidity",
                "temperature",
                "pressure",
                "voc",
                "pm1.0",
                "pm2.5",
                "pm10.0",
                "0.3_um_count",
                "0.5_um_count",
                "1.0_um_count",
                "2.5_um_count",
                "5.0_um_count",
                "10.0_um_count",
            ],
            "data": {
                "123456": {
                    "sensor_index": 123456,
                    "altitude": 569.0,
                    "analog_input": None,
                    "channel_flags": None,
                    "channel_flags_auto": None,
                    "channel_flags_manual": None,
                    "channel_state": None,
                    "confidence": None,
                    "confidence_auto": None,
                    "confidence_manual": None,
                    "date_created_utc": None,
                    "deciviews": None,
                    "deciviews_a": None,
                    "deciviews_b": None,
                    "firmware_upgrade": None,
                    "firmware_version": "7.02",
                    "hardware": "2.0+BME280+PMSX003-B+PMSX003-A",
                    "humidity": 13.0,
                    "humidity_a": None,
                    "humidity_b": None,
                    "icon": None,
                    "is_owner": None,
                    "last_modified_utc": None,
                    "last_seen_utc": None,
                    "latitude": REDACTED,
                    "led_brightness": None,
                    "location_type": {
                        "__type": "<enum 'LocationType'>",
                        "repr": "<LocationType.OUTSIDE: 0>",
                    },
                    "longitude": REDACTED,
                    "memory": None,
                    "model": "PA-II",
                    "name": "Test Sensor",
                    "ozone1": None,
                    "pa_latency": None,
                    "pm0_3_um_count": 76.0,
                    "pm0_3_um_count_a": None,
                    "pm0_3_um_count_b": None,
                    "pm0_5_um_count": 68.0,
                    "pm0_5_um_count_a": None,
                    "pm0_5_um_count_b": None,
                    "pm10_0": 0.0,
                    "pm10_0_a": None,
                    "pm10_0_atm": None,
                    "pm10_0_atm_a": None,
                    "pm10_0_atm_b": None,
                    "pm10_0_b": None,
                    "pm10_0_cf_1": None,
                    "pm10_0_cf_1_a": None,
                    "pm10_0_cf_1_b": None,
                    "pm10_0_um_count": 0.0,
                    "pm10_0_um_count_a": None,
                    "pm10_0_um_count_b": None,
                    "pm1_0": 0.0,
                    "pm1_0_a": None,
                    "pm1_0_atm": None,
                    "pm1_0_atm_a": None,
                    "pm1_0_atm_b": None,
                    "pm1_0_b": None,
                    "pm1_0_cf_1": None,
                    "pm1_0_cf_1_a": None,
                    "pm1_0_cf_1_b": None,
                    "pm1_0_um_count": 0.0,
                    "pm1_0_um_count_a": None,
                    "pm1_0_um_count_b": None,
                    "pm2_5": 0.0,
                    "pm2_5_10minute": None,
                    "pm2_5_10minute_a": None,
                    "pm2_5_10minute_b": None,
                    "pm2_5_1week": None,
                    "pm2_5_1week_a": None,
                    "pm2_5_1week_b": None,
                    "pm2_5_24hour": None,
                    "pm2_5_24hour_a": None,
                    "pm2_5_24hour_b": None,
                    "pm2_5_30minute": None,
                    "pm2_5_30minute_a": None,
                    "pm2_5_30minute_b": None,
                    "pm2_5_60minute": None,
                    "pm2_5_60minute_a": None,
                    "pm2_5_60minute_b": None,
                    "pm2_5_6hour": None,
                    "pm2_5_6hour_a": None,
                    "pm2_5_6hour_b": None,
                    "pm2_5_a": None,
                    "pm2_5_alt": None,
                    "pm2_5_alt_a": None,
                    "pm2_5_alt_b": None,
                    "pm2_5_atm": None,
                    "pm2_5_atm_a": None,
                    "pm2_5_atm_b": None,
                    "pm2_5_b": None,
                    "pm2_5_cf_1": None,
                    "pm2_5_cf_1_a": None,
                    "pm2_5_cf_1_b": None,
                    "pm2_5_um_count": 0.0,
                    "pm2_5_um_count_a": None,
                    "pm2_5_um_count_b": None,
                    "pm5_0_um_count": 0.0,
                    "pm5_0_um_count_a": None,
                    "pm5_0_um_count_b": None,
                    "position_rating": None,
                    "pressure": 1000.74,
                    "pressure_a": None,
                    "pressure_b": None,
                    "primary_id_a": None,
                    "primary_id_b": None,
                    "primary_key_a": None,
                    "primary_key_b": None,
                    "private": None,
                    "rssi": -69,
                    "scattering_coefficient": None,
                    "scattering_coefficient_a": None,
                    "scattering_coefficient_b": None,
                    "secondary_id_a": None,
                    "secondary_id_b": None,
                    "secondary_key_a": None,
                    "secondary_key_b": None,
                    "stats": None,
                    "stats_a": None,
                    "stats_b": None,
                    "temperature": 82.0,
                    "temperature_a": None,
                    "temperature_b": None,
                    "uptime": 13788,
                    "visual_range": None,
                    "visual_range_a": None,
                    "visual_range_b": None,
                    "voc": None,
                    "voc_a": None,
                    "voc_b": None,
                },
                "567890": {
                    "sensor_index": 567890,
                    "altitude": 569.0,
                    "analog_input": None,
                    "channel_flags": None,
                    "channel_flags_auto": None,
                    "channel_flags_manual": None,
                    "channel_state": None,
                    "confidence": None,
                    "confidence_auto": None,
                    "confidence_manual": None,
                    "date_created_utc": None,
                    "deciviews": None,
                    "deciviews_a": None,
                    "deciviews_b": None,
                    "firmware_upgrade": None,
                    "firmware_version": "7.02",
                    "hardware": "2.0+BME280+PMSX003-B+PMSX003-A",
                    "humidity": 13.0,
                    "humidity_a": None,
                    "humidity_b": None,
                    "icon": None,
                    "is_owner": None,
                    "last_modified_utc": None,
                    "last_seen_utc": None,
                    "latitude": REDACTED,
                    "led_brightness": None,
                    "location_type": {
                        "__type": "<enum 'LocationType'>",
                        "repr": "<LocationType.OUTSIDE: 0>",
                    },
                    "longitude": REDACTED,
                    "memory": None,
                    "model": "PA-II",
                    "name": "Test Sensor 2",
                    "ozone1": None,
                    "pa_latency": None,
                    "pm0_3_um_count": 76.0,
                    "pm0_3_um_count_a": None,
                    "pm0_3_um_count_b": None,
                    "pm0_5_um_count": 68.0,
                    "pm0_5_um_count_a": None,
                    "pm0_5_um_count_b": None,
                    "pm10_0": 0.0,
                    "pm10_0_a": None,
                    "pm10_0_atm": None,
                    "pm10_0_atm_a": None,
                    "pm10_0_atm_b": None,
                    "pm10_0_b": None,
                    "pm10_0_cf_1": None,
                    "pm10_0_cf_1_a": None,
                    "pm10_0_cf_1_b": None,
                    "pm10_0_um_count": 0.0,
                    "pm10_0_um_count_a": None,
                    "pm10_0_um_count_b": None,
                    "pm1_0": 0.0,
                    "pm1_0_a": None,
                    "pm1_0_atm": None,
                    "pm1_0_atm_a": None,
                    "pm1_0_atm_b": None,
                    "pm1_0_b": None,
                    "pm1_0_cf_1": None,
                    "pm1_0_cf_1_a": None,
                    "pm1_0_cf_1_b": None,
                    "pm1_0_um_count": 0.0,
                    "pm1_0_um_count_a": None,
                    "pm1_0_um_count_b": None,
                    "pm2_5": 0.0,
                    "pm2_5_10minute": None,
                    "pm2_5_10minute_a": None,
                    "pm2_5_10minute_b": None,
                    "pm2_5_1week": None,
                    "pm2_5_1week_a": None,
                    "pm2_5_1week_b": None,
                    "pm2_5_24hour": None,
                    "pm2_5_24hour_a": None,
                    "pm2_5_24hour_b": None,
                    "pm2_5_30minute": None,
                    "pm2_5_30minute_a": None,
                    "pm2_5_30minute_b": None,
                    "pm2_5_60minute": None,
                    "pm2_5_60minute_a": None,
                    "pm2_5_60minute_b": None,
                    "pm2_5_6hour": None,
                    "pm2_5_6hour_a": None,
                    "pm2_5_6hour_b": None,
                    "pm2_5_a": None,
                    "pm2_5_alt": None,
                    "pm2_5_alt_a": None,
                    "pm2_5_alt_b": None,
                    "pm2_5_atm": None,
                    "pm2_5_atm_a": None,
                    "pm2_5_atm_b": None,
                    "pm2_5_b": None,
                    "pm2_5_cf_1": None,
                    "pm2_5_cf_1_a": None,
                    "pm2_5_cf_1_b": None,
                    "pm2_5_um_count": 0.0,
                    "pm2_5_um_count_a": None,
                    "pm2_5_um_count_b": None,
                    "pm5_0_um_count": 0.0,
                    "pm5_0_um_count_a": None,
                    "pm5_0_um_count_b": None,
                    "position_rating": None,
                    "pressure": 1000.74,
                    "pressure_a": None,
                    "pressure_b": None,
                    "primary_id_a": None,
                    "primary_id_b": None,
                    "primary_key_a": None,
                    "primary_key_b": None,
                    "private": None,
                    "rssi": -69,
                    "scattering_coefficient": None,
                    "scattering_coefficient_a": None,
                    "scattering_coefficient_b": None,
                    "secondary_id_a": None,
                    "secondary_id_b": None,
                    "secondary_key_a": None,
                    "secondary_key_b": None,
                    "stats": None,
                    "stats_a": None,
                    "stats_b": None,
                    "temperature": 82.0,
                    "temperature_a": None,
                    "temperature_b": None,
                    "uptime": 13788,
                    "visual_range": None,
                    "visual_range_a": None,
                    "visual_range_b": None,
                    "voc": None,
                    "voc_a": None,
                    "voc_b": None,
                },
            },
            "api_version": "V1.0.11-0.0.41",
            "firmware_default_version": "7.02",
            "max_age": 604800,
            "data_timestamp_utc": "2022-11-20T23:10:00",
            "timestamp_utc": "2022-11-20T23:10:17",
        },
    }
