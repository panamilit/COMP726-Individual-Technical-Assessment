# Part B - Sepolia Playground

A small Solidity project for practising smart-contract deployment and real
blockchain interactions on the **Sepolia test network**.

The contract lets you:

- deploy contract code to a public test network;
- store and update an on-chain message;
- compare transactions with read-only calls;
- deposit and withdraw Sepolia ETH;
- inspect balances, events and transaction history;
- pause and resume new updates and deposits;
- transfer contract ownership to another wallet.

No real cryptocurrency is required. Sepolia ETH has no monetary value.

## Project structure

```text
Part B - Sepolia Playground/
├── SepoliaPlayground.sol
├── DEPLOYMENT.md
├── REFLECTION.md
└── README.md
```

## Contract overview

| Feature | Blockchain concept |
|---|---|
| `updateMessage()` | State-changing transaction and gas |
| `message()` | Free read-only call |
| `deposit()` | Payable function and contract balance |
| `withdraw()` | ETH transfer and checks-effects-interactions |
| Events | Transaction logs visible in an explorer |
| `setPaused()` | Owner-only access control |
| `transferOwnership()` | Wallet addresses and ownership |

## Quick start

1. Install MetaMask and add the Sepolia network.
2. Obtain a small amount of Sepolia ETH from a faucet.
3. Open the contract in Remix and compile it with Solidity `0.8.20` or later.
4. Connect Remix to MetaMask using **Injected Provider**.
5. Deploy the contract and confirm the transaction in MetaMask.
6. Follow [DEPLOYMENT.md](DEPLOYMENT.md) to try each interaction.

> Use only the Sepolia test network. Do not send real ETH to this educational
> contract.

## Tools

- Solidity `^0.8.20`
- Remix IDE
- MetaMask
- Sepolia test network
- Sepolia Etherscan

## Licence

Created for educational purposes.
