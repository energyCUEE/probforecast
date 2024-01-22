# Probabilistic Solar Power Forecasting Using Multi-Objective Quantile Regression
# Formulation P1 (control average width)

'''math
\begin{array}{ll}
\underset{\underline{\beta},\overline{\beta}}{ \mbox{minimize} }
		& \sum_{i \in \mathcal{I}} [ \rho_{\underline{\alpha}}(y_{i}-\hat{l}_{i}(\underline{\beta}))+\rho_{\overline{\alpha}}(y_{i}-\hat{u}_{i}(\overline{\beta})) ] \\
		\text{subject to} & 0 \leq \hat{l}_{i}(\underline{\beta}) \leq \hat{u}_{i}(\overline{\beta}), \forall i \in \mathcal{I},\\
      &  \frac{1}{N}\sum_{i \in \mathcal{I}} [ \hat{u}_{i}(\overline{\beta})-\hat{l}_{i}(\underline{\beta}) ]  \leq \gamma \cdot \text{sample width},
\end{array}
'''





This repository consists of the following folders.
- **codes** consists of codes of an experiment for the simulated dataset and solar dataset. 
  - **Formulation** consists of .py file for P1 and P3 formulation which reformulated as linear programming.
  are utilized for downloading data, cleaning it, and generating datasets.
- **data** contains solar data and simulated data, which are used in the experiment training and testing process.
- **figures** contains all figures and a python notebook file, visualization.ipynb, used to generate all figures in the conference paper.
- **results** store all the CSV, pkl, npy files using in this project
