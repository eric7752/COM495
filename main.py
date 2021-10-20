from random import *
from Consumer import *
from Producer import *
from statistics import *
import numpy as np
import matplotlib.pyplot as plt


def generate_population(num_con, num_prod, delta):
    consumers = []
    producers = []

    wtps = []
    wtas = []

    min_wtp = float('inf')
    max_wta = -float('inf')

    for i in range(num_con):
        #wtp = np.random.uniform(0, 600)
        wtp = np.random.normal(300, 100)
        if wtp < min_wtp:
            min_wtp = wtp
        wtps.append(wtp)
        consumers.append(Consumer(wtp, delta))

    for i in range(num_prod):
        #wta = randrange(200, 800)
        wta = np.random.normal(500, 100)
        if wta > max_wta:
            max_wta = wta
        wtas.append(wta)
        producers.append(Producer(wta, delta))

    return consumers, producers, wtps, wtas, min_wtp, max_wta


def simulate_round(consumers, producers):
    still_trading = True
    prices = []
    traded_consumers = []
    traded_producers = []

    for con in consumers:
        con.traded = False
    for prod in producers:
        prod.traded = False

    while still_trading:
        valid_trade = False
        if len(consumers) > 0 and len(producers) > 0:
            for con in consumers:  # optimize
                for prod in producers:
                    if con.wtp > prod.wta:
                        valid_trade = True

        if not valid_trade:
            print("no more valid trades")
            still_trading = False
            break

        consumer = choice(consumers)
        producer = choice(producers)

        if consumer.wtp > producer.wta:
            price = uniform(producer.wta, consumer.wtp)
            prices.append(price)
            consumer.traded = True
            producer.traded = True

            traded_consumers.append(consumer)
            consumers.remove(consumer)

            traded_producers.append(producer)
            producers.remove(producer)

    consumers += traded_consumers
    producers += traded_producers

    for con in consumers:
        con.update_wtp()
    for prod in producers:
        prod.update_wta()

    return consumers, producers, prices


def simulate_n_rounds(n, consumers, producers):
    prices = []
    for i in range(n):
        print("round", i)
        consumers, producers, round_prices = simulate_round(consumers, producers)
        prices.append(round_prices)

    return prices


def summary_plot(prices):
    averages = []
    standard_devs = []
    num_trades = []
    for p in prices:
        averages.append(mean(p))
        standard_devs.append(pstdev(p))
        num_trades.append(len(p))

    fig, axs = plt.subplots(3, sharex='all')
    axs[0].plot(averages)
    axs[0].set_title("Average Price by Round")
    axs[1].plot(standard_devs)
    axs[1].set_title("Standard Deviation of Prices by Round")
    axs[2].plot(num_trades)
    axs[2].set_title("Number of Trades by Round")
    plt.show()


def supply_demand(prices, wtps, wtas, min_wtp, max_wta):
    quantities = {}
    price_range = np.linspace(min_wtp, max_wta, 100)

    min_diff = float('inf')
    min_diff_price = 0
    min_diff_quantity = 0

    for price in price_range:
        demand_i = len([wtp for wtp in wtps if wtp > price])
        supply_i = len([wta for wta in wtas if wta < price])
        quantities[price] = [demand_i, supply_i]
        if abs(demand_i - supply_i) < min_diff:
            min_diff = abs(demand_i - supply_i)
            min_diff_price = price
            min_diff_quantity = mean([demand_i, supply_i])

    s_d = list(quantities.values())
    demand = ([item[0] for item in s_d])
    supply = ([item[1] for item in s_d])

    plt.plot(supply, price_range,  label='Supply')
    plt.plot(demand, price_range, label='Demand')
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.title('Supply and Demand Curves')

    plt.plot(0, min_diff_quantity)
    plt.plot([min_diff_quantity, min_diff_quantity], [0, min_diff_price], linestyle='dashed', color='r')
    plt.plot([0, min_diff_quantity], [min_diff_price, min_diff_price], linestyle='dashed', color='r')

    plt.plot(min_diff_quantity, min_diff_price, 'ro', label='Equilibrium')
    plt.legend()
    plt.annotate(str((min_diff_quantity, round(min_diff_price, 2))), (min_diff_quantity, min_diff_price),
                 xytext=(10, 0), textcoords='offset points')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((0, x2, 0, y2))
    plt.show()


def main():
    num_con = eval(input("Enter number of consumers: "))
    num_prod = eval(input("Enter number of producers: "))
    delta = eval(input("Enter delta:"))
    consumers, producers, wtps, wtas, min_wtp, max_wta = generate_population(num_con, num_prod, delta)
    num_rounds = eval(input("Enter number of rounds to simulate: "))
    prices = simulate_n_rounds(num_rounds, consumers, producers)
    summary_plot(prices)
    supply_demand(prices, wtps, wtas, min_wtp, max_wta)


if __name__ == "__main__":
    main()