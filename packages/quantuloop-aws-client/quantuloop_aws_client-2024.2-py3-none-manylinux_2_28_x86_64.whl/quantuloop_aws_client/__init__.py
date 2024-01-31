# Copyright 2024 Quantuloop
"""Client for Quantuloop Quantum Simulator Suite for HPC on AWS."""

import getpass
import random
from functools import partial
from typing import Callable, Literal
from ctypes import cdll, POINTER, c_uint8, c_size_t, c_uint64, c_bool, c_void_p
from os import PathLike, path
from cryptography.hazmat.primitives import serialization


CLIB = cdll.LoadLibrary(
    path.join(path.dirname(__file__), "libquloop_simulation_client.so")
)

MAKE_CONFIG = CLIB.quloop_simulator_client_make_configuration
MAKE_CONFIG.argtypes = [
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint8),
    c_size_t,
    POINTER(c_uint8),
    c_size_t,
    c_uint64,
    c_size_t,
    c_size_t,
    c_bool,
]
MAKE_CONFIG.restype = c_void_p


def setup_server(
    url: str,
    private_key: PathLike,
    passphrase: bool | bytes | None = None,
) -> Callable:
    """Configure simulation server.

    Example:

        .. code-block:: python

            import quantuloop_aws_client as ql

            server = ql.setup_server(
                url="http://127.0.0.1:8000",
                private_key="~/.ssh/id_rsa",
                passphrase=True,
            )

            from ket import Process

            process = Process(server(
                num_qubits=182,
                simulator="quantuloop::sparse"
            ))


    See :func:`quantuloop_aws_client.make_configuration` for more details.

    .. note::

        The quantum execution is configured in batch mode.

    Args:
        url:  Server URL, for example, https://example.com or http://127.0.0.1:8080.
        private_key: Path for the OpenSSH RSA private key.
        passphrase: Password to decrypt the private key. Set to `True` to prompt
            for the password, or pass the password in plain text in bytes.
            Set to `None` if the key is not encrypted. Default: `None`.

    Returns:
        A callable to configure Ket precesses.
    """
    url = url.encode("utf-8")
    url_len = len(url)

    if isinstance(passphrase, bool):
        if passphrase:
            passphrase = bytes(
                getpass.getpass(f"passphrase for {private_key}:"), "utf-8"
            )
        else:
            passphrase = None

    with open(path.expandvars(path.expanduser(private_key)), "rb") as file:
        private_key = serialization.load_ssh_private_key(file.read(), passphrase)
        private_key = private_key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption(),
        )

    private_key_len = len(private_key)

    return partial(
        make_configuration,
        server_config=(
            (c_uint8 * url_len)(*url),
            url_len,
            (c_uint8 * private_key_len)(*private_key),
            private_key_len,
        ),
    )


def make_configuration(  # pylint: disable=too-many-arguments
    num_qubits: int,
    simulator: Literal[
        "kbw::dense", "kbw::sparse", "quantuloop::dense", "quantuloop::sparse"
    ],
    gpu_count: int = 0,
    precision: Literal[1, 2] = 1,
    seed: int | None = None,
    *,
    server_config,
):
    """Generate configuration for Ket process.

    This functions is not intended to be called directly. Instead,
    :func:`quantuloop_aws_client.setup_server` should be used to configure
    the quantum execution.


    Example:

        .. code-block:: python

            import quantuloop_aws_client as ql

            server = ql.setup_server( # this is a partial call for make_configuration.
                url="http://127.0.0.1:8000",
                private_key="~/.ssh/id_rsa",
                passphrase=True,
            )

            from ket import Process

            process = Process(server(
                num_qubits=182,
                simulator="quantuloop::sparse"
            ))

    Args:
        num_qubits: Number of qubits in the simulations.
        simulator: Simulator identifier.
        gpu_count: Maximum number of GPUs; if set to 0, simulation will use all
            available GPUs. Defaults to 0.
        precision: floating point precision used in the simulation; positive
            values are: 1 for single precision (float) and 2 for double precision.
            Defaults to 1.
        seed: Seed for the quantum execution RNG. Defaults to None.
        server_config: Generated from :func:`quantuloop_aws_client.setup_server`.

    Returns:
        Configuration for Ket process.
    """
    simulator = simulator.encode("utf-8")
    simulator_len = len(simulator)

    if seed is None:
        seed = random.randint(0, 2**64 - 1)

    return MAKE_CONFIG(
        *server_config,
        (c_uint8 * simulator_len)(*simulator),
        simulator_len,
        seed,
        num_qubits,
        gpu_count,
        precision == 2,
    )
