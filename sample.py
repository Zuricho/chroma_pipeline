from chroma import Protein, Chroma, conditioners
from chroma.models import graph_classifier, procap
from chroma.utility.chroma import letter_to_point_cloud, plane_split_protein
import os

device = "cpu"

# initialize Chroma
chroma = Chroma(
                weights_backbone="chroma_weights/chroma_backbone_v1.0.pt",
                weights_design="chroma_weights/chroma_design_v1.0.pt",
                device=device,
                )

# Unconditional sampling
protein = chroma.sample(chain_lengths=[64])
protein.to("result/unc_sample.pdb")

