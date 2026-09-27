# Deploy and interact on Sepolia

## 1. Prepare MetaMask

1. Install MetaMask and create or import a wallet.
2. Enable **Show test networks** in MetaMask settings.
3. Select **Sepolia**.
4. Obtain a small amount of Sepolia ETH from a trusted faucet.

Never share your Secret Recovery Phrase or private key. A faucet only needs
your public wallet address.

## 2. Open the contract in Remix

1. Go to [Remix IDE](https://remix.ethereum.org/).
2. Create `SepoliaPlayground.sol` in the `contracts` folder.
3. Copy the contents of
   [`contracts/SepoliaPlayground.sol`](contracts/SepoliaPlayground.sol).
4. Open **Solidity Compiler**.
5. Select compiler version `0.8.20` or later.
6. Click **Compile SepoliaPlayground.sol**.

## 3. Connect Remix to MetaMask

1. Open **Deploy & Run Transactions** in Remix.
2. Choose **Browser wallet** - **"Sepolia Testnet - MetaMask"** as the environment.
3. Approve the connection in MetaMask.
4. Confirm that both Remix and MetaMask show **Sepolia**.
5. Check that the displayed account is the wallet you intend to use.

Do not use **Remix VM** for this exercise: it is a temporary simulated chain,
not the public Sepolia network.

## 4. Deploy

1. Select `SepoliaPlayground` in the contract dropdown.
2. Enter an initial constructor message, for example:

   ```text
   My first Sepolia deployment
   ```

3. Click **Deploy**.
4. Confirm the transaction in MetaMask.
5. Wait until Remix shows the contract under **Deployed Contracts**.
6. Copy the contract address and open it in
   [Sepolia Etherscan](https://sepolia.etherscan.io/)
   or 
   [Sepolia Blockscout](https://eth-sepolia.blockscout.com/).

## 5. Try the interactions

### Read contract state

Click `message`, `owner`, `updateCount`, or `getContractBalance`.

These are read-only calls. MetaMask does not open and no gas is charged.

### Update the message

1. Enter a new value in `updateMessage`.
2. Click the button and confirm the transaction in MetaMask.
3. After confirmation, call `message` and `updateCount` again.
4. Find the transaction and `MessageUpdated` event on Etherscan.

### Deposit Sepolia ETH

1. In Remix, set **Value** to a small amount such as `0.001` and select
   `ether` as the unit.
2. Click `deposit` and confirm the transaction.
3. Call `getContractBalance` to view the total balance in wei.
4. Paste your wallet address into `deposits` to view your recorded deposit.

`0.001 ether` equals `1000000000000000 wei`.

### Withdraw your deposit

1. Enter an amount in wei in `withdraw`.
2. Confirm the transaction.
3. Call `deposits` and `getContractBalance` again to see the new values.

You can withdraw only ETH recorded under your own wallet address.

### Transfer ownership

1. Paste another valid wallet address into `transferOwnership`.
2. Confirm the transaction from the current owner account.
3. Call `owner` to verify the change.

Only the current owner can perform this action. Ownership transfer cannot be
undone unless the new owner transfers it back.

### Test access control

1. Call `setPaused` with `true` from the owner account.
2. Try to call `updateMessage` or `deposit`; the transaction should revert.
3. Call `setPaused` with `false` to resume normal operation.
4. Switch to another MetaMask account and try `setPaused` again; only the
   owner account is allowed to use it.

Withdrawals stay available while the contract is paused, so users are not
locked out of their deposited test ETH.

## Suggested evidence

- successful compilation in Remix;
- MetaMask connected to Sepolia;
- deployed contract address;
- confirmed message update;
- deposit and withdrawal transactions;
- events and transaction history on Sepolia Etherscan.
