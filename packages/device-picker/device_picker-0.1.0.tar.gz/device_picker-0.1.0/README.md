# Device Picker
<p align="center"><img width="250" height="250" margin-right="100%" src="image/logo.png"></p>

## Description

Device Picker is a Python package designed to automatically select the appropriate computational device for machine learning tasks. It supports various frameworks like PyTorch, TensorFlow, and JAX. This tool is particularly useful in environments where multiple computational backends are available, as it simplifies the process of device selection based on the user's preferences and system capabilities.

## Installation

To install Device Picker, use the following pip command:

```bash
pip install device-picker
```

For users on macOS with Apple Silicon (M1, M2 chips), to enable Metal support:

```bash
# for jax
pip install device-picker[jax_metal_support] 
# for tensorflow
pip install device-picker[tensorflow_metal_support] 
```

## Usage

To use the Device Picker in your project, import the `DevicePicker` class and create an instance of it. The class methods `pytorch_device`, `tensorflow_device`, and `jax_device` can optionally take a device name as an argument. If a device name is given, the Device Picker will attempt to use the specified device if it is available. If no device name is provided or if the specified device is not available, the Device Picker will automatically select a suitable default device.

```python
from device_picker import DevicePicker

# Create an instance of DevicePicker
device_picker = DevicePicker()

# Select a specific device for PyTorch, or let the picker choose automatically
pytorch_device = device_picker.pytorch_device('cuda') # You can specify 'cuda', 'mps', or leave it empty

# Select a specific device for TensorFlow
tensorflow_device = device_picker.tensorflow_device('GPU') # Options could be 'GPU', 'CPU', etc.

# Select a specific device for JAX
jax_device = device_picker.jax_device('gpu') # Choose 'gpu', 'tpu', or others

```

## Running Tests

To run the unit tests for Device Picker, execute the following command in the root directory of the project:

```bash
make test
```

## Contributing

Contributions to Device Picker are welcome! Please feel free to submit pull requests, open issues, or suggest improvements.

## License

Device Picker is released under the MIT License. See the [LICENSE](LICENSE) file for more details.