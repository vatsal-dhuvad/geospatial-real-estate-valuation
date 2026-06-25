# Graph Neural Network training
import torch

from torch_geometric.data import Data

edge_index = torch.tensor(
    edges,
    dtype=torch.long
).t().contiguous()

x = torch.tensor(
    df.select_dtypes(
        include=["number"]
    ).values,
    dtype=torch.float
)

data = Data(
    x=x,
    edge_index=edge_index
)

print(data)
