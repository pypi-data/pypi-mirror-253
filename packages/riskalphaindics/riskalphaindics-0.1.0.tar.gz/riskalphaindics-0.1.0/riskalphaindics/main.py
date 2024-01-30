import pandas as pd
import numpy as np

def moving_average(data, window):
    """
    Calculate the moving average of the 'close' prices over a specified window.

    Parameters:
    data (pd.DataFrame): DataFrame containing the 'close' price column.
    window (int): The number of periods over which to calculate the moving average.

    Returns:
    pd.Series: A series containing the moving average of the 'close' prices.
    """
    return data['close'].rolling(window=window).mean()

def exponential_moving_average(data, window):
    """
    Calculate the exponential moving average (EMA) of the 'close' prices.

    Parameters:
    data (pd.DataFrame): DataFrame containing the 'close' price column.
    window (int): The number of periods over which to calculate the EMA.

    Returns:
    pd.Series: A series containing the EMA of the 'close' prices.
    """
    return data['close'].ewm(span=window, adjust=False).mean()

def relative_strength_index(data, periods):
    """
    Calculate the Relative Strength Index (RSI).

    Parameters:
    data (pd.DataFrame): DataFrame containing the 'close' price column.
    periods (int): The number of periods to use for calculating RSI.

    Returns:
    pd.Series: A series containing the RSI values.
    """
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=periods).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=periods).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def average_true_range(data, window):
    """
    Calculate the Average True Range (ATR).

    Parameters:
    data (pd.DataFrame): DataFrame with 'high', 'low', and 'close' price columns.
    window (int): The number of periods over which to calculate the ATR.

    Returns:
    pd.Series: A series containing the ATR values.
    """
    high_low = data['high'] - data['low']
    high_close = np.abs(data['high'] - data['close'].shift())
    low_close = np.abs(data['low'] - data['close'].shift())
    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)
    return true_range.rolling(window=window).mean()

def moving_average_convergence_divergence(data, window_slow, window_fast, signal):
    """
    Calculate the Moving Average Convergence Divergence (MACD) and its signal line.

    Parameters:
    data (pd.DataFrame): DataFrame containing the 'close' price column.
    window_slow (int): The number of periods for the slow EMA.
    window_fast (int): The number of periods for the fast EMA.
    signal (int): The number of periods for the signal line.

    Returns:
    tuple: A tuple containing two pd.Series, the MACD values and the signal line values.
    """
    ema_fast = data['close'].ewm(span=window_fast, adjust=False).mean()
    ema_slow = data['close'].ewm(span=window_slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    return macd, signal_line
