# Sample Hardhat 3 Project (`mocha` and `ethers`)

## Local snake registration

The existing Counter example is retained. SnakeRegistry adds a caller-bound manager
mapping and registration events; only the local chain (31337) is connected to the app.
From the repository root, run `just chain` (suppresses the node's default private-key
banner), then `just deploy-registry` in another terminal. Deployment uses Ignition and
generates ignored public metadata at `.local/snake-registry.json`. No private key is
exported. Keep the same node and manifest for application restarts; redeployment creates
a new instance and makes prior app evidence stale. See
`../docs/level-3/snake-registration-chain-development.md` for operation and reset limits.

Run `npx.cmd hardhat build`, `npx.cmd tsc --noEmit` and `npx.cmd hardhat test` from this
directory on Windows. The sample public-network instructions below are unrelated to
the application's local-only registry workflow and were not executed in this iteration.

This project showcases a Hardhat 3 project using `mocha` for tests and the `ethers` library for Ethereum interactions.

To learn more about Hardhat 3, please visit the [Getting Started guide](https://hardhat.org/docs/getting-started#getting-started-with-hardhat-3). To share your feedback, join our [Hardhat 3](https://hardhat.org/hardhat3-telegram-group) Telegram group or [open an issue](https://github.com/NomicFoundation/hardhat/issues/new) in our GitHub issue tracker.

## Project Overview

This example project includes:

- A simple Hardhat configuration file.
- Foundry-compatible Solidity unit tests.
- TypeScript integration tests using `mocha` and ethers.js
- Examples demonstrating how to connect to different types of networks, including locally simulating OP mainnet.

## Usage

### Running Tests

To run all the tests in the project, execute the following command:

```shell
npx hardhat test
```

You can also selectively run the Solidity or `mocha` tests:

```shell
npx hardhat test solidity
npx hardhat test mocha
```

### Make a deployment to Sepolia

This project includes an example Ignition module to deploy the contract. You can deploy this module to a locally simulated chain or to Sepolia.

To run the deployment to a local chain:

```shell
npx hardhat ignition deploy ignition/modules/Counter.ts
```

To run the deployment to Sepolia, you need an account with funds to send the transaction. The provided Hardhat configuration includes a Configuration Variable called `SEPOLIA_PRIVATE_KEY`, which you can use to set the private key of the account you want to use.

You can set the `SEPOLIA_PRIVATE_KEY` variable using the `hardhat-keystore` plugin or by setting it as an environment variable.

To set the `SEPOLIA_PRIVATE_KEY` config variable using `hardhat-keystore`:

```shell
npx hardhat keystore set SEPOLIA_PRIVATE_KEY
```

After setting the variable, you can run the deployment with the Sepolia network:

```shell
npx hardhat ignition deploy --network sepolia ignition/modules/Counter.ts
```
