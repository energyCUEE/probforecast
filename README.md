# Probabilistic Solar Power Forecasting Using Multi-Objective Quantile Regression

This repository contains a description of our works submitted to the PMAPS2024 conference. We proposed three formulations of probabilistic forecast based on quantile regression providing a prediction interval. Then, we compared the result from our formulation with quantile regression (QR) and quantile regression forest (QRF). The proposed formulation can be described as

**Formulation P1 (control average width)**
```math
\begin{array}{ll}
\underset{\underline{\beta},\overline{\beta}}{ \mbox{minimize} }
		& \sum_{i \in \mathcal{I}} [ \rho_{\underline{\alpha}}(y_{i}-\hat{l}_{i}(\underline{\beta}))+\rho_{\overline{\alpha}}(y_{i}-\hat{u}_{i}(\overline{\beta})) ] \\
		\text{subject to} & 0 \leq \hat{l}_{i}(\underline{\beta}) \leq \hat{u}_{i}(\overline{\beta}), \forall i \in \mathcal{I},\\
      &  \frac{1}{N}\sum_{i \in \mathcal{I}} [ \hat{u}_{i}(\overline{\beta})-\hat{l}_{i}(\underline{\beta}) ]  \leq \gamma \cdot \text{sample width},
\end{array}
```
**Formulation P2 (control large widths)**
```math
\begin{array}{ll}
\underset{\underline{\beta},\overline{\beta}}{ \mbox{minimize} }
		& \sum_{i \in \mathcal{I}} [ \rho_{\underline{\alpha}}(y_{i}-\hat{l}_{i}(\underline{\beta}))+\rho_{\overline{\alpha}}(y_{i}-\hat{u}_{i}(\overline{\beta})) ] \\
		\text{subject to} & 0 \leq \hat{l}_{i}(\underline{\beta}) \leq \hat{u}_{i}(\overline{\beta}), \forall i \in \mathcal{I},\\
      & \frac{1}{K}\sum_{i=1}^K w_{[i]}  \leq \gamma \cdot \text{sample width},
\end{array}
```
**Formulation P3 (control maximum width)**
```math
\begin{array}{ll}
\underset{\underline{\beta},\overline{\beta}}{ \mbox{minimize} }
		& \sum_{i \in \mathcal{I}} [ \rho_{\underline{\alpha}}(y_{i}-\hat{l}_{i}(\underline{\beta}))+\rho_{\overline{\alpha}}(y_{i}-\hat{u}_{i}(\overline{\beta})) ] \\
		\text{subject to} & 0 \leq \hat{l}_{i}(\underline{\beta}) \leq \hat{u}_{i}(\overline{\beta}), \forall i \in \mathcal{I},\\
      &  \underset{i \in \mathcal{I} }{ \max } [ \hat{u}_{i}(\overline{\beta})-\hat{l}_{i}(\underline{\beta}) ] \leq \gamma \cdot \text{sample width},
\end{array}
```

This repository consists of the following folders.
- **codes** consist of an experiment for the simulated and solar datasets. 
  - **Formulation** consists of .py file for P1 and P3 formulation which reformulated as linear programming.
  are utilized for downloading data, cleaning it, and generating datasets.
- **data** contains solar and simulated data used in the experiment training and testing process.
- **figures** contains all figures and a Python notebook file for visualization.ipynb generates all figures in the conference paper.
- **results** store all the CSV, pkl, npy files used in this project
