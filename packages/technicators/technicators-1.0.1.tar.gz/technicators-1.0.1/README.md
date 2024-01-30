# Technicators
[![PyPI - Version](https://img.shields.io/pypi/v/technicators?color=blue)](https://github.com/Tejaromalius/Technicators/blob/main/pyproject.toml)
[![PyPI - License](https://img.shields.io/pypi/l/technicators?color=red)](https://github.com/Tejaromalius/Technicators/blob/main/LICENSE)
[![PyPI - Status](https://img.shields.io/pypi/status/technicators?color=%20%23239b56%20)](https://pypi.org/project/technicators/)

**Technicators** provides a collection of methods for calculating various technical indicators commonly used in financial analysis.

## Installation

```bash
pip install technicators
```

## Usage
```
import pandas as pd
from technicators import Technicators

# Sample time series data
data = pd.Series([...])

# Calculate ALMA
alma_values = Technicators.ALMA(data, period=14)

# Calculate EMA
ema_values = Technicators.EMA(data, period=14)

# Calculate HMA
hma_values = Technicators.HMA(data, period=14)

# Calculate SMMA
smma_values = Technicators.SMMA(data, period=14)

# Calculate TEMA
tema_values = Technicators.TEMA(data, period=14)

# Calculate WMA
wma_values = Technicators.WMA(data, period=14)
```

## Method Details

### ALMA

- Calculates the Arnaud Legoux Moving Average (ALMA) using a variable window.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the ALMA.
  - `offset` (float): Offset multiplier for ALMA calculation. Default is 0.85.
  - `sigma` (float): Standard deviation factor for ALMA calculation. Default is 6.
- **Returns:**
  - `pd.Series`: A time series representing the ALMA values.

### EMA

- Calculates the Exponential Moving Average (EMA) of a given time series.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the EMA.
  - `adjust` (bool): Whether to adjust the EMA calculation. Default is True.
- **Returns:**
  - `pd.Series`: A time series representing the EMA values.

### HMA

- Calculates the Hull Moving Average (HMA) using weighted moving averages.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the HMA.
- **Returns:**
  - `pd.Series`: A time series representing the HMA values.

### SMMA

- Calculates the Smoothed Moving Average (SMMA) using exponential smoothing.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the SMMA.
  - `adjust` (bool): Whether to adjust the SMMA calculation. Default is True.
- **Returns:**
  - `pd.Series`: A time series representing the SMMA values.

### TEMA

- Calculates the Triple Exponential Moving Average (TEMA) using triple exponential smoothing.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the TEMA.
  - `adjust` (bool): Whether to adjust the TEMA calculation. Default is True.
- **Returns:**
  - `pd.Series`: A time series representing the TEMA values.

### WMA

- Calculates the Weighted Moving Average (WMA) using weighted averages.
- **Parameters:**
  - `dataset` (pd.Series): The input time series data.
  - `period` (int): The period over which to calculate the WMA.
- **Returns:**
  - `pd.Series`: A time series representing the WMA values.
