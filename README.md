Here is how you can format the Minikube installation and usage instructions as a GitHub README.md file, using GitHub-flavored Markdown with fenced code blocks for command lines for easy copy-pasting into the GitHub UI:

```markdown
# Minikube Installation and Usage on Windows with PowerShell and Hyper-V

This guide provides simple instructions to:

- Install Hyper-V PowerShell module
- Install Minikube and kubectl CLI tools
- Start a Minikube cluster using Hyper-V driver
- Verify that Minikube and kubectl are set up correctly

---

## Step 1: Open PowerShell as Administrator

Search for "PowerShell" in the Start menu, right-click and select **Run as Administrator**.

---

## Step 2: Enable Hyper-V and Management Tools

Run these commands in PowerShell to enable Hyper-V and its management features:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-All -All
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Management-Tools -All
```

If you want only the PowerShell module and management tools, run:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Tools-All -All
```

Restart your computer afterwards:

```
Restart-Computer
```

---

## Step 3: Install Minikube

Create a directory and download Minikube:

```
New-Item -Path 'C:\' -Name 'minikube' -ItemType Directory -Force

Invoke-WebRequest -OutFile 'C:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing
```

Add Minikube to your system PATH:

```
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\minikube') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\minikube", [EnvironmentVariableTarget]::Machine)
}
```

Close and reopen PowerShell.

---

## Step 4: Install kubectl CLI

Download kubectl executable:

```
Invoke-WebRequest -OutFile 'C:\kubectl.exe' -Uri 'https://dl.k8s.io/release/v1.34.0/bin/windows/amd64/kubectl.exe' -UseBasicParsing
```

Add kubectl to your system PATH:

```
$oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::Machine)
if ($oldPath.Split(';') -notcontains 'C:\') {
  [Environment]::SetEnvironmentVariable('Path', "$oldPath;C:\", [EnvironmentVariableTarget]::Machine)
}
```

Close and reopen PowerShell.

---

## Step 5: Start Minikube with Hyper-V Driver

```
minikube delete --all --purge
minikube start --driver=hyperv
```

If you see errors about Hyper-V PowerShell module, ensure it is installed and enabled (see Step 2).

---

## Step 6: Verify Minikube and kubectl

Check Minikube status:

```
minikube status
```

You should see "Running" for host, kubelet, and apiserver.

Check kubectl access to the cluster:

```
kubectl get nodes
kubectl get pods --all-namespaces
```

---

## Troubleshooting

- If Minikube fails to start due to missing config files, run:

```
minikube delete --all --purge
Remove-Item -Recurse -Force $env:USERPROFILE\.minikube
```

- Run PowerShell as Administrator for all commands.

- If Hyper-V is unavailable or problematic, consider using Docker driver instead (requires Docker Desktop installed):

```
minikube start --driver=docker
```

---

This README is ready to be copy-pasted directly into GitHub's UI for a fully formatted document with command blocks.
```

This format uses fenced triple backticks for command blocks with the `powershell` language tag omitted since GitHub powershell highlighting may vary but it will still render as a code block clearly. Each code block is separated by blank lines for readability. The headings and horizontal rules organize the sections clearly for documentation purposes.

[1](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)
[2](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
[3](https://www.markdownguide.org/extended-syntax/)
[4](https://github.com/adam-p/markdown-here/wiki/markdown-cheatsheet)
[5](https://www.glukhov.org/post/2025/07/markdown-codeblocks/)
[6](https://www.codecademy.com/resources/docs/markdown/code-blocks)
[7](https://www.freecodecamp.org/news/github-flavored-markdown-syntax-examples/)
[8](https://stackoverflow.com/questions/6235995/markdown-github-syntax-highlighting-of-code-block-as-a-child-of-a-list)
[9](https://gist.github.com/MarcoEidinger/c0f0583f19baca0a8f33bcded644be41)
[10](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting)
