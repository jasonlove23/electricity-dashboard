import time
import random
import os

# --- Simulated Circuits ---
circuits = {
    "Living Room": 0.0,
    "Kitchen": 0.0,
    "Server Room": 0.0,
    "Office": 0.0,
    "Garage": 0.0
}

def read_sensor(circuit_name):
    """Simulate reading current (amps)."""
    return round(random.uniform(0.5, 15.0), 2)

def display_readings():
    """Clear screen and print all readings with color coding."""
    # Clear terminal
    os.system('clear' if os.name == 'posix' else 'cls')

    print("=" * 50)
    print("🔌 Real-Time Electricity Outflow Dashboard 🔌".center(50))
    print("=" * 50)
    
    for name in circuits.keys():
        current = circuits[name]
        # Color coding: green <= 7A, yellow 7-12A, red >12A
        if current <= 7:
            color = "\033[92m"  # Green
        elif current <= 12:
            color = "\033[93m"  # Yellow
        else:
            color = "\033[91m"  # Red
        reset = "\033[0m"
        print(f"Circuit: {name.ljust(15)} | Current: {color}{current:5.2f} A{reset}")
    
    print("=" * 50)
    print("\nPress Ctrl+C to stop.")

# --- Main Loop ---
if __name__ == "__main__":
    try:
        while True:
            # Update readings
            for name in circuits.keys():
                circuits[name] = read_sensor(name)
            # Display dashboard
            display_readings()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nDashboard stopped by user.")
