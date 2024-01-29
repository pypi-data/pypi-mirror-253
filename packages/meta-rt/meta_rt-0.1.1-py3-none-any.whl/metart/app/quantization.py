import tensorrt as trt


class Quantization:
    def __init__(self,
                 model_path: str,  # onnx model name
                 precision="fp16",
                 workspace=12):
        self.model_path = model_path
        self.precision = precision
        self.workspace = workspace

    def convert(self, ):
        logger = trt.Logger(trt.Logger.INFO)
        builder = trt.Builder(logger)
        config = builder.create_builder_config()
        config.max_workspace_size = self.workspace * 1 << 30

        flag = 1 << int(trt.NetworkDefinitionCreationFlag.EXPLICIT_BATCH)
        network = builder.create_network(flag)

        parser = trt.OnnxParser(network, logger)
        if not parser.parse_from_file(self.model_path):
            raise RuntimeError(f'Failed to load ONNX file: {self.model_path}')

        inputs = [network.get_input(i) for i in range(network.num_inputs)]
        outputs = [network.get_output(i) for i in range(network.num_outputs)]
        for _input in inputs:
            print("Input '{}' with shape {} and dtype {}".format(_input.name, _input.shape, _input.dtype))
        for _output in outputs:
            print("Output '{}' with shape {} and dtype {}".format(_output.name, _output.shape, _output.dtype))

        if builder.platform_has_fast_fp16 and self.precision == "fp16":
            config.set_flag(trt.BuilderFlag.FP16)
        elif builder.platform_has_fast_int8 and self.precision == "int8":
            config.set_flag(trt.BuilderFlag.INT8)

        with builder.build_engine(network, config) as engine, \
                open(self.model_path.replace('.onnx', '.rt'), 'wb') as f:
            f.write(engine.serialize())
