"""
Parity Quantum Computing GmbH
Rennweg 1 Top 314
6020 Innsbruck, Austria

Copyright (c) 2023.
All rights reserved.

Examples on ParityOS usage.
"""
from parityos import ParityOSOutput, ProblemRepresentation, Qubit
from parityos.compiler_client import CompilerClient
from parityos.device_model import RectangularDigitalDevice
from parityos_addons.examples.runner import run_example


def parityos_example1(
    physical_length: int = 5,
    physical_width: int = 5,
    username: str = "",
) -> ParityOSOutput:
    """
    Compile an all-to-all connected Ising model on a tilted rectangular digital device.

    :param int physical_length: The length of the rectangular lattice of qubits on the device.
    :param int physical_width: The width of the rectangular lattice of qubits on the device.
    :param str username: A valid ParityOS username (if not given, then the ```PARITYOS_USER```
                         environment variable is used instead).
    :returns: The ParityOS output object containing the compiled problem.
    """

    q = [Qubit(i) for i in range(6)]
    interactions = [
        {q[5], q[1]},
        {q[2], q[4]},
        {q[4], q[3]},
        {q[1], q[3]},
        {q[3], q[2]},
        {q[2], q[5]},
        {q[1], q[2]},
        {q[3], q[5]},
        {q[5], q[1], q[3], q[2]},
    ]
    coefficients = [0.625, 0.5, 0.5, 0.625, 0.625, 0.625, 0.125, 0.125, 0.125]
    optimization_problem = ProblemRepresentation(interactions, coefficients=coefficients)

    device_model = RectangularDigitalDevice(physical_length, physical_width)
    print(
        f"Map {len(optimization_problem.interactions)} interactions "
        f"on {len(device_model.qubits)} qubits."
    )
    assert len(optimization_problem.interactions) <= len(device_model.qubits)

    compiler_client = CompilerClient(username)
    parityos_output = compiler_client.compile(optimization_problem, device_model)
    return parityos_output


if __name__ == "__main__":
    run_example(parityos_example1)
