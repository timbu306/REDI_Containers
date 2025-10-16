Step 1: Open PowerShell as Administrator
Search for "PowerShell" in the Start menu.

Right-click "Windows PowerShell" and select "Run as Administrator".

Step 2: Install Hyper-V PowerShell Module and Hyper-V Feature
Run the following command to install Hyper-V with the PowerShell module and management tools, and restart if needed:

powershell
Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
Your machine will restart after this step if Hyper-V is not already enabled.

Step 3: Download and Install Minikube
Run these commands to create a folder and download Minikube executable:

powershell
New-Item -Path 'C:\' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
Add Minikube to your system PATH:

powershell
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
Close and reopen PowerShell after this.

Step 4: Install kubectl (Kubernetes CLI)
Download kubectl binary with this command:

powershell
Invoke-WebRequest -OutFile 'C:\kubectl.exe' -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' -UseBasicParsing
Add kubectl to your system PATH:

powershell
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\", [EnvironmentVariableTarget]::Machine)
}
Close and reopen PowerShell again.

Step 5: Verify Installation
Check Minikube version:

powershell
minikube version
Check kubectl version:

powershell
kubectl version --client
These steps will get Minikube and kubectl installed on your Windows machine with Hyper-V enabled, using PowerShell
