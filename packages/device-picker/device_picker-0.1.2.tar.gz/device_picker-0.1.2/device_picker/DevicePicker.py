import platform


class DevicePicker:
    """
    A class to pick the appropriate device for machine learning tasks
    based on the availability and user preference for frameworks like
    PyTorch, TensorFlow, and JAX. Handles import errors gracefully if a
    particular framework is not installed in the environment.
    """

    def __init__(self):
        self.frameworks = {}
        self._check_framework_availability()

    def _check_framework_availability(self):
        """
        Checks which machine learning frameworks are available in the
        current environment and updates the frameworks dictionary.
        """
        try:
            global torch
            import torch

            self.frameworks["pytorch"] = True
        except ImportError:
            self.frameworks["pytorch"] = False

        try:
            global tf
            import tensorflow as tf

            self.frameworks["tensorflow"] = True
        except ImportError:
            self.frameworks["tensorflow"] = False

        try:
            global jax
            import jax

            self.frameworks["jax"] = True
        except ImportError:
            self.frameworks["jax"] = False

    def pytorch_device(self, device: str = "") -> "torch.device":
        if not self.frameworks["pytorch"]:
            raise ImportError("PyTorch is not available in this environment.")
        if (not device or device.startswith("cuda")) and torch.cuda.is_available():
            print("Use CUDA")
            return torch.device(device)
        if (
            (not device or device.startswith("mps"))
            and torch.backends.mps.is_available()
            and torch.backends.mps.is_built()
            and platform.machine() == 'arm64'
        ):
            print("Use MPS")
            return torch.device("mps")

        print("Use CPU")
        return torch.device("cpu")

    def tensorflow_device(self, device: str = "") -> str:
        device = device.upper()
        if not self.frameworks["tensorflow"]:
            raise ImportError("TensorFlow is not available in this environment.")
        if not device:
            device = "GPU" if tf.config.list_physical_devices("GPU") else "CPU"
        print(f"Use {device}")
        return device

    def jax_device(self, device: str = "") -> str:
        if not self.frameworks["jax"]:
            raise ImportError("JAX is not available in this environment.")
        if (not device or device.lower().startswith('metal') or device.lower() == 'mps') and jax.default_backend() == 'METAL':
            print(f"Use Metal")
            return jax.devices()
        if (not device or device.lower().startswith('cuda') or device.lower().startswith('gpu') ) and jax.default_backend() == 'gpu':
            print(f"Use GPU")
            return jax.devices()
                
        print("Use CPU")
        return jax.devices('cpu')

