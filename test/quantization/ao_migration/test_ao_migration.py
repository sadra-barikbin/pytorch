# Owner(s): ["oncall: quantization"]

from .common import AOMigrationTestCase


class TestAOMigrationQuantization(AOMigrationTestCase):
    def test_package_import_quantize(self):
        self._test_package_import('quantize')

    def test_function_import_quantize(self):
        function_list = [
            '_convert',
            '_observer_forward_hook',
            '_propagate_qconfig_helper',
            '_remove_activation_post_process',
            '_remove_qconfig',
            'add_observer_',
            'add_quant_dequant',
            'convert',
            'get_observer_dict',
            'get_unique_devices_',
            'is_activation_post_process',
            'prepare',
            'prepare_qat',
            'propagate_qconfig_',
            'quantize',
            'quantize_dynamic',
            'quantize_qat',
            'register_activation_post_process_hook',
            'swap_module',
        ]
        self._test_function_import('quantize', function_list)

    def test_package_import_stubs(self):
        self._test_package_import('stubs')

    def test_function_import_stubs(self):
        function_list = [
            'QuantStub',
            'DeQuantStub',
            'QuantWrapper',
        ]
        self._test_function_import('stubs', function_list)

    def test_package_import_quantize_jit(self):
        self._test_package_import('quantize_jit')

    def test_function_import_quantize_jit(self):
        function_list = [
            '_check_is_script_module',
            '_check_forward_method',
            'script_qconfig',
            'script_qconfig_dict',
            'fuse_conv_bn_jit',
            '_prepare_jit',
            'prepare_jit',
            'prepare_dynamic_jit',
            '_convert_jit',
            'convert_jit',
            'convert_dynamic_jit',
            '_quantize_jit',
            'quantize_jit',
            'quantize_dynamic_jit',
        ]
        self._test_function_import('quantize_jit', function_list)

    def test_package_import_fake_quantize(self):
        self._test_package_import('fake_quantize')

    def test_function_import_fake_quantize(self):
        function_list = [
            '_is_per_channel',
            '_is_per_tensor',
            '_is_symmetric_quant',
            'FakeQuantizeBase',
            'FakeQuantize',
            'FixedQParamsFakeQuantize',
            'FusedMovingAvgObsFakeQuantize',
            'default_fake_quant',
            'default_weight_fake_quant',
            'default_fixed_qparams_range_neg1to1_fake_quant',
            'default_fixed_qparams_range_0to1_fake_quant',
            'default_per_channel_weight_fake_quant',
            'default_histogram_fake_quant',
            'default_fused_act_fake_quant',
            'default_fused_wt_fake_quant',
            'default_fused_per_channel_wt_fake_quant',
            '_is_fake_quant_script_module',
            'disable_fake_quant',
            'enable_fake_quant',
            'disable_observer',
            'enable_observer',
        ]
        self._test_function_import('fake_quantize', function_list)


class TestAOMigrationNNQuantized(AOMigrationTestCase):
    def test_package_import_nn_quantized_modules(self):
        r"""Tests the migration of the torch.nn.quantized.modules"""
        self._test_package_import('modules', base='nn.quantized')
        self._test_package_import('modules.activation', base='nn.quantized')
        self._test_package_import('modules.batchnorm', base='nn.quantized')
        self._test_package_import('modules.conv', base='nn.quantized')
        self._test_package_import('modules.dropout', base='nn.quantized')
        self._test_package_import('modules.embedding_ops', base='nn.quantized')
        self._test_package_import('modules.functional_modules', base='nn.quantized')
        self._test_package_import('modules.linear', base='nn.quantized')
        self._test_package_import('modules.normalization', base='nn.quantized')
        self._test_package_import('modules.utils', base='nn.quantized')

    def test_package_import_nn_quantized(self):
        skip = [
            # These are added in the `torch.nn.quantized` to allow
            # for the legacy import, s.a. `import torch.nn.quantized.conv`, etc.
            'activation',
            'batchnorm',
            'conv',
            'dropout',
            'embedding_ops',
            'functional_modules',
            'linear',
            'normalization',
            # Skip the packages that are not yet migrated, but are still
            # part of the `nn.quantized`.
            '_reference',
        ]
        self._test_package_import('quantized', base='nn', skip=skip)

    def test_functional_import(self):
        r"""Tests the migration of the torch.nn.quantized.functional"""
        function_list = [
            'avg_pool2d',
            'avg_pool3d',
            'adaptive_avg_pool2d',
            'adaptive_avg_pool3d',
            'conv1d',
            'conv2d',
            'conv3d',
            'interpolate',
            'linear',
            'max_pool1d',
            'max_pool2d',
            'celu',
            'leaky_relu',
            'hardtanh',
            'hardswish',
            'threshold',
            'elu',
            'hardsigmoid',
            'clamp',
            'upsample',
            'upsample_bilinear',
            'upsample_nearest',
        ]
        self._test_function_import('functional', function_list, base='nn.quantized')

    def test_modules_import(self):
        module_list = [
            # Modules
            'BatchNorm2d',
            'BatchNorm3d',
            'Conv1d',
            'Conv2d',
            'Conv3d',
            'ConvTranspose1d',
            'ConvTranspose2d',
            'ConvTranspose3d',
            'DeQuantize',
            'ELU',
            'Embedding',
            'EmbeddingBag',
            'GroupNorm',
            'Hardswish',
            'InstanceNorm1d',
            'InstanceNorm2d',
            'InstanceNorm3d',
            'LayerNorm',
            'LeakyReLU',
            'Linear',
            'MaxPool2d',
            'Quantize',
            'ReLU6',
            'Sigmoid',
            'Softmax',
            'Dropout',
            # Wrapper modules
            'FloatFunctional',
            'FXFloatFunctional',
            'QFunctional',
        ]
        self._test_function_import('modules', module_list, base='nn.quantized')

    def test_package_import_nn_quantized_dynamic(self):
        self._test_package_import('dynamic', base='nn.quantized')

    def test_package_import_nn_quantized_dynamic_modules(self):
        r"""Tests the migration of the torch.nn.quantized.modules"""
        self._test_package_import('modules', base='nn.quantized.dynamic')
        self._test_package_import('modules.conv', base='nn.quantized.dynamic')
        self._test_package_import('modules.linear', base='nn.quantized.dynamic')
        self._test_package_import('modules.rnn', base='nn.quantized.dynamic')
        
    def test_import_nn_quantized_dynamic_import(self):
        module_list = [
            # Modules
            'Linear',
            'LSTM',
            'GRU',
            'LSTMCell',
            'RNNCell',
            'GRUCell',
            'Conv1d',
            'Conv2d',
            'Conv3d',
            'ConvTranspose1d',
            'ConvTranspose2d',
            'ConvTranspose3d',
        ]
        self._test_function_import('dynamic', module_list, base='nn.quantized')
