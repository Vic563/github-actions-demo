import random
import math

def flip_coin():
    """Returns 'Heads' or 'Tails' randomly"""
    return random.choice(['Heads', 'Tails'])

def calculate_statistics(heads_count, tails_count, num_flips):
    """Calculate advanced statistics for the coin flip results"""
    heads_percentage = (heads_count / num_flips) * 100
    tails_percentage = (tails_count / num_flips) * 100
    
    # Expected counts for a fair coin
    expected_count = num_flips / 2
    
    # Difference from expected
    heads_diff = heads_count - expected_count
    tails_diff = tails_count - expected_count
    
    # Standard deviation for binomial distribution
    std_dev = math.sqrt(num_flips * 0.5 * 0.5)
    
    # Z-score (standard deviations from mean)
    z_score = abs(heads_diff) / std_dev
    
    # Approximate p-value for statistical significance (two-tailed)
    # Using the empirical rule: 68-95-99.7
    if z_score < 1:
        significance = "within expected random variation"
    elif z_score < 2:
        significance = "slightly unusual but still plausible"
    elif z_score < 3:
        significance = "unusual - might indicate bias"
    else:
        significance = "very unusual - suggests possible bias"
    
    return {
        'heads_percentage': heads_percentage,
        'tails_percentage': tails_percentage,
        'heads_diff': heads_diff,
        'tails_diff': tails_diff,
        'std_dev': std_dev,
        'z_score': z_score,
        'significance': significance
    }

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
    
    # Calculate statistics
    stats = calculate_statistics(heads_count, tails_count, num_flips)
    
    # Display results
    print(f"Coin Flip Results ({num_flips} flips):")
    print("-" * 40)
    print(f"Heads: {heads_count} ({stats['heads_percentage']:.1f}%)")
    print(f"Tails: {tails_count} ({stats['tails_percentage']:.1f}%)")
    print()
    
    # Display advanced statistics
    print("Advanced Statistics:")
    print(f"  Expected: {num_flips/2:.0f} per side")
    print(f"  Std Dev: ±{stats['std_dev']:.1f}")
    print(f"  Heads deviation: {stats['heads_diff']:+.1f}")
    print(f"  Tails deviation: {stats['tails_diff']:+.1f}")
    print(f"  Z-score: {stats['z_score']:.2f}")
    print(f"  Result: {stats['significance']}")
    
    # Determine which side won
    if heads_count > tails_count:
        print(f"\nHeads wins by {heads_count - tails_count} flips!")
    elif tails_count > heads_count:
        print(f"\nTails wins by {tails_count - heads_count} flips!")
    else:
        print(f"\nIt's a tie!")

if __name__ == "__main__":
    main()
