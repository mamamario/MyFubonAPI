import fubon_neo
from fubon_neo.sdk import FubonSDK, Order
import argparse

# Global variables
sdk = None
accounts = None

# Factory Pattern: SDK Factory
class SDKFactory:
    """
    A factory class for creating FubonSDK instances.
    """
    def create_sdk(self):
        """
        Creates and returns a FubonSDK instance.
        """
        return FubonSDK()

# Strategy Pattern: Feature Strategy Interface
class FeatureStrategy:
    """
    An interface for different feature strategies.
    """
    def execute(self):
        """
        Executes the feature strategy.
        """
        raise NotImplementedError

# Concrete Strategy: Display Account Info
class DisplayAccountInfoStrategy(FeatureStrategy):
    """
    A strategy for displaying account information.
    """
    def __init__(self, accounts):
        self.accounts = accounts

    def execute(self):
        """
        Displays account information.
        """
        if self.accounts and self.accounts.data:
            print("Account Information:")
            for account in self.accounts.data:
                print(account)
        else:
            print("No account information available.")

# Concrete Strategy: Query Inventories
class QueryInventoriesStrategy(FeatureStrategy):
    """
    A strategy for querying inventories.
    """
    def __init__(self, sdk, accounts):
        self.sdk = sdk
        self.accounts = accounts

    def execute(self):
        """
        Queries and displays inventories.
        """
        try:
            result = self.sdk.accounting.inventories(self.accounts.data[0])
            if result.is_success:
                print(f"Inventories: {len(result.data)} items")
                for i, inv in enumerate(result.data):
                    print(f"Item {i+1}: {inv}")
            else:
                print(f"Error querying inventories: {result}")
        except Exception as e:
            print(f"Error querying inventories: {e}")

# Concrete Strategy: Query Historical Candles
class QueryHistoricalCandlesStrategy(FeatureStrategy):
    """
    A strategy for querying historical candle data.
    """
    def __init__(self, sdk):
        self.sdk = sdk

    def execute(self, symbol, from_date, to_date):
        """
        Queries historical candle data.
        """
        try:
            self.sdk.init_realtime()
            restStock = self.sdk.marketdata.rest_client.stock
            result = restStock.historical.candles(symbol=symbol, from_date=from_date, to_date=to_date)
            print(f"Historical candles: {result}")
        except Exception as e:
            print(f"Error querying historical candles: {e}")

# Concrete Strategy: Query Historical Stats
class QueryHistoricalStatsStrategy(FeatureStrategy):
    """
    A strategy for querying historical stats data.
    """
    def __init__(self, sdk):
        self.sdk = sdk

    def execute(self, symbol):
        """
        Queries historical stats data.
        """
        try:
            self.sdk.init_realtime()
            restStock = self.sdk.marketdata.rest_client.stock
            result = restStock.historical.stats(symbol=symbol)
            print(f"Historical stats: {result}")
        except Exception as e:
            print(f"Error querying historical stats: {e}")

# Concrete Strategy: Query Unrealized Gains/Losses
class QueryUnrealizedGainsLossesStrategy(FeatureStrategy):
    """
    A strategy for querying unrealized gains/losses.
    """
    def __init__(self, sdk, accounts):
        self.sdk = sdk
        self.accounts = accounts

    def execute(self):
        """
        Queries unrealized gains/losses.
        """
        try:
            result = self.sdk.accounting.unrealized_gains_and_loses(self.accounts.data[0])
            print(f"Unrealized gains/losses: {result}")
        except Exception as e:
            print(f"Error querying unrealized gains/losses: {e}")

# Concrete Strategy: Query Realized Gains/Losses
class QueryRealizedGainsLossesStrategy(FeatureStrategy):
    """
    A strategy for querying realized gains/losses.
    """
    def __init__(self, sdk, accounts):
        self.sdk = sdk
        self.accounts = accounts

    def execute(self):
        """
        Queries realized gains/losses.
        """
        try:
            result = self.sdk.accounting.realized_gains_and_loses(self.accounts.data[0])
            print(f"Realized gains/losses: {result}")
        except Exception as e:
            print(f"Error querying realized gains/losses: {e}")

