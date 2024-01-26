import torch


def torch_wasserstein_loss(tensor_a,tensor_b):
    #Compute the first Wasserstein distance between two 1D distributions.
    return(torch_cdf_loss(tensor_a,tensor_b,p=1))


def torch_energy_loss(tensor_a,tensor_b):
    # Compute the energy distance between two 1D distributions.
    return((2**0.5)*torch_cdf_loss(tensor_a,tensor_b,p=2))


def torch_cdf_loss(tensor_a,tensor_b,p=1):
    tensor_a = tensor_a / (torch.sum(tensor_a, dim=-1, keepdim=True) + 1e-14)
    tensor_b = tensor_b / (torch.sum(tensor_b, dim=-1, keepdim=True) + 1e-14)
    cdf_tensor_a = torch.cumsum(tensor_a,dim=-1)
    cdf_tensor_b = torch.cumsum(tensor_b,dim=-1)

    # choose different formulas for different norm situations
    if p == 1:
        cdf_distance = torch.sum(torch.abs((cdf_tensor_a-cdf_tensor_b)),dim=-1)
    elif p == 2:
        cdf_distance = torch.sqrt(torch.sum(torch.pow((cdf_tensor_a-cdf_tensor_b),2),dim=-1))
    else:
        cdf_distance = torch.pow(torch.sum(torch.pow(torch.abs(cdf_tensor_a-cdf_tensor_b),p),dim=-1),1/p)

    cdf_loss = cdf_distance.mean()
    return cdf_loss


def torch_validate_distibution(tensor_a,tensor_b):
    if tensor_a.size() != tensor_b.size():
        raise ValueError("Input weight tensors must be of the same size")


def any_image_to_tensor(image, device):
    if type(image) == list or type(image) == tuple:
        image = [[x.to(device) for x in y] for y in image]
    elif type(image) == dict:
        image = {k: [x.to(device) for x in v] for k, v in image.items()}
    else:
        image = image.to(device)
    return image


def get_torch_device():
    return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def save_model(model, path, save_object=False):
    # Check if model is wrapped with DataParallel

    if isinstance(model, torch.nn.DataParallel):
        # Save the original model parameters
        to_save = model.module
    else:
        to_save = model

    if save_object:
        torch.save(to_save, path)
    else:
        torch.save(to_save.state_dict(), path)
