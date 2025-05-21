# Ecohydrological-Portfolio-Risk-Model
a model to quantify ecohydrological risk based on portfolio of natural assets

## Model
We propose our model based on following original definition of risk:
<p align="center">$$Risk=probability ×F(hazards,exposure,vulnerability)$$</p>
with expanding the 3 risk components to the portfolio view, we have:
<p align="center">$$R_{Species} = \left( MCI_{asset1} \times \frac{\Delta M}{\Delta asset1} \times MCI_{asset2} \times \frac{\Delta M}{\Delta asset2} \right) \times H \times PE$$</p>
<p align="center">$$R_{Ecosystem} = \frac{(MCI_{a1→a2} \times \Delta M_{a1} \times H_{a1} + MCI_{a2→a1} \times \Delta M_{a2} \times H_{a2})}{PE_{Ecosystem}}$$</p>
here, the $MCI$ is the causal interaction strength between two assets, and $asset1$ as well $asset2$ indicates for the assets that interact with specific species.
