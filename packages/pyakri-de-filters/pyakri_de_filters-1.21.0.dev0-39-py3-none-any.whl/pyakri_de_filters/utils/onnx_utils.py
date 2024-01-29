from __future__ import annotations

import os
from typing import List

import onnxruntime
from numba import cuda

# 0:Verbose, 1:Info, 2:Warning, 3:Error, 4:Fatal
ONNXRUNTIME_DEFAULT_LOG_LEVEL = "3"

onnxruntime.set_default_logger_severity(
    int(os.getenv("ONNXRUNTIME_DEFAULT_LOG_LEVEL", ONNXRUNTIME_DEFAULT_LOG_LEVEL))
)


def get_onnx_session(
    onnx_model: str | bytes | os.PathLike,
    providers: List[str] = None,
    gpu_mem_fraction: str = None,
) -> onnxruntime.InferenceSession:
    if not providers:
        providers = onnxruntime.get_available_providers()
    session = onnxruntime.InferenceSession(onnx_model, providers=providers)
    option = session.get_provider_options().get("CUDAExecutionProvider")
    if option:
        # setting gpu memory fraction
        gpu_mem_fraction = float(gpu_mem_fraction) if gpu_mem_fraction else 0.95
        new_mem_limit = int(
            int(cuda.current_context().get_memory_info().total) * gpu_mem_fraction
        )
        option["gpu_mem_limit"] = new_mem_limit
        session.set_providers(["CUDAExecutionProvider"], [option])
    return session
