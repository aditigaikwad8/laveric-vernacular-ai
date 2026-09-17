from __future__ import annotations

from typing import Any

from api.schemas.ai_model_configuration import EffectiveAIModelConfiguration

MPS_CORRELATION_ID_CONTEXT_KEY = "mps_correlation_id"


def get_mps_correlation_id(initial_context: dict[str, Any] | None) -> str | None:
    if not initial_context:
        return None
    correlation_id = initial_context.get(MPS_CORRELATION_ID_CONTEXT_KEY)
    if correlation_id is None:
        return None
    return str(correlation_id)


