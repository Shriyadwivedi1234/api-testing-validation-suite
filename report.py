import subprocess
import sys
from datetime import datetime


def run_tests():
    """Run pytest and generate custom report"""
    
    print("=" * 60)
    print("🚀 API TESTING & VALIDATION SUITE")
    print(f"🌐 Base URL: https://jsonplaceholder.typicode.com")
    print(f"📅 Test Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Base URL: https://reqres.in/api")
    print("=" * 60)
    print()
    
    # Run pytest with verbose output
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"],
        capture_output=False
    )
    
    print()
    print("=" * 60)
    if result.returncode == 0:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED - Check output above")
    print("=" * 60)
    
    return result.returncode


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)