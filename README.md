# dollarAPI

Get the value of a USD in Argentine Pesos.

## API

- `getDollarValue(method)` Where `method` can be either **compra** *(purchasing value)* or **venta** *(selling value)*.


- `valueOf(currency)` Where `currency` expects either a **blue** object or an **official** object, since both have `getDollarValue` because both classes inherit it from the dollarAPI class.