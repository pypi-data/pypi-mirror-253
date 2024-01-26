from enum import Enum


class HXRequestHeaders(str, Enum):
    hx_request = "HX-Request"
    hx_boosted = "HX-Boosted"
    hx_current_url = "HX-Current-URL"
    hx_history_restore_request = "HX-History-Restore-Request"
    hx_prompt = "HX-Prompt"
    hx_target = "HX-Target"
    hx_trigger = "HX-Trigger"
    hx_trigger_name = "HX-Trigger-Name"


class HXResponseHeaders(str, Enum):
    hx_location = "HX-Location"
    hx_push_url = "HX-Push-Url"
    hx_redirect = "HX-Redirect"
    hx_refresh = "HX-Refresh"
    hx_replace_url = "HX-Replace-Url"
    hx_reswap = "HX-Reswap"
    hx_retarget = "HX-Retarget"
    hx_reselect = "HX-Reselect"
    hx_trigger = "HX-Trigger"
    hx_trigger_after_settle = "HX-Trigger-After-Settle"
    hx_trigger_after_swap = "HX-Trigger-After-Swap"
