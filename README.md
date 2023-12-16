# Chroma Pipeline
Protein design pipeline for using Chroma, a protein structure generation model, for various tasks



## Installation

### General case

Folder tree should like:

```
.
└── chroma_pipeline
    ├── chroma
    │       include chroma package here
    ├── chroma_weights
    │       chroma weights here, it should be downloaded from GenerateBio
    └── README.md
```

Install chroma with conda: (this might be incorrect for now)

```bash
git clone https://github.com/Zuricho/chroma_pipeline.git
cd chroma_pipeline
conda create -n chroma python=3.9
pip install -r requirements.txt
```


### (Brainstorming) Install in MacOS (M2 chip)

The installed packages are:
- nglview=3.0.8
- numpy=1.26.2
- pandas=2.1.3
- Pillow=10.1.0
- pytest=7.4.3
- Requests=2.31.0
- scikit-learn==1.1.2
- scipy=1.11.4 
- torch=2.1.1
- tqdm=4.66.1
- transformers==4.24.0

```bash
conda create -n chroma python=3.9
conda install numpy pandas matplotlib scikit-learn nglview pillow pytest requests tqdm transformers pytorch -c pytorch -c conda-forge 
# conda install pytorch::pytorch -c pytorch
```



## Usage

[WIP]
