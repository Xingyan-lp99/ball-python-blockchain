import { mkdir, writeFile } from "node:fs/promises";
import { network } from "hardhat";
import SnakeRegistryModule from "../ignition/modules/SnakeRegistry.js";

const { ethers, ignition } = await network.create({ network: "localhost" });
if ((await ethers.provider.getNetwork()).chainId !== 31337n) {
  throw new Error("Only the local Hardhat chain is supported");
}
const instanceId = ethers.hexlify(ethers.randomBytes(32));
const { registry } = await ignition.deploy(SnakeRegistryModule, {
  parameters: { SnakeRegistryModule: { instanceId } },
  deploymentId: `local-snake-${instanceId.slice(2, 18)}`,
  displayUi: false,
});
const address = await registry.getAddress();
const block = await ethers.provider.getBlock("latest");
if (block === null) throw new Error("Missing deployment block");
const [manager] = await ethers.getSigners();
const manifest = {
  chain_id: 31337,
  contract_address: address,
  instance_id: instanceId,
  deployment_block_number: block.number,
  deployment_block_hash: block.hash,
  runtime_code_hash: ethers.keccak256(await ethers.provider.getCode(address)),
  manager_address: manager.address,
  abi: JSON.parse(registry.interface.formatJson()),
};
await mkdir("../.local", { recursive: true });
// Public deployment metadata only; never export or print private keys.
await writeFile("../.local/snake-registry.json", JSON.stringify(manifest, null, 2));
console.log(`Local SnakeRegistry deployed: ${address}; BR001 wallet: ${manager.address}`);
