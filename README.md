# Probabilistic Solar Power Forecasting Using Multi-Objective Quantile Regression
This repository contains a description of our works submitted to the PMAPS2024 conference. We proposed three formulations of probabilistic forecast based on quantile regression providing a prediction interval. Then, we compared the result from our formulation with quantile regression (QR) and quantile regression forest (QRF).
## Abstract
This paper presents optimization formulations of quantile regression providing lower and upper bounds of pre-diction interval (PI) in probabilistic forecasting. The quality of PI is assessed in terms of reliability (PI coverage probability) and sharpness (PI average width). The formulations rely on a linear additive forecasting model and aim to minimize the pinball loss while enforcing a reduction of PI width from the original width calculated from sample quantiles. The width constraint functions are expressed in three forms: the sum of all widths, the sum of K-largest widths, and the maximum width, where the latter was shown to outperform the other two formulations, the quantile regression (QR) and the quantile regression forest (QRF) in the case of data corrupted by heteroskedastic noise. A renewable energy application of the proposed framework was illustrated by intra-hour solar irradiance probabilistic forecasting at a solar plant in Thailand, in comparison with QR and QRF. Overall, QRF had the lowest average PI width among other methods, while the proposed formulation can bring down the largest PI width at a significant level while losing merely a slight coverage probability. Reducing the largest width decreases uncertainty in renewable energy forecasts, thereby lowering operational costs for reserve preparation in the power system.
## Formulation description
The proposed formulation can be described as
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
## Repository
This repository consists of the following folders.
- **codes** consist of an experiment for the simulated and solar datasets. 
  - **Formulation** consists of .py file for P1 and P3 formulation which reformulated as linear programming.
  are utilized for downloading data, cleaning it, and generating datasets.
- **data** contains solar and simulated data used in the experiment training and testing process.
- **figures** contains all figures and a Python notebook file for visualization.ipynb generates all figures in the conference paper.
- **results** store all the CSV, pkl, npy files used in this project

## Citation
```
@INPROCEEDINGS{10667174,
  author={Amnuaypongsa, Worachit and Wangdee, Wijarn and Songsiri, Jitkomut},
  booktitle={2024 18th International Conference on Probabilistic Methods Applied to Power Systems (PMAPS)}, 
  title={Probabilistic Solar Power Forecasting Using Multi-Objective Quantile Regression}, 
  year={2024},
  volume={},
  number={},
  pages={1-6},
  keywords={Solar irradiance;Renewable energy sources;Uncertainty;Costs;Upper bound;Predictive models;Probabilistic logic;probabilistic forecasting;solar irradiance;quantile regression;prediction interval},
  doi={10.1109/PMAPS61648.2024.10667174}}
```
