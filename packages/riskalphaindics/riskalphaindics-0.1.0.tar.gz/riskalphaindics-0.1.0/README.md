# Riskalphaindics
## Description

This Python package provides functionality to calculate various financial indicators such as Moving Average, Exponential Moving Average (EMA), Relative Strength Index (RSI), Average True Range (ATR), and Moving Average Convergence Divergence (MACD). It's designed for financial market analysis and algorithmic trading strategies.

## Installation

To install this package, ensure you have Poetry installed on your system. If you don't have Poetry, you can install it using pip:

```{bash}
pip install poetry
```

Then, you can install this package using Poetry:


```{bash}
poetry add riskalphaindics
```
## Usage

Below are some examples of how to use the indicators in this package.

### Moving Average

```{python}
from riskalphaindics import moving_average

# Assuming 'data' is a pandas DataFrame with a 'close' column
ma = moving_average(data, window=20)
```

### Exponential Moving Average

```{python}
from riskalphaindics import exponential_moving_average

# Assuming 'data' is a pandas DataFrame with a 'close' column
ema = exponential_moving_average(data, window=20)
```

### Relative Strength Index

```{python}
from riskalphaindics import relative_strength_index

# Assuming 'data' is a pandas DataFrame with a 'close' column
rsi = relative_strength_index(data, periods=14)
```

### Average True Range


```{python}
from riskalphaindics import average_true_range

# Assuming 'data' is a pandas DataFrame with 'high', 'low', and 'close' columns
atr = average_true_range(data, window=14)
```

### Moving Average Convergence Divergence

```{python}
from riskalphaindics import moving_average_convergence_divergence

# Assuming 'data' is a pandas DataFrame with a 'close' column
macd, signal_line = moving_average_convergence_divergence(data, window_slow=26, window_fast=12, signal=9)
```

## Contributing

Contributions to this package are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

MIT.
