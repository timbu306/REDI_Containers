# 🧑‍💻 Minikube Installation and Usage
Windows & macOS (PowerShell / Terminal)

This guide provides simple instructions to:
- ⚙️ Enable Hyper-V and management tools (Windows)
- 🧰 Install Minikube and kubectl CLI tools
- 🚀 Start a Minikube cluster using common drivers
- ✅ Verify that Minikube and kubectl are set up correctly

---

## 🪟 Windows — PowerShell (Admin)

### 1. Open PowerShell as Administrator
Search for "PowerShell", right-click → Run as Administrator.

### 2. Enable Hyper‑V and management tools
```powershell
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
# or only management tools:
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All

Restart-Computer
```

### 3. Install Minikube
```powershell
New-Item -Path 'C:' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' `
  -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' `
  -UseBasicParsing

# Add to machine PATH (if needed)
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
# Close & reopen PowerShell
```

### 4. Install kubectl
```powershell
Invoke-WebRequest -OutFile 'C:\kubectl.exe' `
  -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' `
  -UseBasicParsing

# Ensure C:\ (or folder containing kubectl.exe) is in machine PATH
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:", [EnvironmentVariableTarget]::Machine)
}
# Close & reopen PowerShell
```

### 5. Start Minikube (Hyper‑V)
```powershell
minikube delete --all --purge
minikube start --driver=hyperv
```

### 6. Verify
```powershell
minikube status
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## 🍎 macOS — Terminal

This section covers Homebrew installation (if needed), then kubectl and minikube installation. Works on Intel and Apple Silicon (M1/M2) — PATH notes included.

### 1. Install Homebrew (if not installed)
Run the official installer in Terminal:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Follow the installer messages. After install, ensure brew is in PATH:
- Intel macs: /usr/local/bin is usually already in PATH.
- Apple Silicon: add to your shell profile if installer suggests:
  ```bash
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
  eval "$(/opt/homebrew/bin/brew shellenv)"
  ```

Verify brew:
```bash
brew --version
```

### 2. Install kubectl and minikube via Homebrew
```bash
# Update brew
brew update

# Install kubectl and minikube
brew install kubectl
brew install minikube
```

Optional: install a virtualization driver (recommended options)
- Docker (common): install Docker Desktop for Mac, then:
  ```bash
  minikube start --driver=docker
  ```
- Hyperkit (lightweight, macOS only):
  ```bash
  brew install hyperkit
  minikube start --driver=hyperkit
  ```

If you have Apple Silicon and want a specific architecture, Homebrew handles correct binaries automatically when installed under /opt/homebrew.

### 3. Verify
```bash
minikube status
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## 🛠 Troubleshooting

- If minikube fails due to configs:
```bash
minikube delete --all --purge
# Windows PowerShell:
# Remove-Item -Recurse -Force "$env:USERPROFILE\.minikube"
# macOS / Linux:
rm -rf "$HOME/.minikube"
```
- Always run admin/elevated commands when modifying system features or machine-level PATHs.
- If Hyper‑V or hyperkit is unavailable, use Docker driver (Docker Desktop required):
```bash
minikube start --driver=docker
```

---

This README now includes icons for clarity and an added macOS section with Homebrew, kubectl and Minikube installation steps. Enjoy! 🚀****
