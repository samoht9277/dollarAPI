# dollarAPI

Get the value of a USD in Argentine Pesos.

## API

- `getDollarValue(method)` Where `method` can be either **0** *(purchasing value)* or **1** *(selling value)*.
- `valueOf(currency)` Where `currency` expects either a **blue** object or an **official** object, since both have `getDollarValue` because both classes inherit it from the dollarAPI class.