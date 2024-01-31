import torch
import matplotlib.pyplot as plt

def topk_accuracy(output, target, k=1):
    """Computes the precision for the specified values of k"""
    with torch.no_grad():
        batch_size = target.size(0)
        _, pred = output.topk(k, 1)
        correct = pred.eq(target.unsqueeze(1).expand_as(pred)).sum(dim=0)
        accuracy = correct * (100 / batch_size)
        return accuracy

def track_vfe(model, x=None, y=None, steps=100, plot_Es=False, plot_Xs=False, flatten=True):
    # assert len(x.shape) == 2, f"Invalid shape {x.shape}, input and targets must be pre-processed."
    state = model.init_state(x, y)
    vfes = []
    E = [[] for _ in range(len(model.layers))]
    X = [[] for _ in range(len(model.layers))]
    for step_i in range(steps):
        temp = model.calc_temp(step_i, steps)
        model.step(state, x, y, temp)
        vfes.append(model.vfe(state).item())
        for i in range(len(model.layers)):
            E[i].append(state[i]['e'].square().sum(dim=1).mean().item())
            X[i].append(state[i]['x'].square().sum(dim=1).mean().item())
        
    plt.plot(vfes, label='VFE')

    if plot_Es:
        for i in range(len(model.layers)):
            plt.plot(E[i], label=f'layer {i} E')
    plt.legend()
    plt.show()

    if plot_Xs:
        for i in range(len(model.layers)):
            plt.plot(X[i], label=f'layer {i} X')
    plt.legend()
    plt.show()

    return vfes, E, X
        
def accuracy(model, dataset, batch_size=1024, steps=100, flatten=True):
    with torch.set_grad_enabled(not flatten):
        dataloader = torch.utils.data.DataLoader(dataset, batch_size, shuffle=False)
        correct = 0
        for x, y in dataloader:
            if flatten:
                x = x.flatten(start_dim=1)
            pred = model.classify(x, steps)
            correct += (pred == y).sum().item()
        acc = correct/len(dataset)
    return acc