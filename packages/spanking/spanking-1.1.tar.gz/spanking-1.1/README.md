# spanking

```
from spanking import FunctionBuilder

fb = FunctionBuilder()
fb.create('foodclassifier', 'Given a food name, classify it into Non-veg, Veg or Vegan.')
fb.foodclassifier("Chole Bhature")
fb.publish('foodclassifier')
```