from abc import ABC, abstractmethod
from typing import Tuple, Optional, List

import numpy as np

from vg_bodypix.vendor.types import Box


class AbstractModel(ABC):
    """AbstractModel
    Base class of the model.
    """
    _runtime: str = 'onnx'
    _model_path: str = ''
    _map_score_th: float = 0.6
    _input_shapes: List[List[int]] = []
    _input_names: List[str] = []
    _output_shapes: List[List[int]] = []
    _output_names: List[str] = []

    # onnx/tflite
    _interpreter = None
    _inference_model = None
    _providers = None
    _swap = (2, 0, 1)
    _h_index = 2
    _w_index = 3

    # onnx
    _onnx_dtypes_to_np_dtypes = {
        "tensor(float)": np.float32,
        "tensor(uint8)": np.uint8,
        "tensor(int8)": np.int8,
    }

    # tflite
    _input_details = None
    _output_details = None

    @abstractmethod
    def __init__(
            self,
            *,
            runtime: Optional[str] = 'onnx',
            model_path: Optional[str] = '',
            map_score_th: Optional[float] = 0.6,
            providers: Optional[List] = [
                (
                        'TensorrtExecutionProvider', {
                            'trt_engine_cache_enable': True,
                            'trt_engine_cache_path': '.',
                            'trt_fp16_enable': True,
                        }
                ),
                'CUDAExecutionProvider',
                'CPUExecutionProvider',
            ],
    ):
        self._runtime = runtime
        self._model_path = model_path
        self._map_score_th = map_score_th
        self._providers = providers

        # Model loading
        if self._runtime == 'onnx':
            import onnxruntime  # type: ignore
            session_option = onnxruntime.SessionOptions()
            session_option.log_severity_level = 3
            self._interpreter = \
                onnxruntime.InferenceSession(
                    model_path,
                    sess_options=session_option,
                    providers=providers,
                )
            self._providers = self._interpreter.get_providers()
            self._input_shapes = [
                input.shape for input in self._interpreter.get_inputs()
            ]
            self._input_names = [
                input.name for input in self._interpreter.get_inputs()
            ]
            self._input_dtypes = [
                self._onnx_dtypes_to_np_dtypes[input.type] for input in self._interpreter.get_inputs()
            ]
            self._output_shapes = [
                output.shape for output in self._interpreter.get_outputs()
            ]
            self._output_names = [
                output.name for output in self._interpreter.get_outputs()
            ]
            self._model = self._interpreter.run
            self._swap = (2, 0, 1)
            self._h_index = 2
            self._w_index = 3
            self.strides: int = 0

        elif self._runtime in ['tflite_runtime', 'tensorflow']:
            if self._runtime == 'tflite_runtime':
                from tflite_runtime.interpreter import Interpreter  # type: ignore
                self._interpreter = Interpreter(model_path=model_path)
            elif self._runtime == 'tensorflow':
                import tensorflow as tf  # type: ignore
                self._interpreter = tf.lite.Interpreter(model_path=model_path)
            self._input_details = self._interpreter.get_input_details()
            self._output_details = self._interpreter.get_output_details()
            self._input_shapes = [
                input.get('shape', None) for input in self._input_details
            ]
            self._input_names = [
                input.get('name', None) for input in self._input_details
            ]
            self._input_dtypes = [
                input.get('dtype', None) for input in self._input_details
            ]
            self._output_shapes = [
                output.get('shape', None) for output in self._output_details
            ]
            self._output_names = [
                output.get('name', None) for output in self._output_details
            ]
            self._model = self._interpreter.get_signature_runner()
            self._swap = (0, 1, 2)
            self._h_index = 1
            self._w_index = 2
        elif self._runtime == 'openvino':
            import openvino as ov  # type: ignore
            import vg_bodypix.vendor.openvino_utils as ov_utils

            core = ov.Core()
            model = core.read_model(model=model_path)

            # adjust model to use new map score threshold
            ov_utils.set_mask_score_threshold(model, self._map_score_th)

            compiled_model = core.compile_model(model=model, device_name=providers[0])

            self._interpreter = compiled_model
            # self._providers = self._interpreter.get_providers()
            self._input_shapes = [
                list(input.shape) for input in self._interpreter.inputs
            ]
            self._input_names = [
                input.node.friendly_name for input in self._interpreter.inputs
            ]
            self._input_dtypes = [
                input.element_type.to_dtype().type for input in self._interpreter.inputs
            ]
            self._output_shapes = [
                list(output.shape) for output in self._interpreter.outputs
            ]
            self._output_names = [
                output.node.friendly_name for output in self._interpreter.outputs
            ]
            self._model = compiled_model
            self._swap = (2, 0, 1)
            self._h_index = 2
            self._w_index = 3
            self.strides: int = 0

    @abstractmethod
    def __call__(
            self,
            *,
            input_datas: List[np.ndarray],
    ) -> List[np.ndarray]:
        datas = {
            f'{input_name}': input_data \
            for input_name, input_data in zip(self._input_names, input_datas)
        }
        if self._runtime == 'onnx':
            outputs = [
                output for output in \
                self._model(
                    output_names=self._output_names,
                    input_feed=datas,
                )
            ]
            return outputs
        elif self._runtime in ['tflite_runtime', 'tensorflow']:
            outputs = [
                output for output in \
                self._model(
                    **datas
                ).values()
            ]
            return outputs
        elif self._runtime == 'openvino':
            infer_request = self._model.create_infer_request()

            infer_request.infer(inputs=datas)

            infer_request.start_async()
            infer_request.wait()

            outputs = [infer_request.get_output_tensor(i).data for i in range(len(self._output_names))]
            return outputs

    @abstractmethod
    def _preprocess(
            self,
            *,
            image: np.ndarray,
            swap: Optional[Tuple[int, int, int]] = (2, 0, 1),
    ) -> np.ndarray:
        pass

    @abstractmethod
    def _postprocess(
            self,
            *,
            image: np.ndarray,
            boxes: np.ndarray,
    ) -> List[Box]:
        pass

    @property
    def input_shapes(self) -> List[List[int]]:
        return self._input_shapes

    @property
    def input_size(self) -> Tuple[int, int]:
        shape = self.input_shapes[0]
        return shape[self._w_index], shape[self._h_index]
