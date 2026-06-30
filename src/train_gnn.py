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
import torch

from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):

    def __init__(self):

        super().__init__()

        self.conv1 = GCNConv(
            data.num_features,
            16
        )

        self.conv2 = GCNConv(
            16,
            1
        )

    def forward(
        self,
        x,
        edge_index
    ):

        x = self.conv1(
            x,
            edge_index
        )

        x = torch.relu(x)

        x = self.conv2(
            x,
            edge_index
        )

        return x

model = GCN()

print(model)
