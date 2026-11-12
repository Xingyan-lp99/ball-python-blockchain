import { mkdir, readFile, writeFile } from "node:fs/promises";
import { network } from "hardhat";
import CertificateRegistryModule from "../ignition/modules/CertificateRegistry.js";

const { ethers, ignition } = await network.create({ network: "localhost" });
if ((await ethers.provider.getNetwork()).chainId !== 31337n) throw new Error("Local chain only");
const snake = JSON.parse(await readFile("../.local/snake-registry.json", "utf8"));
const snakeContract = new ethers.Contract(snake.contract_address, snake.abi, ethers.provider);
const anchor = await ethers.provider.getBlock(snake.deployment_block_number);
if (
  ethers.keccak256(await ethers.provider.getCode(snake.contract_address)) !== snake.runtime_code_hash
  || (await snakeContract.instanceId()) !== snake.instance_id
  || anchor?.hash !== snake.deployment_block_hash
) throw new Error("Current SnakeRegistry deployment could not be verified; existing state was left unchanged");
const [administrator, laboratory] = await ethers.getSigners();
if (laboratory.address.toLowerCase() === snake.manager_address.toLowerCase()) throw new Error("Separate lab wallet required");
const instanceId = ethers.hexlify(ethers.randomBytes(32));
const { registry } = await ignition.deploy(CertificateRegistryModule, {
  parameters: { CertificateRegistryModule: { instanceId, snakeRegistry: snake.contract_address, laboratory: laboratory.address } },
  deploymentId: `local-certificate-${instanceId.slice(2, 18)}`, displayUi: false,
});
const address = await registry.getAddress();
const block = await ethers.provider.getBlock("latest");
if (block === null) throw new Error("Missing deployment block");
const manifest = {
  chain_id: 31337, contract_address: address, instance_id: instanceId,
  deployment_block_number: block.number, deployment_block_hash: block.hash,
  runtime_code_hash: ethers.keccak256(await ethers.provider.getCode(address)),
  manager_address: laboratory.address, lab_id: "LAB001", lab_name: "Demo Laboratory LAB001",
  administrator_address: administrator.address,
  snake_contract_address: snake.contract_address, snake_instance_id: snake.instance_id,
  abi: JSON.parse(registry.interface.formatJson()),
};
await mkdir("../.local", { recursive: true });
await writeFile(`../.local/certificate-registry-${instanceId.slice(2, 18)}.json`, JSON.stringify(manifest, null, 2));
await writeFile("../.local/certificate-registry.json", JSON.stringify(manifest, null, 2));
console.log(`Local CertificateRegistry: ${address}; LAB001 wallet: ${laboratory.address}; SnakeRegistry retained: ${snake.contract_address}`);
