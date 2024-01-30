# -*- coding: utf-8 -*-

from odoo import models, api


class RecurrenceRule(models.Model):
    _inherit = 'calendar.recurrence'

    @api.model
    def _rrule_parse(self, rule_str, date_start):
        rule_str = self._clean_rrule_str(rule_str)
        return super()._rrule_parse(rule_str, date_start)

    def _clean_rrule_str(rule_str):
        """Remove rrule property parameters not supported by the dateutil.rrule library."""
        if not rule_str.startswith("RRULE;"):
            return rule_str
        right = rule_str[6:]
        parts = right.split(":", maxsplit=1)
        if len(parts) == 2:
            # Rebuild string without parameters
            return f"RRULE:{parts[1]}"
        return rule_str  # rrule parser fail
