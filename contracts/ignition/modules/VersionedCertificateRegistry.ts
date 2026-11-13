import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";
export default buildModule("VersionedCertificateRegistryModule", (m) => {
  const registry = m.contract("VersionedCertificateRegistry", [m.getParameter("instanceId"), m.getParameter("snakeRegistry")]);
  m.call(registry, "authorizeLaboratory", [m.getParameter("laboratory")]);
  return { registry };
});
