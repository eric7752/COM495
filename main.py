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
    consumer_surplus = []
    producer_surplus = []

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
            #price = producer.wta
            prices.append(price)
            consumer_surplus.append(consumer.wtp - price)
            producer_surplus.append(price - producer.wta)
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

    return consumers, producers, prices, consumer_surplus, producer_surplus


def simulate_n_rounds(n, consumers, producers):
    prices = []
    cons_surplus = []
    prod_surplus = []

    start_price_prod = {}
    end_price_prod = {}

    for i in range(n):
        print("round", i)
        consumers, producers, round_prices, c_surplus, p_surplus = simulate_round(consumers, producers)
        prices.append(round_prices)
        cons_surplus.append(c_surplus)
        prod_surplus.append(p_surplus)

        if i == 0:
            tup = zip(round_prices, p_surplus)
            start_price_prod = dict(tup)
        elif i == n - 1:
            tup = zip(round_prices, p_surplus)
            end_price_prod = dict(tup)

    return consumers, producers, prices, cons_surplus, prod_surplus, start_price_prod, end_price_prod


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
    axs[0].set_ylabel('Average Price ($)')

    axs[1].set_title("Standard Deviation of Prices by Round")
    #coef2 = np.polyfit(np.log(x_vals), standard_devs, 1)
    #axs[1].plot(x_vals, standard_devs, x_vals, coef2[1] + coef2[0] * np.log(x_vals), '--k')
    coef2 = np.polyfit(x_vals, standard_devs, 3)
    poly1d_fn2 = np.poly1d(coef2)
    axs[1].plot(x_vals, standard_devs, x_vals, poly1d_fn2(x_vals), '--k')
    axs[1].set_ylabel('SD ($)')

    axs[2].set_title("Proportion of Individuals Trading Each Round")
    #coef3 = np.polyfit(np.log(x_vals), num_trades, 1)
    #axs[2].plot(x_vals, num_trades, x_vals, coef3[1] + coef3[0] * np.log(x_vals), '--k')
    coef3 = np.polyfit(x_vals, num_trades, 3)
    poly1d_fn3 = np.poly1d(coef3)
    axs[2].plot(x_vals, num_trades, x_vals, poly1d_fn3(x_vals), '--k')

    fig.text(0.5, 0.04, 'Round', ha='center')

    plot_rounds = [prices[i] for i in range(len(prices)) if i % (len(prices) // 25) == 0]
    plt.figure()
    plt.boxplot(plot_rounds)
    plt.xlabel('Round')
    plt.ylabel('Price')
    plt.title('Boxplot of Transaction Prices By Round')

    x_vals, labels = plt.xticks()
    new_x_vals = len(prices) // 25 * x_vals
    plt.xticks(x_vals, new_x_vals, rotation='vertical')


def supply_demand(wtps, wtas, min_wtp, max_wtp, min_wta, max_wta, title):
    quantities = {}
    price_range = np.linspace(min(min_wtp, min_wta), max(max_wta, max_wtp), 100)

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


def utility(cons_surpluses, prod_surpluses, start_prod, end_prod):
    fig, axs = plt.subplots(2, sharex='all')
    cons_total = [sum(rd) for rd in cons_surpluses]
    prod_total = [sum(rd) for rd in prod_surpluses]

    cons_averages = [mean(rd) for rd in cons_surpluses]
    prod_averages = [mean(rd) for rd in prod_surpluses]

    axs[0].set_title("Average Surplus by Round")
    axs[0].plot(cons_averages, label='Consumer')
    axs[0].plot(prod_averages, label='Producer')
    axs[0].legend()

    axs[1].set_title("Total Surplus by Round")
    axs[1].plot(cons_total, label='Consumer')
    axs[1].plot(prod_total, label='Producer')
    axs[1].legend()

    fig.text(0.5, 0.04, 'Round', ha='center')
    fig.text(0.04, 0.5, 'Surplus ($)', va='center', rotation='vertical')

    plt.figure()

    start_prod_sorted = sorted(start_prod.items())
    end_prod_sorted = sorted(end_prod.items())

    rnge1 = start_prod_sorted[-1][0] - start_prod_sorted[0][0]
    rnge2 = end_prod_sorted[-1][0] - end_prod_sorted[0][0]

    low_cutoff1 = (1/3) * rnge1 + start_prod_sorted[0][0]
    low_cutoff2 = (1/3) * rnge2 + end_prod_sorted[0][0]
    mid_cutoff1 = (2/3) * rnge1 + start_prod_sorted[0][0]
    mid_cutoff2 = (2/3) * rnge2 + end_prod_sorted[0][0]

    print("start:", low_cutoff1, mid_cutoff1)
    print("end:", low_cutoff2, mid_cutoff2)

    low_price_s = [x[1] for x in start_prod_sorted if x[0] < low_cutoff1]
    mid_price_s = [x[1] for x in start_prod_sorted if low_cutoff1 <= x[0] < mid_cutoff1]
    high_price_s = [x[1] for x in start_prod_sorted if mid_cutoff1 <= x[0]]

    low_price_s_end = [x[1] for x in end_prod_sorted if x[0] < low_cutoff2]
    mid_price_s_end = [x[1] for x in end_prod_sorted if low_cutoff2 <= x[0] < mid_cutoff2]
    high_price_s_end = [x[1] for x in end_prod_sorted if mid_cutoff2 <= x[0]]

    print("low start", mean(low_price_s))
    print("mid start", mean(mid_price_s))
    print("high start", mean(high_price_s))

    print("low end", mean(low_price_s_end))
    print("mid end", mean(mid_price_s_end))
    print("high end", mean(high_price_s_end))


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
    consumers, producers, prices, cons_surpluses, prod_surpluses, start_prod, end_prod = \
        simulate_n_rounds(num_rounds, consumers, producers)
    summary_plot(prices, len(consumers) + len(producers))
    utility(cons_surpluses, prod_surpluses, start_prod, end_prod)

    supply_demand(wtps, wtas, min_wtp, max_wtp, min_wta, max_wta, "First Round Supply and Demand Curves")
    end_wtps, end_wtas, end_min_wtp, end_max_wtp, end_min_wta, end_max_wta = end_preferences(consumers, producers)
    end_wtps.sort()
    end_wtas.sort()
    #print(len(end_wtps), end_wtps)
    #print(len(end_wtas), end_wtas)
    supply_demand(end_wtps, end_wtas, end_min_wtp, end_max_wtp, end_min_wta, end_max_wta,
                  "Final Round Supply and Demand Curves")
    plt.show()


if __name__ == "__main__":
    main()