import os
import torch
import gc
import threading
import time
import psutil

def cpu():
    """
    Returns the CPU device.

    Returns:
        torch.device: The CPU device.
    """
    return torch.device('cpu')

def gpu(i=0, cuda=True):
    """
    If cuda is true and gpu is available, return gpu (i); otherwise, return cpu()
    :param i: Index i, indicating which GPU block to use
    :param cuda: Boolean value indicating whether to use cuda, if not, CPU can be used, set to False
    """
    if cuda and torch.cuda.is_available() and torch.cuda.device_count() >= i + 1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')

def allgpu():
    """
    Those who can use this function must be very rich.
    """
    devices = []
    for i in range(torch.cuda.device_count()):
        devices.append(i)
    return devices if devices else [torch.device('cpu')]

def num_workers(batch_size):
    """
    确定用于数据加载的并行工作进程的数量
    """
    num_workers = min([os.cpu_count(), batch_size if batch_size > 1 else 0, 8])
    return num_workers

def release_memory(*args):
    """
    Function to release memory resources, particularly useful when working with PyTorch and CUDA.
    """
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    if not isinstance(args, list):
        args = list(args)
    for i in range(len(args)):
        args[i] = None
    gc.collect()
    return args


class PeakCPUMemory:
    def __init__(self):
        self.process = psutil.Process()
        self.peak_monitoring = False

    def peak_monitor(self):
        self.cpu_memory_peak = -1

        while True:
            self.cpu_memory_peak = max(self.process.memory_info().rss, self.cpu_memory_peak)
            if not self.peak_monitoring:
                break

    def start(self):
        self.peak_monitoring = True
        self.thread = threading.Thread(target=self.peak_monitor)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.peak_monitoring = False
        self.thread.join()
        return self.cpu_memory_peak

cpu_peak_tracker = PeakCPUMemory()

def start_measure():
    # Time
    measures = {"time": time.time()}

    gc.collect()
    torch.cuda.empty_cache()

    # CPU mem
    measures["cpu"] = psutil.Process().memory_info().rss
    cpu_peak_tracker.start()

    # GPU mem
    for i in range(torch.cuda.device_count()):
        measures[str(i)] = torch.cuda.memory_allocated(i)
    torch.cuda.reset_peak_memory_stats()

    return measures

def end_measure(start_measures):
    # Time
    measures = {"time": time.time() - start_measures["time"]}

    gc.collect()
    torch.cuda.empty_cache()

    # CPU mem
    measures["cpu"] = (psutil.Process().memory_info().rss - start_measures["cpu"]) / 2**20
    measures["cpu-peak"] = (cpu_peak_tracker.stop() - start_measures["cpu"]) / 2**20

    # GPU mem
    for i in range(torch.cuda.device_count()):
        measures[str(i)] = (torch.cuda.memory_allocated(i) - start_measures[str(i)]) / 2**20
        measures[f"{i}-peak"] = (torch.cuda.max_memory_allocated(i) - start_measures[str(i)]) / 2**20

    return measures

def log_measures(measures, description):
    print(f"{description}:")
    print(f"- Time: {measures['time']:.2f}s")
    for i in range(torch.cuda.device_count()):
        print(f"- GPU {i} allocated: {measures[str(i)]:.2f}MiB")
        peak = measures[f"{i}-peak"]
        print(f"- GPU {i} peak: {peak:.2f}MiB")
    print(f"- CPU RAM allocated: {measures['cpu']:.2f}MiB")
    print(f"- CPU RAM peak: {measures['cpu-peak']:.2f}MiB")

if __name__=="__main__":
    def simple_computation():
        a = torch.randn(1000, 1000)
        b = torch.randn(1000, 1000)
        c = torch.matmul(a, b)
        return c

    start_measures = start_measure()

    result = simple_computation()
    measures = end_measure(start_measures)
    log_measures(measures, "Simple Computation")

