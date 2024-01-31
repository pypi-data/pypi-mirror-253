"""The Quantuloop Quantum Simulator Suite for HPC is a collection of
high-performance quantum computer simulators for the Ket programming language.

As quantum algorithms explore distinct aspects of quantum computation
to extract advantages, there is no silver bullet for the simulation
of a quantum computer.

To use this simulator, you will need a Quantuloop Access Token. For more information,
visiting https://simulator.quantuloop.com."""

from __future__ import annotations

# Copyright (C) 2024 Quantuloop - All rights reserved

from os import environ, PathLike
from typing import Literal
import quantuloop_dense
import quantuloop_sparse


def set_token(token: str | None = None, token_file: PathLike | None = None):
    """Set Quantuloop Access Token.

    This token is used to authenticate access to the simulator.

    Args:
        token: A Quantuloop Access Token. This token is used to authenticate access to the
            simulator. If you do not provide a token, the simulator will not work.
        token_file: A file containing the Quantuloop Access Token. The file must contain a
            single line with the access token. If you specify both a token and a token file,
            the function will raise a ValueError.
    """
    quantuloop_dense.set_token(token, token_file)


def get_simulator(
    num_qubits: int,
    execution: Literal["live", "batch"] = "live",
    simulator: Literal["dense", "sparse"] | None = None,
    *,
    gpu_count: int | None = None,
    precision: Literal[1, 2] | None = None,
):
    """Get a Quantuloop simulator configuration.

    Args:
        num_qubits: Number of qubits in simulation.
        execution: Quantum execution mode.
        gpu_count: An integer that determine the maximum number of GPUs used in the execution.
            If set to 0, the simulator will use all available GPUs.
        precision: A integer the specifies the floating point precision used in the simulation.
            Positive values are 1 for single precision (float) and 2 for double precision.
    """

    if simulator == "dense":
        return quantuloop_dense.get_simulator(
            num_qubits=num_qubits,
            execution=execution,
            gpu_count=gpu_count,
            precision=precision,
        )
    if simulator == "sparse":
        return quantuloop_sparse.get_simulator(
            num_qubits=num_qubits,
            execution=execution,
            gpu_count=gpu_count,
            precision=precision,
        )
    raise ValueError("simulator must be 'dense' or 'sparse'")
