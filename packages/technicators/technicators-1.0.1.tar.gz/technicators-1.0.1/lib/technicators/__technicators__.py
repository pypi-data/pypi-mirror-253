import math
import numpy as np
import pandas as pd


class Technicators:
  @classmethod
  def ALMA(cls, dataset: pd.Series, period: int, offset: float = 0.85, sigma: float = 6) -> pd.Series:
    """
      Calculates the Arnaud Legoux Moving Average (ALMA) using a variable window.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the ALMA.
      - offset (float): Offset multiplier for ALMA calculation. Default is 0.85.
      - sigma (float): Standard deviation factor for ALMA calculation. Default is 6.

      Returns:
      - pd.Series: A time series representing the ALMA values.
    """
    offset_multiplier = offset * (period - 1)
    standard_deviation = period / sigma
    indices = np.arange(period)

    weights = np.exp(-1 * np.square(indices - offset_multiplier) / (2 * np.square(standard_deviation)))
    norm_weights = weights / np.sum(weights)
    padded_prices = np.pad(dataset, (period - 1, 0), mode="edge")

    alma_values = np.convolve(padded_prices, norm_weights[::-1], mode="valid")
    return pd.Series(alma_values, name="ALMA")

  @classmethod
  def EMA(cls, dataset: pd.Series, period: int, adjust: bool = True) -> pd.Series:
    """
      Calculates the Exponential Moving Average (EMA) of a given time series.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the EMA.
      - adjust (bool): Whether to adjust the EMA calculation. Default is True.

      Returns:
      - pd.Series: A time series representing the EMA values.
    """
    return pd.Series(
      dataset.ewm(span=period, adjust=adjust).mean(),
      name="EMA",
    )

  @classmethod
  def HMA(cls, dataset: pd.Series, period: int) -> pd.Series:
    """
      Calculates the Hull Moving Average (HMA) using weighted moving averages.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the HMA.

      Returns:
      - pd.Series: A time series representing the HMA values.
    """
    half_length = int(period / 2)
    sqrt_length = int(math.sqrt(period))

    wmaf = cls.WMA(dataset, period=half_length)
    wmas = cls.WMA(dataset, period=period)
    deltawma = pd.Series(2 * wmaf - wmas)

    hma = cls.WMA(deltawma, period=sqrt_length)
    return pd.Series(hma, name="HMA")

  @classmethod
  def SMMA(cls, dataset: pd.Series, period: int, adjust: bool = True) -> pd.Series:
    """
      Calculates the Smoothed Moving Average (SMMA) using exponential smoothing.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the SMMA.
      - adjust (bool): Whether to adjust the SMMA calculation. Default is True.

      Returns:
      - pd.Series: A time series representing the SMMA values.
    """
    return pd.Series(
      dataset.ewm(alpha=1 / period, adjust=adjust).mean(),
      name="SMMA"
    )

  @classmethod
  def TEMA(cls, dataset: pd.Series, period: int, adjust: bool = True) -> pd.Series:
    """
      Calculates the Triple Exponential Moving Average (TEMA) using triple exponential smoothing.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the TEMA.
      - adjust (bool): Whether to adjust the TEMA calculation. Default is True.

      Returns:
      - pd.Series: A time series representing the TEMA values.
    """
    triple_ema = 3 * cls.EMA(dataset, period)

    ema_power_three = (
      cls.EMA(dataset, period)
      .ewm(ignore_na=False, span=period, adjust=adjust)
      .mean()
      .ewm(ignore_na=False, span=period, adjust=adjust)
      .mean()
    )


    return pd.Series(
      (triple_ema - 3 * cls.EMA(dataset, period).ewm(span=period, adjust=adjust).mean() + ema_power_three),
      name="TEMA"
    )

  @classmethod
  def WMA(cls, dataset: pd.Series, period: int) -> pd.Series:
    """
      Calculates the Weighted Moving Average (WMA) using weighted averages.

      Parameters:
      - dataset (pd.Series): The input time series data.
      - period (int): The period over which to calculate the WMA.

      Returns:
      - pd.Series: A time series representing the WMA values.
    """
    denominator = (period * (period + 1)) / 2
    weights = np.arange(1, period + 1)

    def linear(w):
      def _compute(x):
        return (w * x).sum() / denominator

      return _compute

    _close = dataset.rolling(period, min_periods=period)

    return pd.Series(
      _close.apply(linear(weights), raw=True),
      name="WMA"
    )
