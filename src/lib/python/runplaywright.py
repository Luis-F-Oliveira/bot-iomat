import subprocess

def run_playwright():
  subprocess.run(["C:\\Program Files\\nodejs\\npm.cmd", "install", "@types/node"])
  subprocess.run(["C:\\Program Files\\nodejs\\npm.cmd", "install", "-g", "typescript"])
  subprocess.run(["C:\\Program Files\\nodejs\\npm.cmd", "install", "-g", "typescript"])
  subprocess.run(["C:\\Program Files\\nodejs\\npx.cmd", "tsc"])
  subprocess.run(["C:\\Program Files\\nodejs\\npm.cmd", "run", "dev"])