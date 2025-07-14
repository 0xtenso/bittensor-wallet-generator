import json
from typing import Dict, Any
from bittensor_wallet import Wallet
from bittensor_wallet.errors import KeyFileError


def create_new_wallet(
    wallet_name: str = "default",
    wallet_path: str = "./wallets",
    overwrite: bool = True
) -> Dict[str, Any]:
    "Creates a new Bittensor wallet and returns address information."
    
    result = {
        "success": False,
        "wallet_name": wallet_name,
        "coldkey_address": "",
        "hotkey_address": "",
    }
    
    try:
        wallet = Wallet(name=wallet_name, path=wallet_path)
        
        # Create coldkey and hotkey
        print("\n=== Creating Coldkey ===")
        wallet.create_new_coldkey(n_words=12, use_password=False, overwrite=overwrite)
        print("\n=== Creating Hotkey ===")
        wallet.create_new_hotkey(n_words=12, use_password=False, overwrite=overwrite)
        
        # Extract wallet information (mnemonics are printed during creation above)
        result.update({
            "success": True,
            "coldkey_address": wallet.coldkeypub.ss58_address,
            "hotkey_address": wallet.hotkey.ss58_address,
        })
        
        print(f"\nWallet '{wallet_name}' created successfully!")
        print(f"Coldkey Address: {result['coldkey_address']}")
        print(f"Hotkey Address: {result['hotkey_address']}")
        
    except Exception as e:
        result["error"] = str(e)
        print(f"Error: {e}")
    
    return result


def create_wallet_from_mnemonic(
    wallet_name: str,
    coldkey_mnemonic: str,
    hotkey_mnemonic: str,
    wallet_path: str = "./wallets"
) -> Dict[str, Any]:
    "Creates a wallet from existing mnemonic phrases."
    
    result = {
        "success": False,
        "wallet_name": wallet_name,
        "coldkey_address": "",
        "hotkey_address": "",
    }
    
    try:
        wallet = Wallet(name=wallet_name, path=wallet_path)
        
        # Regenerate from mnemonics
        wallet.regenerate_coldkey(mnemonic=coldkey_mnemonic, use_password=False, overwrite=True)
        wallet.regenerate_hotkey(mnemonic=hotkey_mnemonic, use_password=False, overwrite=True)
        
        result.update({
            "success": True,
            "coldkey_address": wallet.coldkeypub.ss58_address,
            "hotkey_address": wallet.hotkey.ss58_address,
        })
        
        print(f"Wallet '{wallet_name}' restored successfully!")
        print(f"Coldkey Address: {result['coldkey_address']}")
        print(f"Hotkey Address: {result['hotkey_address']}")
        
    except Exception as e:
        result["error"] = str(e)
        print(f"Error: {e}")
    
    return result


if __name__ == "__main__":
    print("BITTENSOR WALLET GENERATOR")
    print("=" * 50)
    print("NOTE: The mnemonics are printed above during wallet creation.")
    print("Please save them securely - they are NOT stored in the JSON output for security.")
    print("=" * 50)
    
    # Create a new wallet
    wallet_info = create_new_wallet("test_wallet")
    
    if wallet_info["success"]:
        print("\n" + "="*50)
        print("WALLET INFORMATION")
        print("="*50)
        print(f"Name: {wallet_info['wallet_name']}")
        print(f"Coldkey Address: {wallet_info['coldkey_address']}")
        print(f"Hotkey Address: {wallet_info['hotkey_address']}")  
        
        # Save to JSON
        with open(f"{wallet_info['wallet_name']}_info.json", "w") as f:
            json.dump(wallet_info, f, indent=2)
        print(f"\nWallet info saved to {wallet_info['wallet_name']}_info.json")
        print("(Note: Mnemonics and private keys are NOT included in JSON file for security)")
    else:
        print(f"Failed to create wallet: {wallet_info['error']}") 