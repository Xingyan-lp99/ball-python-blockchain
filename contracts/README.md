# Local Snake Registration

SnakeRegistry adds a caller-bound manager
mapping and registration events; only the local chain (31337) is connected to the app.
From the repository root, run `just chain` (suppresses the node's default private-key
banner), then `just deploy-registry` in another terminal. Deployment uses Ignition and
generates ignored public metadata at `.local/snake-registry.json`. No private key is
exported. Keep the same node and manifest for application restarts; redeployment creates
a new instance and makes prior app evidence stale. See
`../docs/level-3/snake-registration-chain-development.md` for operation and reset limits.

Run `npx.cmd hardhat build`, `npx.cmd tsc --noEmit` and `npx.cmd hardhat test` from this
directory on Windows.
