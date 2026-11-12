import { buildModule } from "@nomicfoundation/hardhat-ignition/modules";

export default buildModule("CertificateRegistryModule", (m) => {
  const registry = m.contract("CertificateRegistry", [m.getParameter("instanceId"), m.getParameter("snakeRegistry")]);
  m.call(registry, "authorizeLaboratory", [m.getParameter("laboratory")]);
  return { registry };
});
