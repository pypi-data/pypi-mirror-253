from multiprocessing import Process, Queue, cpu_count, current_process
from threading import Thread


def _create_queue(parameters: list) -> Queue:
    """
    Transform a list with sets of parameters into a FIFO queue.

    Parameters
    ----------
    parameters: list
        List containing sets of parameters.

    Returns
    -------
    Queue:
        Given parameters in a FIFO queue.
    """
    queue = Queue()

    for parameter in parameters:
        queue.put(parameter)

    return queue


def _run_multi(multi: callable, target: callable, parameters: list, number: int = None) -> None:
    """
    Shared steps in the 'run_processes' and 'run_threads' functions.

    Parameters
    ----------
    multi: callable:
        Either 'run_processes' or 'run_threads'.
    target: callable
        Callable to be run repeatedly.
    parameters: list
        List containing sets of parameters to repeatedly run the callable with.
    number: int
        Number of subprocesses or threads to run.
    """
    # Create a FIFO queue containing the given parameters.
    queue = _create_queue(parameters=parameters)

    # Create the given number of subprocesses / threads.
    if multi == run_processes:
        multi = cpu_count() if number is None else number
        multi = [Process(target=_run_target, args=[target, queue]) for _ in range(multi)]
    else:
        multi = cpu_count() * 8 if number is None else number
        multi = [Thread(target=_run_target, args=[target, queue]) for _ in range(multi)]

    # Start the subprocesses / threads and wait for them to finish before continuing.
    [item.start() for item in multi]
    [item.join() for item in multi]

    # Close the queue and its thread.
    queue.close()
    queue.join_thread()


def _run_target(target: callable, parameters: Queue) -> None:
    """
    Repeatedly run a callable until its queue is empty.

    Parameters
    ----------
    target: callable
        Callable to run until the queue is empty.
    parameters: Queue
        Queue containing sets of parameters to repeatedly run the callable with.
    """
    while not parameters.empty():
        parameter = parameters.get()
        target(*parameter)


def run_processes(target: callable, parameters: list, processes: int = None) -> None:
    """
    Run computationally heavy workloads faster by using multiprocessing.

    WARNING:

    It is recommended to use this function with an 'if name equals main' statement.
    Code outside this statement runs repeatedly as well when calling this function.
    This function is protected against endless recursion caused by itself.
    It can be used outside an 'if name equals main' statement if necessary.
    It is recommended to use a lock when writing to a single file.

    Parameters
    ----------
    target: callable
        Callable to be run repeatedly.
    parameters: list
        List containing sets of parameters to repeatedly run the callable with.
    processes: int
        Number of subprocesses to run.
        It can be equal to or less than the number of available CPU cores.
        It is the number of available CPU cores by default.
    """
    if current_process().name != "MainProcess":
        return

    _run_multi(multi=run_processes, target=target, parameters=parameters, number=processes)


def run_threads(target: callable, parameters: list, threads: int = None) -> None:
    """
    Run I/O heavy workloads faster by using multithreading.

    WARNING:

    It is recommended to use a lock when writing to a single file.

    Parameters
    ----------
    target: callable
        Callable to be run repeatedly.
    parameters: list
        List containing sets of parameter to repeatedly run the callable with.
    threads: int
        Number of threads to run.
        It is eight times the number of available CPU cores by default.
    """
    _run_multi(multi=run_threads, target=target, parameters=parameters, number=threads)
