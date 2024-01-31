from pclib.nn.layers import Conv2d, FC
from pclib.utils.functional import format_y
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.grad import conv2d_input, conv2d_weight

# Based on Whittington and Bogacz 2017
class ConvClassifier(nn.Module):
    """
    | Similar to the FCClassifier, except uses convolutions instead of fully connected layers.
    | This network is not currently customisable, but requires altering the init_layers() code to change the architecture.

    Args:
        | steps (int): Number of steps to run the network for.
        | bias (bool): Whether to include bias terms in the network.
        | symmetric (bool): Whether to use symmetric weights. 
        | actv_fn (function): Activation function to use in the network.
        | d_actv_fn (function): Derivative of the activation function to use in the network.
        | gamma (float): step size for x updates
        | device (torch.device): Device to run the network on.
        | dtype (torch.dtype): Data type to use for network parameters.
    
    Attributes:
        | num_classes (int): Number of classes in the dataset.
        | steps (int): Number of steps to run the network for.
        | device (torch.device): Device to run the network on.
        | factory_kwargs (dict): Keyword arguments for the layers.
        | layers (torch.nn.ModuleList): List of layers in the network.

    """
    __constants__ = ['in_features', 'out_features']
    in_features: int
    num_classes: int

    def __init__(self, steps=20, bias=True, symmetric=True, actv_fn=F.relu, d_actv_fn=None, gamma=0.1, device=torch.device('cpu'), dtype=None):
        self.factory_kwargs = {'actv_fn': actv_fn, 'd_actv_fn': d_actv_fn, 'gamma': gamma, 'has_bias': bias, 'symmetric': symmetric, 'dtype': dtype}
        super().__init__()

        self.num_classes = 10
        self.steps = steps
        self.device = device

        self.init_layers()
        self.register_buffer('epochs_trained', torch.tensor(0, dtype=torch.long))
        self.register_buffer('min_vfe', torch.tensor(float('inf'), dtype=torch.float32))

    def __str__(self):
        base_str = super().__str__()

        custom_info = "\n  (params): \n" + \
            f"    in_shape: (-1, 1, 32, 32)" + \
            f"    out_shape: (-1, 10)" + \
            f"    steps: {self.steps}" + \
            f"    bias: {self.factory_kwargs['has_bias']}" + \
            f"    symmetric: {self.factory_kwargs['symmetric']}" + \
            f"    actv_fn: {self.factory_kwargs['actv_fn'].__name__}" + \
            f"    gamma: {self.factory_kwargs['gamma']}" + \
            f"    device: {self.device}" + \
            f"    dtype: {self.factory_kwargs['dtype']}" + \
            f"    epochs_trained: {self.epochs_trained}" + \
            f"    min_vfe: {self.min_vfe}\n"
        
        string = base_str[:base_str.find('\n')] + custom_info + base_str[base_str.find('\n'):]
        
        return string


    def init_layers(self):
        """
        | Initialises the layers of the network.
        | Not currently customisable, but can be changed by altering this code.
        """
        layers = []
        layers.append(Conv2d(None, (1, 32, 32),         maxpool=2, **self.factory_kwargs))
        layers.append(Conv2d((1, 32, 32), (32, 16, 16), maxpool=2, **self.factory_kwargs))
        layers.append(Conv2d((32, 16, 16), (64, 8, 8),  maxpool=2, **self.factory_kwargs))
        layers.append(Conv2d((64, 8, 8), (64, 4, 4),    maxpool=2, **self.factory_kwargs))
        layers.append(Conv2d((64, 4, 4), (64, 2, 2),    maxpool=2, **self.factory_kwargs))
        layers.append(Conv2d((64, 2, 2), (64, 1, 1),    maxpool=2, **self.factory_kwargs))
        layers.append(FC(64, 128, **self.factory_kwargs))
        layers.append(FC(128, 10, **self.factory_kwargs))
        self.layers = nn.ModuleList(layers)

    def inc_epochs(self, n=1):
        """
        | Increments the number of epochs trained by n.

        Args:
            | n (int): Number of epochs to increment by
        """
        self.epochs_trained += n


    def vfe(self, state, batch_reduction='mean', unit_reduction='sum'):
        """
        | Calculates the Variational Free Energy (VFE) of the model.
        | This is the sum of the squared prediction errors of each layer.
        | how batches and units are reduced is controlled by batch_reduction and unit_reduction.

        Args:
            | state (list): List of layer state dicts, each containing 'x' and 'e'
            | batch_reduction (str): How to reduce over batches ['sum', 'mean', None]
            | unit_reduction (str): How to reduce over units ['sum', 'mean']

        Returns:
            | vfe (torch.Tensor): VFE of the model (scalar)
        """
        # Reduce units for each layer
        if unit_reduction == 'sum':
            vfe = [state_i['e'].square().sum(dim=[i for i in range(1, state_i['e'].dim())]) for state_i in state]
        elif unit_reduction =='mean':
            vfe = [state_i['e'].square().mean(dim=[i for i in range(1, state_i['e'].dim())]) for state_i in state]
        # Reduce layers
        vfe = sum(vfe)
        # Reduce batches
        if batch_reduction == 'sum':
            vfe = vfe.sum()
        elif batch_reduction == 'mean':
            vfe = vfe.mean()

        return vfe

    def step(self, state, obs=None, y=None, temp=None):
        """
        | Performs one step of inference, updating all Xs first, then calculates Errors.

        Args:
            | state (list): List of layer state dicts, each containing 'x' and 'e'
            | obs (Optional[torch.Tensor]): Input data
            | y (Optional[torch.Tensor]): Target data
            | temp (Optional[float]): Temperature for simulated annealing

        """
        for i, layer in enumerate(self.layers):
            if i > 0 or obs is None:
                if i < len(self.layers) - 1 or y is None:
                    e_below = state[i-1]['e'] if i > 0 else None
                    layer.update_x(state[i], e_below, temp=temp)
        for i, layer in enumerate(self.layers):
            if i < len(self.layers) - 1:
                pred = self.layers[i+1].predict(state[i+1])
                layer.update_e(state[i], pred, temp=temp)


    def _init_xs(self, state, obs=None, y=None):
        """
        | Initialises Xs.
        | If y is provided, xs are initialised top-down using predictions.
        | Else if obs is provided, xs are initialised bottom-up using propagations.
        
        Args:
            | state (list): List of layer state dicts, each containing 'x' and 'e' (and 'eps' for FCPW)
            | obs (Optional[torch.Tensor]): Input data
            | y (Optional[torch.Tensor]): Target data
        """
        with torch.no_grad():
            if y is not None:
                for i, layer in reversed(list(enumerate(self.layers))):
                    if i == len(self.layers) - 1: # last layer
                        state[i]['x'] = y.detach()
                    if i > 0:
                        pred = layer.predict(state[i])
                        if isinstance(layer, FC) and isinstance(self.layers[i-1], Conv2d):
                            shape = self.layers[i-1].shape
                            pred = pred.view(pred.shape[0], shape[0], shape[1], shape[2])
                        state[i-1]['x'] = pred.detach()
                if obs is not None:
                    state[0]['x'] = obs.detach()

            elif obs is not None:
                for i, layer in enumerate(self.layers):
                    if i == 0:
                        state[0]['x'] = obs.detach()
                    else:
                        x_below = state[i-1]['x'].detach()
                        state[i]['x'] = layer.propagate(x_below)

    def init_state(self, obs=None, y=None):
        """
        | Initialises the state of the network.

        Args:
            | obs (Optional[torch.Tensor]): Input data
            | y (Optional[torch.Tensor]): Target data

        Returns:
            | state (list): List of layer state dicts, each containing 'x' and 'e'
        """
        if obs is not None:
            b_size = obs.shape[0]
        elif y is not None:
            b_size = y.shape[0]
        else:
            raise ValueError('Either obs or y must be provided to init_state.')
        state = []
        for layer in self.layers:
            state.append(layer.init_state(b_size))
        
        self._init_xs(state, obs, y)
        
        return state

    def to(self, device):
        self.device = device
        for layer in self.layers:
            layer.to(device)
        return self

    def get_output(self, state):
        """
        | Returns the output of the network.

        Args:
            | state (list): List of layer state dicts, each containing 'x' and 'e'

        Returns:
            | out (torch.Tensor): Output of the network
        """
        return state[-1]['x']

    def calc_temp(self, step_i, steps):
        """
        | Calculates the temperature for the current step.

        Args:
            | step_i (int): Current step
            | steps (int): Total number of steps
        
        Returns:
            | temp (float): Temperature for the current step = 1 - (step_i / steps)
        """
        return 1 - (step_i / steps)

    def forward(self, obs=None, y=None, steps=None, back_on_step=False):
        """
        | Performs inference phase of the network.

        Args:
            | obs (Optional[torch.Tensor]): Input data
            | y (Optional[torch.Tensor]): Target data
            | steps (Optional[int]): Number of steps to run inference for
            | back_on_step (bool): Whether to backpropagate on each step. Default False.
        
        Returns:
            | out (torch.Tensor): Output of the network
            | state (list): List of layer state dicts, each containing 'x' and 'e'
        """
        if steps is None:
            steps = self.steps

        state = self.init_state(obs, y)

        for i in range(steps):
            temp = self.calc_temp(i, steps)
            self.step(state, obs, y, temp)
            if back_on_step:
                self.vfe(state).backward()
            
        out = self.get_output(state)
            
        return out, state

    def generate(self, y, steps=None):
        """
        | Generates an image from the target y.

        Args:
            | y (torch.Tensor): Target data
            | steps (Optional[int]): Number of steps to run inference for

        Returns:
            | out (torch.Tensor): Generated image
        """
        y = format_y(y, self.num_classes)
        _, state = self.forward(y=y, steps=steps)
        return state[0]['x']
    
    def classify(self, obs, state=None, steps=None):
        """
        | Classifies the input obs.

        Args:
            | obs (torch.Tensor): Input data
            | state (Optional[list]): List of layer state dicts, each containing 'x' and 'e'
            | steps (Optional[int]): Number of steps to run inference for
        
        Returns:
            | out (torch.Tensor): Predicted class
        """
        if steps is None:
            steps = self.steps

        vfes = torch.zeros(obs.shape[0], self.num_classes, device=self.device)
        for target in range(self.num_classes):
            targets = torch.full((obs.shape[0],), target, device=self.device, dtype=torch.long)
            y = format_y(targets, self.num_classes)
            _, state = self.forward(obs, y, steps)
            vfes[:, target] = self.vfe(state, batch_reduction=None)
        
        return vfes.argmin(dim=1)