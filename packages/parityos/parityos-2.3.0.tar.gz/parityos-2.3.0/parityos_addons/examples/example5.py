"""
Parity Quantum Computing GmbH
Rennweg 1 Top 314
6020 Innsbruck, Austria

Copyright (c) 2020-2022.
All rights reserved.

A ParityOS usage example tailored to the QPU with star-topology.
"""
from parityos import CompilerClient, ParityOSOutput
from parityos.base import Circuit, CNOT, Qubit
from parityos.device_model import DeviceModelBase
from parityos_addons.interfaces import QiskitExporter
from parityos_addons.spin_hamiltonians import SpinZ, spinz_to_hamiltonian


class StarDevice(DeviceModelBase):
    """
    Describes a quantum device with star topology, with entangling gates between the central
    qubit and each of the outer qubits.
    """

    device_type = "cnot"
    preset = "digital_default"

    def __init__(self, outer_size: int = 3):
        """
        Create a device model where the qubits are laid out in a star topology, with the first
        qubit in the center and the outer qubits connected only to the central one. The number
        of outer qubits is set by the `outer_size` argument.

        :param int outer_size: Number of outer qubits.
        """
        qubit_connections = {frozenset({Qubit((0, 0)), Qubit((1, r))}) for r in range(outer_size)}
        self.set_qubit_connections(qubit_connections, add_local_fields=True)


def fan_in_circuit(outer_size: int = 3) -> Circuit:
    """
    Create a fan-in circuit for a quantum device with star topology.

    :param int outer_size: Number of outer qubits.
    :returns: A circuit of CNOT gates from all outer qubits targeted on the central qubit.
    """
    central_qubit = Qubit((0, 0))
    outer_qubits = [Qubit((1, i)) for i in range(outer_size)]
    return Circuit([CNOT(outer_qubit, central_qubit) for outer_qubit in outer_qubits])


def parityos_example5(
    logical_size: int = 5,
    physical_size: int = 4,
    username: str = "",
) -> ParityOSOutput:
    """
    Compile a dimple Ising model on a star-shaped digital device.

    :param int logical_size: The number of spins in the Ising model.
    :param int physical_size: Total number of qubits on the device.
    :param str username: A valid ParityOS username (if not given, then the ```PARITYOS_USER```
                         environment variable is used instead).
    :returns: The ParityOS output object containing the compiled problem.
    """
    # Define a problem Hamiltonian: the all-to-all connected Ising model
    spins = [SpinZ(label) for label in range(logical_size)]
    ising_model = sum(spin1 * spin2 for spin1, spin2 in zip(spins[:-1], spins[1:]))
    optimization_problem = spinz_to_hamiltonian(ising_model)

    # Create a device model that is big enough to contain the compiled problem
    # For the all-to-all connected case, compilation on a rectangular device requires more qubits
    # than the optimal LHZ triangle, therefore we set the size to twice the number of interactions.
    device_model = StarDevice(outer_size=physical_size - 1)
    print(
        f"Map {len(optimization_problem.interactions)} interactions "
        f"on {len(device_model.qubits)} qubits."
    )
    assert len(optimization_problem.interactions) <= len(device_model.qubits)

    # Compile the logical problem
    compiler_client = CompilerClient(username)
    parityos_output = compiler_client.compile(optimization_problem, device_model)

    # Create a circuit from the output
    parityos_circuit = parityos_output.initial_state_preparation_circuit
    # Add additional entangling gates
    parityos_circuit.append(fan_in_circuit(outer_size=physical_size - 1))

    # Transform to Qiskit
    qiskit_exporter = QiskitExporter(qubits=device_model.qubits)
    qiskit_circuit = qiskit_exporter.to_qiskit(parityos_circuit)

    return qiskit_circuit


if __name__ == "__main__":
    print(parityos_example5())
