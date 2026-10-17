"""Repairs for Teufel Raumfeld (Raumkernel Addon)."""

from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant.components.repairs import RepairsFlow
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult


class RestartRequiredFixFlow(RepairsFlow):
    """Offer to restart Home Assistant after the integration was updated."""

    def __init__(self, version: str | None) -> None:
        """Initialize."""
        self._version = version

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the first step of the fix flow."""
        return await self.async_step_confirm()

    async def async_step_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Restart Home Assistant once the user submits."""
        if user_input is not None:
            await self.hass.services.async_call("homeassistant", "restart")
            return self.async_create_entry(title="", data={})

        return self.async_show_form(
            step_id="confirm",
            data_schema=vol.Schema({}),
            description_placeholders={"version": self._version or ""},
        )


async def async_create_fix_flow(
    hass: HomeAssistant,
    issue_id: str,
    data: dict[str, Any] | None,
) -> RepairsFlow:
    """Create the fix flow for a Raumfeld repair issue."""
    return RestartRequiredFixFlow((data or {}).get("version"))
