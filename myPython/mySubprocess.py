import sys
import subprocess

try:
  #result = subprocess.run(['ls', '-l'], capture_output=True, text=True, check=True)
  result = subprocess.Popen(['ls', '-l'])
  print("Command output:")
  print(result.stdout)
except subprocess.CalledProcessError as e:
  print("Error executing command: ", e)
  print("Stderr: ", e.stderr)
except FileNotFoundError:
  print("Error: The specified command was not found.")

