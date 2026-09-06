import os ,sys 
from dotenv import load_dotenv

from langchain.tools import tool 
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper



@tool 
def multiply(a :float ,b :float):
    """Multiply these two given numbers a and b
    Args : 
       a : float =First number 
       b : float = second number 
    Returns :
       a * b 
    """

    return a * b 



@tool
def add(a :float ,b :float):
    """Add two numbers  a and b
    Args : 
       a : float = first number 
       b : float = second number  
    Returns : 
       a + b 
    """

    return a + b 






@tool
def currency_converter(
    from_curr: str,
    to_curr:   str,
    value:     float
) -> str:                          # ✅ return str!
    """Convert value from one currency
    to another using real time exchange rate.

    Args:
        from_curr: Source currency code (USD, INR, EUR)
        to_curr:   Target currency code (USD, INR, EUR)
        value:     Amount to convert

    Returns:
        Converted amount as string
    """
    try:
        alpha_vantage = AlphaVantageAPIWrapper()  # ✅ removed redundant env!

        response = alpha_vantage._get_exchange_rate(
            from_currency=from_curr,
            to_currency=to_curr
        )

        exchange_rate = float(
            response['Realtime Currency Exchange Rate']
                    ['5. Exchange Rate']
        )

        converted = value * exchange_rate

        return (
            f"{value} {from_curr} = "
            f"{converted:.2f} {to_curr} "
            f"(Rate: {exchange_rate:.4f})"
        )

    except KeyError:
        return f"Currency {from_curr} or {to_curr} not found!"
    except Exception as e:
        return f"Error: {str(e)}"