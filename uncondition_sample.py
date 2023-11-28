from chroma import Chroma

chroma = Chroma(
				weights_backbone="chroma_weights/chroma_backbone_v1.0.pt",
				weights_design="chroma_weights/chroma_design_v1.0.pt"
				)
				
protein = chroma.sample(chain_lengths=[200])

protein.to("result/sample.pdb")

