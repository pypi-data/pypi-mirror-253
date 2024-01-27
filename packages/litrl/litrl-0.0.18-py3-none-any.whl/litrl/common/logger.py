from __future__ import annotations

from pathlib import Path
from typing import Any

from lightning.pytorch.loggers import MLFlowLogger
from loguru import logger


class LitRLLogger(MLFlowLogger):
    def __init__(
        self,
        run_id: str | None = None,
        tags: dict[str, Any] | None = None,
        save_dir: str | None = None,
        *,
        log_model: bool = True,
    ) -> None:
        if save_dir is None:
            save_dir = Path("temp", "mlruns").as_uri()
            logger.info(f"Save dir is {save_dir}")
        super().__init__(
            tracking_uri=save_dir,
            artifact_location=save_dir,
            save_dir=save_dir,
            tags=tags,
            log_model=log_model,
            run_id=run_id,
        )
        self._save_dir = save_dir

    @property
    def save_dir(self) -> str:
        return self._save_dir
