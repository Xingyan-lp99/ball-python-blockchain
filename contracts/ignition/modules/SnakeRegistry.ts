import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("SnakeRegistryModule", (m) => {
  const instanceId = m.getParameter("instanceId");
  const registry = m.contract("SnakeRegistry", [instanceId]);
  return { registry };
});
