import random

def flip_coin():
    """Returns 'Heads' or 'Tails' randomly"""
    return random.choice(['Heads', 'Tails'])

def main():
    # Number of coin flips
    num_flips = 100
    
    # Counters for heads and tails
    heads_count = 0
    tails_count = 0
    
    # Perform the coin flips
    for i in range(num_flips):
        result = flip_coin()
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1
    
    # Calculate percentages
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100
    
    # Display results
    print(f"Coin Flip Results ({num_flips} flips):")
    print("-" * 30)
    print(f"Heads: {heads_count} ({heads_percentage:.1f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.1f}%)")
    
    # Determine which side won
    if heads_count > tails_count:
        print(f"\nHeads wins by {heads_count - tails_count} flips!")
    elif tails_count > heads_count:
        print(f"\nTails wins by {tails_count - heads_count} flips!")
    else:
        print(f"\nIt's a tie!")

if __name__ == "__main__":
    main()