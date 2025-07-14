# Bittensor Wallet Generator

A simple Python script to generate new Bittensor wallets and extract addresses and private keys.

## What it does

- Creates new Bittensor wallets (coldkey + hotkey)
- Returns SS58 addresses and private keys in hex format
- Restores wallets from existing mnemonic phrases
- Saves wallet information to JSON file

## Requirements

```bash
pip install bittensor-wallet
```

## Usage

### Generate New Wallet

```python
from wallet_generator import create_new_wallet

# Create new wallet
wallet_info = create_new_wallet("my_wallet")

if wallet_info["success"]:
    print(f"Coldkey Address: {wallet_info['coldkey_address']}")
    print(f"Coldkey Private Key: {wallet_info['coldkey_private_key']}")
    print(f"Hotkey Address: {wallet_info['hotkey_address']}")
    print(f"Hotkey Private Key: {wallet_info['hotkey_private_key']}")
```

### Restore from Mnemonic

```python
from wallet_generator import create_wallet_from_mnemonic

wallet_info = create_wallet_from_mnemonic(
    "restored_wallet",
    "your coldkey mnemonic phrase here...",
    "your hotkey mnemonic phrase here..."
)
```

### Run Script Directly

```bash
python wallet_generator.py
```

This will create a test wallet and save the information to `test_wallet_info.json`.

## Output Format

```json
{
  "success": true,
  "wallet_name": "test_wallet",
  "coldkey_address": "5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY",
  "hotkey_address": "5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty",
  "coldkey_mnemonic": "abandon abandon abandon...",
  "hotkey_mnemonic": "abandon abandon abandon...",
  "coldkey_private_key": "398f0c28f98885e046333d4a41c19cee4c37368a9832c6502f6cfd182e2aef89",
  "hotkey_private_key": "398f0c28f98885e046333d4a41c19cee4c37368a9832c6502f6cfd182e2aef89",
  "error": ""
}
```

## Security Warning

⚠️ **Keep your private keys and mnemonics safe!** Anyone with access to these can control your funds.

- Store them offline in a secure location
- Never share them publicly
- Test on testnet before using real funds

## File Structure

- `wallet_generator.py` - Main script
- `requirements.txt` - Dependencies
- `./wallets/` - Generated wallet files (created automatically)
- `*_info.json` - Exported wallet information

That's it! Simple wallet generation for Bittensor. 