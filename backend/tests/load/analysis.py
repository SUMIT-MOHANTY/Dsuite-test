import subprocess
import json

def run_load_test():
    # Simple load test runner
    result = subprocess.run(
        ['locust', '-f', 'locustfile.py', '--headless', '-u', '10', '-r', '2', '-t', '30s', '--json'],
        capture_output=True,
        text=True,
        cwd='backend/tests/load'
    )
    return result.stdout

if __name__ == '__main__':
    output = run_load_test()
    print("Load test completed")
