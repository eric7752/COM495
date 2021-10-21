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
    max_wtp = -float('inf')
    min_wta = float('inf')
    max_wta = -float('inf')

    for i in range(num_con):
        wtp = np.random.uniform(0, 600)
        #wtp = np.random.normal(300, 100)
        if wtp < min_wtp:
            min_wtp = wtp
        if wtp > max_wtp:
            max_wtp = wtp
        wtps.append(wtp)
        consumers.append(Consumer(wtp, delta))

    for i in range(num_prod):
        wta = randrange(200, 800)
        #wta = np.random.normal(500, 100)
        if wta > max_wta:
            max_wta = wta
        if wta < min_wta:
            min_wta = wta
        wtas.append(wta)
        producers.append(Producer(wta, delta))

    return consumers, producers, wtps, wtas, min_wtp, max_wtp, min_wta, max_wta


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

    return consumers, producers, prices


def summary_plot(prices, num_agents):
    averages = []
    standard_devs = []
    num_trades = []
    for p in prices:
        averages.append(mean(p))
        standard_devs.append(pstdev(p))
        num_trades.append(2*len(p)/num_agents)

    x_vals = list(range(1, len(averages) + 1))

    fig, axs = plt.subplots(3, sharex='all')

    axs[0].set_title("Average Price by Round")
    #coef = np.polyfit(np.log(x_vals), averages, 1)
    #axs[0].plot(x_vals, averages, x_vals, coef[1] + coef[0] * np.log(x_vals), '--k')
    coef = np.polyfit(x_vals, averages, 3)
    poly1d_fn = np.poly1d(coef)
    axs[0].plot(x_vals, averages, x_vals, poly1d_fn(x_vals), '--k')


    axs[1].set_title("Standard Deviation of Prices by Round")
    #coef2 = np.polyfit(np.log(x_vals), standard_devs, 1)
    #axs[1].plot(x_vals, standard_devs, x_vals, coef2[1] + coef2[0] * np.log(x_vals), '--k')
    coef2 = np.polyfit(x_vals, standard_devs, 3)
    poly1d_fn2 = np.poly1d(coef2)
    axs[1].plot(x_vals, standard_devs, x_vals, poly1d_fn2(x_vals), '--k')

    axs[2].set_title("Proportion of Transacting Individuals by Round")
    #coef3 = np.polyfit(np.log(x_vals), num_trades, 1)
    #axs[2].plot(x_vals, num_trades, x_vals, coef3[1] + coef3[0] * np.log(x_vals), '--k')
    coef3 = np.polyfit(x_vals, num_trades, 3)
    poly1d_fn3 = np.poly1d(coef3)
    axs[2].plot(x_vals, num_trades, x_vals, poly1d_fn3(x_vals), '--k')

    plt.show()


def supply_demand(wtps, wtas, min_wtp, max_wtp, min_wta, max_wta, title):
    quantities = {}
    price_range = np.linspace(min(min_wtp, min_wta), max(max_wta, max_wtp), 1000)

    min_diff = float('inf')
    min_diff_price = 0
    min_diff_quantity = 0

    for price in price_range:
        demand_i = len([wtp for wtp in wtps if wtp >= price])
        supply_i = len([wta for wta in wtas if wta <= price])
        quantities[price] = [demand_i, supply_i]
        if abs(demand_i - supply_i) < min_diff:
            min_diff = abs(demand_i - supply_i)
            min_diff_price = price
            min_diff_quantity = mean([demand_i, supply_i])

    s_d = list(quantities.values())
    demand = ([item[0] for item in s_d])
    supply = ([item[1] for item in s_d])

    plt.figure()
    plt.plot(supply, price_range,  label='Supply')
    plt.plot(demand, price_range, label='Demand')
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.title(title)

    plt.plot(0, min_diff_quantity)
    plt.plot([min_diff_quantity, min_diff_quantity], [0, min_diff_price], linestyle='dashed', color='r')
    plt.plot([0, min_diff_quantity], [min_diff_price, min_diff_price], linestyle='dashed', color='r')

    plt.plot(min_diff_quantity, min_diff_price, 'ro', label='Equilibrium')
    plt.legend()
    plt.annotate(str((min_diff_quantity, round(min_diff_price, 2))), (min_diff_quantity, min_diff_price),
                 xytext=(10, 0), textcoords='offset points')
    x1, x2, y1, y2 = plt.axis()
    plt.axis((0, x2, 0, y2))


def end_preferences(consumers, producers):
    wtps = []
    wtas = []

    min_wtp = float('inf')
    max_wtp = -float('inf')
    min_wta = float('inf')
    max_wta = -float('inf')

    for consumer in consumers:
        wtps.append(consumer.wtp)
        if consumer.wtp < min_wtp:
            min_wtp = consumer.wtp
        if consumer.wtp > max_wtp:
            max_wtp = consumer.wtp
    for producer in producers:
        wtas.append(producer.wta)
        if producer.wta > max_wta:
            max_wta = producer.wta
        if producer.wta < min_wta:
            min_wta = producer.wta

    return wtps, wtas, min_wtp, max_wtp, min_wta, max_wta


def main():
    num_con = eval(input("Enter number of consumers: "))
    num_prod = eval(input("Enter number of producers: "))
    delta = eval(input("Enter delta:"))
    consumers, producers, wtps, wtas, min_wtp, max_wtp, min_wta, max_wta = generate_population(num_con, num_prod, delta)
    num_rounds = eval(input("Enter number of rounds to simulate: "))
    consumers, producers, prices = simulate_n_rounds(num_rounds, consumers, producers)
    summary_plot(prices, len(consumers) + len(producers))
    supply_demand(wtps, wtas, min_wtp, max_wtp, min_wta, max_wta, "First Round Supply and Demand Curves")
    end_wtps, end_wtas, end_min_wtp, end_max_wtp, end_min_wta, end_max_wta = end_preferences(consumers, producers)
    supply_demand(end_wtps, end_wtas, end_min_wtp, end_max_wtp, end_min_wta, end_max_wta,
                  "Final Round Supply and Demand Curves")
    plt.show()

if __name__ == "__main__":
    main()