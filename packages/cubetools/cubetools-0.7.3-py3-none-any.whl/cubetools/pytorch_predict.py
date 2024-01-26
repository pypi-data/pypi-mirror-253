# -*- coding:utf-8 -*-
import gc
import torch
from copy import deepcopy


# 通用PyTorch推理框架
class Model(object):
    def __init__(self, net, model_path, param_key=None, extra_key_prefix=None, strict=True, cudnn_benchmark=True):
        if cudnn_benchmark:
            import torch.backends.cudnn as cudnn
            cudnn.benchmark = True
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.cpu_device = torch.device('cpu')

        if net is not None:
            net_params = torch.load(model_path, map_location=self.cpu_device)
            if param_key is not None and param_key in net_params:
                    net_params = net_params[param_key]

            # remove unnecessary 'module.' or 'model.'
            for k, v in deepcopy(net_params).items():
                if k.startswith('module.model.'):
                    net_params[k[13:]] = v
                    net_params.pop(k)
                elif k.startswith('module.'):
                    net_params[k[7:]] = v
                    net_params.pop(k)
                elif k.startswith('model.'):
                    net_params[k[6:]] = v
                    net_params.pop(k)
                elif extra_key_prefix and k.startswith(extra_key_prefix):
                    # extra_key_prefix 应为以“.”结尾的字符串，例如： 'module.', 'model.'
                    net_params[k[len(extra_key_prefix):]] = v
                    net_params.pop(k)

            net.load_state_dict(net_params, strict=strict)
            self.model = net
        else:
            self.model = torch.jit.load(model_path, map_location=self.cpu_device)

        self.model.eval()
        self.model = self.model.to(self.device)

    def predict(self, inputs):
        inputs = to_device(inputs, self.device)

        with torch.no_grad():
            if isinstance(inputs, dict):
                results = self.model(**inputs)
            elif isinstance(inputs, list):
                results = self.model(*inputs)
            else:
                results = self.model(inputs)

        results = to_device(results, self.cpu_device)
        gc.collect()
        torch.cuda.empty_cache()
        return results


def to_device(data, device):
    if isinstance(data, tuple):
        data = list(data)

    if isinstance(data, torch.Tensor):
        data = data.to(device)
    elif isinstance(data, dict):
        for k, v in data.items():
            data[k] = to_device(v, device)
    elif isinstance(data, list):
        for i in range(len(data)):
            data[i] = to_device(data[i], device)

    return data
