import talib

# Check the version of TA-Lib
print("TA-Lib version:", talib.__version__)

# Check if TA-Lib functions can be imported
try:
        # Example: Print the moving average of a sample data
            close_data = [1.2, 2.3, 3.4, 4.5, 5.6]
            output = talib.SMA(close_data)
            print("Moving Average:", output)

            print("TA-Lib is installed successfully.")
except Exception as e:
        print("Error:", e)
        print("TA-Lib installation may not be successful.")