# Concrete Strategy: Query Bank Remain
class QueryBankRemainStrategy(FeatureStrategy):
    """
    A strategy for querying bank balance.
    """
    def __init__(self, sdk, accounts):
        self.sdk = sdk
        self.accounts = accounts

    def execute(self):
        """
        Queries bank balance.
        """
        try:
            result = self.sdk.accounting.bank_remain(self.accounts.data[0])
            print(f"Bank balance: {result}")
        except Exception as e:
            print(f"Error querying bank balance: {e}")

import os

def initialize_sdk():
    """Initializes SDK and logs in."""
    global sdk, accounts
    # Factory Pattern: Use SDKFactory to create FubonSDK instance
    sdk_factory = SDKFactory()
    sdk = sdk_factory.create_sdk()
    try:
        # Read account information from environment variables
        username = os.environ.get("FUBON_USERNAME")
        password = os.environ.get("FUBON_PASSWORD")
        pfx_path = os.environ.get("FUBON_PFX_PATH")
        pfx_password = os.environ.get("FUBON_PFX_PASSWORD")

        if not all([username, password, pfx_path, pfx_password]):
            print("Error: Missing environment variables for account information.")
            return False

        accounts = sdk.login(username, password, pfx_path, pfx_password)
        print("Login successful:", accounts)
    except Exception as e:
        print(f"Login failed: {e}")
        return False
    return True

if __name__ == "__main__":
    # Initialize SDK
    if not initialize_sdk():
        exit()

    # Argument parsing
    parser = argparse.ArgumentParser(description="Fubon API Tool")
    parser.add_argument("--account", action="store_true", help="Display account info")
    parser.add_argument("--inventory", action="store_true", help="Query inventories")
    parser.add_argument("--historical_candles", nargs=3, metavar=("SYMBOL", "FROM_DATE", "TO_DATE"), help="Query historical candles")
    parser.add_argument("--historical_stats", nargs=1, metavar=("SYMBOL"), help="Query historical stats")
    parser.add_argument("--unrealized", action="store_true", help="Query unrealized gains/losses")
    parser.add_argument("--realized", action="store_true", help="Query realized gains/losses")
    parser.add_argument("--bank", action="store_true", help="Query bank balance")
    args = parser.parse_args()

    # Strategy Pattern: Feature selection using strategies
    if args.account:
        # Strategy Pattern: Execute DisplayAccountInfoStrategy
        strategy = DisplayAccountInfoStrategy(accounts)
        strategy.execute()
    elif args.inventory:
        # Strategy Pattern: Execute QueryInventoriesStrategy
        strategy = QueryInventoriesStrategy(sdk, accounts)
        strategy.execute()
    elif args.historical_candles:
        # Strategy Pattern: Execute QueryHistoricalCandlesStrategy
        symbol, from_date, to_date = args.historical_candles
        strategy = QueryHistoricalCandlesStrategy(sdk)
        strategy.execute(symbol, from_date, to_date)
    elif args.historical_stats:
        # Strategy Pattern: Execute QueryHistoricalStatsStrategy
        symbol = args.historical_stats[0]
        strategy = QueryHistoricalStatsStrategy(sdk)
        strategy.execute(symbol)
    elif args.unrealized:
        # Strategy Pattern: Execute QueryUnrealizedGainsLossesStrategy
        strategy = QueryUnrealizedGainsLossesStrategy(sdk, accounts)
        strategy.execute()
    elif args.realized:
        # Strategy Pattern: Execute QueryRealizedGainsLossesStrategy
        strategy = QueryRealizedGainsLossesStrategy(sdk, accounts)
        strategy.execute()
    elif args.bank:
        # Strategy Pattern: Execute QueryBankRemainStrategy
        strategy = QueryBankRemainStrategy(sdk, accounts)
        strategy.execute()
    else:
        print("No action specified.")

    # Disconnect
    try:
        sdk.marketdata.websocket_client.stock.disconnect()
    except:
        pass
