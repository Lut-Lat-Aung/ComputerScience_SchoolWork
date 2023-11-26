

from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import arviz as az
import pymc3 as pm

city_day = pd.read_csv('city_day.csv', parse_dates=['Date'])
delhi = city_day[city_day['City'] == 'Delhi']
delhi.head()
df = delhi.query('20160101 < Date < 20170101').dropna(subset=['Date', 'PM2.5'])
df.head()
df.describe()
pm_25 = df['PM2.5'].to_numpy()

y = np.log(pm_25)
# y = pm_25
t = np.arange(1, len(y) + 1)

b_hat = np.sum((t - t.mean())*((y - y.mean()))) / np.sum((t - t.mean())**2)
a_hat = y.mean() - b_hat * t.mean()

a_hat, b_hat

plt.plot(t, y, 'C0.')

plt.plot(t, a_hat + b_hat * t, c='k', label=f'y = {a_hat:.4f} + {b_hat:.4f}*x')
plt.ylabel('PM10')
plt.xlabel('Day of year', rotation=0)
plt.legend()

# error variance
np.sum((y - a_hat - b_hat * t) ** 2 / (len(y) - 2))

_, ax = plt.subplots(1, 1)
x = np.linspace(-15, 15, 1000)
ax.plot(x, stats.norm.pdf(x, 0, 10), label='a')
ax.plot(x, stats.norm.pdf(x, 0, 1), label='b')
ax.plot(x, stats.halfnorm.pdf(x, 0, 5), label='e')
ax.legend()

n = 200
t_a = 3
t_b = 0.2
t_e = 0.2
e = np.random.normal(0, 0.2, n)

x = np.random.normal(10, 1, n)
t_y = t_a + t_b * x
Y = t_y + e

_, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(x, Y, 'o')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y', rotation=0)
ax[0].plot(x, t_y, 'k')
az.plot_kde(y, ax=ax[1])
ax[1].set_xlabel('y')
plt.tight_layout()

with pm.Model() as model_l:
  # priors
  a = pm.Normal('a', mu=0, sigma=10)
  b = pm.Normal('b', mu=0, sigma=1)
  e = pm.HalfNormal('e', 5)

  y_pred = pm.Normal('y_pred', mu=a + b * x, sd=e, observed=Y)
  trace_l = pm.sample(2000, tune=3000)
  idata = az.from_pymc3(trace_l)

az.plot_trace(
    idata,
    var_names=['a', 'b', 'e'],
    lines=[
        ('a', {}, t_a),
        ('b', {}, t_b),
        ('e', {}, t_e),
    ]
)

with pm.Model() as model_l:
    
    # priors
    a = pm.Normal('a', mu=0, sigma=10)
    b = pm.Normal('b', mu=0, sigma=1)
    e = pm.HalfNormal('e', 5)
    
    # likelihood
    y_pred = pm.Normal('y_pred', mu=a + b*t, sd=e, observed=y)
    trace_l = pm.sample(
        2000,
        tune=5000
    )
    idata = az.from_pymc3(trace_l)

plt.plot(t, y, 'C0.')
alpha_m = trace_l['a'].mean()
beta_m = trace_l['b'].mean()
draws = range(0, len(trace_l['a']), 10)
plt.plot(t, trace_l['a'][draws] + trace_l['b'][draws] * t[:, np.newaxis], c='gray', alpha=0.5)
plt.plot(t, alpha_m + beta_m *t, c='k',
        label=f'y = {alpha_m:.4f} + {beta_m:.4f}*x')
plt.ylabel('log PM2.5')
plt.xlabel('Day of year', rotation=0)
plt.legend();

az.plot_posterior(
    idata,
    var_name= ['a','b','c']

)