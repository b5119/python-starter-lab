"""
Prime Number Finder
Find prime numbers in a range or check if a number is prime.
Uses nested loops for prime checking algorithm.
"""

def is_prime(n):
    """Check if a number is prime using trial division."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to square root
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def find_n_primes(n):
    """Find the first n prime numbers."""
    primes = []
    num = 2
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    return primes

def print_primes(primes):
    """Print primes in a formatted grid."""
    if not primes:
        print("No primes found in this range.")
        return
    
    print(f"\nFound {len(primes)} prime number(s):")
    for i in range(0, len(primes), 10):
        print(" ".join(f"{p:6}" for p in primes[i:i+10]))

def main():
    print("🔢 Prime Number Finder\n")
    
    while True:
        print("\nOptions:")
        print("1. Check if a number is prime")
        print("2. Find primes in a range")
        print("3. Find first N prime numbers")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == '1':
            try:
                num = int(input("Enter a number: "))
                if is_prime(num):
                    print(f"✅ {num} is a prime number!")
                else:
                    print(f"❌ {num} is not a prime number.")
            except ValueError:
                print("❌ Please enter a valid integer!")
        
        elif choice == '2':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                
                if start > end:
                    print("❌ Start must be less than or equal to end!")
                    continue
                
                print("\n🔍 Searching for primes...")
                primes = find_primes_in_range(start, end)
                print_primes(primes)
                
            except ValueError:
                print("❌ Please enter valid integers!")
        
        elif choice == '3':
            try:
                n = int(input("How many primes to find? "))
                if n <= 0:
                    print("❌ Please enter a positive number!")
                    continue
                
                print(f"\n🔍 Finding first {n} primes...")
                primes = find_n_primes(n)
                print_primes(primes)
                
            except ValueError:
                print("❌ Please enter a valid integer!")
        
        elif choice == '4':
            print("\n👋 Thanks for using Prime Finder!")
            break
        
        else:
            print("❌ Invalid option! Please choose 1-4.")

if __name__ == "__main__":
    main()