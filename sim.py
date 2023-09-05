import random
import simpy

# Function to simulate customer arrival with Poisson inter-arrival times
def customer_generator(env, a, p, servers, counts):
    customer_id = 0
    while True:
        inter_arrival_time = random.expovariate(1/a)  # Poisson inter-arrival time
        yield env.timeout(inter_arrival_time)
        customer_id += 1
        counts.append(counts[-1] + 1)  # Increment count
        env.process(customer(env, f'Customer {customer_id}', p, servers, counts))

# Function to simulate customer service
def customer(env, name, p, servers, counts):
    #print(f"{name} arrives at time {env.now}")
    with servers.request() as request:
        yield request
        #print(f"{name} starts being served at time {env.now}")
        yield env.timeout(random.expovariate(1/p))  # Simulate service time
        #print(f"{name} leaves at time {env.now}")
        counts.append(counts[-1] - 1)  # decrement count

def run(a, p, num_servers):
    # Environment setup
    env = simpy.Environment()

    # Resource (servers) setup
    servers = simpy.Resource(env, capacity=num_servers)

    # List to store the number of arrived and left customers
    #counts = [0, 0]  # [arrived_count, left_count]
    counts = [0]

    # Create customer generator and add it to the environment
    env.process(customer_generator(env, a, p, servers, counts))

    # Run the simulation
    env.run(until=1000)  # Run the simulation for a specified time

    # Print the number of customers
    #print(f"Total customers: {counts}")

    return counts

